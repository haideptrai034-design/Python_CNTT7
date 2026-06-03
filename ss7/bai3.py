"""
(1) Phân tích và thiết kế giải pháp
1. Phân tích Input / Output
Input
raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

Kiểu dữ liệu:

str

Ngoài ra chương trình còn nhận:

Lựa chọn menu từ người dùng (input())
Mã nhân viên cần tìm kiếm (input())
Output
Chức năng 1

Hiển thị nguyên chuỗi dữ liệu.

Ví dụ:

 eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT
Chức năng 2

Hiển thị báo cáo đã chuẩn hóa.

Ví dụ:

ID         HỌ TÊN             SĐT           PHÒNG BAN
------------------------------------------------------
EMP-001    Nguyen Van A       ******4321    SALE
EMP-002    Tran Thi B         ******5678    MKT
EMP-003    Le Van C           Invalid Format IT
Chức năng 3

Tìm kiếm theo mã nhân viên.

Ví dụ:

Nhập mã nhân viên: emp-002

ID: EMP-002
Tên: Tran Thi B
SĐT: ******5678
Phòng ban: MKT

Hoặc:

Không tìm thấy nhân viên
2. Đề xuất giải pháp
Bước 1: Tách nhân viên

Dùng:

employees = raw_data.split("|")
Bước 2: Tách từng trường

Mỗi nhân viên:

fields = employee.split(";")

Gồm:

id
name
phone
department
Bước 3: Chuẩn hóa dữ liệu
ID
emp_id = fields[0].strip().upper()
Họ tên
name = fields[1].strip().title()
Phòng ban
department = fields[3].strip().upper()
Số điện thoại

Xóa dấu "-"

phone = phone.replace("-", "")

Kiểm tra:

phone.isdigit()

Nếu đúng:

masked_phone = "******" + phone[-4:]

Nếu sai:

masked_phone = "Invalid Format"
Bước 4: Lưu dữ liệu đã chuẩn hóa

Dùng list:

employees_data = []

Mỗi nhân viên:

{
    "id": emp_id,
    "name": name,
    "phone": masked_phone,
    "department": department
}
Bước 5: Tìm kiếm

Chuẩn hóa dữ liệu nhập:

search_id = input(...).strip().upper()

So sánh:

if employee["id"] == search_id:
Bước 6: Kiểm tra menu

Sử dụng:

try:
    choice = int(input(...))
except ValueError:

để bắt trường hợp nhập chữ.

3. Pseudocode
Khởi tạo raw_data

Lặp vô hạn

    Hiển thị menu

    Nhập lựa chọn

    Nếu nhập không phải số
        Thông báo lỗi
        Tiếp tục

    Nếu chọn 1
        In raw_data

    Nếu chọn 2
        Chuẩn hóa dữ liệu
        In bảng báo cáo

    Nếu chọn 3
        Nhập mã nhân viên

        Chuẩn hóa mã tìm kiếm

        Duyệt danh sách nhân viên

        Nếu tìm thấy
            In thông tin
        Ngược lại
            In không tìm thấy

    Nếu chọn 4
        In thoát chương trình
        Kết thúc

    Nếu khác 1-4
        Thông báo lỗi
(2) Triển khai Code
"""

# Dữ liệu gốc
raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "


def normalize_data(raw_data):
    """
    Chuẩn hóa dữ liệu nhân viên
    Trả về danh sách dictionary
    """

    employees_data = []

    employees = raw_data.split("|")

    for employee in employees:
        fields = employee.split(";")

        emp_id = fields[0].strip().upper()
        name = fields[1].strip().title()
        phone = fields[2].strip()
        department = fields[3].strip().upper()

        # Xóa dấu -
        phone = phone.replace("-", "")

        # Kiểm tra định dạng số điện thoại
        if phone.isdigit():
            phone = "******" + phone[-4:]
        else:
            phone = "Invalid Format"

        employees_data.append({
            "id": emp_id,
            "name": name,
            "phone": phone,
            "department": department
        })

    return employees_data


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    try:
        choice = int(input("Nhập lựa chọn: "))
    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    if choice == 1:
        print("\nDỮ LIỆU GỐC:")
        print(raw_data)

    elif choice == 2:

        employees = normalize_data(raw_data)

        print("\nBÁO CÁO NHÂN SỰ")
        print("-" * 60)

        print(
            f"{'ID':<12}"
            f"{'HỌ TÊN':<25}"
            f"{'SĐT':<18}"
            f"{'PHÒNG BAN':<10}"
        )

        print("-" * 60)

        for emp in employees:
            print(
                f"{emp['id']:<12}"
                f"{emp['name']:<25}"
                f"{emp['phone']:<18}"
                f"{emp['department']:<10}"
            )

    elif choice == 3:

        employees = normalize_data(raw_data)

        search_id = input(
            "Nhập mã nhân viên cần tìm: "
        ).strip().upper()

        found = False

        for emp in employees:
            if emp["id"] == search_id:
                found = True

                print("\nTHÔNG TIN NHÂN VIÊN")
                print(f"ID: {emp['id']}")
                print(f"Họ tên: {emp['name']}")
                print(f"SĐT: {emp['phone']}")
                print(f"Phòng ban: {emp['department']}")
                break

        if not found:
            print("Không tìm thấy nhân viên")

    elif choice == 4:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")