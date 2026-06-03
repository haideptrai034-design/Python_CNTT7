"""
(1) Phân tích & Đề xuất giải pháp
A. Phân tích Input / Output
Input (Dữ liệu đầu vào)

Người dùng nhập:

Số lượng nhân sự mới

Kiểu dữ liệu:

int

Ví dụ hợp lệ:

1
5
10

Ví dụ không hợp lệ:

0
-3
-10
Output (Kết quả đầu ra)
Nếu dữ liệu không hợp lệ

Hệ thống phải báo lỗi:

LỖI: Số lượng nhân sự phải lớn hơn 0!

và bắt nhập lại.

Nếu dữ liệu hợp lệ

Hệ thống hiển thị:

Ghi nhận thành công!

và kết thúc chương trình.

B. Đề xuất 2 giải pháp validation loop
Giải pháp 1 — Dùng while True
Ý tưởng
Tạo vòng lặp vô hạn
Nếu dữ liệu đúng → break
Nếu sai → nhập lại
Ví dụ
while True:

    number = int(input("Nhập số lượng nhân sự: "))

    if number > 0:
        print("Ghi nhận thành công!")
        break

    print("LỖI: Dữ liệu không hợp lệ")
Giải pháp 2 — Dùng điều kiện trực tiếp trong while
Ý tưởng
Gán giá trị ban đầu
Lặp khi dữ liệu chưa hợp lệ
Ví dụ
number = 0

while number <= 0:

    number = int(input("Nhập số lượng nhân sự: "))

    if number <= 0:
        print("LỖI: Dữ liệu không hợp lệ")

print("Ghi nhận thành công!")
C. Bảng so sánh hai giải pháp
Tiêu chí	while True	while điều kiện
Độ ngắn gọn	Ngắn	Hơi dài hơn
Dễ đọc	Trung bình	Rất dễ hiểu
Gần ngôn ngữ tự nhiên	Không bằng	Rất gần
Dễ bảo trì	Tốt	Tốt
Phù hợp validation	Rất phổ biến	Rất phù hợp
D. Chốt lựa chọn

Tôi chọn:

while number <= 0
Lý do

Cách này:

Dễ hiểu với người mới học
Điều kiện lặp thể hiện rõ nghiệp vụ
Đọc giống ngôn ngữ tự nhiên:

“Trong khi số lượng còn nhỏ hơn hoặc bằng 0 thì tiếp tục nhập”

Rất phù hợp cho bài toán validation input.

(2) Triển khai Code
"""

# Khởi tạo giá trị ban đầu không hợp lệ
employee_count = 0

# Lặp cho đến khi nhập đúng số > 0
while employee_count <= 0:

    # Nhập số lượng nhân sự mới
    employee_count = int(
        input("Vui lòng nhập số lượng nhân sự mới trong tháng này: ")
    )

    # Kiểm tra dữ liệu không hợp lệ
    if employee_count <= 0:
        print("LỖI: Số lượng nhân sự phải lớn hơn 0!")

# Khi thoát khỏi vòng lặp nghĩa là dữ liệu đã hợp lệ
print("Ghi nhận thành công!")
print("Số lượng nhân sự mới:", employee_count)