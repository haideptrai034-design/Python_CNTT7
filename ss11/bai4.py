"""
1. Phân tích Input / Output
Dữ liệu ban đầu
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    }
]
Kiểu dữ liệu
product_list → list
Mỗi sản phẩm → dictionary
product_id → str
product_name → str
price → int
quantity → int
sold → int
Input
Menu
1
2
3
4
5
Bán hàng
Mã sản phẩm
Số lượng mua
Nhập kho
Mã sản phẩm
Số lượng nhập
Output
Hiển thị sản phẩm
Mã SP: SP001 | Tên: Áo polo nam | Giá: 299000 |
Tồn kho: 20 | Đã bán: 5 | Trạng thái: Còn hàng
Báo cáo doanh thu
Áo polo nam | Đã bán: 5 | Doanh thu: 1495000
2. Giải pháp
Chức năng 1 - Hiển thị sản phẩm

Xác định trạng thái:

if quantity == 0:
    status = "Hết hàng"
elif quantity <= 5:
    status = "Sắp hết hàng"
else:
    status = "Còn hàng"
Chức năng 2 - Bán sản phẩm
Bước 1

Chuẩn hóa mã:

product_id = input(...).strip().upper()
Bước 2

Tìm sản phẩm:

for product in product_list:
Bước 3

Kiểm tra số lượng mua

quantity_buy > 0
Bước 4

Kiểm tra tồn kho

quantity_buy <= product["quantity"]
Bước 5

Cập nhật dữ liệu

product["quantity"] -= quantity_buy
product["sold"] += quantity_buy
Bước 6

Tính tiền

total_price = product["price"] * quantity_buy
Chức năng 3 - Nhập kho

Kiểm tra:

import_quantity > 0

Sau đó:

product["quantity"] += import_quantity
Chức năng 4 - Báo cáo doanh thu
Doanh thu từng sản phẩm
revenue = price * sold
Tổng doanh thu
total_revenue += revenue
Tìm sản phẩm bán chạy nhất
max_sold

hoặc:

best_seller = max(product_list,
                  key=lambda product: product["sold"])
3. Pseudocode
Lặp vô hạn

    Hiển thị menu

    Nhập lựa chọn

    Nếu = 1:
        Hiển thị sản phẩm

    Nếu = 2:
        Nhập mã sản phẩm
        Tìm sản phẩm

        Nếu không tồn tại:
            Thông báo lỗi

        Nhập số lượng mua

        Nếu không hợp lệ:
            Thông báo lỗi

        Nếu vượt tồn kho:
            Thông báo lỗi

        Cập nhật tồn kho
        Cập nhật số lượng bán
        Tính tiền

    Nếu = 3:
        Nhập mã sản phẩm

        Nếu không tồn tại:
            Thông báo lỗi

        Nhập số lượng nhập

        Nếu không hợp lệ:
            Thông báo lỗi

        Cộng thêm tồn kho

    Nếu = 4:
        Tính doanh thu từng sản phẩm
        Tính tổng doanh thu
        Tìm sản phẩm bán chạy nhất

    Nếu = 5:
        Thoát

    Ngược lại:
        Báo lỗi menu
4. Source Code Hoàn Chỉnh
"""

# ==========================
# DANH SÁCH SẢN PHẨM BAN ĐẦU
# ==========================

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:

    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm")
    print("3. Nhập thêm hàng")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    # ==================================
    # 1. HIỂN THỊ SẢN PHẨM
    # ==================================

    if choice == "1":

        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")

        else:

            print("\nDanh sách sản phẩm hiện tại:")

            for index, product in enumerate(product_list, start=1):

                quantity = product["quantity"]

                if quantity == 0:
                    status = "Hết hàng"
                elif quantity <= 5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"

                print(
                    f"{index}. "
                    f"Mã SP: {product['product_id']} | "
                    f"Tên: {product['product_name']} | "
                    f"Giá: {product['price']} | "
                    f"Tồn kho: {product['quantity']} | "
                    f"Đã bán: {product['sold']} | "
                    f"Trạng thái: {status}"
                )

    # ==================================
    # 2. BÁN HÀNG
    # ==================================

    elif choice == "2":

        product_id = input(
            "Nhập mã sản phẩm khách muốn mua: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                try:

                    buy_quantity = int(
                        input("Nhập số lượng khách mua: ")
                    )

                    if buy_quantity <= 0:
                        print("Số lượng mua không hợp lệ")
                        break

                    if buy_quantity > product["quantity"]:
                        print("Số lượng trong kho không đủ để bán")
                        break

                    product["quantity"] -= buy_quantity
                    product["sold"] += buy_quantity

                    total_price = (
                        product["price"] * buy_quantity
                    )

                    print(
                        f"Khách cần thanh toán: {total_price}"
                    )

                except ValueError:
                    print("Số lượng mua không hợp lệ")

                break

        if not found:
            print("Không tìm thấy sản phẩm cần bán")

    # ==================================
    # 3. NHẬP KHO
    # ==================================

    elif choice == "3":

        product_id = input(
            "Nhập mã sản phẩm cần nhập thêm: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                try:

                    import_quantity = int(
                        input("Nhập số lượng nhập thêm: ")
                    )

                    if import_quantity <= 0:
                        print("Số lượng nhập kho không hợp lệ")
                        break

                    product["quantity"] += import_quantity

                    print("Nhập kho thành công")

                except ValueError:
                    print("Số lượng nhập kho không hợp lệ")

                break

        if not found:
            print("Không tìm thấy sản phẩm cần nhập kho")

    # ==================================
    # 4. BÁO CÁO DOANH THU
    # ==================================

    elif choice == "4":

        total_revenue = 0
        total_sold = 0

        print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")

        for index, product in enumerate(product_list, start=1):

            revenue = (
                product["price"] * product["sold"]
            )

            total_revenue += revenue
            total_sold += product["sold"]

            print(
                f"{index}. "
                f"{product['product_name']} | "
                f"Đã bán: {product['sold']} | "
                f"Doanh thu: {revenue}"
            )

        if total_sold == 0:

            print("Chưa có doanh thu phát sinh.")

        else:

            best_seller = max(
                product_list,
                key=lambda product: product["sold"]
            )

            print(f"\nTổng doanh thu: {total_revenue}")

            print(
                f"Sản phẩm bán chạy nhất: "
                f"{best_seller['product_name']}"
            )

    # ==================================
    # 5. THOÁT
    # ==================================

    elif choice == "5":

        print("Thoát chương trình.")
        break

    # ==================================
    # MENU KHÔNG HỢP LỆ
    # ==================================

    else:
        print(
            "Lựa chọn không hợp lệ, vui lòng nhập lại!"
        )