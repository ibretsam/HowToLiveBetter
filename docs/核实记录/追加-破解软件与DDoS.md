# Bổ sung: mục 11 điều 20 (bản vá bẻ khóa, công cụ tạo mã), điều 21 (DDoS) và hướng dẫn đầu mục

Ngày xác minh: 2026-10-14. Công cụ: Git Bash curl lấy trực tiếp (spp.gov.cn, npc.gov.cn, ga.sz.gov.cn, jtgl.beijing.gov.cn, ncac.gov.cn, jsfy.gov.cn, sdcourt.gov.cn đều nối trực tiếp được), python bỏ thẻ rồi grep nguyên văn. WebSearch dùng 3 lần chỉ để tìm URL, mọi số trong điều sách theo nguồn chính thức dưới.

## Kiểm tra trùng

- grep toàn sách “破解”“注册机”“DDoS”“流量攻击”“压力测试”: chưa điều cùng việc.
- Mục 11 điều 2 (gian lận trò chơi) đã dẫn điểm 6 điều 217 Hình sự, nhưng hành động là làm công cụ gian lận, đọc/ghi bộ nhớ trò chơi; điều 20 bẻ xác thực giấy phép phần mềm, bán công cụ bẻ khóa, khác hành động, dẫn nhau.
- Mục 9 điều 24 (dịch sang tiếng Trung, đăng lại, tài nguyên ổ mạng) nói đưa tác phẩm lên mạng; điều 20 nói chính việc vượt biện pháp kỹ thuật. Ghi chú điều 20 dẫn “đưa cả bản bẻ khóa lên mạng” tới mục 9 điều 24, không chép lại ngưỡng.
- Mục 11 điều 8 (điều khiển trái phép máy người khác), điều 9 (kiểm thử chưa được phép) liên quan điều 21 nhưng khác hành động, ghi chú điều 21 dẫn hai điều.
- Hai việc khác hành động (xâm phạm bản quyền, phá hoại hệ thống thông tin máy tính), mỗi việc một điều.

## I. Điều luật

