# Thông tin về bản dịch tiếng Việt

Đây là bản dịch tiếng Việt chưa chính thức của **《高性价比人生指南》 — Hướng dẫn sống tốt hơn với chi phí hợp lý**, do [eternity4719](https://github.com/eternity4719) biên soạn và duy trì. [Đọc bản dịch](README.md) · [Xem bản gốc](../README.md).

Bản dịch dựa trên nội dung ngày **01/10/2026**, tại phiên bản [`6f6d969abe19fd4aa8b30979d634f2a187be0a55`](https://github.com/eternity4719/HowToLiveBetter/tree/6f6d969abe19fd4aa8b30979d634f2a187be0a55). Phạm vi gồm phần hướng dẫn đọc và thuật ngữ trong README, toàn bộ 34 chương với 649 mục, cùng tám bài viết dài dành cho người đọc. Mã nguồn, hướng dẫn dành cho người đóng góp, kỹ năng AI và nhật ký kiểm chứng vẫn dùng bản gốc.

## Cách thực hiện và tình trạng rà soát

**Đã dịch đủ phạm vi 43 tệp:** README, 34 chương với 649 mục và tám bài viết dài. Có đủ 137/137 lô, tương ứng 4.103/4.103 đoạn trong kế hoạch dịch. Ví dụ Markdown và chú thích trong ví dụ lệnh của README cũng đã được chuyển ngữ.

Bản dịch được thực hiện trực tiếp bằng mô hình AI, đối chiếu với từng đoạn nguồn, sau đó được AI rà soát song ngữ lần hai để sửa các lỗi nghĩa (phủ định bị đảo, điều kiện, ngưỡng “từ N trở lên/trở xuống”, thuật ngữ y khoa và pháp lý) và viết lại các câu quá vắn tắt. Không dùng Google Translate hay dịch vụ dịch trả phí. Các đoạn dịch đã duyệt nằm trong `translation-checkpoint/vi-reviewed-cache/`; tệp Markdown trong `vi/` được sinh lại từ đó bằng `python3 tools/assemble-vi.py`.

Kiểm tra tự động đạt: đủ tệp, đoạn và số thứ tự; đúng ID và thứ tự các đoạn; giữ các số viết bằng chữ số, mức độ bằng chứng và chú thích HTML; giữ nguồn dẫn và địa chỉ bên ngoài; giữ cấu trúc tiêu đề, trường thông tin, bảng và ví dụ mã; các liên kết tương đối và neo nội bộ tồn tại. Xem [báo cáo hiện tại](../translation-checkpoint/current-qa.json).

Đây vẫn là **bản nháp do AI dịch**, chưa được biên dịch viên hoặc chuyên gia y tế, pháp luật duyệt. Việc đủ nội dung và đạt kiểm tra cấu trúc không chứng minh mọi câu dịch đều chính xác. Các khẳng định và hướng dẫn của nguồn được giữ theo phiên bản đã ghi, chưa được kiểm chứng độc lập hay cập nhật. Những chỗ nguồn có bất nhất cũng không được âm thầm sửa trong bản dịch.

Các tiêu đề, chi phí, phần “Nói dễ hiểu”, lợi ích và ghi chú được chuyển sang tiếng Việt. Số thứ tự chương và mục, mức độ bằng chứng A/B/C, các số liệu và ký hiệu thống kê được giữ để đối chiếu. Mục “Nguồn” giữ nguyên tên tài liệu, thông tin thư mục và trích dẫn trong bản gốc, kể cả tiếng Trung hoặc tiếng Anh, để người đọc tra cứu chính xác. Các chú thích HTML dùng cho công cụ của bản gốc cũng được giữ nguyên.

## Bối cảnh của nội dung

Luật, thủ tục, trợ cấp, bảo hiểm y tế, bảo hiểm xã hội và số điện thoại trong sách thuộc **Trung Quốc đại lục**, trừ khi bản gốc ghi rõ quốc gia khác. Số tiền tính bằng **nhân dân tệ (CNY)**, trừ khi ghi rõ đơn vị khác. Bản dịch giữ bối cảnh và thời điểm của bản gốc; không thay chúng bằng quy định, đơn vị tiền hoặc số điện thoại của Việt Nam.

Khi nguồn dùng đơn vị số lớn của Trung Quốc, bản dịch giữ nguyên con số để dễ đối chiếu: **vạn** (万) nghĩa là mười nghìn, 亿 được viết là **trăm triệu** và 万亿 là **nghìn tỷ**. Chẳng hạn “5 vạn nhân dân tệ” là năm mươi nghìn nhân dân tệ, “86.5 trăm triệu nhân dân tệ” là 8,65 tỷ nhân dân tệ.

Số thập phân giữ **dấu chấm** như bản gốc, không dùng dấu phẩy kiểu Việt Nam: “0.4 miligam” là không phẩy bốn miligam, không phải bốn trăm miligam. Ngưỡng “từ N trở lên” và “N trở xuống” bao gồm chính số N.

Các đường dẫn đến trang tìm kiếm trực tuyến, PDF, EPUB, bản HTML ngoại tuyến và kỹ năng AI của dự án gốc dẫn đến **nội dung tiếng Trung**. Bản tiếng Việt hiện được cung cấp dưới dạng Markdown trong thư mục `vi/`. Các liên kết đến nhật ký kiểm chứng cũng dẫn về tài liệu gốc tiếng Trung.

## Ghi công và giấy phép

Tác phẩm gốc: **高性价比人生指南**, tác giả **eternity4719**, tại [HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter).

Nội dung bản dịch được chia sẻ theo [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) — cùng giấy phép với [nội dung gốc](../LICENSE). Thay đổi trong bản này là chuyển ngữ sang tiếng Việt, thêm hướng dẫn về bản dịch và điều chỉnh liên kết nội bộ. Bản dịch không hàm ý tác giả gốc đã kiểm tra hoặc chứng thực nội dung tiếng Việt.

Tác giả gốc yêu cầu bản dịch được duy trì trong fork riêng. Khi cập nhật, hãy ghi lại phiên bản nguồn, đối chiếu từng mục thay đổi và giữ nguyên các nguồn dẫn. [Danh sách đối chiếu tệp](translation-manifest.json) ghi đường dẫn nguồn, đường dẫn bản dịch và dấu kiểm SHA-256 của từng tệp nguồn.

Để kiểm tra bản dịch trong bản sao kho mã này, chạy `python3 tools/check-vi.py` từ thư mục gốc.
