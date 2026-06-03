"""
(1) Phân tích và thiết kế giải pháp
1. Phân tích Input / Output
Input (Dữ liệu đầu vào)

Hệ thống yêu cầu nhân viên lễ tân nhập 3 thông tin:

Thông tin	Ví dụ	Kiểu dữ liệu
Họ và tên bệnh nhân	Nguyễn Văn A	str
Mã bệnh án	BN1024	str
Khoa / Phòng khám	Khoa Nội	str

Vì:

Dữ liệu chứa chữ cái và ký tự
Không dùng để tính toán số học

=> Tất cả đều dùng kiểu chuỗi (str).

Output (Kết quả đầu ra)

Hệ thống cần hiển thị:

Phiếu khám bệnh điện tử
Thông tin bệnh nhân đã nhập
Thông báo xác nhận tiếp nhận thành công

Ví dụ:

========== PHIẾU KHÁM BỆNH ==========
Họ tên bệnh nhân : Nguyễn Văn A
Mã bệnh án       : BN1024
Khoa khám        : Khoa Nội
=====================================

Tiếp nhận bệnh nhân thành công!
2. Đề xuất giải pháp
Ý tưởng xử lý

Chương trình hoạt động theo quy trình:

Nhập thông tin bệnh nhân bằng input()
Lưu dữ liệu vào các biến
In phiếu khám bệnh bằng print()
Hiển thị thông báo xác nhận
Các hàm sử dụng
Hàm	Chức năng
input()	Nhập dữ liệu từ bàn phím
print()	Hiển thị thông tin ra màn hình
3. Thiết kế thuật toán (Pseudocode)
Bắt đầu chương trình

Nhập họ tên bệnh nhân
Lưu vào biến ho_ten

Nhập mã bệnh án
Lưu vào biến ma_benh_an

Nhập khoa/phòng khám
Lưu vào biến khoa_kham

In tiêu đề phiếu khám bệnh

In họ tên bệnh nhân
In mã bệnh án
In khoa/phòng khám

In thông báo tiếp nhận thành công

Kết thúc chương trình
(2) Triển khai Code Python
"""

ho_ten = input("Nhập họ tên bệnh nhân: ")
ma_benh_an = input("Nhập mã bệnh án: ")
khoa_kham = input("Nhập khoa/phòng khám: ")

print("\n========== PHIẾU KHÁM BỆNH ==========")
print("Họ tên bệnh nhân :", ho_ten)
print("Mã bệnh án       :", ma_benh_an)
print("Khoa khám        :", khoa_kham)
print("=====================================")

# Thông báo xác nhận
print("\nTiếp nhận bệnh nhân thành công!")