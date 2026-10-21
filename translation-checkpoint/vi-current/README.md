# Checkpoint cập nhật tiếng Việt — nguồn 5f210ca

Mốc khởi đầu: `19a127a`, nhánh làm việc `codex/vi-current-source`. Bản dịch cũ và
`vi-reviewed-cache/` giữ nguyên để kiểm tra snapshot 01/10/2026.

## Quy trình một mục

1. Đọc `tasks/e-<chương>-<mục>.json`: nguồn đầy đủ, bản dịch cũ và dấu kiểm nguồn.
2. Viết `drafts/<ID>.json`. Các trường bắt buộc là `id`, `source_commit`,
   `source_sha256`, `translator` và `translation`. Trong `translation` có sáu
   chuỗi: `title`, `cost`, `plain`, `benefit`, `notes`, `extra`.
   Với gói `intro-*`, dùng hai chuỗi `title`, `intro`; với gói `doc-*` hoặc
   `guide`, dùng chuỗi `markdown`. Gói nguồn của các phần này nằm trong
   `other-tasks/`; cơ chế rà soát và dấu kiểm giống các mục.
3. Chỉ dịch văn xuôi. Công cụ sao chép số thứ tự, thẻ chi phí, mức bằng chứng và
   trường nguồn; chú thích mức bằng chứng được chuyển ngữ theo quy tắc có sẵn.
   Giữ nguyên URL trong bản nháp, công cụ đổi liên kết khi dựng trang.
4. Chạy kiểm tra cấu trúc; người/tác vụ khác đối chiếu song ngữ toàn bộ mục.
   Sửa lỗi trước khi lập bản ghi duyệt trong `reviews/<ID>.json`.
5. Bản ghi duyệt gắn với dấu kiểm toàn bộ bản nháp và nguồn. Mọi thay đổi sau đó
   đều làm bản ghi hết hiệu lực. Chỉ bản có rà soát hợp lệ mới được đưa lên trang.

Không tự điền trạng thái “đã duyệt” chỉ vì kiểm tra tự động đạt. Người dịch không
được là người duyệt của cùng một mục. Đọc nguồn trước, không sửa lời khuyên hoặc
thêm kết luận bằng trí nhớ. Điểm bất nhất của nguồn được ghi vào `notes` của bản
ghi rà soát để theo dõi, không âm thầm sửa khi dịch.

Tên thuốc hoặc mảnh chữ cần nhận diện trên nhãn Trung Quốc có thể giữ nguyên,
kèm giải thích tiếng Việt. Liệt kê rõ trong trường tùy chọn `retained_terms`,
dạng `{"notes": ["tên gốc"], "benefit": ["tên gốc"]}`. Từng chuỗi phải có trong
trường nguồn tương ứng; không miễn kiểm tra cho cả trường hay cả tệp.

## Thuật ngữ và quy ước cho lô thử

| Nguồn | Cách dùng tiếng Việt |
|---|---|
| 成本 / 说人话 / 收益 / 备注 | Chi phí / Nói dễ hiểu / Lợi ích / Ghi chú |
| 总死亡率 / 病死率 | Tỷ lệ tử vong do mọi nguyên nhân / tỷ lệ tử vong trong số người mắc bệnh |
| 心肺复苏 / 胸外按压 | Hồi sinh tim phổi / ép ngực |
| 气道梗阻 / 心脏骤停 | Tắc nghẽn đường thở / ngừng tim |
| 对乙酰氨基酚 / 安乃近 | Paracetamol (acetaminophen) / metamizole |
| 粒细胞缺乏症 | Mất bạch cầu hạt |
| 劳动合同 / 劳务关系 | Hợp đồng lao động / quan hệ cung ứng dịch vụ lao động (phân biệt với quan hệ lao động) |
| 经济补偿 / 赔偿金 | Khoản bồi thường khi chấm dứt hợp đồng / khoản bồi thường do vi phạm; diễn đạt theo đúng trường hợp trong nguồn |
| 工伤 / 失业保险金 | Tai nạn lao động / trợ cấp bảo hiểm thất nghiệp |
| 不满 / 以下 / 以上 | Chưa đủ / trở xuống / trở lên; kiểm tra điều kiện có bao gồm ngưỡng |
| 万 / 亿 | Vạn (mười nghìn) / trăm triệu; giữ hệ số viết bằng chữ số như nguồn |

Giữ nguyên chữ số và dấu thập phân của nguồn, không tự đổi sang VND hoặc số điện
thoại Việt Nam. HR/RR/OR/CI giữ nguyên cùng số liệu; không đổi odds thành xác suất
nếu nguồn phân biệt. Tên luật/thuốc và câu trích dẫn được dịch hoặc giữ nguyên có
ghi nhận theo mục đích tra cứu, không làm mất điều kiện, phủ định hoặc mốc thời gian.