| # | URL | Nguyên văn |
|---|-----|------|
| L1 | <https://www.spp.gov.cn/zdgz/202012/t20201227_503682.shtml> | Điểm 20 Tu chính án Hình sự (XI) viết lại điều 217: “以营利为目的，有下列侵犯著作权或者与著作权有关的权利的情形之一，违法所得数额较大或者有其他严重情节的，处三年以下有期徒刑，并处或者单处罚金；违法所得数额巨大或者有其他特别严重情节的，处三年以上十年以下有期徒刑，并处罚金”. **Điểm 6**: “未经著作权人或者与著作权有关的权利人许可，故意避开或者破坏权利人为其作品、录音录像制品等采取的保护著作权或者与著作权有关的权利的技术措施的。” Điểm 1 gồm “计算机软件”. |
| L2 | <http://www.npc.gov.cn/npc/c2/c30834/202011/t20201119_308796.html> | Luật Quyền tác giả (sửa 2020). Điều 49: “为保护著作权和与著作权有关的权利，权利人可以采取技术措施。未经权利人许可，任何组织或者个人不得故意避开或者破坏技术措施，不得以避开或者破坏技术措施为目的制造、进口或者向公众提供有关装置或者部件，不得故意为他人避开或者破坏技术措施提供技术服务。……本法所称的技术措施，是指用于防止、限制未经权利人许可浏览、欣赏作品、表演、录音录像制品或者通过信息网络向公众提供作品、表演、录音录像制品的有效技术、装置或者部件。” Điều 50: “下列情形可以避开技术措施，但不得向他人提供避开技术措施的技术、装置或者部件……（四）对计算机及其系统或者网络的安全性能进行测试；（五）进行加密研究或者计算机软件反向工程研究。” Đầu điều 53: “……违法经营额五万元以上的，可以并处违法经营额一倍以上五倍以下的罚款；没有违法经营额、违法经营额难以计算或者不足五万元的，可以并处二十五万元以下的罚款”; điểm 6 “故意避开或者破坏技术措施的，故意制造、进口或者向他人提供主要用于避开、破坏技术措施的装置或者部件的，或者故意为他人避开或者破坏技术措施提供技术服务的”. Điều 54: thiệt hại thực/lợi bất hợp pháp, khó tính thì “参照该权利使用费”, cố ý và nghiêm trọng “一倍以上五倍以下”. Loại tác phẩm điều 3 có phần mềm. |
| L3 | <https://www.spp.gov.cn/xwfbh/wsfbt/202504/t20250424_693977.shtml> | Khoản 1 điều 13 法释〔2025〕5号: “违法所得数额在三万元以上的，应当认定为……『违法所得数额较大』”; “（一）非法经营数额在五万元以上的”. Khoản 2: “明知他人实施侵犯著作权犯罪，而向他人提供主要用于避开、破坏技术措施的装置或者部件，或者为他人避开、破坏技术措施提供技术服务，违法所得数额、非法经营数额达到前款规定标准的，应当以侵犯著作权罪追究刑事责任。” Khoản 3: “达到本条前两款相应规定标准十倍以上的，应当认定为……『违法所得数额巨大或者有其他特别严重情节』。” |
| L4 | <https://jtgl.beijing.gov.cn/jgj/jgxx/flfg/fl/11033925/index.html> | Bản hợp nhất Hình sự. Khoản 3 điều 285: “提供专门用于侵入、非法控制计算机信息系统的程序、工具，或者明知他人实施侵入、非法控制计算机信息系统的违法犯罪行为而为其提供程序、工具，情节严重的，依照前款的规定处罚。” Khoản 1 điều 286: “违反国家规定，对计算机信息系统功能进行删除、修改、增加、干扰，造成计算机信息系统不能正常运行，后果严重的，处五年以下有期徒刑或者拘役；后果特别严重的，处五年以上有期徒刑。” Điều 287-1 (sử dụng trái phép mạng thông tin) dưới ba năm. |
| L5 | <https://ga.sz.gov.cn/ZWGK/ZCFG/ZCJD/content/post_1304363.html> | 法释〔2011〕19号. Điều 3: cung cấp chương trình/công cụ chuyên dụng ngoài điểm (1) “二十人次以上的”, “违法所得五千元以上或者造成经济损失一万元以上的” là nghiêm trọng. Điều 4: “（一）造成十台以上计算机信息系统的主要软件或者硬件不能正常运行的；……（三）违法所得五千元以上或者造成经济损失一万元以上的；（四）造成为一百台以上计算机信息系统提供域名解析、身份认证、计费等基础服务或者为一万以上用户提供服务的计算机信息系统不能正常运行累计一小时以上的”; đặc biệt nghiêm trọng “（一）数量或者数额达到前款第（一）项至第（三）项规定标准五倍以上的”. Điều 9: “明知他人实施刑法第二百八十五条、第二百八十六条规定的行为，具有下列情形之一的，应当认定为共同犯罪……（一）为其提供用于破坏计算机信息系统功能、数据或者应用程序的程序、工具，违法所得五千元以上或者提供十人次以上的；（二）为其提供互联网接入、服务器托管、网络存储空间、通讯传输通道、费用结算、交易服务、广告服务、技术培训、技术支持等帮助，违法所得五千元以上的”. Điều 11: hệ thống máy tính “包括计算机、网络设备、通信设备、自动化控制设备等”. |
| L6 | <https://www.spp.gov.cn/spp/fl/202506/t20250627_699863.shtml> | Điều 33 Luật Xử phạt quản lý trị an (sửa 2025): “有下列行为之一，造成危害的，处五日以下拘留；情节较重的，处五日以上十五日以下拘留：……（二）违反国家规定，对计算机信息系统功能进行删除、修改、增加、干扰的；……（五）提供专门用于侵入、非法控制计算机信息系统的程序、工具……” |

## II. Vụ việc

