"""
(1) Phân tích lỗi

Giả sử đoạn code cũ có dạng như sau:

for i in range(3):

    working_days = int(input("Nhập số ngày công: "))

    if working_days == 0:
        print("Cảnh báo: Nhân viên không đủ điều kiện nhận thưởng")

    bonus = working_days * 100000

    print("Tiền thưởng:", bonus)
    print("Đã gửi email chúc mừng!")
Vấn đề nằm ở đâu?

Phần này:

if working_days == 0:
    print("Cảnh báo")

chỉ đơn giản là in cảnh báo.

Sau khi in xong, chương trình KHÔNG dừng.

Nó vẫn tiếp tục chạy các dòng bên dưới:

bonus = working_days * 100000

print("Tiền thưởng:", bonus)
print("Đã gửi email chúc mừng!")
Trace code khi nhập ngày công = 0

Giả sử HR nhập:

0
Bước 1
working_days = 0
Bước 2

Kiểm tra điều kiện:

if working_days == 0:

Điều kiện đúng.

=> In ra:

Cảnh báo: Nhân viên không đủ điều kiện nhận thưởng
Bước 3

Sau khi in cảnh báo xong, chương trình KHÔNG thoát vòng lặp.

Nó chạy tiếp:

bonus = working_days * 100000

Tức là:

bonus = 0 * 100000

=> bonus = 0

Bước 4

Tiếp tục:

print("Tiền thưởng:", bonus)

In ra:

Tiền thưởng: 0
Bước 5

Tiếp tục gửi email:

print("Đã gửi email chúc mừng!")

=> Đây chính là lỗi nghiệp vụ.

Nguyên nhân cốt lõi

Chương trình:

Có kiểm tra điều kiện
Nhưng không điều hướng luồng xử lý

Nó thiếu lệnh:

continue

hoặc thiếu else.

Lỗi logic kinh điển

Đây là lỗi:

“Đi vào nhánh điều kiện nhưng không ngăn chương trình chạy tiếp”

Rất phổ biến trong vòng lặp.

Ý nghĩa của continue

continue dùng để:

Bỏ qua phần còn lại của vòng lặp hiện tại và chuyển sang lần lặp tiếp theo.

Đây chính là thứ hệ thống cần.

(2) Sửa lỗi
"""
# Lặp qua 3 nhân viên
for i in range(3):

    print(f"\nNhân viên {i + 1}")

    # Nhập số ngày công
    working_days = int(input("Nhập số ngày công: "))

    # Nếu ngày công = 0
    if working_days == 0:
        print("Cảnh báo: Nhân viên không đủ điều kiện nhận thưởng")

        # Bỏ qua phần tính thưởng
        continue

    # Tính thưởng cho nhân viên hợp lệ
    bonus = working_days * 100000

    # Hiển thị thưởng
    print("Tiền thưởng:", bonus, "VNĐ")

    # Gửi email
    print("Đã gửi email chúc mừng!")