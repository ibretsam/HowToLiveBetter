# Issue #28: bổ sung nguồn cho tám mục (2026-09-23)

Nguồn nhiệm vụ: GitHub issue #28 (dlgrv), đề nghị bổ sung tài liệu gốc cho 8 mục đánh dấu “kinh nghiệm tác giả”, “chờ kiểm chứng”, “TODO”, mỗi mục kèm trích dẫn, liên kết. Chỉ coi trích dẫn trong issue là đầu mối; từng hàng bên dưới đều được tự tải nguyên bản và đối chiếu từng chữ trong đợt này.

## Đối chiếu và xử lý từng mục

| Mục | Nguồn | Đối chiếu lại | Ý chính nguyên văn | Xử lý |
|---|---|---|---|---|
| Mục 18 chương 13 (điện giật) | <https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-from-electrical-hazards.html> | Có (curl 403, Chrome headless lấy được) | Phần First aid: “Look first. Don't touch. The person may still be in contact with the electrical source.” “Turn off the source of electricity if possible. If not, move the source away from you and the affected person using a non-conducting object made of cardboard, plastic or wood.” “If either has stopped or seems dangerously slow or shallow, begin cardiopulmonary resuscitation (CPR) immediately.” | Sử dụng |
| Như trên | <https://doi.org/10.7326/0003-4819-145-7-200610030-00011> (Spies & Trohman 2006) | Có (tóm tắt Europe PMC) | “patients successfully resuscitated after cardiopulmonary arrest often have a favorable prognosis” | Sử dụng |
| Như trên | Moran 1986 JAMA (10.1001/jama.1986.03370160055007) | Không | Europe PMC không có tóm tắt, không kiểm chứng được nội dung | Không dùng |
| Như trên | ERC 2021, ngừng tim trong tình huống đặc biệt (10.1016/j.resuscitation.2021.02.011) | Có (tóm tắt) | Các nguyên nhân, bối cảnh, nhóm người đặc biệt trong tóm tắt đều không có điện giật; issue nói “bản 2021 không có chương điện giật” là đúng | Xóa khỏi cột nguồn; câu cũ nói tài liệu “có chương điện giật” là sai |
| Mục 9 chương 20 (không rung lắc trẻ nhỏ) | <https://doi.org/10.15585/mmwr.mm6520a1> (MMWR 2016) | Có (tóm tắt) | “During this period, AHT resulted in nearly 2,250 deaths among U.S. resident children aged <5 years” | Sử dụng |
| Như trên | <https://doi.org/10.1007/s00247-018-4149-1> (tuyên bố đồng thuận Choudhary 2018) | Có (tóm tắt) | “Abusive head trauma (AHT) is the leading cause of fatal head injuries in children younger than 2 years”; nguyên nhân “multifactorial (shaking, shaking and impact, impact, etc.)”; “subdural hematoma… complex retinal hemorrhages” | Sử dụng |
| Như trên | Bản AAP tán thành (10.1542/peds.2018-1504) | Chưa kiểm chứng | Tán thành cùng nội dung tuyên bố đồng thuận, không thêm riêng | Không dùng |
| Mục 27 chương 13 (vùng hoang vắng) | <https://www.nps.gov/articles/000/desertdrivingsafety.htm> | Có (curl trực tiếp) | “Staying with your car is the most important thing you can do in the event of an emergency. While not often, people have died from exposure trying to walk back to the paved roads.” | Sử dụng, không đổi cấp |
| Mục 15 chương 4 (giới hạn lướt màn hình) | PDF báo cáo CNNIC lần 56 | Có (pdftotext trích nguyên văn tiếng Trung được) | Dòng 821, bản dịch: “Tính tới tháng 6 năm 2025, người dùng internet nước ta lên mạng trung bình 30.6 giờ mỗi tuần, tăng 1.9 giờ so với tháng 12 năm 2024”; dòng 94: “Người dùng video ngắn đạt 10.68 trăm triệu, chiếm 95.1% tổng người dùng internet” | Sử dụng, bỏ TODO |
| Mục 17 chương 5 (quỹ chỉ số) | SPIVA U.S. Scorecard Year-End 2024 | Có (trang chính thức 403 và Chrome headless bị từ chối, đối chiếu snapshot Wayback 2025-05-12) | “65% of all active large-cap U.S. equity funds underperformed the S&P 500, worse than the 60% rate observed in 2023 and slightly above the 64% average annual rate reported over the 24-year history”; “Over the 15-year period ending December 2024, there were no categories in which a majority of active managers outperformed.” | Sử dụng, bỏ TODO. Mục thiếu số “dài hạn”, nên ngoài 65% một năm issue dẫn, thêm trung bình 24 năm và kết luận 15 năm |
| Như trên | PDF SPIVA Institutional Scorecard Year-End 2024 | Không dùng | Tài khoản tổ chức và tài khoản wrap, độc giả thông thường không mua được loại này | Không dùng |
| Mục 2 chương 14 (mật khẩu email) | <https://www.cisa.gov/secure-our-world/use-strong-passwords> | Có (curl trực tiếp) | “Create long, random, unique passwords with a password manager”; “At least 16 characters—longer is stronger!”; “Use a different strong password for each account” | Sử dụng, không đổi cấp |
| Mục 3 chương 14 (PIN SIM) | FCC DOC-398483A1 (thông cáo báo chí 2023-11-15) | Có (pdftotext) | Quản lý việc nhà mạng xác minh danh tính trước chuyển số, thay SIM, nhằm chống lừa đổi SIM “without ever gaining physical control of a consumer's phone” | **Không dùng**. Mục phòng trường hợp mất điện thoại, SIM bị tháo lắp vào máy khác, tức đối phương đã có SIM vật lý; hai việc khác nhau |
| Mục 4 chương 14 (mất điện thoại) | <https://www.fcc.gov/consumers/guides/protect-your-mobile-device> | Có (curl 403, Chrome headless lấy được) | “Even if you think you may have only lost the device, you should remotely lock it to be safe. If the device was stolen, immediately report the theft to the police, including the make and model, serial and IMEI or MEID or ESN number.” “Immediately report the theft or loss to your service provider.” | Sử dụng; thứ tự bước vẫn là kinh nghiệm tác giả, ghi rõ ở cột nguồn |

## Xếp cấp

**Chỉ hai mục đổi cấp: mục 18 chương 13 và mục 9 chương 20, đều từ C lên B.** Nay cả hai có hướng dẫn chính thức hoặc đồng thuận chuyên môn, thêm một nghiên cứu hỗ trợ, nhưng chưa có con số quy trực tiếp thành “làm vậy giảm chết bao nhiêu”, theo cách đánh giá là B.

Các mục khác giữ cấp. Hướng dẫn thao tác của cơ quan chính thức (NPS, CISA, FCC) không phải nghiên cứu, theo thông lệ sách vẫn C (mục 27 chương 13 luôn xử lý như vậy). Hai mục chương 4, 5 chỉ bỏ TODO, bổ sung số, không đổi cấp.

## Những chỗ không làm theo issue

- Không nhập bản dịch vào kho này (quy tắc CLAUDE.md); đợt này chỉ xử lý đề xuất nguồn cho bản tiếng Trung.
- Issue đề nghị có thể mở PR trực tiếp. Đợt này đã sửa xong cục bộ, không cần PR.
