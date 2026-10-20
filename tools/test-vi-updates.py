#!/usr/bin/env python3
"""Corruption and review-invalidation checks for the translation checkpoint."""
import copy
import unittest
from vi_updates import digest, validate_draft, validate_review


class CheckpointTests(unittest.TestCase):
    def setUp(self):
        original = {
            "number": 1, "title": "满18岁",
            "fields": {"cost": "花5元", "plain": "风险下降20%",
                       "benefit": "HR 0.80，95% CI 0.70–0.90",
                       "notes": "见[原文](https://example.org/study)。"},
            "extra": "", "tags": {},
        }
        self.task = {"id": "e-1-1", "source_commit": "fixed-revision",
                     "source_sha256": digest(original), "original": original}
        self.draft = {
            **{k: self.task[k] for k in ("id", "source_commit", "source_sha256")},
            "translator": "translator-one",
            "translation": {"title": "Đủ 18 tuổi", "cost": "Tốn 5 nhân dân tệ",
                            "plain": "Nguy cơ giảm 20%", "benefit": "HR 0.80, 95% CI 0.70–0.90",
                            "notes": "Xem [bản gốc](https://example.org/study).", "extra": ""},
        }
        self.review = {
            "id": "e-1-1", "source_sha256": self.draft["source_sha256"],
            "draft_sha256": digest(self.draft), "reviewer": "reviewer-two", "status": "passed",
            "checks": {"meaning": True, "numbers_and_units": True,
                       "conditions_and_negation": True, "references": True, "readability": True},
            "notes": "Compared with source.",
        }

    def test_valid_checkpoint_is_repeatable_without_mutating_data(self):
        before = copy.deepcopy((self.task, self.draft, self.review))
        for _ in range(2):
            validate_draft(self.task, self.draft)
            validate_review(self.draft, self.review)
        self.assertEqual(before, (self.task, self.draft, self.review))

    def test_corrupted_translation_is_rejected(self):
        cases = [
            ("title", "Đủ 19 tuổi"), ("cost", ""), ("plain", "[CHƯA DỊCH] 20%"),
            ("benefit", "0.80, 95% CI 0.70–0.90"),
            ("notes", "Xem [bản gốc](https://different.example/study)."),
            ("plain", "风险下降20%"),
        ]
        for field, value in cases:
            with self.subTest(field=field, value=value):
                draft = copy.deepcopy(self.draft)
                draft["translation"][field] = value
                with self.assertRaises(AssertionError):
                    validate_draft(self.task, draft)

    def test_source_tampering_is_rejected(self):
        self.task["original"]["title"] = "满19岁"
        with self.assertRaises(AssertionError):
            validate_draft(self.task, self.draft)

    def test_review_is_invalidated_even_by_numeric_preserving_edit(self):
        self.draft["translation"]["plain"] = "Nguy cơ tăng 20%"
        validate_draft(self.task, self.draft)  # Structural checks cannot detect reversed meaning.
        with self.assertRaises(AssertionError):
            validate_review(self.draft, self.review)

    def test_self_review_or_incomplete_review_is_rejected(self):
        self.review["reviewer"] = self.draft["translator"]
        with self.assertRaises(AssertionError):
            validate_review(self.draft, self.review)
        self.review["reviewer"] = "reviewer-two"
        self.review["checks"]["meaning"] = False
        with self.assertRaises(AssertionError):
            validate_review(self.draft, self.review)

    def test_supplementary_table_structure_cannot_be_dropped(self):
        original = "# 数字\n\n| 年龄 | 数值 |\n|---|---|\n| 18岁 | 20% |\n"
        task = {**self.task, "id": "guide", "original": original, "source_sha256": digest(original)}
        draft = {**self.draft, "id": "guide", "source_sha256": task["source_sha256"],
                 "translation": {"markdown": "# Con số\n\n| Tuổi | Giá trị |\n|---|---|\n| 18 tuổi | 20% |\n"}}
        validate_draft(task, draft)
        draft["translation"]["markdown"] = "# Con số\n\n18 tuổi: 20%."
        with self.assertRaises(AssertionError):
            validate_draft(task, draft)

    def test_retained_drug_names_must_exist_in_source(self):
        self.task["original"]["title"] = "药品对乙酰氨基酚"
        self.task["source_sha256"] = digest(self.task["original"])
        self.draft["source_sha256"] = self.task["source_sha256"]
        self.draft["translation"]["title"] = "Thuốc paracetamol (对乙酰氨基酚)"
        self.draft["retained_terms"] = {"title": ["对乙酰氨基酚"]}
        validate_draft(self.task, self.draft)
        self.draft["retained_terms"]["title"].append("不存在")
        with self.assertRaises(AssertionError):
            validate_draft(self.task, self.draft)


if __name__ == "__main__":
    unittest.main()
