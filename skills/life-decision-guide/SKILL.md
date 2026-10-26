---
name: life-decision-guide
description: Dùng nội dung Hướng dẫn sống tốt hơn với chi phí hợp lý của eternity4719 (github.com/eternity4719/HowToLiveBetter), qua bản dịch Việt tại github.com/ibretsam/HowToLiveBetter, để trả lời quyết định cụ thể trong đời sống — có nên làm, có đáng, chọn thế nào, gặp sự cố làm gì trước, được nhận khoản nào, có phạm luật không. Tra mục trước, so sánh chi phí tiền/thời gian/nỗ lực, mức lợi ích và bằng chứng A/B/C, luôn ghi chương và mục. Từ kích hoạt gồm có nên, có đáng, có cần, chọn thế nào, giúp tôi quyết định, có phạm luật không, được nhận gì, làm gì trước.
---

# Quyết định trong đời sống: tra sách trước khi trả lời

## Skill này làm gì

Khi có câu hỏi cụ thể về một việc trong đời sống, tra các mục liên quan trong **Hướng dẫn sống tốt hơn với chi phí hợp lý**, rồi sắp xếp câu trả lời theo cách tính của sách.

**Không tra được thì không trình bày như đã tra.** Mỗi con số, điều luật và kết luận phải dẫn được về một mục trong nội dung sách. Nếu không có mục tương ứng, nói rõ sách không đề cập. Có thể đưa nhận định thông thường, nhưng phải ghi rõ đó là hiểu biết chung, không phải nội dung sách. Không tự điền số liệu, DOI hay số điều luật từ trí nhớ.

Sách chia lợi ích thành bốn loại: tuổi thọ, thời gian và sức lực, tiền bạc, tự do thân thể. **Tính riêng từng loại, không quy đổi chéo**: “tổng tử vong giảm 12%” và “mỗi năm tiết kiệm 500 nhân dân tệ” không cùng một thước đo.

Bản dịch giữ nguyên bối cảnh Trung Quốc của nguồn. Các số 120, 119, 12356 bên dưới là số trong hướng dẫn gốc cho Trung Quốc; không giới thiệu chúng như số trợ giúp tại Việt Nam hay quốc gia khác. Khi áp dụng câu trả lời, xác định đúng địa phương và tuân thủ quy tắc an toàn của công cụ đang sử dụng.

## Bước 0: xem có cần xử lý ngay không

- **Tình huống cấp cứu đang diễn ra** (ngã bất tỉnh không thở, chảy máu nhiều, cháy, đuối nước, điện giật, ngộ độc, dấu hiệu đột quỵ hoặc nhồi máu cơ tim): trước hết nêu việc gọi 120 / 119 trong bối cảnh Trung Quốc và hành động đầu tiên tại hiện trường theo chương 13, không mở đầu bằng phân tích lợi ích/chi phí.
- **Nhắc đến ý nghĩ tự sát hoặc không sống nổi nữa**: hướng dẫn gốc đưa đường dây hỗ trợ tâm lý toàn quốc Trung Quốc 12356 trước, rồi dùng các mục trong chương 1 và chương 29. Không phân tích theo kiểu khuyên răn, không đánh giá động cơ.
- **Đang trong thủ tục pháp lý** (đã bị triệu tập, tạm giữ hoặc khởi kiện): trước hết chỉ tới mục tương ứng ở chương 8, nói rõ sách chỉ đưa nguyên tắc chung và vụ việc cụ thể cần luật sư.
- Trường hợp khác làm theo các bước dưới đây.

## Bước 1: lấy nội dung sách

**Tại máy**: nếu thư mục hiện tại hoặc thư mục cha có `README.md` và `book/01-不要早死.md` thì đọc trực tiếp. Tên tệp của fork giữ nguyên để không làm hỏng liên kết; nội dung đã chuyển sang tiếng Việt.

**Từ xa**: nếu chưa có kho, tải bản tiếng Việt. Clone nông một lần để dùng các lệnh tiếp theo:

```bash
git clone --depth 1 https://github.com/ibretsam/HowToLiveBetter.git "${TMPDIR:-/tmp}/hltb"
```

Hướng dẫn gốc mô tả toàn bộ nội dung tiếng Trung khoảng 1.3 MB; dung lượng bản dịch Việt khác. Nếu không dùng được Git, tải từng tệp; có thể viết trực tiếp chữ Trung Quốc trong tên tệp:

```bash
curl -fsSL --compressed "https://raw.githubusercontent.com/ibretsam/HowToLiveBetter/main/book/02-不要慢慢死.md"
```

Cả hai cách đều không được thì nói thật là không lấy được nội dung. Không thuật lại sách theo ấn tượng.

## Bước 2: xác định chương

