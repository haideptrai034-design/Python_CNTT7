"""
(1) Phân tích lỗi
1. Tuple product_info ban đầu có bao nhiêu phần tử?
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

Tuple có 4 phần tử:

Index	Giá trị
0	"SP001"
1	"Áo polo nam"
2	"Size L"
3	299000
2. Phần tử "SP001" nằm ở index nào?
"SP001"

Nằm ở index 0.

3. Vì sao dòng sau lấy sai mã sản phẩm?
product_code = product_info[1]

Vì:

product_info[1]

trả về:

"Áo polo nam"

Trong khi mã sản phẩm "SP001" nằm ở index 0.

Đúng phải là:

product_code = product_info[0]
4. Phần tử "Áo polo nam" nằm ở index nào?

Nằm ở index 1.

5. Vì sao dòng sau lấy sai tên sản phẩm?
product_name = product_info[2]

Vì:

product_info[2]

trả về:

"Size L"

Trong khi tên sản phẩm nằm ở index 1.

Đúng phải là:

product_name = product_info[1]
6. Vì sao dòng sau gây lỗi?
product_length = product_info.length()

Tuple không có phương thức:

length()

nên Python báo:

AttributeError
7. Muốn đếm số phần tử trong tuple cần dùng hàm nào?

Dùng hàm:

len()

Ví dụ:

product_length = len(product_info)

Kết quả:

4
8. Vì sao dòng sau không hợp lệ?
product_info[3] = 279000

Vì tuple là kiểu dữ liệu immutable (bất biến).

Sau khi tạo ra, các phần tử trong tuple không thể thay đổi trực tiếp.

Python sẽ báo:

TypeError: 'tuple' object does not support item assignment
9. Tuple có cho phép sửa trực tiếp phần tử không?

❌ Không.

Tuple là kiểu dữ liệu bất biến.

Ví dụ:

t = (1, 2, 3)

t[0] = 10

=> Lỗi.

10. Muốn cập nhật giá bán từ 299000 thành 279000 cần làm gì?

Phải tạo một tuple mới.

Ví dụ:

product_info = (
    product_info[0],
    product_info[1],
    product_info[2],
    279000
)

Hoặc:

product_info = product_info[:3] + (279000,)
(2) Source Code Đúng
"""

# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm
product_code = product_info[0]

# Lấy tên sản phẩm
product_name = product_info[1]

# Đếm số lượng thông tin sản phẩm
product_length = len(product_info)

# Tạo tuple mới với giá bán cập nhật
product_info = (
    product_info[0],
    product_info[1],
    product_info[2],
    279000
)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)