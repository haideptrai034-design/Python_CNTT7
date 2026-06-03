# 1. Phân tích Input / Output
# Input
# Dữ liệu	Kiểu dữ liệu
# Lựa chọn menu	string
# Mã sản phẩm	string
# Tên sản phẩm	string
# Số lượng	int
# Đơn giá	int
# Output
# Danh sách sản phẩm trong giỏ hàng.
# Tổng số lượng sản phẩm.
# Tổng tiền cần thanh toán.
# Thông báo thêm, cập nhật hoặc xóa sản phẩm thành công.
# Thông báo lỗi khi nhập dữ liệu không hợp lệ hoặc không tìm thấy sản phẩm.
# 2. Đề xuất giải pháp

# Chương trình sử dụng:

# Danh sách lồng nhau (list) để lưu thông tin giỏ hàng.
# Vòng lặp while True để hiển thị menu liên tục.
# Cấu trúc match-case để xử lý các chức năng.
# Vòng lặp for để tìm kiếm sản phẩm theo mã.
# Các câu lệnh if-else để kiểm tra dữ liệu hợp lệ.

# Các bước thực hiện:

# Chức năng 1
# Duyệt toàn bộ giỏ hàng.
# Tính thành tiền từng sản phẩm.
# Tính tổng số lượng và tổng tiền.
# Chức năng 2
# Nhập mã sản phẩm, tên sản phẩm, số lượng, đơn giá.
# Kiểm tra số lượng > 0 và đơn giá ≥ 0.
# Nếu mã đã tồn tại thì cộng thêm số lượng.
# Nếu chưa tồn tại thì thêm sản phẩm mới vào cuối danh sách.
# Chức năng 3
# Nhập mã sản phẩm cần cập nhật.
# Nhập số lượng mới.
# Kiểm tra số lượng hợp lệ.
# Tìm sản phẩm theo mã.
# Nếu tìm thấy thì cập nhật số lượng.
# Nếu không tìm thấy thì thông báo lỗi.
# Chức năng 4
# Nhập mã sản phẩm cần xóa.
# Tìm sản phẩm theo mã.
# Nếu tìm thấy thì xóa khỏi danh sách.
# Nếu không tìm thấy thì thông báo lỗi.
# Chức năng 5
# Thoát chương trình.
# 3. Thiết kế thuật toán (Pseudocode)
# Khởi tạo danh sách cart_items

# Lặp vô hạn

#     Hiển thị menu

#     Nhập lựa chọn

#     Nếu chọn 1
#         Hiển thị danh sách sản phẩm
#         Tính tổng số lượng
#         Tính tổng tiền

#     Nếu chọn 2
#         Nhập mã sản phẩm
#         Nhập tên sản phẩm
#         Nhập số lượng
#         Nhập đơn giá

#         Nếu số lượng <= 0 hoặc đơn giá < 0
#             Báo lỗi
#         Ngược lại
#             Tìm mã sản phẩm

#             Nếu đã tồn tại
#                 Cộng thêm số lượng
#             Ngược lại
#                 Thêm sản phẩm mới

#     Nếu chọn 3
#         Nhập mã sản phẩm
#         Nhập số lượng mới

#         Tìm sản phẩm

#         Nếu tìm thấy
#             Cập nhật số lượng
#         Ngược lại
#             Thông báo không tìm thấy

#     Nếu chọn 4
#         Nhập mã sản phẩm

#         Tìm sản phẩm

#         Nếu tìm thấy
#             Xóa sản phẩm
#         Ngược lại
#             Thông báo không tìm thấy

#     Nếu chọn 5
#         Thoát chương trình

#     Ngược lại
#         Thông báo lựa chọn không hợp lệ

cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]
while True:
    print("-------------------------------------------")
    print("     SHOPEE CART MANAGEMENT SYSTEM       ")
    print("-------------------------------------------")
    print("1.Xem chi tiết giỏ hàng và Tổng tiền")
    print("2.Thêm sản phẩm mới hoặc Tăng số lượng")
    print("3.Cập nhật số lượng sản phẩm")
    print("4.Xóa sản phẩm khỏi giỏ hàng")
    print("5.Thoát chương trình.")
    print("-------------------------------------------")
    choice = input("Nhập lựa chọn của bạn (1-5): ")

    match (choice):
        case "1":
            tong_so_luong = 0
            tong_tien = 0
        
            print("\n===== CHI TIET GIO HANG =====")
            print(f"{'Ma SP':<10}{'Ten san pham':<25}{'SL':<5}{'Don gia':<15}{'Thanh tien'}")
            for item in cart_items:
                thanh_tien = item[2] * item[3] # sl * don gia
                tong_so_luong += item[2] 
                tong_tien += thanh_tien 
                print(f"{item[0]:<10}{item[1]:<25}{item[2]:<5}{item[3]:<15}{thanh_tien}")
            print(f"tổng số lượng sản phẩm trong giỏ: {tong_so_luong}")  
            print(f"Tổng tiền thanh toán: {tong_tien}")  
            
        case "2":
            ma_sp = input("Nhap ma san pham: ")
            ten_sp = input("Nhap ten san pham: ")
            so_luong = int(input("Nhap so luong: "))
            don_gia = int(input("Nhap don gia: "))
            
            if so_luong <= 0 or don_gia < 0:
                 print("không thực hiện thao tác")
            else:
                found = False
                for i in cart_items:
                    if ma_sp == i[0]:
                        i[2]+= so_luong
                        found = True
                        break
                if found == False:
                    cart_items.append([ma_sp,ten_sp,so_luong,don_gia])
                    print("Da them vào giỏ hàng")
        case "3":
            find_masp = input("Nhập mã sản phẩm cần thay đổi: ")
            find_so_luong = int(input("Nhập số lượng cần thay đổi: "))

            found = False

            for i in cart_items:
                if find_masp == i[0]:
                    if find_so_luong <= 0:
                        print("Số lượng không hợp lệ")
                    else:
                        i[2] = find_so_luong
                        print("Cập nhật thành công")
                    found = True
                    break

            if found == False:
                print("Không tìm thấy sản phẩm")

        case "4":
            ma_sp = input("Nhap ma san pham can xoa: ")

            flag = False

            for i in range(len(cart_items)):
                if cart_items[i][0] == ma_sp:
                    del cart_items[i]
                    flag = True
                    print("Xoa san pham thanh cong!")
                    break

            if flag == False:
                print("Khong tim thay ma san pham!")
        case "5":
            print("Đã thoát")
            break
        case _:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại")
            