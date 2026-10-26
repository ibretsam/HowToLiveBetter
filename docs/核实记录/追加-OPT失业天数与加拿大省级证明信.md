# Bổ sung: mục 32 điều 11, 12, giới hạn ngày thất nghiệp OPT Mỹ và thư xác nhận cấp tỉnh Canada

2026-10-14. Cả hai thêm cuối mục 32, không chèn giữa. Mục dưới 20 điều, không cần hướng dẫn đầu mục. Kiểm tra trùng: grep “OPT”“PAL”“省级证明信”“STEM” toàn sách không trúng.

Bốn câu hỏi: ① độc giả học Mỹ, Canada sẽ gặp; ② ngày thất nghiệp OPT là ranh giới có thể mất tình trạng cư trú, nhiều người chỉ biết “OPT cho tìm việc”, không biết ngày không việc có trần; miễn cho thạc sĩ/tiến sĩ Canada từ 2026 là thay đổi mới, bị từ chối phải lấy thư mới cũng ít người biết; ③ hành động mới (đếm ngày, nộp trước tốt nghiệp; hỏi hoàn học phí trước lấy thư); ④ có nguyên văn chính thức.

## Điều 11: ngày thất nghiệp OPT

### 1. 8 CFR 214.2(f)(10)(ii)(E)
- URL: <https://www.ecfr.gov/current/title-8/chapter-I/subchapter-B/part-214/section-214.2>; lần này lấy toàn văn bản 2026-10-09 bằng giao diện phiên bản eCFR (`/api/versioner/v1/full/2026-10-09/title-8.xml?part=214&section=214.2`, cần proxy và `--compressed`).
- Nguyên văn: “(E) Periods of unemployment during post-completion OPT. During post-completion OPT, F-1 status is dependent upon employment. Students may not accrue an aggregate of more than 90 days of unemployment during any post-completion OPT period described in 8 CFR 274a.12(c)(3)(i)(B). Students granted a 24-month OPT extension under paragraph (f)(10)(ii)(C)(2) of this section may not accrue an aggregate of more than 150 days of unemployment during a total OPT period, including any post-completion OPT period described in 8 CFR 274a.12(c)(3)(i)(B) and any subsequent 24-month extension period.”
- Đoạn này bản 2026-09-01 và 2026-10-09 giống từng chữ, quy tắc mới thời hạn nhập cảnh cố định không đổi nó.

### 2. Hạn nộp: 60 hay 30 ngày
- Bản 2026-09-14 (f)(11)(i)(B)(2): “the student may properly file his or her Form I-765 or successor form up to 90 days prior to his or her program end date and no later than 60 days after his or her program end date. The student must also file his or her Form I-765 or successor form with USCIS within 30 days of the date the DSO enters the recommendation for OPT into his or her SEVIS record.”
- Từ bản 2026-09-15 câu đổi “no later than 30 days after his or her program end date”. Danh sách eCFR cho thấy 214.2 sửa nội dung 2026-09-15, tương ứng quy tắc thời hạn nhập cảnh cố định công bố 2026-07-17, dự kiến hiệu lực 2026-09-15 (mục 32 điều 2). eCFR không phản ánh lệnh tạm dừng tòa, nên trang “current” hiện 30 ngày.
- Trong thời gian tòa tạm dừng áp cũ, USCIS vẫn ghi 60 ngày: <https://www.uscis.gov/working-in-the-united-states/students-and-exchange-visitors/optional-practical-training-opt-for-f-1-students> (lấy 2026-10-14) — “Initial post-completion OPT … Must apply within 30 days after your DSO enters the recommendation for OPT into your SEVIS record, and May apply up to 90 days before you complete your degree, but no later than 60 days after you complete your degree.”
- Vì vậy điều sách ghi 60 ngày, ghi chú quy tắc mới sẽ đổi 30, khuyên nộp trước tốt nghiệp.

