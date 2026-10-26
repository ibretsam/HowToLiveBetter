# Skill quyết định trong đời sống (life-decision-guide)

Cho trợ lý AI dựa vào **Hướng dẫn sống tốt hơn với chi phí hợp lý** để trả lời câu hỏi cụ thể: có nên làm, có đáng, chọn thế nào, gặp sự cố làm gì trước, được nhận khoản hỗ trợ nào, làm vậy có phạm luật không.

Skill **tra các mục liên quan trong sách trước, rồi sắp xếp câu trả lời theo cách tính lợi ích và chi phí của sách**. Mỗi ý đều ghi chương và mục. Không tìm thấy thì nói rõ, không tự nhớ rồi điền số liệu.

Toàn bộ quy tắc nằm trong [SKILL.md](SKILL.md). Hai công cụ dùng chung tệp này, không duy trì hai bản khác nhau. Bản tiếng Việt giữ bối cảnh Trung Quốc của nguyên tác; số điện thoại, pháp luật và khoản trợ cấp không tự động áp dụng tại Việt Nam.

## Cài cho Claude Code

Mở Claude Code ngay trong kho này thì không cần cài: `.claude/skills/life-decision-guide/` đã trỏ tới quy tắc chung.

Để dùng từ mọi thư mục, tải bản tiếng Việt vào thư mục skill cá nhân:

```bash
mkdir -p ~/.claude/skills/life-decision-guide && curl -fsSL -o ~/.claude/skills/life-decision-guide/SKILL.md "https://raw.githubusercontent.com/ibretsam/HowToLiveBetter/main/skills/life-decision-guide/SKILL.md"
```

Sau đó hỏi trực tiếp “Mỗi ngày đi làm mất hai giờ có đáng không?” hoặc “Bạn nhờ tôi ký bảo lãnh, có nên ký không?”. Cũng có thể nói rõ “Dùng life-decision-guide để trả lời”.

## Cài cho Codex

Mở Codex trong kho này thì không cần cài: `AGENTS.md` ở thư mục gốc đã chỉ tới skill.

Để dùng ở mọi thư mục, tải vào thư mục skill cá nhân `~/.agents/skills`:

```bash
mkdir -p ~/.agents/skills/life-decision-guide && curl -fsSL -o ~/.agents/skills/life-decision-guide/SKILL.md "https://raw.githubusercontent.com/ibretsam/HowToLiveBetter/main/skills/life-decision-guide/SKILL.md"
```

Sau đó hỏi trực tiếp để kích hoạt theo mô tả, hoặc nhập `$life-decision-guide`. Dùng dấu `$`, không phải `/`; theo hướng dẫn của nguồn, bản Codex mới sẽ báo `Unrecognized command` nếu nhập `/life-decision-guide`. Nếu chưa thấy skill, khởi động lại Codex.

Các bản Codex cũ chưa có skill dùng lời nhắc tùy chỉnh: đặt tệp tại `~/.codex/prompts/life-decision-guide.md` rồi gọi bằng `/life-decision-guide`. Cách này đã được thông báo ngừng khuyến khích sử dụng ([openai/codex#10848](https://github.com/openai/codex/issues/10848)); bản mới dùng cách cài skill bên trên.

## Lấy nội dung sách ở đâu

Có kho trên máy thì đọc `book/` tại máy. Nếu chưa có, lấy bản tiếng Việt:

```bash
git clone --depth 1 https://github.com/ibretsam/HowToLiveBetter.git "${TMPDIR:-/tmp}/hltb"
```

Nguồn tiếng Trung mô tả dung lượng nội dung khoảng 1.3 MB và thao tác clone nông mất vài giây; dung lượng bản tiếng Việt khác. Không truy cập được mạng thì nói rõ không lấy được nội dung, không tự viết thay sách.

## Khi chỉnh sửa skill

Không chép vào SKILL.md danh sách hay số liệu sẽ thay đổi theo nội dung sách. Danh sách chương tra bảng “Những câu hỏi cuốn sách muốn trả lời” trong README; tên tệp chương hiện có xem trong `book/`. Thuật toán phân mức lợi ích/chi phí của bản gốc nằm ở hai phần định nghĩa `COST_W` và `e.ratio` trong `index.html` của nguồn tiếng Trung. Khi thêm/bớt chương hoặc đổi thuật toán, không cần duy trì một bản sao trong thư mục này.
