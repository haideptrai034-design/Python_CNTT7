"""
(1) Phân tích lỗi

Đây là một lỗi logic (logic error) chứ không phải lỗi cú pháp.

Chương trình vẫn chạy bình thường vì:

Các biến đều tồn tại
Kiểu dữ liệu hợp lệ
Không vi phạm cú pháp của ngôn ngữ lập trình

Tuy nhiên, dữ liệu bị gán sai vị trí, dẫn đến kết quả in ra không đúng.

Ví dụ luồng thực thi (trace code)

Giả sử người dùng nhập:

Họ tên: Nguyễn Văn A
Tuổi: 25
Triệu chứng: Đau đầu

Nhưng trong code legacy có thể đang viết kiểu như:

name = input("Họ tên: ")
age = input("Tuổi: ")
symptom = input("Triệu chứng: ")

print("Họ tên bệnh nhân:", symptom)
print("Tuổi:", name)
print("Triệu chứng:", age)
"""

"""
Trace dữ liệu

Sau khi nhập:

Biến	Giá trị
name	Nguyễn Văn A
age	25
symptom	Đau đầu

Nhưng khi in:

print("Họ tên bệnh nhân:", symptom)

=> In ra:

Họ tên bệnh nhân: Đau đầu

Tương tự:

print("Tuổi:", name)

=> In ra:

Tuổi: Nguyễn Văn A
Nguyên nhân gây lỗi logic

Nguyên nhân chính:

Lập trình viên đã tham chiếu sai biến khi xuất dữ liệu
Thứ tự mapping dữ liệu bị nhầm lẫn

Cụ thể:

Thông tin cần in	Biến đúng	Biến đang dùng sai
Họ tên	name	symptom
Tuổi	age	name
Triệu chứng	symptom	age
(2) Sửa lỗi
"""

name = input("Nhập họ tên bệnh nhân: ")
age = input("Nhập tuổi: ")
symptom = input("Nhập triệu chứng lâm sàng: ")

print("\n===== PHIẾU KHÁM BỆNH =====")
print("Họ tên bệnh nhân:", name)
print("Tuổi:", age)
print("Triệu chứng lâm sàng:", symptom)