## Kiểm tra và tiếp tục

```sh
python3 tools/check-vi.py
python3 tools/check-vi-updates.py
python3 tools/test-vi-updates.py
python3 tools/build-vi-site.py
python3 tools/check-vi-site.py
python3 tools/prepare-vi-updates.py
```

Lệnh cuối chỉ bổ sung gói công việc còn thiếu, không ghi đè bản dịch/rà soát.
Nếu nguồn của gói đã thay đổi, công cụ dừng để xử lý phiên bản thay vì ghi đè.
`inventory.json` liệt kê toàn bộ công việc; `other-tasks/` chứa tiêu đề/lời dẫn
của 34 chương, 9 bài dài và hướng dẫn đọc. Chúng chưa được coi là hoàn thành
khi chỉ đủ bản dịch của các mục.

Lô thử: chương 13 các mục 1, 2, 3, 26, 27, 28, 45–48; chương 34 các mục 1–12;
chương 19 các mục 1, 2, 19–24. Tổng 30 mục, mỗi chương có tác vụ phụ trách riêng.

Đợt 2: 38 mục còn lại của chương 13, toàn bộ 14 mục chương 16 và 17 mục chương
20, cộng ba lời dẫn. Tổng 69 mục: 9 mục mới, 57 cập nhật và 3 rà soát lại. Có
72 hồ sơ rà soát độc lập mới; báo cáo nằm trong `batch-2-report.json`. Không nhận
lại các ID đã có review hợp lệ khi bắt đầu đợt tiếp theo.

Đợt 3: toàn bộ 7 mục chương 18, 20 mục chương 27 và 21 mục chương 30, cộng ba
lời dẫn và bài hướng dẫn trước/sau sinh gồm 45 việc. Tổng 48 mục: 9 mục mới,
32 cập nhật và 7 rà soát lại. Có 52 hồ sơ rà soát độc lập mới; báo cáo nằm trong
`batch-3-report.json`. Các bản nháp/rà soát đã có từ hai đợt trước giữ nguyên.

Đợt 4: toàn bộ 50 mục chương 5, 29 mục chương 9 và 16 mục còn lại của chương
19 (mục 3–18), cộng ba lời dẫn và bài hướng dẫn sau thôi việc gồm 34 việc.
Tổng 95 mục: 12 mục mới, 59 cập nhật và 24 rà soát lại. Có 99 hồ sơ rà soát
độc lập mới; báo cáo nằm trong `batch-4-report.json`. Giữ nguyên 155 bản nháp
và 155 hồ sơ rà soát của ba đợt trước.

Đợt 5: toàn bộ 23 mục chương 7, 46 mục chương 8 và 21 mục chương 33, cộng
ba lời dẫn và bài phân tích về việc giúp người lạ gặp nạn. Tổng 90 mục: 4 mục
mới, 78 cập nhật và 8 rà soát lại. Có 94 hồ sơ rà soát độc lập mới; báo cáo nằm
trong `batch-5-report.json`. Giữ nguyên 254 bản nháp và 254 hồ sơ rà soát của
bốn đợt trước.

Đợt 6: toàn bộ 47 mục chương 2, 13 mục chương 17 và 15 mục chương 24, cộng
ba lời dẫn và bài hướng dẫn sau chẩn đoán bệnh mạn tính gồm 37 việc. Tổng 75
mục: 13 mục mới, 50 cập nhật và 12 rà soát lại. Có 79 hồ sơ rà soát độc lập mới;
báo cáo nằm trong `batch-6-report.json`. Giữ nguyên 348 bản nháp và 348 hồ sơ
rà soát của năm đợt trước.

Đợt 7: toàn bộ 48 mục chương 1, 35 mục chương 6 và 10 mục chương 28, cộng
ba lời dẫn và bài danh sách trang bị khẩn cấp cho gia đình. Tổng 93 mục:
17 mục mới, 73 cập nhật và 3 rà soát lại. Có 97 hồ sơ rà soát độc lập mới;
báo cáo nằm trong `batch-7-report.json`. Giữ nguyên 427 bản nháp và 427 hồ sơ
rà soát của sáu đợt trước. Bài trang bị khẩn cấp giữ hai TODO cần xác minh
của nguyên bản; bất nhất về gây nôn ở mục 1.48/13.20 được ghi công khai trong
`vi/TRANSLATION.md`. Kiểm tra bản dịch không phải kiểm chứng độc lập y khoa.

