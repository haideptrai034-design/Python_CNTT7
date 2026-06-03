while True:
    so_nhan_vien = int(input("Nhập số lượng nhân viên: "))

    for i in range(so_nhan_vien):
        print("Nhân viên thứ", i+1)

        ten = input("Nhập tên nhân viên ")
        so_ngay_lam = int(input("Nhập số ngày đi làm: "))

        print("THông tin nhân viên")
        print('tên nhân viên: ',ten)
        print('số ngày đi làm ', so_ngay_lam)

        if so_ngay_lam < 20 :
            print("Đánh giá: Cần cải thiện chuyên cần")
        else:
             print("Đánh giá: Nhân viên chuyên cần tốt")

        tiep_tuc = input("Tiếp tục chương trình? (y/n): ")

        if tiep_tuc == "n":
            print("Chương trình kết thúc")
            break