Chọn trước 1 đến 3 chương: đọc bảng “Những câu hỏi cuốn sách muốn trả lời” trong README ở thư mục gốc. Mỗi chương chiếm một dòng, cho biết chương trả lời chuyện gì. Đối chiếu vấn đề người dùng hỏi với bảng này. Khi chương được thêm/bớt, bảng cũng thay đổi; không giữ thêm danh sách chương trong skill.

Tệp chương ở `book/`, có số chương và tên chương trong tên tệp. Chạy `ls book/` để xem đủ danh sách và tìm đúng tệp theo số.

Các bài dài ở `docs/`, chẳng hạn kết hôn có đáng không, trang bị khẩn cấp cho gia đình, giấy phép cho nền tảng, có nên dừng lại giúp người lạ gặp nạn.

## Bước 3: tìm mục

Nguồn gốc ghi tệp chương lớn nhất khoảng 110 KB; không cần đọc cả chương ngay, hãy tìm theo từ khóa. Nếu có công cụ Grep/Read thì dùng công cụ; nếu chỉ có shell thì dùng lệnh. Kích thước bản tiếng Việt có thể lớn hơn:

```bash
rg -n '^### ' book/ | rg 'từ khóa 1|từ khóa 2'  # Xem tiêu đề trước
rg -n -B2 -A8 'từ khóa' book/08-别把自己搭进去.md  # Tìm kèm ngữ cảnh
sed -n '/^### 16\. /,/^### 17\. /p' book/08-别把自己搭进去.md  # Lấy trọn mục theo số
```

**Đọc hết mục đã tìm**, đặc biệt là trường “Ghi chú”: đối tượng áp dụng, tranh luận và ngoại lệ đều nằm ở đó. Chỉ đọc tiêu đề sẽ làm mất điều kiện.

Một mục có dạng:

```markdown
### 5. Đổi muối ăn trong nhà sang muối ít natri (muối kali)
<!-- 成本标签: 钱=少 时间=少 毅力=否 收益=中 口径=死亡率 -->
- Chi phí: Mỗi túi đắt thêm vài nhân dân tệ
- Nói dễ hiểu: …xác suất tử vong thấp hơn khoảng 12%…
- Lợi ích: Đột quỵ giảm 14%, biến cố tim mạch giảm 13%, tổng tử vong giảm 12%
- Mức độ bằng chứng: A
- Nguồn: Neal B, et al. (2021). NEJM. https://doi.org/10.1056/NEJMoa2105675
- Ghi chú: Còn tranh luận. Người suy giảm chức năng thận hoặc đang dùng thuốc lợi tiểu giữ kali không dùng. …
```

Chú thích HTML là nhãn chi phí cho máy đọc, giữ nguyên mã của nguồn: tiền `钱=0/少/多` (không tốn/ít/nhiều), thời gian `时间=少/中/多` (ít/vừa/nhiều), nỗ lực `毅力=否/些/是` (không/một ít/có), lợi ích `收益=大/中/小` (lớn/vừa/nhỏ), loại lợi ích `口径=死亡率/金钱/时间/自由` (tử vong/tiền bạc/thời gian/tự do). Một số mục có thêm `人群=`: `怀孕` (mang thai), `婴幼儿` (trẻ nhỏ), `孩子` (trẻ em), `老人` (người cao tuổi), `35岁`, `60岁`, `女性` (phụ nữ). Dấu phẩy là “hoặc”, dấu cộng là “và”. Nhãn này cho biết chỉ hữu ích với những nhóm đó; người dùng rõ ràng không thuộc nhóm thì có thể không đề xuất mục đó.

## Bước 4: sắp xếp

Dùng thuật toán của sách, không phân loại theo cảm giác:

1. Thuật toán phân mức lấy từ `index.html` của bản nguồn, không viết lại theo trí nhớ. Đọc trực tiếp hai dòng:

   ```bash
   rg -n 'COST_W = |e\.ratio = ' index.html
   ```

   Dòng trước là trọng số mỗi mức trong ba loại chi phí; điểm chi phí bằng tiền + thời gian + nỗ lực. Dòng sau ghép mức lợi ích và điểm chi phí thành “rất cao / cao / thông thường”. Trang tiếng Việt không có bộ lọc này; chỉ dùng thuật toán khi thực sự đã đọc mã nguồn gốc.
2. Nếu chỉ tải từng tệp nội dung bằng curl, không có `index.html`, đừng nêu mức lợi ích/chi phí. Thay vào đó liệt kê đúng mức lợi ích và ba nhãn chi phí để người dùng tự cân nhắc.
3. Trước hết sắp theo mức lợi ích/chi phí; cùng mức thì theo bằng chứng A > B > C, rồi theo độ phù hợp với hoàn cảnh người dùng.
4. **Không xếp hạng chéo giữa các loại lợi ích**. Những mục đổi lấy tiền và những mục đổi lấy tuổi thọ được liệt kê riêng, mỗi nhóm có thứ tự riêng.
5. “Thông thường” không có nghĩa là không nên làm; người dùng phải tự cân nhắc chi phí đó. Phân mức lợi ích/chi phí là nhận định của tác giả, theo tiêu chuẩn của sách chỉ tính là mức C; đây là chuyện khác với mức bằng chứng.

