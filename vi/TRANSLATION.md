# Thông tin về bản dịch tiếng Việt

**Tiến độ và lịch dự kiến:** [Kế hoạch hoàn thành bản dịch — cập nhật 20/10/2026](TRANSLATION-PLAN.md).

**Đã hoàn tất đợt 4 ngày 20/10/2026:** thêm 95 mục, ba lời dẫn và bài hướng dẫn sau thôi việc gồm 34 việc đã được dịch, rà soát song ngữ độc lập và kiểm tra: 12 mục mới, 59 mục cập nhật và 24 mục được kiểm tra lại. Tổng bốn đợt có 242 mục, mười lời dẫn và hai bài hướng dẫn được rà soát theo nguồn đích. Trang dựng hiện có 303 mục khớp nguồn, 387 mục cần cập nhật và 75 mục chưa dịch. Các chương 5, 9, 13, 16, 18, 19, 20, 27, 30 và 34 đã có đủ các mục cùng lời dẫn theo nguồn mới. [Checkpoint và quy trình tiếp tục](https://github.com/ibretsam/HowToLiveBetter/tree/main/translation-checkpoint/vi-current).

Các tệp Markdown cũ trong `vi/book/`, `vi/docs/` và `vi/README.md` vẫn là bản lưu theo nguồn 01/10 để kiểm tra hồi quy. Trang đọc áp dụng các bản cập nhật đã rà soát trong checkpoint lên dữ liệu hiển thị, với liên kết phiên bản nguồn riêng cho từng mục; không đổi mốc nguồn chung của phần chưa xử lý.

**Trang đọc hiện tại:** [ibretsam.github.io/HowToLiveBetter](https://ibretsam.github.io/HowToLiveBetter/).

Ngày **20/10/2026**, fork đã đồng bộ mã nguồn và nội dung Trung văn đến commit [`5f210ca`](https://github.com/eternity4719/HowToLiveBetter/commit/5f210ca953b7b538c042ad8515d5c355b766a194): **34 chương, 765 mục và chín bài viết dài**. Bản dịch được phục hồi từ nhánh `codex/vietnamese-cloud-checkpoint` của fork, commit `7128efb`.

Trang đọc so sánh từng mục với phiên bản dùng để dịch:

- **Bản nháp tiếng Việt:** có bản dịch và nội dung nguồn của mục chưa thay đổi.
- **Bản dịch chưa cập nhật:** có bản dịch cũ, nhưng nguồn mới đã thay đổi. Trang ghi rõ bản dịch vẫn chưa hoàn tất theo nguồn mới và cho đối chiếu toàn bộ bản gốc mới.
- **Chưa hoàn tất bản dịch:** nội dung mới chưa có bản dịch, hoặc chưa thể ghép bản dịch cũ với mục hiện tại một cách chắc chắn. Trang hiển thị đầy đủ tiếng Trung, không bỏ mục.

Nguồn, mức độ bằng chứng và chi phí trên nhãn của trang lấy từ phiên bản mới; nội dung tiếng Việt cũ được giữ nguyên và ghi rõ ngày nguồn. Lời dẫn chương và hướng dẫn đọc chưa được cập nhật tiếp tục mang cảnh báo; lời dẫn các chương 5, 9, 13, 16, 18, 19, 20, 27, 30 và 34 cùng bài hướng dẫn trước/sau sinh và sau thôi việc đã qua rà soát được ghi nhận theo nguồn mới. Xem [tổng hợp tình trạng hiện tại](https://ibretsam.github.io/HowToLiveBetter/coverage.json). Những mô tả “đã dịch đủ” bên dưới chỉ áp dụng cho **phiên bản 01/10/2026**, không phải tất cả thay đổi mới.

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

Với đơn vị tiền nhỏ, **hào** (角) bằng một phần mười nhân dân tệ; **phân** (分) bằng một phần trăm nhân dân tệ.

Số thập phân giữ **dấu chấm** như bản gốc, không dùng dấu phẩy kiểu Việt Nam: “0.4 miligam” là không phẩy bốn miligam, không phải bốn trăm miligam. Ngưỡng “từ N trở lên” và “N trở xuống” bao gồm chính số N.

Các đường dẫn đến PDF, EPUB, bản HTML ngoại tuyến và kỹ năng AI của dự án gốc dẫn đến **nội dung tiếng Trung**. Bản tiếng Việt có trang đọc GitHub Pages riêng và các tệp Markdown trong `vi/`. Các liên kết đến nhật ký kiểm chứng dẫn về tài liệu gốc tiếng Trung. Các nút tra cứu trực tuyến trong README được dịch từ phiên bản cũ vẫn trỏ về trang gốc; dùng liên kết trang tiếng Việt ở đầu tài liệu này.

## Ghi công và giấy phép

Tác phẩm gốc: **高性价比人生指南**, tác giả **eternity4719**, tại [HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter).

Nội dung bản dịch được chia sẻ theo [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) — cùng giấy phép với [nội dung gốc](../LICENSE). Thay đổi trong bản này là chuyển ngữ sang tiếng Việt, thêm hướng dẫn về bản dịch và điều chỉnh liên kết nội bộ. Bản dịch không hàm ý tác giả gốc đã kiểm tra hoặc chứng thực nội dung tiếng Việt.

Tác giả gốc yêu cầu bản dịch được duy trì trong fork riêng. Khi cập nhật, hãy ghi lại phiên bản nguồn, đối chiếu từng mục thay đổi và giữ nguyên các nguồn dẫn. [Danh sách đối chiếu tệp](translation-manifest.json) ghi đường dẫn nguồn, đường dẫn bản dịch và dấu kiểm SHA-256 của từng tệp nguồn.

Để kiểm tra bản dịch trong bản sao kho mã này, chạy `python3 tools/check-vi.py` từ thư mục gốc.

## Xây dựng và cập nhật trang đọc

Từ thư mục gốc:

```sh
npm --prefix tools/epub ci
python3 tools/check-vi.py
python3 tools/check-vi-updates.py
python3 tools/test-vi-updates.py
python3 tools/build-vi-site.py
python3 tools/check-vi-site.py
python3 -m http.server 8000 --directory dist/vi-site
```

Mở `http://localhost:8000`. Workflow `.github/workflows/vietnamese-pages.yml` chạy khi nội dung liên quan thay đổi trên nhánh `main`, kiểm tra rồi triển khai `dist/vi-site` lên GitHub Pages của fork.

Đợt dịch hiện tại ghim nguồn `5f210ca`. Khi đồng bộ upstream tiếp, cần lập đợt checkpoint mới và đối chiếu lại các bản cập nhật theo nguồn mới trước khi đổi `source_commit` và `synced_at` trong `vi/site-config.json`. Không đổi dấu kiểm hoặc mốc nguồn của bản dịch cũ chỉ để vượt qua kiểm tra. Giữ `translation_base_commit` cho bản lưu 01/10. Công cụ không tự dịch nội dung mới; nếu checkpoint không khớp nguồn xuất bản, quá trình dựng trang sẽ dừng. Trình kiểm tra bản dịch cũ đối chiếu snapshot đã ghim trong Git, trình kiểm tra bản cập nhật xác nhận nguồn và rà soát từng phần, còn trình kiểm tra trang đọc xác nhận mọi mục đều có mặt với nhãn đúng.
