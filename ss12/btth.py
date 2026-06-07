cart_items = [
    {"id": "P001", "name": "Dien thoai iPhone 15", "number": 1, "price": 25000000},
    {"id": "P002", "name": "Op lung Silicon", "number": 2, "price": 150000},
]

while True:
    print("SHOPEE CART MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Xem chi tiết giỏ hàng & tính tổng tiền")
    print("2. Thêm sản phẩm mới/ Cộng dồn số lượng")
    print("3. Cập nhập số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("==============================")

    choice = input("Mời bạn chọn chức năng (1-5): ")

    if not choice.isdigit():
        print("vui lòng nhập số")
        continue

    match choice:
        case 1:
            stt = 0
            total_number = 0
            total_price = 0

            if len(cart_items) == 0:
                print("Không có phần tử nào")
            else:
                for item in cart_items:
                    stt += 1
                    print(f"{stt}{item['id']}{item[name]}{item[number]}{item[price]}")
                    total_number += item[number]
                    total_price += (item[number] * item[price])
        case 2:
            print()
        case 3:
            print()
        case 4:
            print()
        case 5:
            print("Thoát chương trình")
            break
        case _:
            print("Vui lòng chọn từ 1 đến 5")
