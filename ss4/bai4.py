# Mã số bí ẩn
so_may_man = 79

# Số lượt chơi tối đa
so_luot = 5

# Vòng lặp chơi game
for i in range(1, so_luot + 1):
    du_doan = int(input(f"Lượt {i} - Nhập số dự đoán: "))

    # Kiểm tra đoán đúng
    if du_doan == so_may_man:
        print("🎉 Chúc mừng! Bạn đã đoán đúng và nhận được quà đặc biệt!")
        break

    # Gợi ý nếu đoán sai
    elif du_doan < so_may_man:
        print("Số bạn đoán nhỏ hơn mã số may mắn!")

    else:
        print("Số bạn đoán lớn hơn mã số may mắn!")

# Nếu hết lượt mà chưa đoán đúng
else:
    print("Bạn đã hết 5 lượt chơi. Chúc bạn may mắn lần sau!")