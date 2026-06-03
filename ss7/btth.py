raw_input = "   nGuyen vaN aN  ;  2004   "

while True:  

    print("\n===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")

    choice = input("Nhập lưa chọn của bạn")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    if choice == 1:
        print("Dữ liệu gốc:")
        print(raw_input)
    elif choice == 2:
        parts = raw_input.split(";")

        name = parts[0].strip().title()
        birth_year = int(parts[1].strip())

        age = 2026 - birth_year

        print("\n===== THÔNG TIN THÀNH VIÊN =====")
        print(f"Họ tên   : {name}")
        print(f"Năm sinh : {birth_year}")
        print(f"Tuổi     : {age}")
    elif choice == 3:
        parts = raw_input.split(";")

        name = parts[0].strip().title()
        birth_year = parts[1].strip()

        name_parts = name.split()

        first_name = name_parts[0]
        middle_name = name_parts[1]
        last_name = name_parts[2]

        # Email
        email = (
            first_name[0].lower()
            + middle_name[0].lower()
            + last_name.lower()
            + "@company.com"
        )

        # ID
        member_id = last_name.upper() + birth_year[-2:]

        print("\n==============================")
        print("       THẺ THÀNH VIÊN")
        print("==============================")
        print(f"{'Họ tên':<10}: {name}")
        print(f"{'Mã ID':<10}: {member_id}")
        print(f"{'Email':<10}: {email}")
        print("==============================")
    elif choice == 4 :
        print("\nCảm ơn bạn đã sử dụng chương trình!")
        break
    else:
        print("\nLựa chọn không hợp lệ, vui lòng nhập lại!")
