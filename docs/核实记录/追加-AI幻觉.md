# Bổ sung: mục 6 điều 31, đừng dựa chatbot AI để tự đánh giá bệnh và vấn đề pháp luật

2026-10-09, issue #103 “AI 什么时候不可信”. Độc giả muốn sách trả lời ba việc: vì sao mô hình ngôn ngữ lớn tạo ảo giác, kiểm tra bằng nguồn ngoài thế nào, trước quyết định lớn đừng tin mù quáng câu trả lời chuyên môn của AI. Bốn câu hỏi: người bình thường nay hay hỏi AI về bệnh, pháp luật; giọng trả lời rất chắc chắn nên đa số không nghĩ phải kiểm tra; các điều AI có sẵn chỉ nói trạm trung chuyển (mục 11 điều 19, mục 14 điều 10), AI tạo ảnh (mục 9 điều 1) và kê khai dịch vụ (mục 11 điều 17), chưa có “có tin câu trả lời không”; nguồn là thử nghiệm ngẫu nhiên đã bình duyệt và tạp chí luật học. Người dùng quyết định đặt ở danh sách việc không nên làm của mục 6.

Nguyên lý (điểm 1 của issue) không triển khai theo quy tắc sách, chỉ một câu trong ghi chú.

## 1. Thử nghiệm ngẫu nhiên người bình thường dùng AI đánh giá bệnh
- Thư mục: Bean AM và cộng sự (2026). Nature Medicine 32(2):609-615. <https://doi.org/10.1038/s41591-025-04074-y> (PMID 41663592, PMC12920132), toàn văn XML lấy qua Europe PMC REST. Tập, số, trang đối chiếu Crossref.
- Nguyên văn tóm tắt: “We tested whether LLMs can assist members of the public in identifying underlying conditions and choosing a course of action (disposition) in ten medical scenarios in a controlled study with 1,298 participants. Participants were randomly assigned to receive assistance from an LLM (GPT-4o, Llama 3, Command R+) or a source of their choice (control). Tested alone, LLMs complete the scenarios accurately, correctly identifying conditions in 94.9% of cases and disposition in 56.3% on average. However, participants using the same LLMs identified relevant conditions in fewer than 34.5% of cases and disposition in fewer than 44.2%, both no better than the control group.”
- Nguyên văn nội dung: “Participants in the control group had 1.76 (95% CI = 1.45–2.13) times higher odds of identifying a relevant condition than the aggregate of the participants using LLMs. They were also 1.57 (95% CI = 1.28–1.92) times more likely to identify conditions from the more serious 'red flag' list.”
- Nguyên văn nội dung: “Participants using LLMs did not have statistically significant differences in disposition accuracy from the control group”
- Nhóm chứng dùng gì: “Post-treatment surveys indicated that most participants used a search engine or went directly to trusted websites, most often the NHS website”
- Nguyên nhân thất bại: “with both users providing LLMs with incomplete information and LLMs suggesting correct answers but not effectively conveying this information to the users”; “Despite these correct suggestions appearing in the conversations, users did not consistently include them in the final responses”
- Mỗi người hai ca: “We assigned each participant two scenarios to complete consecutively.” Mẫu phân tầng theo dân số Anh: “stratified to reflect the demographics of the UK”.
- “Điểm AI tự thi không dự báo hiệu quả người thường dùng nó”: “Standard benchmarks for medical knowledge and simulated patient interactions do not predict the failures we find with human participants.”

## 2. Mô hình ngôn ngữ lớn phổ thông trả lời pháp luật
- Thư mục: Dahl M, Magesh V, Suzgun M, Ho DE (2024). Journal of Legal Analysis 16(1):64-93. <https://doi.org/10.1093/jla/laae003>, tóm tắt lấy qua Crossref.
- Nguyên văn tóm tắt: “Using OpenAI's ChatGPT 4 and other public models, we show that LLMs hallucinate at least 58% of the time, struggle to predict their own hallucinations, and often uncritically accept users' incorrect legal assumptions.” Định nghĩa ảo giác: “textual output that is not consistent with legal facts”.
- Bản arXiv cùng bài (<https://arxiv.org/abs/2401.01301>, lấy qua arXiv API) nêu phạm vi câu hỏi và số từng mô hình trong tóm tắt: “legal hallucinations are alarmingly prevalent, occurring between 58% of the time with ChatGPT 4 and 88% with Llama 2, when these models are asked specific, verifiable questions about random federal court cases”. Điều sách viết “hỏi án lệ tòa án liên bang Mỹ”, “Llama 2 tới 88%” theo câu này. Chưa kiểm tra từng đơn vị tác giả, chỉ viết “một nhóm nghiên cứu Mỹ”.

## 3. Công cụ AI pháp lý chuyên nghiệp
- Thư mục: Magesh V và cộng sự (2025). Journal of Empirical Legal Studies 22(2):216-242. <https://doi.org/10.1111/jels.12413>, tóm tắt lấy qua Crossref.
- Nguyên văn tóm tắt: “the AI research tools made by LexisNexis (Lexis+ AI) and Thomson Reuters (Westlaw AI-Assisted Research and Ask Practical Law AI) each hallucinate between 17% and 33% of the time”; “certain legal research providers have touted methods such as retrieval-augmented generation (RAG) as "eliminating" or "avoid[ing]" hallucinations”

## 4. Nguyên nhân ảo giác (chỉ trong ghi chú)
- Thư mục: Kalai AT, Nachum O, Vempala SS, Zhang E (2025). Why Language Models Hallucinate. arXiv:2509.04664, lấy qua arXiv API. Trang OpenAI tiếng Trung đính kèm issue tương ứng bài này. Chưa bình duyệt nên chỉ một câu trong ghi chú, không vào lợi ích.
- Nguyên văn tóm tắt: “We argue that language models hallucinate because the training and evaluation procedures reward guessing over acknowledging uncertainty”; “language models are optimized to be good test-takers, and guessing when uncertain improves test performance”

## 5. Bằng chứng phía ngược lại
- Thư mục: Ayers JW và cộng sự (2023). JAMA Internal Medicine 183(6):589. <https://doi.org/10.1001/jamainternmed.2023.1838>, tóm tắt lấy qua Europe PMC.
- Nguyên văn tóm tắt: “a public and nonidentifiable database of questions from a public social media forum (Reddit's r/AskDocs) was used to randomly draw 195 exchanges”; “evaluators preferred chatbot responses to physician responses in 78.6% (95% CI, 75.0%-81.8%) of the 585 evaluations”
- Bài đánh giá chất lượng câu trả lời và sự đồng cảm, không xem người hỏi cuối cùng đánh giá đúng không, nên không mâu thuẫn Bean 2026. Ghi chú nói rõ.

## Không nhận
- Mata v. Avianca (luật sư Mỹ bị phạt vì dùng ChatGPT bịa án lệ): API tìm CourtListener không ra bản ý kiến này, chưa lấy văn bản gốc, không viết.
- Thống kê chính thức, bản án trong nước về người thường dùng AI hỏi bệnh hoặc pháp luật sai: lần này chưa tra.
- Lợi ích xếp nhỏ: kết cục Bean 2026 là “có nhận ra bệnh liên quan không”, thuộc chỉ số trung gian, không có số tử vong hay nhập viện.
