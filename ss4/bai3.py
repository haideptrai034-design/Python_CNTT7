# Nhập số lượng hóa đơn
so_hoa_don = int(input("Nhập số lượng hóa đơn trong ca: "))

# Nhập hóa đơn đầu tiên để khởi tạo Max và Min
hoa_don = int(input("Nhập giá trị hóa đơn thứ 1: "))

max_hoa_don = hoa_don
min_hoa_don = hoa_don

# Vòng lặp nhập các hóa đơn còn lại
for i in range(2, so_hoa_don + 1):
    hoa_don = int(input(f"Nhập giá trị hóa đơn thứ {i}: "))

    # Kiểm tra hóa đơn lớn nhất
    if hoa_don > max_hoa_don:
        max_hoa_don = hoa_don

    # Kiểm tra hóa đơn nhỏ nhất
    if hoa_don < min_hoa_don:
        min_hoa_don = hoa_don

# In kết quả
print("Hóa đơn lớn nhất:", max_hoa_don, "VND")
print("Hóa đơn nhỏ nhất:", min_hoa_don, "VND")