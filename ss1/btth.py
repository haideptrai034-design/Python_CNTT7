import random
_name = input("Nhập tên bệnh nhân: ")
male = input("Giới tính: ")
year = int(input("Năm sinh: "))
phone = input("Số điện thoại: ")
emai = input("Nhập email: ")
trieuchung = input("Triệu chứng ban đầu: ")
money = float(input("Chi phí khám: "))

ba_so_ngau_nhien = f"{random.randint(0, 999):03d}"
ma_benh_nhan = f"BN{year}{ba_so_ngau_nhien}"

print('---Thẻ bệnh nhân---')

print(f"{'Mã BN      '}: {ma_benh_nhan}\n")
print(f"{'Tên        '}: {_name} ({type(_name).__name__})")
print(f"{'Giới tính  '}: {male} ({type(male).__name__})")
print(f"{'Năm sinh   '}: {year} ({type(year).__name__})")
print(f"{'Điện thoại '}: {phone} ({type(phone).__name__})")
print(f"{'Email      '}: {emai} ({type(emai).__name__})")
print(f"{'Triệu chứng'}: {trieuchung} ({type(trieuchung).__name__})")
print(f"{'Chi phí    '}: {money} VND ({type(money).__name__})")