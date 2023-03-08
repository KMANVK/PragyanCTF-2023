# Challenge : Listener


![image](https://user-images.githubusercontent.com/94669750/223689369-fd3e2d74-10e3-431f-9fa6-cce172b1f8ec.png)



# Giải Pháp :

_Mở file bằng wireshark và phân tích dữ liệu.

_Nhận thấy protocol ATT chiếm dữ liệu đến 86.9% => tôi nghĩ bài này liên quan đến Bluetooth Attribute Protocol và bắt đầu vào phân tích nó .

_Sau khi phân tích, chúng tôi thấy rằng có một số cuộc trò chuyện giữa các thiết bị G613và localhost, khi tìm kiếm G613, hóa ra đó là bàn phím không dây Logitech.

_Nhận thấy trường dữ liệu ở value btatt có byte thứ 3 thay đổi liên tục trong kích thước của dữ liệu là 8 byte. (tổng cộng khoảng 3 value đươc thay đổi nằm trong các gói có độ dài là 20 byte ).
![image](https://user-images.githubusercontent.com/94669750/223676253-ffd2c68c-5665-4190-9f95-c1924eebdf6a.png)
![image](https://user-images.githubusercontent.com/94669750/223676394-49695785-972d-46be-b22a-5e69cdd9a8cd.png)
![image](https://user-images.githubusercontent.com/94669750/223676607-d32db922-d592-402c-8dcd-c31cb4ad6c53.png)

=> tôi nghĩ rằng các gói đó chứa thông tin về phím được nhấn trên bàn phím.

_Sợt gg tìm hiểu chút về nó thì bàn phím sử dụng một thứ gọi là HID scan code (https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2)

_Mỗi khóa được ánh xạ tới một giá trị hex nào đó. Khi giải mã một số byte thứ 3 từ các gói giá trị, kết quả sẽ cho một số chuỗi có ý nghĩa.

_Sử dụng tshark để lấy nó ra chúng ta sẽ thấy rõ hơn : ***$tshark -r secret.pcap -T fields -e btatt.value > data.txt***

![image](https://user-images.githubusercontent.com/94669750/223682924-a0fbb01a-2fb9-4419-a49c-fa993c07a920.png)

=> Độ dài dữ liệu của gói bàn phím là 8 byte, thông tin gõ phím ở byte thứ 3

_ oke, bây giờ chúng t sẽ dựa vào đây để viết kịch bản cho nó : 

![image](https://user-images.githubusercontent.com/94669750/223684888-146b6f0e-ff17-4723-9f79-e8935c851bc2.png)
![image](https://user-images.githubusercontent.com/94669750/223687989-200539ce-b076-4d06-9814-f5290f0a9e72.png)


_ Listener.py:

    mappings = { 0x0E:"K",0x10:"M", 0x2C:" "}

    nums = []

    keys = open('data.txt')


    for line in keys:

        if line[:2] != '00' or line[4:6] != '00':
           nums.append(int(line[4:6],16))
        # 00:00:xx:....

    keys.close()

    output = ""

    for n in nums:
        if n == 0:
           continue
        if n in mappings:
           output += mappings[n]
        else:
           output += '[unknown]'

    print('output:' + output)

=> sau khi giải mã tôi nhận được : 

![image](https://user-images.githubusercontent.com/94669750/223686820-1ec7bb23-2db3-424c-a9b7-1d0d07e761a9.png)

=> Và cuối cùng chỉ cần đổi "M" thành "-" và "K" thành "." và decode morse sẽ nhận được cờ

![image](https://user-images.githubusercontent.com/94669750/223687507-46554f4a-4cd0-44a0-b3a7-97bba30a844b.png)

#flag : p_ctf{B1U3T00TH_C4N_B3_1NT3RC3PT3D_ASJHVCLKU}