Đợt 8: toàn bộ 28 mục chương 12, 23 mục chương 10 và 18 mục chương 15,
cộng ba lời dẫn và bài phân tích kết hôn. Tổng 69 mục: 17 mục mới, 51 cập nhật
và 1 rà soát lại. Có 73 hồ sơ rà soát độc lập mới; báo cáo nằm trong
`batch-8-report.json`. Giữ nguyên 524 bản nháp và 524 hồ sơ rà soát của bảy
đợt trước. Bài phân tích giữ đủ năm nhóm cân nhắc, bảy phần dữ liệu và danh
sách tự điền; các giới hạn và bất nhất của nguồn được ghi ở hồ sơ rà soát.

Đợt 9: toàn bộ 27 mục chương 3, 25 mục chương 23 và 21 mục chương 11,
cộng ba lời dẫn và bài về nhịp sinh học/ca đêm. Tổng 73 mục: 9 mục mới,
51 cập nhật và 13 rà soát lại. Có 77 hồ sơ rà soát độc lập mới; báo cáo nằm
trong `batch-9-report.json`. Giữ nguyên 597 bản nháp và 597 hồ sơ rà soát
của tám đợt trước. Bài dài giữ đủ chín phần, bốn tiểu mục và năm kết quả
thí nghiệm; không đổi kết quả chỉ số trung gian thành khẳng định giảm tử vong.

Đợt 10: toàn bộ 17 mục chương 31, 13 mục chương 21 và 13 mục chương 26,
cộng ba lời dẫn và bài giấy phép nền tảng. Tổng 43 mục: 5 mục mới,
32 cập nhật và 6 rà soát lại. Có 47 hồ sơ rà soát độc lập mới; báo cáo nằm
trong `batch-10-report.json`. Giữ nguyên 674 bản nháp và 674 hồ sơ rà soát
của chín đợt trước. Bài dài giữ ba bảng với 22 dòng nội dung, bốn phần chính,
một tiểu mục và ba ý về giới hạn của tài liệu. Giữ bối cảnh pháp luật Trung Quốc
và ghi các bất nhất của nguồn trong hồ sơ rà soát.

Đợt 11: toàn bộ 12 mục chương 25, 14 mục chương 29 và 12 mục chương 22,
cộng ba lời dẫn và bài “Trước khi đổi việc hoặc chuyển thành phố”. Tổng 38 mục:
5 mục mới, 30 cập nhật và 3 rà soát lại. Có 42 hồ sơ rà soát độc lập mới;
báo cáo nằm trong `batch-11-report.json`. Giữ nguyên 721 bản nháp và 721 hồ sơ
rà soát của mười đợt trước. Bài dài được dịch mới đủ 64 việc trong chín phần,
giữ điều kiện và liên kết tham chiếu; các giới hạn của nguồn được ghi trong
hồ sơ rà soát. Cả chín bài dài đã hoàn tất theo nguồn đích, hướng dẫn đọc còn lại.

Đợt 12: toàn bộ 18 mục chương 4, 12 mục chương 14 và 12 mục chương 32,
cộng ba lời dẫn và hướng dẫn đọc. Tổng 42 mục: 5 mới, 22 cập nhật, 15 rà soát
lại; thêm 46 hồ sơ rà soát độc lập, xem `batch-12-report.json`. Giữ nguyên
763 bản nháp và 763 hồ sơ rà soát của mười một đợt trước. Hướng dẫn đọc được
đối chiếu đủ 34 câu hỏi, 41 thuật ngữ, 34 phần giới thiệu chương, bảng, ví dụ
và liên kết. Bộ kiểm tra phân biệt ví dụ Markdown có văn xuôi cần dịch với
câu lệnh phải giữ nguyên. Tổng 809 đơn vị đã rà soát: 765 mục, 34 lời dẫn,
chín bài dài và hướng dẫn đọc. Phạm vi nội dung đọc của nguồn đích đã hoàn tất.

Ngày 21/10/2026 đã thấy upstream `d78ca9b`, nhưng checkpoint này vẫn ghim
`5f210ca`. Các thay đổi upstream mới cần checkpoint và lượt đối chiếu riêng;
không đổi dấu kiểm của bản cũ hoặc coi tỷ lệ đợt này là tỷ lệ theo nguồn mới nhất.

Không có dịch vụ dịch ngoài hoặc lịch chạy nền trong quy trình này. Tiến độ chỉ
tăng theo bản dịch đã lưu, kiểm tra và rà soát hợp lệ. Khi gián đoạn, đọc inventory,
kiểm tra các tệp đã có rồi nhận lô tiếp theo; không bắt đầu lại toàn bộ.
