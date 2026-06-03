"""
(1) Phân tích lỗi

Đây là lỗi logic rất phổ biến khi mới học vòng lặp.

Giả sử thực tập sinh viết code kiểu như sau:

total_budget = 0

for i in range(3):
    salary = int(input("Nhập lương nhân viên: "))
    total_budget = salary

print("Tổng quỹ lương:", total_budget)
Vì sao sai?

Dòng gây lỗi là:

total_budget = salary

Dấu = trong Python là gán giá trị, không phải cộng dồn.

Mỗi lần vòng lặp chạy:

Giá trị cũ của total_budget bị ghi đè
Chỉ giữ lại mức lương mới nhất
Trace code (dò luồng thực thi)

Giả sử nhập:

5000000
4000000
6000000
Ban đầu
total_budget = 0

Giá trị:

total_budget = 0
Lần lặp 1

Người dùng nhập:

5000000

Chương trình chạy:

total_budget = salary

=> lúc này:

total_budget = 5000000
Lần lặp 2

Người dùng nhập:

4000000

Chạy tiếp:

total_budget = salary

=> giá trị cũ bị mất

total_budget = 4000000
Lần lặp 3

Người dùng nhập:

6000000

Tiếp tục:

total_budget = salary

=> lại ghi đè

total_budget = 6000000
Kết quả cuối cùng
print(total_budget)

In ra:

6000000

Chỉ còn lương của nhân viên cuối cùng.

Lỗi logic kinh điển

Đây gọi là lỗi:

“Gán đè giá trị thay vì cộng dồn trong vòng lặp”

Người mới học thường nhầm:

total = value

với:

total = total + value
Nguyên tắc đúng khi cộng dồn

Muốn cộng nhiều giá trị trong vòng lặp phải dùng:

bien_tong = bien_tong + gia_tri_moi

hoặc viết ngắn gọn:

bien_tong += gia_tri_moi
Minh họa đúng
total_budget = 0

# nhập 5 triệu
total_budget = total_budget + 5000000
# = 5000000

# nhập 4 triệu
total_budget = total_budget + 4000000
# = 9000000

# nhập 6 triệu
total_budget = total_budget + 6000000
# = 15000000
(2) Sửa lỗi
"""
# Khởi tạo biến tổng quỹ lương
total_budget = 0

# Lặp 3 lần để nhập lương 3 nhân viên
for i in range(3):

    # Nhập lương nhân viên
    salary = int(input(f"Nhập lương nhân viên {i + 1}: "))

    # Cộng dồn vào tổng quỹ lương
    total_budget += salary

# Hiển thị kết quả cuối cùng
print("Tổng quỹ lương:", total_budget, "VNĐ")