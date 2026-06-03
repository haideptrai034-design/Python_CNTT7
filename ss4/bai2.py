# Khởi tạo biến
tong_doanh_thu = 0
so_ngay_dat_muc_tieu = 0

# Vòng lặp nhập doanh thu 7 ngày
for i in range(1, 8):
    doanh_thu = int(input(f"Nhập doanh thu ngày {i}: "))

    # Cộng dồn tổng doanh thu
    tong_doanh_thu += doanh_thu

    # Kiểm tra ngày đạt mục tiêu
    if doanh_thu >= 5000000:
        so_ngay_dat_muc_tieu += 1

# Tính doanh thu trung bình
doanh_thu_trung_binh = tong_doanh_thu / 7

# In kết quả
print("Tổng doanh thu cả tuần:", tong_doanh_thu, "VND")
print("Doanh thu trung bình mỗi ngày:", doanh_thu_trung_binh, "VND")
print("Số ngày đạt mục tiêu doanh thu:", so_ngay_dat_muc_tieu)