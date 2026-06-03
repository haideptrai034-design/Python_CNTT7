# Nhập tổng tiền hóa đơn
tong_tien = int(input("Nhập tổng tiền hóa đơn: "))

# Kiểm tra điều kiện giảm giá
if tong_tien >= 500000:
    giam_gia = tong_tien * 0.1
else:
    giam_gia = 0

# Tính số tiền khách phải trả
thanh_toan = tong_tien - giam_gia

# In kết quả
print("Số tiền giảm giá:", giam_gia, "VND")
print("Số tiền khách phải trả:", thanh_toan, "VND")