## Bước 5: viết câu trả lời

Sau khi sắp xếp, dùng cấu trúc sau:

1. **Kết luận trong một câu**: có đáng không, có nên làm không, bước đầu là gì.
2. **Những việc nên làm trước**: 3 đến 7 mục theo thứ tự bên trên. Mỗi mục một đến ba dòng, gồm hành động bắt đầu bằng động từ, chi phí, lợi ích, mức bằng chứng và xuất xứ kiểu “chương 8, mục 17 (giấy vay nợ và bảo lãnh)”. Cụm trong ngoặc lấy từ tiêu đề để người đọc tìm lại.
3. **Không nên làm / không cần làm**: tách riêng những việc sách nói rõ không đáng hoặc có bằng chứng ngược lại.
4. **Sách không đề cập**: nói thật; không trình bày hiểu biết chung như nội dung sách.
5. Nếu cần, thêm một câu cho biết khi nào nên xem lại quyết định hoặc dấu hiệu nào khiến cần đổi ý.

Khi viết, giữ các nguyên tắc sau:

- **Nói rõ ai được lợi**. Sách chia thành bốn nhóm theo khả năng lợi ích quay về bản thân, từ cao đến thấp: ① chính bạn; ② vợ/chồng và thân nhân trực hệ; ③ bạn bè, đồng nghiệp, họ hàng khác; ④ người lạ. Với nhóm ④ (cứu người lạ, bảo lãnh, giúp chuyển tiền), nêu cả lợi ích và rủi ro bị vu vạ, bị cuốn vào vụ việc, bị trả đũa. Không chỉ nói mặt lợi, cũng không khuyên mặc kệ tất cả.
- **“Pháp luật bảo vệ bạn” phải đi cùng chi phí của quá trình**. Chỉ nêu kết quả mà bỏ quá trình là coi xác suất thắng kiện như lợi ích. Cần nói có phải kiện không, khoảng bao lâu và ai trả luật sư. Hướng dẫn skill gốc ghi “sơ thẩm thông thường từ 6 tháng, có thể kéo dài; thủ tục đơn giản 3 tháng”; khi trả lời phải đối chiếu bản nội dung hiện hành, trong đó thời hạn thông thường được diễn đạt là theo quy định xét xử trong 6 tháng, có thể gia hạn, không phải dự báo thời gian thực tế. Phí luật sư không nằm trong chi phí tố tụng mà quy tắc “bên thua chịu” đề cập.
- **Giữ đúng số liệu của mục**, không thay số nào. Giữ khoảng tin cậy, đối tượng và năm nếu mục có ghi. Khi giải thích HR, RR, OR bằng ngôn ngữ thường dùng, vẫn giữ giá trị gốc và ý nghĩa đúng của từng chỉ số; không tự thêm số liệu, triệu chứng hay cơ chế mà mục không có.
- **Viết dễ hiểu** để người trưởng thành không được đào tạo chuyên môn đọc một lần là hiểu. Giải thích thuật ngữ ngay bằng lời thường; pháp luật cần nói thành hậu quả gì, nên làm gì. Trường nguồn giữ nguyên để đối chiếu.
- **Giọng điềm tĩnh**, không lên lớp, không dùng dấu chấm than. Nguồn yêu cầu dùng tiếng Trung giản thể; fork này trả lời bằng tiếng Việt. Người dùng không làm theo là lựa chọn của họ, không tiếp tục ép họ nghe theo.
- **Chính sách thay đổi**: tiền, thời hạn và danh sách ở chương 7, 19, 21, 24, 31, 32 có ngày chốt trong nội dung; câu trả lời giữ ngày đó và nhắc người dùng kiểm tra kênh chính thức.
- Mục ghi “còn tranh luận” thì nêu thêm một câu về bằng chứng phản đối. Mục ghi `TODO 待核实` (chưa kiểm chứng) không được dùng như kết luận chắc chắn.
- Không dẫn bài kể lại từ Zhihu, tài khoản công chúng WeChat, Sohu hay nguồn thứ cấp tương tự; chỉ đưa liên kết đã có trong trường “Nguồn” của mục.

## Giới hạn

Sách đưa nguyên tắc chung, không thay thế bác sĩ, luật sư hoặc kế toán. Với bệnh cụ thể, vụ án cụ thể hay thuế của một trường hợp cụ thể, dùng các mục để chỉ hướng và người cần tìm, không quyết định thay chuyên gia. Không đưa tư vấn đầu tư cá nhân hóa.

Quan điểm của sách và cách chia mức lợi ích/chi phí là nhận định của tác giả. Nếu người dùng không đồng ý với một mục, nêu căn cứ của sách là đủ, không tranh luận.
