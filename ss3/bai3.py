"""
(1) Phân tích và thiết kế giải pháp
A. Phân tích Input / Output
Input (Dữ liệu đầu vào)

Hệ thống sẽ yêu cầu nhập 3 thông tin cho mỗi nhân viên:

Dữ liệu	Kiểu dữ liệu	Ví dụ
Mã nhân viên	string	NV001
Họ và tên	string	Nguyễn Văn A
Phòng ban	string	IT
Edge Cases cần xử lý
Bẫy 1 — Bỏ trống

Ví dụ:

Người dùng chỉ nhấn Enter.

Bẫy 2 — Chỉ chứa khoảng trắng

Ví dụ:

"     "

Dữ liệu nhìn có vẻ có ký tự nhưng thực tế vô nghĩa.

Output (Kết quả đầu ra)
Trường hợp hợp lệ

Hệ thống in Phiếu Hồ sơ:

===== HỒ SƠ NHÂN SỰ =====
Mã nhân viên : NV001
Họ và tên    : Nguyễn Văn A
Phòng ban    : IT
=========================
Trường hợp không hợp lệ

Hiển thị cảnh báo:

LỖI: Mã nhân viên hoặc Họ tên không hợp lệ!

Và KHÔNG in phiếu hồ sơ.

B. Đề xuất giải pháp
1. Sử dụng vòng lặp

Dùng:

for i in range(3):

để lặp đúng 3 lần cho 3 nhân viên.

2. Kiểm tra dữ liệu hợp lệ

Dùng:

.strip()

để loại bỏ khoảng trắng đầu/cuối.

Ví dụ:

name = "    "

Sau:

name.strip()

sẽ trở thành:

""

=> có thể kiểm tra rỗng dễ dàng.

3. Điều kiện kiểm tra

Nếu:

mã nhân viên rỗng
HOẶC
họ tên rỗng

thì báo lỗi.

if employee_id.strip() == "" or full_name.strip() == "":
4. Điều hướng chương trình

Khi dữ liệu lỗi:

in cảnh báo
bỏ qua phần in hồ sơ

Dùng:

continue
C. Thiết kế thuật toán (Pseudocode)
Bắt đầu chương trình

Lặp 3 lần:

    Nhập mã nhân viên
    Nhập họ tên
    Nhập phòng ban

    Nếu mã nhân viên rỗng
    HOẶC họ tên rỗng:

        In cảnh báo lỗi
        Chuyển sang nhân viên tiếp theo

    Ngược lại:

        In phiếu hồ sơ nhân sự

In thông báo hoàn thành

Kết thúc chương trình
(2) Triển khai Code Python
"""
# Hệ thống khởi tạo hồ sơ nhân sự

# Lặp đúng 3 lần cho 3 nhân viên
for i in range(3):

    print(f"\n===== NHẬP THÔNG TIN NHÂN VIÊN {i + 1} =====")

    # Nhập dữ liệu
    employee_id = input("Nhập mã nhân viên: ")
    full_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban: ")

    # Kiểm tra dữ liệu không hợp lệ
    # strip() dùng để loại bỏ khoảng trắng đầu/cuối
    if employee_id.strip() == "" or full_name.strip() == "":

        print("\nLỖI: Mã nhân viên hoặc Họ tên không hợp lệ!")

        # Bỏ qua phần in hồ sơ
        continue

    # In phiếu hồ sơ điện tử
    print("\n===== HỒ SƠ NHÂN SỰ =====")
    print("Mã nhân viên :", employee_id)
    print("Họ và tên    :", full_name)
    print("Phòng ban    :", department)
    print("=========================")

# Kết thúc chương trình
print("\nĐã hoàn tất onboarding cho 3 nhân viên!")