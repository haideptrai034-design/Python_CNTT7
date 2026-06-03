"""
(1) Phân tích lỗi
Vì sao student_name.strip() không làm thay đổi trực tiếp biến student_name?

Trong Python, chuỗi (string) là kiểu dữ liệu bất biến (immutable).

Điều đó có nghĩa là sau khi được tạo ra, nội dung của chuỗi không thể bị thay đổi trực tiếp.

Ví dụ:

student_name = "  nguYEn vAn a  "

student_name.strip()

Lệnh strip() tạo ra một chuỗi mới:

"nguYEn vAn a"

nhưng kết quả này không được lưu vào đâu cả, nên Python bỏ đi ngay sau khi thực hiện.

Biến student_name vẫn giữ nguyên giá trị ban đầu:

"  nguYEn vAn a  "
Vì sao student_name.title() không tạo ra kết quả "Nguyen Van A"?

Tương tự:

student_name.title()

sẽ trả về:

"  Nguyen Van A  "

nhưng vì không gán lại cho biến nên giá trị mới bị mất.

Do đó:

print(student_name)

vẫn in ra:

"  nguYEn vAn a  "
Vì sao student_code.upper() không làm mã học viên chuyển thành chữ hoa?

upper() cũng trả về một chuỗi mới:

student_code.upper()

trả về:

"  RK-001-PYTHON  "

nhưng không gán lại nên:

student_code

vẫn là:

"  rk-001-python  "
Vì sao email.lower() không làm email chuyển thành chữ thường?

Tương tự:

email.lower()

trả về:

"  student01@gmail.com  "

nhưng kết quả không được lưu lại.

Do đó:

email

vẫn là:

"  Student01@GMAIL.COM  "
Muốn các phương thức xử lý chuỗi có hiệu lực cần làm gì?

Phải gán lại kết quả trả về cho biến.

Ví dụ:

student_name = student_name.strip()

hoặc:

student_name = student_name.strip().title()

Khi đó biến sẽ nhận giá trị mới đã được xử lý.

(2) Sửa lỗi
"""

student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)




