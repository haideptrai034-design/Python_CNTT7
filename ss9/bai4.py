"""
I. Phân tích Input / Output
Dữ liệu ban đầu
order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]
Chức năng 1: Hiển thị danh sách đơn hàng
Input

Không có.

Output

Nếu có dữ liệu:

Danh sách đơn hàng hiện tại:
1. GE001 - PENDING
2. GE002 - DELIVERING
3. GE003 - CANCELLED

Nếu danh sách rỗng:

Danh sách đơn hàng hiện đang trống.
Chức năng 2: Cập nhật danh sách đơn hàng
2.1 Thêm đơn hàng
Input
Mã đơn hàng: ge004
Trạng thái: pending
Xử lý
strip()
upper()
append()
Output
"GE004 - PENDING"

được thêm vào cuối danh sách.

2.2 Sửa đơn hàng theo vị trí
Input
Vị trí: 2
Mã mới: ge100
Trạng thái mới: completed
Output
order_list[1] = "GE100 - COMPLETED"
2.3 Xóa đơn hàng theo vị trí
Input
Vị trí: 3
Output
Đã xóa: GE003 - CANCELLED
Chức năng 3: Thống kê đơn hàng
Input

Danh sách đơn hàng.

Output
===== THỐNG KÊ ĐƠN HÀNG =====
PENDING: 2
DELIVERING: 1
COMPLETED: 0
CANCELLED: 1
Tổng số đơn hàng: 4
II. Đề xuất giải pháp
Các kiến thức cần dùng
Hàm/Phương thức	Công dụng
append()	Thêm đơn hàng
pop()	Xóa đơn hàng theo vị trí
strip()	Xóa khoảng trắng
upper()	Chuyển chữ hoa
split()	Tách trạng thái
enumerate()	Đánh số thứ tự
len()	Đếm số phần tử
try-except	Bắt lỗi nhập dữ liệu
match-case	Xử lý menu
Cách thống kê trạng thái

Ví dụ:

order = "GE001 - PENDING"

Tách chuỗi:

parts = order.split(" - ")
status = parts[1]

Kết quả:

status = "PENDING"

Sau đó tăng biến đếm tương ứng.

III. Pseudocode
Khởi tạo danh sách đơn hàng

Lặp vô hạn

    Hiển thị menu chính

    Nhập lựa chọn

    Nếu nhập sai
        báo lỗi
        quay lại menu

    match lựa chọn

        case 1:
            Hiển thị danh sách

        case 2:
            Hiển thị menu cập nhật

            match lựa chọn con

                case 1:
                    Thêm đơn hàng

                case 2:
                    Sửa đơn hàng theo vị trí

                case 3:
                    Xóa đơn hàng theo vị trí

                case 4:
                    Quay lại menu chính

        case 3:
            Thống kê trạng thái

        case 4:
            Thoát chương trình
IV. Source Code Hoàn Chỉnh
"""

# ==============================
# HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS
# ==============================

order_list = ["GE001 - PENDING", "GE002 - DELIVERING", "GE003 - CANCELLED"]

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    try:
        choice = int(input("Nhập lựa chọn: "))
    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    match choice:

        # =================================
        # HIỂN THỊ DANH SÁCH
        # =================================
        case 1:

            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("\nDanh sách đơn hàng hiện tại:")

                for index, order in enumerate(order_list, start=1):
                    print(f"{index}. {order}")

        # =================================
        # CẬP NHẬT DANH SÁCH
        # =================================
        case 2:

            while True:

                print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
                print("1. Thêm đơn hàng mới")
                print("2. Sửa đơn hàng theo vị trí")
                print("3. Xóa đơn hàng theo vị trí")
                print("4. Quay lại menu chính")

                try:
                    sub_choice = int(input("Nhập lựa chọn: "))
                except ValueError:
                    print("Lựa chọn không hợp lệ!")
                    continue

                match sub_choice:

                    # =====================
                    # THÊM ĐƠN HÀNG
                    # =====================
                    case 1:

                        order_code = input("Nhập mã đơn hàng: ").strip().upper()

                        status = input("Nhập trạng thái: ").strip().upper()

                        new_order = f"{order_code} - {status}"

                        order_list.append(new_order)

                        print("Thêm đơn hàng thành công!")

                    # =====================
                    # SỬA ĐƠN HÀNG
                    # =====================
                    case 2:

                        try:
                            position = int(input("Nhập vị trí cần sửa: "))
                        except ValueError:
                            print("Vị trí không hợp lệ!")
                            continue

                        index = position - 1

                        if 0 <= index < len(order_list):

                            order_code = input("Nhập mã mới: ").strip().upper()

                            status = input("Nhập trạng thái mới: ").strip().upper()

                            order_list[index] = f"{order_code} - {status}"

                            print("Cập nhật thành công!")

                        else:
                            print("Không tồn tại đơn hàng ở vị trí này!")

                    # =====================
                    # XÓA ĐƠN HÀNG
                    # =====================
                    case 3:

                        try:
                            position = int(input("Nhập vị trí cần xóa: "))
                        except ValueError:
                            print("Vị trí không hợp lệ!")
                            continue

                        index = position - 1

                        if 0 <= index < len(order_list):

                            removed_order = order_list.pop(index)

                            print(f"Đã xóa: {removed_order}")

                        else:
                            print("Không tồn tại đơn hàng ở vị trí này!")

                    # =====================
                    # QUAY LẠI
                    # =====================
                    case 4:
                        break

                    case _:
                        print("Lựa chọn không hợp lệ!")

        # =================================
        # THỐNG KÊ
        # =================================
        case 3:

            pending_count = 0
            delivering_count = 0
            completed_count = 0
            cancelled_count = 0

            for order in order_list:

                parts = order.split(" - ")

                if len(parts) == 2:

                    status = parts[1]

                    match status:

                        case "PENDING":
                            pending_count += 1

                        case "DELIVERING":
                            delivering_count += 1

                        case "COMPLETED":
                            completed_count += 1

                        case "CANCELLED":
                            cancelled_count += 1

            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            print(f"PENDING: {pending_count}")
            print(f"DELIVERING: {delivering_count}")
            print(f"COMPLETED: {completed_count}")
            print(f"CANCELLED: {cancelled_count}")
            print(f"Tổng số đơn hàng: {len(order_list)}")

        # =================================
        # THOÁT
        # =================================
        case 4:
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
