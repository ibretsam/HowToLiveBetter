# Tiến độ và kế hoạch hoàn thành bản dịch tiếng Việt

Cập nhật: **20/10/2026 (giờ Việt Nam), sau đợt 2**. Đã dịch và rà soát song ngữ độc lập tổng cộng 99 mục và bốn lời dẫn chương. Chưa thiết lập lịch chạy tự động.

## Phạm vi và phiên bản đích

Hoàn thành nội dung dành cho người đọc tại commit nguồn [`5f210ca953b7b538c042ad8515d5c355b766a194`](https://github.com/eternity4719/HowToLiveBetter/commit/5f210ca953b7b538c042ad8515d5c355b766a194): **34 chương, 765 mục, 9 bài viết dài và README/hướng dẫn đọc**, gồm tiêu đề, lời dẫn chương, bảng và liên kết. Tổng cộng 44 tệp nội dung. Đã kiểm tra GitHub ngày 20/10/2026: đây vẫn là commit mới nhất trên nhánh main của upstream.

Các commit nguồn xuất hiện sau mốc này được ghi thành đợt cập nhật riêng, để có tiêu chí hoàn thành rõ ràng. Mã nguồn, hướng dẫn đóng góp và nhật ký kiểm chứng không thuộc phạm vi dịch sách.

## Tiến độ đã kiểm chứng

| Trạng thái mục | Số lượng | Tỷ lệ trên 765 mục |
|---|---:|---:|
| Bản nháp tiếng Việt khớp nguồn hiện tại | 191 | 25,0% |
| Có bản tiếng Việt cũ, cần cập nhật | 478 | 62,5% |
| Chưa có bản dịch dùng được cho mục hiện tại | 96 | 12,5% |
| Tổng có bản tiếng Việt, gồm bản cũ | 669 | 87,5% |

**87,5% là độ phủ bản dịch, không phải tỷ lệ hoàn thành theo nguồn mới.** 191 mục khớp nguồn gồm 92 mục có nguồn chưa đổi chưa qua quy trình rà soát mới và 99 mục đã qua rà soát độc lập trong hai đợt. Tất cả vẫn là bản nháp AI, chưa được biên dịch viên chuyên nghiệp duyệt.

Lô thử đã xử lý **11 mục chưa dịch và 19 mục cần cập nhật**, cộng lời dẫn chương 34. Chương 34 có đủ 12/12 mục và lời dẫn khớp nguồn đích. Trước khi bắt đầu, số liệu là 95/554/116; danh sách công việc trong checkpoint giữ mốc ban đầu để đối chiếu.

**Đợt 2 xử lý 69 mục và ba lời dẫn:** dịch mới 9 mục, cập nhật 57 mục và rà soát lại 3 mục có nguồn chưa đổi. Hoàn thiện chương 13 (48/48 mục), chương 16 (14/14) và chương 20 (17/17), gồm cả lời dẫn. Cùng chương 34, hiện có bốn chương được rà soát đầy đủ theo nguồn đích. Hồ sơ từng mục ghi các lỗi đã sửa và điểm bất nhất của nguồn được giữ nguyên; xem `translation-checkpoint/vi-current/batch-2-report.json`.

Bài viết dài: 1/9 bản nháp còn khớp nguồn, 7/9 cần cập nhật, 1/9 chưa dịch. Phần hướng dẫn đọc và lời dẫn chương cần đối chiếu riêng; không được bỏ qua khi đủ 765 mục.

Ở mốc ban đầu, trong 554 mục thay đổi, có 404 mục đổi phần “Nói dễ hiểu”, 275 đổi “Lợi ích”, 364 đổi “Ghi chú”, 169 đổi “Nguồn”, 25 đổi “Chi phí” và 8 đổi “Mức độ bằng chứng”. Các nhóm chồng lấp. Cần dịch và soát những phần thay đổi trong ngữ cảnh cả mục, không mặc định dịch lại mọi câu cũ.

Ở mốc ban đầu, 116 mục mới chứa khoảng 114.483 ký tự Hán; toàn bộ 554 mục cũ bị ảnh hưởng chứa khoảng 356.584 ký tự Hán (không phải tất cả đều thay đổi). Tám bài dài cần xử lý chứa khoảng 22.870 ký tự Hán. Đây là số đo độ lớn nguồn, không phải số từ tiếng Việt hoặc dự toán token.

Kiểm tra hiện tại:

- `python3 tools/check-vi.py`: đạt cho snapshot cũ 01/10/2026 — 137 lô, 4.103 đoạn, 43 tệp, 649 mục. Không dùng kết quả này để tuyên bố đã dịch xong nguồn mới.
- `python3 tools/check-vi-site.py`: đạt độ phủ 34 chương, 765 mục và 9 bài dài, cùng nhãn trạng thái và liên kết nguồn.
- `python3 tools/check-vi-updates.py`: 103 bản nháp đạt, 103 bản ghi rà soát độc lập hợp lệ (99 mục và bốn lời dẫn).
- `python3 tools/test-vi-updates.py`: 7 bài kiểm tra bảo vệ checkpoint đạt, gồm số liệu, URL, thiếu trường, cấu trúc bảng, thuật ngữ giữ nguyên và sửa sau rà soát.
- Thử tiếp tục: 62 tệp bản nháp/rà soát giữ nguyên dấu kiểm sau khi chạy lại bước chuẩn bị.
- Trang đọc giữ cảnh báo cho phần chưa xử lý; nhãn lời dẫn lấy theo trạng thái thực tế.

## Kế hoạch và thời gian dự kiến

### Checklist trước khi bắt đầu

Các ô đã đánh dấu phản ánh việc đã thực hiện và có bằng chứng trong kho mã hoặc lần kiểm tra ngày 20/10/2026. Ô trống là việc còn phải làm; việc ghi vào checklist không có nghĩa là đã thực hiện.

**Đã có nền tảng**

- [x] Chốt nơi duy trì và xuất bản: fork `ibretsam/HowToLiveBetter`, trang GitHub Pages tiếng Việt đã hoạt động.
- [x] Chốt phiên bản nguồn `5f210ca` và phạm vi 44 tệp: 34 chương, 9 bài dài, README/hướng dẫn đọc; bao gồm lời dẫn, bảng và liên kết.
- [x] Ghi số liệu ban đầu: 95 mục còn khớp nguồn, 554 cần cập nhật, 116 chưa dịch; thống kê riêng bài dài và phần ngoài mục.
- [x] Lưu bản dịch cũ và checkpoint trong lịch sử Git; xác nhận kiểm tra snapshot cũ và kiểm tra độ phủ trang đọc đều đạt.
- [x] Ghi quy ước dịch và tiêu chí hoàn thành: giữ bối cảnh Trung Quốc, số liệu, nguồn dẫn, đơn vị, điều kiện và mức độ bằng chứng; công khai đây là bản dịch AI.

**Cần hoàn tất trước lô dịch thử**

- [x] Tạo nhánh làm việc `codex/…` từ trạng thái sạch; ghi commit khởi đầu để có thể đối chiếu và khôi phục. Chỉ đưa các lô đã kiểm tra lên nhánh xuất bản.
- [x] Xuất danh sách công việc theo từng mục/đoạn: ID, tệp, nguồn đích, dấu kiểm nguồn, bản dịch hiện có và phần nguồn thay đổi; xác minh các mục đổi tiêu đề hoặc số thứ tự được ghép đúng.
- [x] Đưa 34 lời dẫn chương, tiêu đề, README/thuật ngữ và 9 bài dài vào danh sách công việc riêng, tránh chỉ đếm 765 mục rồi bỏ sót phần còn lại.
- [x] Chuẩn bị cơ chế lưu và tiếp tục theo từng lô: bản dịch nháp, bản đã rà soát, dấu kiểm nguồn và lỗi còn lại. Chạy lại phải giữ được các lô đã đạt.
- [x] Điều chỉnh bộ xuất và kiểm tra để nhận bản dịch của nguồn mới theo từng mục/tệp; giữ kiểm tra snapshot cũ. Không chạy bộ lắp ghép cũ lên nguồn mới hoặc đổi mốc chung chỉ để xóa nhãn “chưa cập nhật”.
- [x] Chuẩn bị kiểm tra số liệu, đơn vị, liên kết, trích dẫn, trường nội dung và phần còn tiếng Trung; thử với dữ liệu có lỗi để chắc chắn công cụ phát hiện được. Phân biệt trích dẫn được giữ nguyên với văn xuôi chưa dịch.
- [x] Lập bảng thuật ngữ dùng chung từ bản dịch hiện có: y tế, pháp luật, bảo hiểm, tiền tệ và ngưỡng số; chốt cách xử lý tên riêng, trích dẫn và điểm không rõ nghĩa của nguồn.
- [x] Chia lô nhỏ theo chương/tệp, có thứ tự ưu tiên và bước rà soát song ngữ riêng. Nếu làm song song, mỗi tệp chỉ có một người hoặc tác vụ phụ trách tại một thời điểm.
- [x] Chọn 30 mục của chương 13, 19, 34 có mục mới/sửa, số liệu, phủ định và điều kiện. Kiểm tra liên kết trong lô; kiểm tra bảng bằng mẫu nguồn–bản dịch và 10 bảng trong hướng dẫn đọc hiện có.
- [x] Kiểm tra hạn mức và thời gian phiên làm việc thực tế; ghi cách dừng và tiếp tục khi hết hạn mức. Kế hoạch hiện dùng AI trong phiên làm việc, chưa có lịch chạy nền hay dịch vụ dịch ngoài trả phí.

**Cần đạt trước khi mở rộng dịch toàn bộ**

- [x] Hoàn thành lô thử, đối chiếu từng đoạn với nguồn và sửa hết lỗi; kiểm tra cấu trúc đạt. Kết quả lô thử được tính vào khối lượng chung.
- [x] Thử dừng rồi tiếp tục một lô; xác nhận không mất bản đã rà soát, không ghi đè nhầm và không tăng tiến độ cho bản còn lỗi.
- [x] Dựng trang thử với cả mục đã cập nhật và mục chưa xử lý; xác nhận nhãn trạng thái đúng, lời dẫn/bài dài được theo dõi, bản gốc và liên kết vẫn truy cập được.
- [x] Ghi thời gian lô thử trong `translation-checkpoint/vi-current/pilot-report.json`. Đánh giá lại ước lượng: tạm giữ 24–36 giờ và mốc mục tiêu 26/10/2026; thời gian chạy ba tác vụ song song không phải tổng giờ công, còn bài dài chưa được thử.

Chỉ bắt đầu dịch toàn bộ khi các mục trong hai nhóm “Cần hoàn tất” và “Cần đạt” đã được đánh dấu kèm kết quả kiểm tra. Không cần hoàn thành bản dịch toàn bộ để vượt qua checklist chuẩn bị này.

**Ước lượng đang giữ: 24–36 giờ xử lý chủ động**, gồm dịch, đối chiếu, sửa lỗi và triển khai. Lô thử đã được đo, nhưng có ba tác vụ song song và chưa bao phủ bài dài; chưa đủ cơ sở rút ngắn lịch chỉ theo thời gian chạy của lô này. Ước lượng sẽ được hiệu chỉnh tiếp sau lô có bài dài. Mốc 26/10 vẫn là mục tiêu có điều kiện, không phải cam kết tự chạy nền.

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

“Khớp nguồn” gồm bản nháp có nguồn chưa đổi và bản cập nhật đã được rà soát theo nguồn đích. Các số được lấy từ dữ liệu trang dựng sau đợt 2 ngày 20/10/2026.

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
| 13. Tình huống khẩn cấp: làm gì trước | 48 | 48 | 0 | 0 |
| 14. An toàn tài khoản và thông tin | 12 | 3 | 6 | 3 |
| 15. Thuê và mua nhà | 18 | 0 | 9 | 9 |
| 16. Sống thế nào sau khi mắc bệnh mạn tính | 14 | 14 | 0 | 0 |
| 17. Khi gia đình có người cao tuổi | 13 | 1 | 8 | 4 |
| 18. Nuôi con có đáng không | 7 | 1 | 5 | 1 |
| 19. Đang làm việc, nghỉ việc và tai nạn lao động | 24 | 13 | 11 | 0 |
| 20. Chăm trẻ mới sinh thế nào | 17 | 17 | 0 | 0 |
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
| 34. Đừng để thuốc dự trữ trong nhà gây hại | 12 | 12 | 0 | 0 |

Xem [thông tin và quy ước bản dịch](TRANSLATION.md) · [trang đọc](https://ibretsam.github.io/HowToLiveBetter/) · [thống kê máy đọc](https://ibretsam.github.io/HowToLiveBetter/coverage.json).
