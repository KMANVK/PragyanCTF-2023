# Challenge : Nuclearophine 
 
![image](https://user-images.githubusercontent.com/94669750/223690040-58017ca8-f608-4bd6-9179-046eff9cc338.png)

# Giải Pháp :

_ Mở file bằng wireshark để phân tích 

_ Nhận thấy Protocol UDP chiếm đến 93.6% 

_ Follow UDP Stream thì tôi phát hiện chữ ký tệp của file .wav: 

![image](https://user-images.githubusercontent.com/94669750/223691326-5351d0c8-a458-417b-9e76-3513161903ba.png)

=> Chuyển sang raw và đưa lên cyberchef decode hex và lưu dưới dạng file .wav (các bạn cũng có thể lưu nó lun không cần chuyển qua raw)

_ Đọc lướt qua 1 lượt thì tôi còn để ý trong đó nó còn chứa 1 file zip và 1 file txt : 

![image](https://user-images.githubusercontent.com/94669750/223692499-bfae6e78-9587-406b-b947-607f1a70292d.png)

=> Binwalk file wav và tôi nhận được : *** "binwalk --dd='.*' 1.wav" ***

![image](https://user-images.githubusercontent.com/94669750/223693425-b4b28e29-6406-4e77-b021-5b2528082f82.png)

_ Nhưng muốn mở file txt lên thì cần pass (tôi đã thử crack nó bằng johntheripper với rockyou.txt nhưng ko thành công)

_ Và bắt đầu chuyên mục tìm kiếm tiếp :vv , tôi phát hiện thêm điều thú vị khi follow TCP Stream là :

![image](https://user-images.githubusercontent.com/94669750/223692863-753ea8f9-a8c2-41f7-948f-a3b96001b9dd.png)

=> nghĩa là : Walt Walt, bạn có thể gửi cho tôi bản thiết kế mà bạn đã làm cho Nuclearophine không? Nó sẽ thay đổi cuộc sống Yeah, trong một phút nữa Jesse. Tôi đã mã hóa nó để tránh những bàn tay tò mò. Tuyệt vời. Gửi mật khẩu cho tệp cùng với nó, cảm ơnHmmmmmm bạn biết gì không? hãy thử và tìm nó..........Ôi trời, tôi cũng tình cờ gửi một đoạn ghi âm. Vì chúa, Jesse ĐỪNG NGHE NÓ.......Mày có bị bắt không???!!!!!!!!

=> Đọc kỹ nó thì chợt nhớ lại file wav lúc nãy chắc sẽ có liên quan đến pass 

_ Nhưng mở file thì bị lỗi, và sợt gg tìm cách fix nó lại =)))

_ Dựa vào đây để fix nó lại : https://parsiya.net/blog/2018-06-05-contextis-xmas-ctf-writeup/#a-closer-look-at-wave-files

_ Nhìn kỹ thì nó bị sai ở phần Subchunk2ID-datadata
![image](https://user-images.githubusercontent.com/94669750/223696385-6e09538e-ab71-4172-b40c-3223228f315b.png)

_ Tôi đổi *"6E 6F 6F 6F"* thành *"64 61 74 61"* và mở được file 

_ Bật nó lên nghe thì như tiếng con gì kêu nên nghe ko được =)))

_ Tôi đem bỏ nó vào Sonic Visualiser để phân tích nhưng cx ko phát hiện đc gì :vv

_ Nhờ có người anh của tôi trợ giúp nên tôi biết được nó là DTMF

_ Đưa nó lên đây giải mã(http://dialabc.com/sound/detect/) và tôi có được pass :

![image](https://user-images.githubusercontent.com/94669750/223698067-65ac6820-182d-4c61-a1a9-66fa1a6e87c8.png)


=> Pass : ***D65B85C1B657DC2BCD54CB89D7C***

=> Nhập pass và t mở được file txt : có được phần 2 của flag 

![image](https://user-images.githubusercontent.com/94669750/223700105-f7600b1c-168f-489c-bae5-19cffe764402.png)

_ Phần đầu của lá cờ thì t dùng stegolsb file wav và t nhận được nó : ***$stegolsb wavsteg -r -i 1.wav -o output.txt -n 1 -b 1000***

![image](https://user-images.githubusercontent.com/94669750/223699124-0abb5090-0f24-487c-946f-0618cd006972.png)

![image](https://user-images.githubusercontent.com/94669750/223699739-5cca397b-36b5-4127-a2a1-dc5793b6447a.png)

#flag : p_ctf{3veryw8ere_1_5e3_8e3p_800p}