| # | URL | Nguyên văn |
|---|-----|------|
| C1 | <https://www.spp.gov.cn/xwfbh/wsfbt/202504/t20250424_693978.shtml> | Vụ điển hình bảo vệ hình sự sở hữu trí tuệ hai cơ quan tối cao 2025, vụ 6 Lưu X Sinh, Lưu X xâm phạm bản quyền: “2019年3月至2022年7月间，被告人刘某生以营利为目的，未经著作权人许可，自行制作用于避开著作权技术保护措施的『加密狗』，擅自复制相关软件等，销售『加密狗』和盗版软件。……刘某生、刘某涉及非法经营数额分别为106万余元和14万余元。” Tòa trung cấp số 3 Thượng Hải: “刘某生情节特别严重，刘某情节严重，二人均已构成侵犯著作权罪，遂判处刑罚”. Trang không nêu thời hạn tù. |
| C2 | <https://www.spp.gov.cn/spp/2024zgjtzwlft/202402/t20240228_645416.shtml> | Viện kiểm sát tối cao 2024-02-28: “这是《刑法修正案（十一）》施行后，全国首例『故意避开或者破坏技术措施型』侵犯著作权犯罪案件”; “刘某生、刘甲、刘某旺……销售金额达100余万元。……同年4月12日，法院……分别判处三名被告人有期徒刑三年二个月至一年不等，部分适用缓刑，并处罚金70万元至8万元不等。” |
| C3 | <https://www.spp.gov.cn/spp/zdgz/202304/t20230418_611586.shtml> | Kiểm sát Nhật báo 2023-04-18 (website Viện kiểm sát tối cao): thợ sửa Lưu X “在QQ群中购得50套盗版加密狗”, “以8万元的价格购买”, “以每个数千元的价格在网上加价出售”; “4月12日，被告人刘某因侵犯著作权罪被法院判处有期徒刑一年二个月，适用缓刑，并处罚金8万元” (Viện kiểm sát quận Phổ Đà, Thượng Hải truy tố). Kiểm sát viên giải thích kiểm soát truy cập “一般表现为身份认证软件、口令验证程序等形式” — căn cứ câu giải thích dễ hiểu “kiểm mã đăng ký, dongle đều là biện pháp kỹ thuật”. |
| C4 | <https://www.ncac.gov.cn/xxfb/ywxx/202508/t20250801_925366.html> | Cục Bản quyền quốc gia, Văn phòng “扫黄打非”, vụ 6 trong mười vụ lớn chống vi phạm bản quyền toàn quốc 2024: “2021年5月以来，李某某等人委托他人制作游戏机辅助破解程序、加工生产游戏核验系统破解装置，并通过销售该装置牟利，非法经营数额3900余万元。……2024年11月，江苏省徐州经济技术开发区人民法院以侵犯著作权罪，判处李某某等10人有期徒刑三年六个月至二年六个月不等，部分适用缓刑，并处罚金1100万元至150万元不等。” |
| C5 | <https://www.spp.gov.cn/spp/jczdal/202004/t20200408_458415.shtml> | 检例第69号: “2017年初，被告人姚晓杰等人接受王某某（另案处理）雇佣，招募多名网络技术人员，在境外成立『暗夜小组』黑客组织。『暗夜小组』从被告人丁虎子等3人处购买大量服务器资源，再利用木马软件操控控制端服务器实施DDoS攻击……三次利用14台控制端服务器下的计算机，持续对某互联网公司云服务器上运营的三家游戏公司的客户端IP进行DDoS攻击……出现游戏无法登录、用户频繁掉线……支付4万余元”; “2018年6月8日……南山区人民法院判决认定被告人姚晓杰等11人犯破坏计算机信息系统罪……分别判处有期徒刑一年至二年不等”. Chứng cứ truy nguồn là báo cáo chi nhánh Quảng Đông Trung tâm Điều phối xử lý khẩn cấp mạng máy tính quốc gia. |
| C6 | <https://www.jsfy.gov.cn/article/91613.html> | Vụ 2 trong vụ điển hình tội hại an ninh mạng Tòa cấp cao Giang Tô 2020-09-24: “2017年3月被告人唐某、王某，建立一个具有会员充值、任务提交功能的DDOS（分布式拒绝服务）网站……被告人蔡某、李某、刘某、张某及其公司，先后在该网址注册会员并充值，提交对其他同类网址平台IP等的DDOS攻击任务”; “南通市海门区人民法院经审理认定，被告人唐某、王某等人构成破坏计算机信息系统罪，分别判处有期徒刑十个月至五年六个月不等”; “通过DDOS对80余个目标IP网站进行流量攻击”. |
| C7 | <http://www.sdcourt.gov.cn/dyzy/372897/372899/33201805/index.html> | Bình luận Nhân dân Pháp viện báo (website Tòa Sơn Đông đăng 2025-02-08), vụ tham khảo trong kho 2024-18-1-254-001: “理论与实践均认为分布式拒绝服务（DDoS）攻击属于干扰计算机信息系统”; “网络攻击请求者张某及网站经营管理者唐某某等人构成共同犯罪……张某系犯意发起者，无疑属于主犯”; “张某为打压同行、提升自己公司排名，对同行公司网站的11个IP地址或者域名提交百余次DDoS攻击任务”; “对相关人员如何定罪量刑，司法实践做法不尽一致”. Nguyên văn vụ trong Kho án nhân dân cần đăng nhập, chưa lấy trực tiếp; trang chinacourt.org đăng lại không mở được. |
| C8 | <https://www.spp.gov.cn/spp/zdgz/202009/t20200901_478510.shtml> | Viện kiểm sát tối cao 2020-09-01: “7月17日，法院对北京市海淀区检察院提起公诉的一起涉嫌非法利用信息网络案作出一审判决，被告人王某建立专门的网络DDoS攻击平台、向他人提供DDoS攻击流量，被判处有期徒刑一年，并处罚金5万元”; nền tảng có “『青铜』『白银』『黄金』『钻石』等多种DDoS攻击套餐”. |

