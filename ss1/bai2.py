"""
(1) Phân tích lỗi

Đây là một lỗi xử lý kiểu dữ liệu (data type error) trong chương trình.

Chương trình:

 Không lỗi cú pháp
 Vẫn chạy bình thường
 Nhưng dữ liệu được lưu sai kiểu
Đặc điểm của hàm input() trong Python

Trong Python, hàm:

input()

luôn trả về dữ liệu dưới dạng chuỗi ký tự (str), dù người dùng nhập:

số nguyên
số thực
hay văn bản

Ví dụ:

weight = input("Nhập cân nặng: ")
print(type(weight))

Nếu nhập:

65.5

thì kết quả vẫn là:

<class 'str'>
Trace code (dò luồng thực thi)

Giả sử code legacy như sau:

weight = input("Nhập cân nặng: ")

print("Cân nặng:", weight)
print(type(weight))
Bước 1: Người dùng nhập
65.5
Bước 2: Hàm input() nhận dữ liệu

Python nhận:

"65.5"

Lưu ý:

Có dấu ngoặc kép ngầm hiểu
Nghĩa là Python xem đây là chuỗi ký tự
Bước 3: Kiểm tra kiểu dữ liệu
print(type(weight))

Kết quả:

<class 'str'>
Nguyên nhân gây lỗi

Nguyên nhân chính:

Lập trình viên chỉ dùng input()
Nhưng không thực hiện ép kiểu dữ liệu (type casting)

Do đó:

Dữ liệu nhập vào vẫn là chuỗi (str)
Không thể dùng cho các phép tính BMI

Ví dụ lỗi:

bmi = weight / 2

Sẽ gây lỗi vì:

"65.5" / 2

là không hợp lệ.

(2) Sửa lỗi
"""
weight = float(input("Nhập cân nặng bệnh nhân: "))

print("Cân nặng:", weight)
print("Kiểu dữ liệu:", type(weight))