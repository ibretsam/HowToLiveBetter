# Checkpoint tiếng Việt — đợt 13, nguồn e2605d3

Nguồn đích: `e2605d3e2242bd6216c9255192b8a8957a08c55a`, sau 17 commit
upstream kể từ `5f210ca953b7b538c042ad8515d5c355b766a194`.
Phạm vi: 34 chương với 767 mục, 34 tiêu đề/lời dẫn, 9 bài dài và hướng dẫn đọc.
Mốc fork trước đợt này: `8910333e4ac3ccf657f585bd731d88f21d8a2876`.

## Phân loại thay đổi

- 67 mục cần đối chiếu lại: 65 mục đã có và hai mục mới 5.51, 34.13.
- 9 phần ngoài mục thay đổi: lời dẫn chương 1, 5, 12, 13, 34; bài trang bị
  khẩn cấp, giúp người lạ, sau chẩn đoán bệnh mạn tính; hướng dẫn đọc.
- 735 phần có nội dung nguồn và đường dẫn khớp hoàn toàn được kế thừa hồ sơ
  rà soát từ `../vi-current/`. Đây không phải 735 lượt rà soát mới.

`tasks/` và `other-tasks/` lưu nguồn đầy đủ theo commit mới. Trường
`previous_translation` chứa các trường bản dịch gần nhất, để đối chiếu; không
phải bằng chứng rằng bản dịch đó đã được cập nhật. `inventory.json` giữ trạng
thái lúc bắt đầu: current, outdated hoặc pending.

`inheritance.json` ghi đường dẫn checkpoint cũ cùng SHA-256 của nguồn, toàn bộ
bản nháp và toàn bộ hồ sơ duyệt cho từng phần kế thừa. Bộ nạp kiểm tra hồ sơ
cũ theo nguồn cũ, rồi so sánh nội dung nguồn và đường dẫn với gói mới. Nguồn
đổi, dấu kiểm đổi, kế thừa vòng hoặc trùng bản nháp mới đều bị từ chối. Không
đổi tên người duyệt, không ký lại bản nháp cũ và không ghi đè checkpoint cũ.

Những phần thay đổi có bản nháp mới trong `drafts/`, do tác vụ khác đối chiếu
song ngữ trước khi ghi `reviews/`. Tuân theo [quy trình và thuật ngữ](../vi-current/README.md).
Giữ nguyên số liệu, điều kiện, phủ định, nguồn dẫn và bối cảnh Trung Quốc.
Không dùng kết quả kiểm tra cấu trúc thay cho rà soát nghĩa.

Checkpoint hoạt động được chọn bằng `checkpoint` trong `vi/site-config.json`.
Chạy từ thư mục gốc:

```sh
python3 tools/check-vi.py
python3 tools/check-vi-updates.py
python3 tools/test-vi-updates.py
python3 tools/build-vi-site.py
python3 tools/check-vi-site.py
```

`batch-13-report.json` ghi số hồ sơ mới, phần kế thừa, kiểm tra bảo toàn dữ
liệu cũ và kết quả rà soát. Trạng thái xuất bản và commit phát hành xem workflow
Vietnamese GitHub Pages trong fork `ibretsam/HowToLiveBetter`.