## III. Phân cấp

- Điều 20: A (nguyên văn Hình sự, Luật Quyền tác giả, giải thích tư pháp + vụ hai cơ quan tối cao, Viện kiểm sát tối cao, Cục Bản quyền công bố). Tiêu chí tự do, lợi ích lớn (tránh trách nhiệm hình sự).
- Điều 21: A (Hình sự, nguyên văn 法释〔2011〕19号 + 检例第69号 + vụ Tòa Giang Tô + tin Viện kiểm sát tối cao). Tiêu chí tự do, lợi ích lớn (tránh trách nhiệm hình sự).
- “Bán trojan điều khiển máy người khác thuộc khoản 3 điều 285” không viết riêng thành kết luận ở điều 21, chỉ liệt kê ngưỡng luật trong lợi ích, ghi chú dẫn điều 8; chưa thấy vụ chính thức “bán nền tảng kiểm thử tải bị kết khoản 3 điều 285”; vụ nền tảng công bố lần lượt kết phá hoại hệ thống (Hải Môn), sử dụng mạng trái phép (Hải Điến).

## IV. Không viết

- Cá nhân tự cài bản bẻ khóa, bồi thường dân sự khi công ty dùng phần mềm lậu bị kiện: đợt này chưa kiểm Điều lệ bảo vệ phần mềm và án tương ứng, không viết.
- “Thua trò chơi rồi đánh IP nhà đối thủ”: chưa có vụ chính thức nhắm mạng nhà game thủ cá nhân, chỉ viết máy chủ công ty trò chơi (检例第69号).

## V. Hướng dẫn đầu mục

Mục tăng lên 21 điều, theo quy tắc CLAUDE.md thêm sáu nhóm: trước khi bắt tay, công cụ gian lận và bẻ khóa, đụng hệ thống người khác, nhận việc và nghề phụ, nghỉ việc và quyền sở hữu, ra mắt sản phẩm. Mỗi điều trong 21 xuất hiện đúng một lần, tên ngắn đều có ba chữ Hán liên tiếp khớp tiêu đề. Thêm 25 dẫn chiếu (21 hướng dẫn, điều 20, 21 mỗi điều 2).
