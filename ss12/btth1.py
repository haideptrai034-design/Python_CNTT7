"""
(1) Phân tích và thiết kế giải pháp
1. Phân tích Input / Output
Dữ liệu ban đầu
cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]
Kiểu dữ liệu
cart_items → list
Mỗi sản phẩm → dictionary
id → str
name → str
number → int
price → int
Input
Menu
1 → Xem giỏ hàng
2 → Thêm sản phẩm
3 → Cập nhật số lượng
4 → Xóa sản phẩm
5 → Thoát
Thêm sản phẩm
Mã sản phẩm
Tên sản phẩm
Số lượng
Đơn giá
Cập nhật
Mã sản phẩm
Số lượng mới
Xóa
Mã sản phẩm
Output
Xem giỏ hàng
ID     Tên sản phẩm             SL      Đơn giá
P001   Dien thoai iPhone 15      1      25000000
P002   Op lung Silicon           2      150000

Tổng số lượng: 3
Tổng tiền: 25300000
2. Đề xuất giải pháp
Chức năng 1: Xem giỏ hàng

Duyệt list:

for item in cart_items:

Tính:

total_quantity += item["number"]
total_money += item["number"] * item["price"]
Chức năng 2: Thêm sản phẩm
Bước 1

Chuẩn hóa mã:

product_id = input(...).strip().upper()
Bước 2

Kiểm tra số lượng và đơn giá

quantity > 0
price > 0

Nếu không:

Dữ liệu không hợp lệ
Bước 3

Kiểm tra mã đã tồn tại

for item in cart_items:

Nếu:

item["id"] == product_id

thì:

item["number"] += quantity

Ngược lại:

cart_items.append(...)
Chức năng 3: Cập nhật số lượng

Tìm theo mã.

Nếu tồn tại:

item["number"] = new_quantity
Chức năng 4: Xóa sản phẩm

Tìm theo mã.

Nếu tồn tại:

cart_items.remove(item)
Chức năng 5
break
3. Pseudocode
Lặp vô hạn

    Hiển thị menu

    Nhập lựa chọn

    Nếu = 1:
        Hiển thị giỏ hàng
        Tính tổng SL
        Tính tổng tiền

    Nếu = 2:
        Nhập thông tin sản phẩm

        Kiểm tra hợp lệ

        Nếu mã tồn tại:
            Cộng dồn số lượng

        Nếu chưa tồn tại:
            Thêm mới

    Nếu = 3:
        Nhập mã sản phẩm
        Nhập số lượng mới

        Nếu tồn tại:
            Cập nhật

        Nếu không:
            Thông báo lỗi

    Nếu = 4:
        Nhập mã sản phẩm

        Nếu tồn tại:
            Xóa

        Nếu không:
            Thông báo lỗi

    Nếu = 5:
        Thoát

    Ngược lại:
        Báo menu không hợp lệ
(2) Source Code Hoàn Chỉnh
"""

# ==========================
# DỮ LIỆU BAN ĐẦU
# ==========================

cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]

while True:

    print("\n===== AMAZON CART MANAGEMENT =====")
    print("1. Xem giỏ hàng")
    print("2. Thêm sản phẩm")
    print("3. Cập nhật số lượng")
    print("4. Xóa sản phẩm")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ").strip()

    # ==========================
    # XEM GIỎ HÀNG
    # ==========================

    if choice == "1":

        if len(cart_items) == 0:
            print("Giỏ hàng đang trống.")
            continue

        total_quantity = 0
        total_money = 0

        print("\n===== CHI TIẾT GIỎ HÀNG =====")

        print(
            f"{'ID':<10}"
            f"{'Tên sản phẩm':<30}"
            f"{'SL':<10}"
            f"{'Đơn giá':<15}"
        )

        for item in cart_items:

            print(
                f"{item['id']:<10}"
                f"{item['name']:<30}"
                f"{item['number']:<10}"
                f"{item['price']:<15}"
            )

            total_quantity += item["number"]
            total_money += (
                item["number"] * item["price"]
            )

        print("\nTổng số lượng:", total_quantity)
        print("Tổng tiền:", total_money)

    # ==========================
    # THÊM SẢN PHẨM
    # ==========================

    elif choice == "2":

        product_id = input(
            "Nhập mã sản phẩm: "
        ).strip().upper()

        product_name = input(
            "Nhập tên sản phẩm: "
        ).strip()

        try:

            quantity = int(
                input("Nhập số lượng: ")
            )

            price = int(
                input("Nhập đơn giá: ")
            )

            if quantity <= 0 or price <= 0:
                print("Dữ liệu không hợp lệ.")
                continue

        except ValueError:
            print("Dữ liệu không hợp lệ.")
            continue

        found = False

        for item in cart_items:

            if item["id"] == product_id:

                item["number"] += quantity

                found = True

                print(
                    "Sản phẩm đã tồn tại, "
                    "đã cộng dồn số lượng."
                )

                break

        if not found:

            new_item = {
                "id": product_id,
                "name": product_name,
                "number": quantity,
                "price": price
            }

            cart_items.append(new_item)

            print("Thêm sản phẩm thành công.")

    # ==========================
    # CẬP NHẬT SỐ LƯỢNG
    # ==========================

    elif choice == "3":

        product_id = input(
            "Nhập mã sản phẩm: "
        ).strip().upper()

        found = False

        for item in cart_items:

            if item["id"] == product_id:

                found = True

                try:

                    new_quantity = int(
                        input(
                            "Nhập số lượng mới: "
                        )
                    )

                    if new_quantity <= 0:
                        print(
                            "Số lượng không hợp lệ."
                        )
                        break

                    item["number"] = new_quantity

                    print(
                        "Cập nhật thành công."
                    )

                except ValueError:
                    print(
                        "Số lượng không hợp lệ."
                    )

                break

        if not found:
            print(
                "Mã sản phẩm không tồn tại "
                "trong giỏ hàng."
            )

    # ==========================
    # XÓA SẢN PHẨM
    # ==========================

    elif choice == "4":

        product_id = input(
            "Nhập mã sản phẩm cần xóa: "
        ).strip().upper()

        found = False

        for item in cart_items:

            if item["id"] == product_id:

                cart_items.remove(item)

                found = True

                print("Xóa thành công.")

                break

        if not found:
            print(
                "Mã sản phẩm không tồn tại "
                "trong giỏ hàng."
            )

    # ==========================
    # THOÁT
    # ==========================

    elif choice == "5":

        print("Thoát chương trình.")
        break

    # ==========================
    # MENU KHÔNG HỢP LỆ
    # ==========================

    else:

        print(
            "Lựa chọn không hợp lệ. "
            "Vui lòng nhập từ 1 đến 5."
        )