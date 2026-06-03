"""
(1) Phân tích và thiết kế giải pháp
1. Input / Output
Dữ liệu ban đầu
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    }
]

Kiểu dữ liệu:

product_list: list
Mỗi sản phẩm: dictionary
Input từ người dùng

Menu:

1 → Hiển thị sản phẩm
2 → Thêm sản phẩm
3 → Cập nhật sản phẩm
4 → Xóa sản phẩm
5 → Thoát

Thông tin sản phẩm:

product_id     : str
product_name   : str
price          : int
quantity       : int
Output

Ví dụ:

1. Mã SP: SP001 | Tên: Áo polo nam | Giá: 299000 | Số lượng: 20

hoặc

Không tìm thấy mã sản phẩm cần cập nhật!
2. Giải pháp
Chức năng 1 - Hiển thị

Kiểm tra:

if len(product_list) == 0

Nếu rỗng:

Danh sách sản phẩm hiện đang trống.

Ngược lại dùng:

enumerate()

để in.

Chức năng 2 - Thêm sản phẩm
Chuẩn hóa mã
product_id = input(...).strip().upper()

Ví dụ:

"   sp004 "

thành:

SP004
Kiểm tra trùng mã

Duyệt danh sách:

for product in product_list:

so sánh:

product["product_id"]
Kiểm tra giá và số lượng
price = int(input())

Nếu:

price <= 0

=> Không hợp lệ

Dùng:

try:
    ...
except ValueError:

để bắt trường hợp nhập chữ.

Thêm sản phẩm
product_list.append(new_product)
Chức năng 3 - Cập nhật

Nhập:

product_id

Chuẩn hóa:

strip().upper()

Tìm sản phẩm.

Nếu tồn tại:

product["product_name"] = ...
product["price"] = ...
product["quantity"] = ...
Chức năng 4 - Xóa

Tìm sản phẩm theo mã.

Nếu có:

product_list.remove(product)
Chức năng 5
break
3. Thuật toán (Pseudocode)
Lặp vô hạn:

    Hiển thị menu

    Nhập lựa chọn

    Nếu lựa chọn = 1:
        Hiển thị danh sách sản phẩm

    Nếu lựa chọn = 2:
        Nhập sản phẩm mới
        Chuẩn hóa mã
        Kiểm tra trùng mã
        Kiểm tra giá và số lượng
        Thêm sản phẩm

    Nếu lựa chọn = 3:
        Nhập mã cần cập nhật
        Tìm sản phẩm
        Nếu tìm thấy:
            Cập nhật
        Ngược lại:
            Thông báo không tìm thấy

    Nếu lựa chọn = 4:
        Nhập mã cần xóa
        Tìm sản phẩm
        Nếu tìm thấy:
            Xóa
        Ngược lại:
            Thông báo không tìm thấy

    Nếu lựa chọn = 5:
        Thoát chương trình

    Ngược lại:
        Báo lựa chọn không hợp lệ
(2) Triển khai Code
"""

# Danh sách sản phẩm ban đầu
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    # ================= HIỂN THỊ =================
    if choice == "1":

        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")

            for index, product in enumerate(product_list, start=1):
                print(
                    f"{index}. Mã SP: {product['product_id']} | "
                    f"Tên: {product['product_name']} | "
                    f"Giá: {product['price']} | "
                    f"Số lượng: {product['quantity']}"
                )

    # ================= THÊM =================
    elif choice == "2":

        product_id = input("Nhập mã sản phẩm: ").strip().upper()

        duplicate = False

        for product in product_list:
            if product["product_id"] == product_id:
                duplicate = True
                break

        if duplicate:
            print("Mã sản phẩm bị trùng")
            continue

        product_name = input("Nhập tên sản phẩm: ").strip()

        try:
            price = int(input("Nhập giá sản phẩm: "))
            quantity = int(input("Nhập số lượng sản phẩm: "))

            if price <= 0 or quantity <= 0:
                print("Giá/Số lượng không hợp lệ")
                continue

        except ValueError:
            print("Giá/Số lượng không hợp lệ")
            continue

        new_product = {
            "product_id": product_id,
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        }

        product_list.append(new_product)

        print("Thêm sản phẩm thành công")

    # ================= CẬP NHẬT =================
    elif choice == "3":

        product_id = input(
            "Nhập mã sản phẩm cần cập nhật: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                product_name = input(
                    "Nhập tên sản phẩm mới: "
                ).strip()

                try:
                    price = int(input("Nhập giá mới: "))
                    quantity = int(input("Nhập số lượng mới: "))

                    if price <= 0 or quantity <= 0:
                        print("Giá/Số lượng không hợp lệ")
                        break

                    product["product_name"] = product_name
                    product["price"] = price
                    product["quantity"] = quantity

                    print("Cập nhật sản phẩm thành công")

                except ValueError:
                    print("Giá/Số lượng không hợp lệ")

                break

        if not found:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")

    # ================= XÓA =================
    elif choice == "4":

        product_id = input(
            "Nhập mã sản phẩm cần xóa: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:
                product_list.remove(product)
                found = True
                print("Xóa sản phẩm thành công")
                break

        if not found:
            print("Không tìm thấy mã sản phẩm cần xoá!")

    # ================= THOÁT =================
    elif choice == "5":
        print("Thoát chương trình.")
        break

    # ================= SAI MENU =================
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")