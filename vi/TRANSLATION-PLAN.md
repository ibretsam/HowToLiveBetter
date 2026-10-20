# Tiến độ và kế hoạch hoàn thành bản dịch tiếng Việt

Cập nhật: **20/10/2026 (giờ Việt Nam)**. Đây là kế hoạch công việc; chưa thiết lập lịch chạy tự động và chưa bắt đầu đợt dịch mới theo kế hoạch này.

## Phạm vi và phiên bản đích

Hoàn thành nội dung dành cho người đọc tại commit nguồn [`5f210ca953b7b538c042ad8515d5c355b766a194`](https://github.com/eternity4719/HowToLiveBetter/commit/5f210ca953b7b538c042ad8515d5c355b766a194): **34 chương, 765 mục, 9 bài viết dài và README/hướng dẫn đọc**, gồm tiêu đề, lời dẫn chương, bảng và liên kết. Tổng cộng 44 tệp nội dung. Đã kiểm tra GitHub ngày 20/10/2026: đây vẫn là commit mới nhất trên nhánh main của upstream.

Các commit nguồn xuất hiện sau mốc này được ghi thành đợt cập nhật riêng, để có tiêu chí hoàn thành rõ ràng. Mã nguồn, hướng dẫn đóng góp và nhật ký kiểm chứng không thuộc phạm vi dịch sách.

## Tiến độ đã kiểm chứng

| Trạng thái mục | Số lượng | Tỷ lệ trên 765 mục |
|---|---:|---:|
| Có bản nháp tiếng Việt, nguồn chưa đổi | 95 | 12,4% |
| Có bản tiếng Việt cũ, cần cập nhật | 554 | 72,4% |
| Chưa có bản dịch dùng được cho mục hiện tại | 116 | 15,2% |
| Tổng có bản tiếng Việt, gồm bản cũ | 649 | 84,8% |

**84,8% là độ phủ bản dịch, không phải tỷ lệ hoàn thành theo nguồn mới.** 95 mục còn khớp nguồn cũng vẫn là bản nháp AI, chưa được biên dịch viên chuyên nghiệp duyệt.

Bài viết dài: 1/9 bản nháp còn khớp nguồn, 7/9 cần cập nhật, 1/9 chưa dịch. Phần hướng dẫn đọc và lời dẫn chương cần đối chiếu riêng; không được bỏ qua khi đủ 765 mục.

Trong 554 mục thay đổi, có 404 mục đổi phần “Nói dễ hiểu”, 275 đổi “Lợi ích”, 364 đổi “Ghi chú”, 169 đổi “Nguồn”, 25 đổi “Chi phí” và 8 đổi “Mức độ bằng chứng”. Các nhóm chồng lấp. Cần dịch và soát những phần thay đổi trong ngữ cảnh cả mục, không mặc định dịch lại mọi câu cũ.

116 mục mới chứa khoảng 114.483 ký tự Hán; toàn bộ 554 mục cũ bị ảnh hưởng chứa khoảng 356.584 ký tự Hán (không phải tất cả đều thay đổi). Tám bài dài cần xử lý chứa khoảng 22.870 ký tự Hán. Đây là số đo độ lớn nguồn, không phải số từ tiếng Việt hoặc dự toán token.

Kiểm tra hiện tại:

- `python3 tools/check-vi.py`: đạt cho snapshot cũ 01/10/2026 — 137 lô, 4.103 đoạn, 43 tệp, 649 mục. Không dùng kết quả này để tuyên bố đã dịch xong nguồn mới.
- `python3 tools/check-vi-site.py`: đạt độ phủ 34 chương, 765 mục và 9 bài dài, cùng nhãn trạng thái và liên kết nguồn.
- Trang đọc đang hiển thị đầy đủ nội dung nguồn và cảnh báo bản dịch chưa hoàn tất.

## Kế hoạch và thời gian dự kiến

**Ước lượng ban đầu: 24–36 giờ xử lý chủ động**, gồm dịch, đối chiếu, sửa lỗi và triển khai. Đây chưa phải số đo tốc độ thực tế của đợt mới. Hiệu chỉnh ước lượng sau lô thử 20–30 mục có cả mục mới và mục sửa nhiều.

**Mục tiêu dự kiến: 26/10/2026**, nếu bắt đầu đợt dịch trong ngày 20/10 và dành khoảng 6 giờ xử lý chủ động mỗi ngày, không bị gián đoạn bởi giới hạn sử dụng. Các ngày dưới đây là lịch dự kiến, không phải cam kết chạy nền. Nếu phiên làm việc không tiếp tục hoặc phát sinh lỗi bảo toàn nội dung, ngày hoàn thành phải được tính lại theo số giờ còn lại.

| Giai đoạn | Công việc và sản phẩm cần đạt | Ước lượng | Mốc dự kiến |
|---|---|---:|---|
| 1. Chuẩn bị và đo tốc độ | Chốt danh sách mục; lưu dấu kiểm nguồn và trạng thái theo từng mục; điều chỉnh bộ xuất/kiểm tra đang ghim nguồn cũ để hỗ trợ bản dịch cập nhật từng phần; chạy lô thử 20–30 mục | 3–4 giờ | 20/10 |
| 2. Bổ sung nội dung thiếu | Dịch đủ 116 mục mới; rà soát song ngữ; lưu checkpoint sau từng lô | 5–7 giờ | 21/10 |
| 3. Cập nhật bản cũ | Đối chiếu và sửa 554 mục; giữ phần không thay đổi; kiểm tra lại 95 mục đang khớp nguồn | 9–13 giờ | 22–24/10 |
| 4. Hoàn thiện phần ngoài mục | Dịch bài dài mới, cập nhật 7 bài dài, kiểm tra bài còn lại; cập nhật README, thuật ngữ, 34 lời dẫn và tiêu đề chương | 3–5 giờ | 25/10 |
| 5. Rà soát và phát hành | Soát toàn bộ bản dịch theo nguồn; xử lý lỗi số liệu, ngưỡng, phủ định, liên kết; xác nhận thống kê; triển khai và kiểm tra trang thật | 4–7 giờ | 26/10 |

Lô thử thuộc khối lượng 765 mục, không cộng thêm mục ngoài phạm vi. Ưu tiên trong từng giai đoạn: cấp cứu, thuốc, sức khỏe, thai sản và trẻ nhỏ; tiếp theo pháp luật, lao động, tiền bạc; sau đó các chủ đề còn lại.

Thực hiện trực tiếp bằng AI trong phiên làm việc; kế hoạch không dựa vào dịch vụ dịch ngoài trả phí. Không tính thời gian chờ phiên làm việc hoặc hạn mức vào số giờ xử lý chủ động. Kết quả đích là **bản dịch AI đầy đủ, đã rà soát song ngữ và đạt kiểm tra tự động**, chưa bao gồm chứng nhận hoặc duyệt của chuyên gia y tế/pháp lý, biên dịch viên.

## Tiêu chí hoàn thành

- Có đủ bản tiếng Việt cho 765/765 mục và toàn bộ nội dung đọc trong 44 tệp của phiên bản đích.
- Mỗi mục, lời dẫn và bài dài có nguồn đối chiếu và bản ghi rà soát tương ứng; không đổi mốc nguồn chung để làm biến mất cảnh báo của phần chưa xử lý.
- Không còn mục/bài mang trạng thái thiếu hoặc cũ so với phiên bản đích; không còn placeholder trong nội dung đọc. Nguồn dẫn, trích dẫn nguyên văn và tên tài liệu có thể giữ tiếng Trung/Anh để tra cứu.
- Bảo toàn số liệu, đơn vị, điều kiện, phủ định, mức bằng chứng, trích dẫn và bối cảnh Trung Quốc; kiểm tra liên kết và thứ tự mục. Mọi lỗi kiểm tra nội dung phải được giải quyết trước khi ghi hoàn thành.
- Lời dẫn và hướng dẫn đọc có kiểm tra trạng thái thực tế, thay cho nhãn cũ được gán cố định trong bộ dựng trang hiện tại.
- Workflow Pages thành công; kiểm tra bản phát hành thực tế trên desktop/mobile, tìm kiếm, điều hướng và thông báo trạng thái.

Cập nhật báo cáo sau mỗi lô đã rà soát: số mục mới hoàn thành, số mục đã cập nhật, bài/lời dẫn đã xong, lỗi còn lại và ước lượng giờ còn lại. Chỉ tăng tiến độ khi bản dịch đã lưu, đối chiếu và đạt kiểm tra liên quan; không tăng vì tác vụ mới được bắt đầu.

## Danh sách theo chương

“Khớp nguồn” dưới đây chỉ có nghĩa là nguồn chưa đổi so với bản nháp hiện có. Các số được lấy từ dữ liệu trang dựng ngày 20/10/2026.

| Chương | Tổng mục | Khớp nguồn | Cần cập nhật | Chưa dịch |
|---|---:|---:|---:|---:|
| 1. Đừng chết sớm | 48 | 0 | 40 | 8 |
| 2. Đừng để mình chết dần | 47 | 10 | 32 | 5 |
| 3. Đừng lãng phí sức lực | 27 | 6 | 18 | 3 |
| 4. Đừng lãng phí thời gian | 18 | 9 | 9 | 0 |
| 5. Đừng lãng phí tiền | 50 | 17 | 27 | 6 |
| 6. Danh sách những việc tưởng lợi mà không lợi | 35 | 3 | 25 | 7 |
| 7. Sống thế nào khi không có tiền | 23 | 5 | 17 | 1 |
| 8. Đừng tự đẩy mình vào rắc rối: an toàn pháp lý và tài sản | 46 | 3 | 41 | 2 |
| 9. Những giới hạn pháp lý người bình thường dễ vi phạm | 29 | 2 | 21 | 6 |
| 10. Yêu và kết hôn có đáng không | 23 | 1 | 19 | 3 |
| 11. Những ranh giới pháp luật mà lập trình viên và người làm kỹ thuật dễ vượt qua | 21 | 2 | 15 | 4 |
| 12. Khởi nghiệp và kinh doanh: đừng mất cả tài sản gia đình | 28 | 0 | 23 | 5 |
| 13. Tình huống khẩn cấp: làm gì trước | 48 | 1 | 43 | 4 |
| 14. An toàn tài khoản và thông tin | 12 | 3 | 6 | 3 |
| 15. Thuê và mua nhà | 18 | 0 | 9 | 9 |
| 16. Sống thế nào sau khi mắc bệnh mạn tính | 14 | 1 | 8 | 5 |
| 17. Khi gia đình có người cao tuổi | 13 | 1 | 8 | 4 |
| 18. Nuôi con có đáng không | 7 | 1 | 5 | 1 |
| 19. Đang làm việc, nghỉ việc và tai nạn lao động | 24 | 5 | 13 | 6 |
| 20. Chăm trẻ mới sinh thế nào | 17 | 1 | 12 | 4 |
| 21. Ra nước ngoài, du lịch và an toàn ở nước ngoài | 13 | 1 | 10 | 2 |
| 22. Thư giãn thế nào: nơi giải trí và giảm căng thẳng | 12 | 1 | 9 | 2 |
| 23. Học kỹ năng nào đáng công | 25 | 5 | 18 | 2 |
| 24. Khám chữa bệnh: bớt tốn tiền, bớt đi đường vòng | 15 | 1 | 10 | 4 |
| 25. Những việc cần làm sau khi một người qua đời | 12 | 0 | 10 | 2 |
| 26. Làm website hoặc nền tảng: điều kiện, đăng ký và máy chủ | 13 | 1 | 10 | 2 |
| 27. Mang thai và sinh nở: từ phát hiện có thai đến xuất viện, làm giấy tờ | 20 | 3 | 13 | 4 |
| 28. Đừng làm hỏng sức khỏe vì ngoại hình | 10 | 0 | 8 | 2 |
| 29. Sau một cú sốc lớn | 14 | 2 | 11 | 1 |
| 30. Trẻ sau khi đi học | 21 | 3 | 14 | 4 |
| 31. Những con đường sau tuổi mười tám | 17 | 4 | 12 | 1 |
| 32. Du học: tư cách cư trú, làm thêm, bảo hiểm và công nhận bằng khi về nước | 12 | 3 | 7 | 2 |
| 33. Sống thế nào sau khi bị khuyết tật | 21 | 0 | 20 | 1 |
| 34. Đừng để thuốc dự trữ trong nhà gây họa | 12 | 0 | 11 | 1 |

Xem [thông tin và quy ước bản dịch](TRANSLATION.md) · [trang đọc](https://ibretsam.github.io/HowToLiveBetter/) · [thống kê máy đọc](https://ibretsam.github.io/HowToLiveBetter/coverage.json).