### 3. SEVP giải thích: không đăng ký chủ tính thất nghiệp, có thể chấm dứt thủ công
- URL: <https://studyinthestates.dhs.gov/sevis-help-hub/student-records/fm-student-employment/f-1-optional-practical-training-opt> (lấy có proxy 2026-10-14).
- Nguyên văn: “While students are not required to have an employer when OPT is requested in SEVIS, students authorized for post-completion OPT are expected to be employed. A student on post-completion OPT can be unemployed for a total of 90 days. A student whose record lacks employer information is considered unemployed. SEVP officials can manually terminate a student who accrues 90 total days of unemployment.”

### 4. Đề xuất phí OPT
- Federal Register API lấy tóm tắt văn bản 2026-20660: “This rule proposes new fees for Optional Practical Training (OPT) … $70,000 for initial OPT; and $30,000 for any subsequent OPT.” Loại Proposed Rule, công bố 2026-10-08, comments_close_on 2026-11-09.
- URL: <https://www.federalregister.gov/documents/2026/10/08/2026-20660/optional-practical-training-fees>
- Chỉ đề xuất, ghi chú nói rõ chưa hiệu lực.

### Cấp bằng chứng và mức lợi ích
- A: nguyên văn quy định liên bang cộng giải thích chính thức.
- Lợi ích lớn, tự do: vượt trần dẫn chấm dứt F-1, cùng mức điều 3, 4 mục này (vi phạm visa, đứt tình trạng), dùng cách đánh dấu của mục.

## Điều 12: thư xác nhận tỉnh/lãnh thổ Canada (PAL/TAL)

### 1. IRCC, Provincial attestation letter or territorial attestation letter
- URL: <https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/get-documents/provincial-attestation-letter.html> (curl hết thời gian, Chrome không giao diện có proxy lấy được; dcterms.modified 2026-09-02).
- Là gì: “The provincial attestation letter or territorial attestation letter (PAL/TAL) is a letter from the province or territory where you plan to study that confirms there's space for you provided by the designated learning institution (DLI) you plan to attend usually required to apply for a study permit”; “It confirms that you've been assigned one of the available spaces to study in that province or territory.”
- Cách lấy, khi nộp: “You should contact your school (DLI) to find out how to apply for a PAL/TAL.”; “You should submit a PAL/TAL with your study permit application, not after”
- Miễn (trích): “preschool primary school (including kindergarten) secondary school (up to grade 12) degree-granting graduate program at the master's or doctoral level at a public DLI starting January 1, 2026”; “You're an exchange student studying under an exchange arrangement between your home institution and a DLI in Canada, and you don't pay tuition fees to the DLI.”; “You're applying for a study permit extension at the same DLI and level of study as your current study permit.”; “You need to provide proof that you meet one of the above exceptions if you don't provide a PAL/TAL with your study permit application.”
- Quebec: “If you want to study in Quebec, you need an attestation of issuance of your Quebec Acceptance Certificate (CAQ), which is issued by the Government of Quebec.”
- Hiệu lực: “until December 31, 2026, for the 2026 study permit cap year”; “Your PAL/TAL needs to be valid when you apply for your study permit. It does not need to be valid when you start your studies.”
- Lấy lại: “You can't reapply with the same PAL/TAL if your study permit application was approved or refused.”; “As of January 22, 2025, you must get a new PAL/TAL before you submit your study permit application when changing schools.”

### 2. IRCC, Study permit: Get the right documents
- URL: <https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/get-documents.html> (Chrome không giao diện có proxy; dcterms.modified 2026-10-06).
- Nguyên văn: “Get a provincial or territorial attestation letter (PAL/TAL) from your school. In most cases, you need to accept your offer and pay your tuition fees, either in part or in full, to get your PAL/TAL.”

### Cấp bằng chứng và mức lợi ích
- A: nguyên văn website cơ quan di trú.
- Lợi ích vừa, tiền bạc, theo nhận định: thiếu thư hoặc nộp lại thư cũ mất phí đơn, thời gian, học phí có thể không hoàn hết; hậu quả tiền/thời gian, không liên quan tự do thân thể. Website không có quy định thống nhất hoàn bao nhiêu học phí khi bị từ chối, nên chỉ yêu cầu hỏi trường, không số.
- Không viết “không thư sẽ bị trả hồ sơ”: chưa tìm thấy nguyên văn phát biểu ấy trong hai trang.
