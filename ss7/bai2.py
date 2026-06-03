"""
(1) Phân tích lỗi
1. Vì sao transaction.strip() không làm thay đổi trực tiếp chuỗi ban đầu?

Vì chuỗi trong Python là immutable (bất biến).

Ví dụ:

transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

transaction.strip()

strip() tạo ra một chuỗi mới:

"nguyEN vAn a | PYTHON-01 | 15000000 | paid"

nhưng không được gán lại cho biến transaction, nên giá trị ban đầu vẫn giữ nguyên.

Muốn thay đổi:

transaction = transaction.strip()
2. Chuỗi giao dịch thực tế được phân tách bằng ký tự nào?

Dữ liệu có dạng:

"  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

Các trường được ngăn cách bởi:

|

Vì vậy cần dùng:

split("|")
3. Vì sao transaction.split("-") là sai?

Dấu - không phải ký tự phân cách giữa các trường dữ liệu.

Nếu dùng:

parts = transaction.split("-")

Python sẽ tách ở vị trí:

PYTHON-01

thành:

["  nguyEN vAn a | PYTHON", "01 | 15000000 | paid  "]

Trong khi ta cần 4 phần dữ liệu riêng biệt:

[
    "nguyEN vAn a",
    "PYTHON-01",
    "15000000",
    "paid"
]
4. Sau khi tách bằng sai delimiter, dữ liệu trong parts bị lệch như thế nào?

Ví dụ:

parts = transaction.split("-")
print(parts)

Kết quả:

[
 '  nguyEN vAn a | PYTHON',
 '01 | 15000000 | paid  '
]

Lúc này:

parts[0] chứa cả tên học viên và một phần mã khóa học
parts[1] chứa phần còn lại

Dữ liệu không còn đúng cấu trúc 4 trường nên chương trình dễ phát sinh lỗi khi truy xuất.

5. Vì sao cần .strip() lại từng phần sau khi split()?

Sau khi tách:

parts = transaction.split("|")

Ta nhận được:

[
 '  nguyEN vAn a ',
 ' PYTHON-01 ',
 ' 15000000 ',
 ' paid  '
]

Các phần tử vẫn còn khoảng trắng ở đầu và cuối.

Ví dụ:

parts[0]

là:

'  nguyEN vAn a '

chứ không phải:

'nguyEN vAn a'

Do đó cần:

name = parts[0].strip()
6. Vì sao cần chuyển amount từ chuỗi sang số trước khi định dạng tiền?

Sau khi tách:

amount = "15000000"

Đây vẫn là chuỗi (str).

Để định dạng tiền:

f"{amount:,}"

Python yêu cầu dữ liệu phải là số.

Cần chuyển:

amount = int(amount)

Sau đó:

f"{amount:,}"

Kết quả:

15,000,000
(2) Sửa lỗi
"""

transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

# Xóa khoảng trắng đầu cuối
transaction = transaction.strip()

# Tách dữ liệu
parts = transaction.split("|")

# Chuẩn hóa từng trường
student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = int(parts[2].strip())
status = parts[3].strip().upper()

# Hiển thị báo cáo
print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", f"{amount:,} VND")
print("Trạng thái:", status)