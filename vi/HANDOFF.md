# Đọc và khôi phục bản dịch

Mở [README tiếng Việt](README.md) để đọc 34 chương và tám bài viết. Xem
[thông tin bản dịch](TRANSLATION.md) về nguồn, giấy phép, bối cảnh Trung Quốc
và giới hạn của bản nháp AI.

Gói ZIP có thư mục `HowToLiveBetter/` chứa các tệp đã theo dõi trong Git,
và `HowToLiveBetter-Vietnamese.bundle` chứa lịch sử của nhánh
`codex/vietnamese-cloud-checkpoint`. Không có thông tin đăng nhập hay cấu hình
Git riêng của phiên cloud.

Sau khi giải nén, muốn khôi phục cả lịch sử vào một thư mục mới, chạy:

```sh
git clone -b codex/vietnamese-cloud-checkpoint HowToLiveBetter-Vietnamese.bundle HowToLiveBetter-restored
cd HowToLiveBetter-restored
python3 tools/assemble-vi.py
python3 tools/check-vi.py --write-report
```

Cloud đã bị GitHub từ chối quyền ghi với HTTP 403. Người có quyền ghi vào fork
`ibretsam/HowToLiveBetter` có thể đặt remote của bản khôi phục và đẩy đúng nhánh:

```sh
git remote set-url origin https://github.com/ibretsam/HowToLiveBetter.git
git push origin codex/vietnamese-cloud-checkpoint
```

Các lệnh này cần quyền GitHub hợp lệ của người thực hiện. Chưa có commit hoàn tất
nào được đẩy lên fork từ phiên cloud; gói ZIP và Git bundle bảo toàn toàn bộ
kết quả để việc cấp quyền không làm mất bản dịch.
