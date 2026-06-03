"""
I. PHÂN TÍCH INPUT / OUTPUT
Dữ liệu ban đầu
order_list = ["GE001", "GE002", "GE003"]
Chức năng 1: Hiển thị danh sách đơn hàng
Input

Không cần nhập dữ liệu.

Output

Nếu danh sách có dữ liệu:

Danh sách đơn hàng hiện tại:
1. GE001
2. GE002
3. GE003

Nếu danh sách rỗng:

Danh sách đơn hàng hiện đang trống.
Chức năng 2: Thêm đơn hàng
Input
ge004
Xử lý
strip()
upper()
append()
Output
["GE001", "GE002", "GE003", "GE004"]
Chức năng 3: Xóa đơn hàng
Input
GE002
Output
Đã xóa đơn hàng GE002

Nếu không tồn tại:

Không tìm thấy mã đơn hàng cần xóa!
Chức năng 4: Thoát
Output
Thoát chương trình.
II. GIẢI PHÁP
Các phương thức cần sử dụng
Phương thức	Công dụng
append()	Thêm phần tử vào cuối list
remove()	Xóa phần tử theo giá trị
strip()	Xóa khoảng trắng đầu cuối
upper()	Chuyển thành chữ hoa
len()	Kiểm tra danh sách rỗng
enumerate()	Đánh số thứ tự khi hiển thị
Ý tưởng xử lý
Hiển thị danh sách

Kiểm tra:

if len(order_list) == 0:

Nếu rỗng → thông báo.

Ngược lại:

for index, order in enumerate(order_list, start=1):

để đánh số.

Thêm đơn hàng

Chuẩn hóa:

order_code = input(...).strip().upper()

Sau đó:

order_list.append(order_code)
Xóa đơn hàng

Chuẩn hóa:

order_code = input(...).strip().upper()

Kiểm tra:

if order_code in order_list:

Nếu có:

order_list.remove(order_code)

Nếu không:

print("Không tìm thấy mã đơn hàng cần xóa!")
Xử lý menu sai

Dùng:

try:
    choice = int(input())
except ValueError:

để bắt:

abc
@
2.5
III. PSEUDOCODE
Khai báo order_list

Lặp vô hạn

    Hiển thị menu

    Nhập lựa chọn

    Nếu nhập không phải số
        báo lỗi
        quay lại menu

    match choice

        case 1
            hiển thị danh sách

        case 2
            nhập mã đơn hàng
            chuẩn hóa
            thêm vào list

        case 3
            nhập mã đơn hàng
            chuẩn hóa

            nếu tồn tại
                xóa
            ngược lại
                báo lỗi

        case 4
            thoát chương trình

        case _
            báo lựa chọn không hợp lệ
IV. SOURCE CODE HOÀN CHỈNH
"""

# =====================================
# HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS
# =====================================

order_list = ["GE001", "GE002", "GE003"]

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")

    try:
        choice = int(input("Nhập lựa chọn: "))
    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    match choice:

        # ====================
        # HIỂN THỊ DANH SÁCH
        # ====================
        case 1:

            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("\nDanh sách đơn hàng hiện tại:")

                for index, order in enumerate(order_list, start=1):
                    print(f"{index}. {order}")

        # ====================
        # THÊM ĐƠN HÀNG
        # ====================
        case 2:

            order_code = input(
                "Nhập mã đơn hàng mới: "
            )

            order_code = (
                order_code
                .strip()
                .upper()
            )

            order_list.append(order_code)

            print(
                f"Đã thêm đơn hàng {order_code}"
            )

        # ====================
        # XÓA ĐƠN HÀNG
        # ====================
        case 3:

            order_code = input(
                "Nhập mã đơn hàng cần xóa: "
            )

            order_code = (
                order_code
                .strip()
                .upper()
            )

            if order_code in order_list:

                order_list.remove(order_code)

                print(
                    f"Đã xóa đơn hàng {order_code}"
                )

            else:
                print(
                    "Không tìm thấy mã đơn hàng cần xóa!"
                )

        # ====================
        # THOÁT
        # ====================
        case 4:
            print("Thoát chương trình.")
            break

        # ====================
        # MENU KHÔNG HỢP LỆ
        # ====================
        case _:
            print(
                "Lựa chọn không hợp lệ, vui lòng nhập lại!"
            )