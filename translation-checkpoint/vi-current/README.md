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

Không có dịch vụ dịch ngoài hoặc lịch chạy nền trong quy trình này. Tiến độ chỉ
tăng theo bản dịch đã lưu, kiểm tra và rà soát hợp lệ. Khi gián đoạn, đọc inventory,
kiểm tra các tệp đã có rồi nhận lô tiếp theo; không bắt đầu lại toàn bộ.
