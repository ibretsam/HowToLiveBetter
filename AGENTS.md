# AGENTS.md

Kho này chứa nội dung của **Hướng dẫn sống tốt hơn với chi phí hợp lý**. Fork `ibretsam/HowToLiveBetter` duy trì bản tiếng Việt chưa chính thức; nguyên tác do `eternity4719` biên soạn.

- **Sửa cuốn sách** (thêm/bớt mục, sửa nội dung, thay đổi công cụ): đọc hết [CLAUDE.md](CLAUDE.md) trước khi làm. Tất cả quy tắc trong đó đều áp dụng. Tên tệp là CLAUDE.md vì lý do lịch sử; quy tắc không phụ thuộc công cụ sử dụng.
- **Dùng sách để trả lời câu hỏi** (có nên làm không, có đáng không, chọn thế nào, gặp sự cố làm gì trước, được nhận khoản hỗ trợ nào, có vi phạm pháp luật không): thực hiện theo [skills/life-decision-guide/SKILL.md](skills/life-decision-guide/SKILL.md), tra mục liên quan trước khi trả lời và ghi rõ chương, mục được dùng. Cách cài để dùng ở thư mục khác nằm trong [skills/life-decision-guide/README.md](skills/life-decision-guide/README.md).

## Duy trì bản tiếng Việt

Nguồn tiếng Trung được ghim bằng `source_commit` trong `vi/site-config.json` và đọc từ lịch sử Git. Các tệp `book/` và chín bài đọc chính trong `docs/` là bản xuất tiếng Việt từ dữ liệu đã rà soát. Dùng `python3 tools/export-vi-markdown.py` để xuất lại, hoặc thêm `--check` để kiểm tra. Không ghi đè bản lưu trong `vi/book/`, `vi/docs/`, `vi/README.md` hay sửa dấu kiểm của checkpoint nhằm vượt qua xác thực.

Các công cụ phân tích tiếng Trung của upstream cần chạy trên bản nguồn tiếng Trung tại commit đã ghim. Kiểm tra bản fork bằng `tools/check-vi.py`, `tools/check-vi-updates.py`, `tools/check-vi-site.py` và `tools/export-vi-markdown.py --check`.
