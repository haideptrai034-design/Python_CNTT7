"""
(1) Phân tích lỗi
Câu 1: Tham số nào nhận giá trị nào?

Hàm được định nghĩa:

def calculate_final_price(price, discount, shipping_fee):

Thứ tự tham số là:

price
discount
shipping_fee

Nhưng lại gọi hàm:

calculate_final_price(100000, 15000, 0.1)

=> Python gán theo vị trí:

Giá trị truyền vào	Tham số nhận
100000	price
15000	discount
0.1	shipping_fee

Nghĩa là:

price = 100000
discount = 15000
shipping_fee = 0.1
Câu 2: Vì sao ra số âm khổng lồ?

Công thức:

total = price - (price * discount) + shipping_fee

Thay giá trị vào:

total = 100000 - (100000 * 15000) + 0.1

Tính:

100000 * 15000 = 1500000000

Nên:

total = 100000 - 1500000000 + 0.1
total = -1499900000 + 0.1
total = -1499899999.9

Vì 15000 bị hiểu nhầm là tỉ lệ giảm giá thay vì phí ship, nên phép nhân tạo ra một số cực lớn làm kết quả âm.

Câu 3: Vì sao bị lỗi TypeError?

Dòng gây lỗi:

final_payment = order_total + 5000

Python báo:

TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

Nghĩa là:

None + 5000

không thể thực hiện được.

Câu 4: Biến order_total đang mang giá trị gì?

Giá trị của order_total là:

None

Vì:

def calculate_final_price(...):
    ...
    print(...)

Hàm chỉ print() mà không có return.

Khi một hàm kết thúc mà không có return, Python tự động trả về:

None

Do đó:

order_total = calculate_final_price(...)

thực chất là:

order_total = None
Câu 5: Khác nhau giữa print() và return
print()

Chỉ hiển thị dữ liệu lên màn hình.

Ví dụ:

def test():
    print(100)

x = test()
print(x)

Kết quả:

100
None
return

Trả kết quả về cho nơi gọi hàm.

Ví dụ:

def test():
    return 100

x = test()
print(x)

Kết quả:

100

Biến x nhận được giá trị 100 và có thể tiếp tục tính toán.

Câu 6: Cần sửa hàm như thế nào?

Thay:

print(total)

bằng:

return total

để hàm trả kết quả về cho biến:

order_total = calculate_final_price(...)
(2) Source Code Đúng
"""
# Hàm tính tổng tiền đơn hàng
def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total


# Giá 100000, giảm giá 10%, phí ship 15000
order_total = calculate_final_price(100000, 0.1, 15000)

# Cộng thêm phí đóng gói
final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)