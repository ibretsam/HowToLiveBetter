# Thông tin về bản dịch tiếng Việt

Đây là bản dịch tiếng Việt chưa chính thức của **《高性价比人生指南》 — Hướng dẫn sống tốt hơn với chi phí hợp lý**, do [eternity4719](https://github.com/eternity4719) biên soạn và duy trì. [Đọc bản dịch](README.md) · [Xem bản gốc](../README.md).

Bản dịch dựa trên nội dung ngày **01/10/2026**, tại phiên bản [`6f6d969abe19fd4aa8b30979d634f2a187be0a55`](https://github.com/eternity4719/HowToLiveBetter/tree/6f6d969abe19fd4aa8b30979d634f2a187be0a55). Phạm vi gồm phần hướng dẫn đọc và thuật ngữ trong README, toàn bộ 34 chương với 649 mục, cùng tám bài viết dài dành cho người đọc. Mã nguồn, hướng dẫn dành cho người đóng góp, kỹ năng AI và nhật ký kiểm chứng vẫn dùng bản gốc.

## Cách thực hiện và tình trạng rà soát

**Bản dịch chưa hoàn thành.** Checkpoint hiện có 26/137 lô kết quả từ Cloudflare Workers AI, chứa 993/4.103 đoạn; còn thiếu 111 lô. Chỉ chương 18 đã được xuất thành tệp dịch. README tiếng Việt và 41 tài liệu nguồn còn lại chưa được xuất. Đây là **bản nháp dịch máy**, chưa được biên dịch viên hoặc chuyên gia rà soát toàn bộ.

Kiểm tra cloud phát hiện 31 đoạn không khớp ký hiệu bảo vệ, 336 đoạn cần đối chiếu số và 17 đoạn còn chữ Trung trong kết quả dịch. Các nhóm này có thể trùng nhau. Chênh lệch số có thể do cách viết dấu phân cách, nhưng cũng có đoạn lệch thứ tự hoặc bị cắt; không được coi cache là bản dịch đã đạt kiểm tra. Chưa kiểm tra xong toàn bộ liên kết nội bộ và ý nghĩa từng câu. Xem [báo cáo kiểm tra](../translation-checkpoint/cloud-qa.json) và [tình trạng cloud](../translation-checkpoint/CLOUD-STATUS.md).

Các tiêu đề, chi phí, phần “Nói dễ hiểu”, lợi ích và ghi chú được chuyển sang tiếng Việt. Số thứ tự chương và mục, mức độ bằng chứng A/B/C, các số liệu và ký hiệu thống kê được giữ để đối chiếu. Mục “Nguồn” giữ nguyên tên tài liệu, thông tin thư mục và trích dẫn trong bản gốc, kể cả tiếng Trung hoặc tiếng Anh, để người đọc tra cứu chính xác. Các chú thích HTML dùng cho công cụ của bản gốc cũng được giữ nguyên.

## Bối cảnh của nội dung

Luật, thủ tục, trợ cấp, bảo hiểm y tế, bảo hiểm xã hội và số điện thoại trong sách thuộc **Trung Quốc đại lục**, trừ khi bản gốc ghi rõ quốc gia khác. Số tiền tính bằng **nhân dân tệ (CNY)**, trừ khi ghi rõ đơn vị khác. Bản dịch giữ bối cảnh và thời điểm của bản gốc; không thay chúng bằng quy định, đơn vị tiền hoặc số điện thoại của Việt Nam.

Các đường dẫn đến trang tìm kiếm trực tuyến, PDF, EPUB, bản HTML ngoại tuyến và kỹ năng AI của dự án gốc dẫn đến **nội dung tiếng Trung**. Bản tiếng Việt hiện được cung cấp dưới dạng Markdown trong thư mục `vi/`. Các liên kết đến nhật ký kiểm chứng cũng dẫn về tài liệu gốc tiếng Trung.

## Ghi công và giấy phép

Tác phẩm gốc: **高性价比人生指南**, tác giả **eternity4719**, tại [HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter).

Nội dung bản dịch được chia sẻ theo [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) — cùng giấy phép với [nội dung gốc](../LICENSE). Thay đổi trong bản này là chuyển ngữ sang tiếng Việt, thêm hướng dẫn về bản dịch và điều chỉnh liên kết nội bộ. Bản dịch không hàm ý tác giả gốc đã kiểm tra hoặc chứng thực nội dung tiếng Việt.

Tác giả gốc yêu cầu bản dịch được duy trì trong fork riêng. Khi cập nhật, hãy ghi lại phiên bản nguồn, đối chiếu từng mục thay đổi và giữ nguyên các nguồn dẫn. [Danh sách đối chiếu tệp](translation-manifest.json) ghi đường dẫn nguồn, đường dẫn bản dịch và dấu kiểm SHA-256 của từng tệp nguồn.

Để kiểm tra bản dịch trong bản sao kho mã này, chạy `python3 tools/check-vi.py` từ thư mục gốc.
