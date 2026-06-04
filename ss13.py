parking_lot = []
next_id = 1

while True:
    print("\n===== SMART PARKING SYSTEM =====")
    print("1. Check-in xe")
    print("2. Báo cáo tồn kho")
    print("3. Tìm kiếm xe")
    print("4. Check-out xe")
    print("5. Thoát")
    print("===============================")

    try:
        choice = int(input("Chọn chức năng: "))
    except ValueError:
        print("ERR-01: Vui lòng nhập số nguyên!")
        continue

    # =========================
    # 1. CHECK-IN
    # =========================
    if choice == 1:

        while True:
            plate = input("Nhập biển số xe: ").strip()

            if plate == "":
                print("ERR-02: Biển số không được để trống!")
            else:
                break

        duplicate = False

        for car in parking_lot:
            if car["plate"].lower() == plate.lower():
                duplicate = True
                break

        if duplicate:
            print("ERR-07: Biển số đã tồn tại trong bãi!")
            continue

        while True:
            try:
                vehicle_type = int(
                    input("Loại xe (1-Xe máy | 2-Ô tô): ")
                )

                if vehicle_type in [1, 2]:
                    break

                print("ERR-03: Loại xe không hợp lệ!")

            except ValueError:
                print("ERR-03: Loại xe không hợp lệ!")

        while True:
            try:
                entry_time = int(input("Nhập giờ vào: "))
                break
            except ValueError:
                print("ERR-01: Giờ phải là số nguyên!")

        if vehicle_type == 1:
            vehicle_name = "Xe máy"
        else:
            vehicle_name = "Ô tô"

        new_car = {
            "id": next_id,
            "plate": plate,
            "type": vehicle_name,
            "entry_time": entry_time
        }

        parking_lot.append(new_car)

        print("CHECK-IN THÀNH CÔNG!")
        print(new_car)

        next_id += 1

    # =========================
    # 2. BÁO CÁO TỒN KHO
    # =========================
    elif choice == 2:

        if len(parking_lot) == 0:
            print("ERR-05: Bãi xe hiện đang trống!")
        else:
            print("\n===== DANH SÁCH XE TRONG BÃI =====")

            print(
                f"{'ID':<5}"
                f"{'BIỂN SỐ':<15}"
                f"{'LOẠI XE':<15}"
                f"{'GIỜ VÀO':<10}"
            )

            print("-" * 45)

            for car in parking_lot:
                print(
                    f"{car['id']:<5}"
                    f"{car['plate']:<15}"
                    f"{car['type']:<15}"
                    f"{car['entry_time']:<10}"
                )

    # =========================
    # 3. TÌM KIẾM XE
    # =========================
    elif choice == 3:

        plate = input("Nhập biển số cần tìm: ").strip()

        if plate == "":
            print("ERR-02: Biển số không được để trống!")
            continue

        found = False

        for car in parking_lot:
            if car["plate"].lower() == plate.lower():
                print("ĐÃ TÌM THẤY XE:")
                print(car)
                found = True
                break

        if not found:
            print("ERR-04: Không tìm thấy xe!")

    # =========================
    # 4. CHECK-OUT
    # =========================
    elif choice == 4:

        plate = input("Nhập biển số cần check-out: ").strip()

        if plate == "":
            print("ERR-02: Biển số không được để trống!")
            continue

        target_car = None

        for car in parking_lot:
            if car["plate"].lower() == plate.lower():
                target_car = car
                break

        if target_car is None:
            print("ERR-04: Không tìm thấy xe!")
            continue

        while True:
            try:
                exit_time = int(input("Nhập giờ ra: "))

                if exit_time < target_car["entry_time"]:
                    print(
                        "ERR-06: Giờ ra phải lớn hơn hoặc bằng giờ vào!"
                    )
                    continue

                break

            except ValueError:
                print("ERR-01: Giờ phải là số nguyên!")

        parking_hours = exit_time - target_car["entry_time"]

        if target_car["type"] == "Xe máy":
            fee = parking_hours * 5000
        else:
            fee = parking_hours * 10000

        print("\n===== THÔNG TIN THANH TOÁN =====")
        print(f"Biển số: {target_car['plate']}")
        print(f"Loại xe: {target_car['type']}")
        print(f"Giờ vào: {target_car['entry_time']}")
        print(f"Giờ ra : {exit_time}")
        print(f"Số giờ gửi: {parking_hours}")
        print(f"Phí gửi xe: {fee:,} VNĐ")

        parking_lot.remove(target_car)

        print("CHECK-OUT THÀNH CÔNG!")

    # =========================
    # 5. THOÁT
    # =========================
    elif choice == 5:

        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    # =========================
    # MENU SAI
    # =========================
    else:
        print("ERR-01: Lựa chọn không hợp lệ!")
