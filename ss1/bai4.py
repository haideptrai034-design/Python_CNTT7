"""
(1) Phân tích và Đề xuất giải pháp
1. Phân tích Input / Output
Input (Dữ liệu đầu vào)

Điều dưỡng nhập:

Thông tin	Ví dụ	Kiểu dữ liệu ban đầu
Mã bệnh nhân	BN999	str
Nhiệt độ cơ thể	37.5	str
Nhịp tim	85	str
Giải thích

Trong Python, dữ liệu nhập từ:

input()

luôn có kiểu:

<class 'str'>

Dù người dùng nhập số hay chữ.

Output mong muốn
Thông tin	Kiểu dữ liệu mong muốn
Mã bệnh nhân	str
Nhiệt độ cơ thể	float
Nhịp tim	int

Ví dụ:

<class 'float'>
<class 'int'>
2. Đề xuất các giải pháp ép kiểu dữ liệu
Giải pháp 1: Ép kiểu trực tiếp khi nhập
"""
temperature = float(input("Nhập nhiệt độ: "))
heart_rate = int(input("Nhập nhịp tim: "))

"""
Ưu điểm
Code ngắn gọn
Ít biến
Xử lý nhanh
Nhược điểm
Khó debug nếu nhập sai
Không lưu được dữ liệu gốc
Giải pháp 2: Lưu chuỗi trước rồi ép kiểu sau
"""
temp_input = input("Nhập nhiệt độ: ")
heart_input = input("Nhập nhịp tim: ")

temperature = float(temp_input)
heart_rate = int(heart_input)

"""
Ưu điểm
Dễ debug
Có thể kiểm tra dữ liệu trước khi chuyển kiểu
Dễ mở rộng validation trong hệ thống lớn
Nhược điểm
Dùng nhiều biến hơn
Code dài hơn
3. Bảng so sánh hai giải pháp
Tiêu chí	Giải pháp 1	Giải pháp 2
Số lượng biến	Ít	Nhiều hơn
Độ ngắn gọn	Rất ngắn gọn	Dài hơn
Dễ debug	Trung bình	Tốt
Khả năng mở rộng	Trung bình	Cao
Phù hợp hệ thống lớn	Khá	Rất tốt
4. Chốt lựa chọn

Trong môi trường bệnh viện, nên chọn:

✅ Giải pháp 2
Lý do

Hệ thống y tế cần:

Độ ổn định cao
Dễ kiểm tra lỗi nhập liệu
Dễ mở rộng kiểm tra dữ liệu
An toàn dữ liệu bệnh nhân

Việc lưu dữ liệu gốc trước khi ép kiểu giúp:

Kiểm tra dữ liệu nhập sai
Log lỗi dễ dàng
Hạn chế mất dữ liệu quan trọng

=> Phù hợp hơn cho hệ thống thực tế của bệnh viện.

(2) Triển khai Code Python
"""

patient_id = input("Nhập mã bệnh nhân: ")
temp_input = input("Nhập nhiệt độ cơ thể: ")
heart_input = input("Nhập nhịp tim: ")

temperature = float(temp_input)
heart_rate = int(heart_input)

print("\n========= THÔNG TIN SINH HIỆU =========")
print("Mã bệnh nhân :", patient_id)
print("Nhiệt độ     :", temperature)
print("Nhịp tim     :", heart_rate)

print("\n===== KIỂM TRA KIỂU DỮ LIỆU =====")
print("Kiểu nhiệt độ :", type(temperature))
print("Kiểu nhịp tim :", type(heart_rate))