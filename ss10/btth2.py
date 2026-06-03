# (1) Phân tích và thiết kế giải pháp
# 1. Phân tích Input / Output
# Input
# Dữ liệu	Kiểu dữ liệu
# Lựa chọn menu chính	string
# Lựa chọn menu phụ	string
# Tên bài hát	string
# Vị trí chèn	int
# Vị trí xóa	int
# Output
# Danh sách các bài hát trong playlist.
# Thông báo thêm bài hát thành công.
# Thông báo xóa bài hát thành công.
# Danh sách sau khi sắp xếp.
# 3 bài hát đầu tiên trong playlist.
# Các thông báo lỗi khi người dùng nhập sai.
# 2. Đề xuất giải pháp

# Chương trình sử dụng:

# list để lưu danh sách bài hát.
# append() để thêm bài hát vào cuối danh sách.
# insert() để chèn bài hát vào vị trí bất kỳ.
# remove() để xóa bài hát theo tên.
# pop() để xóa bài hát theo vị trí.
# sort() để sắp xếp danh sách theo bảng chữ cái.
# len() để đếm số lượng bài hát.
# while True để hiển thị menu liên tục.
# match-case để xử lý các chức năng của menu.
# Chức năng 1: Thêm bài hát
# Hiển thị menu phụ.
# Nếu chọn 1:
# Nhập tên bài hát.
# Dùng append().
# Nếu chọn 2:
# Nhập tên bài hát.
# Nhập vị trí muốn chèn.
# Kiểm tra vị trí hợp lệ.
# Dùng insert().
# Chức năng 2: Xem danh sách phát
# Kiểm tra danh sách có rỗng không.
# Nếu không rỗng thì hiển thị tất cả bài hát.
# Chức năng 3: Xóa bài hát
# Hiển thị menu phụ.
# Xóa theo tên:
# Dùng remove().
# Xóa theo vị trí:
# Dùng pop().
# Chức năng 4: Sắp xếp và Trích xuất
# Hiển thị menu phụ.
# Sắp xếp danh sách bằng sort().
# Trích xuất 3 bài hát đầu tiên bằng slicing playlist[:3].
# Chức năng 5: Thoát
# Kết thúc chương trình.
# 3. Thuật toán (Pseudocode)
# Khởi tạo playlist rỗng

# Lặp vô hạn

#     Hiển thị menu

#     Nhập lựa chọn

#     Nếu chọn 1
#         Hiển thị menu thêm bài hát

#         Nếu chọn thêm cuối
#             Nhập tên bài hát
#             Thêm vào cuối danh sách

#         Nếu chọn chèn theo vị trí
#             Nhập tên bài hát
#             Nhập vị trí

#             Nếu vị trí hợp lệ
#                 Chèn bài hát
#             Ngược lại
#                 Báo lỗi

#     Nếu chọn 2
#         Nếu danh sách rỗng
#             Báo danh sách trống
#         Ngược lại
#             Hiển thị danh sách phát

#     Nếu chọn 3
#         Nếu danh sách rỗng
#             Báo danh sách trống
#         Ngược lại
#             Hiển thị menu xóa

#             Nếu xóa theo tên
#                 Xóa bài hát

#             Nếu xóa theo vị trí
#                 Xóa bài hát theo vị trí

#     Nếu chọn 4
#         Nếu danh sách rỗng
#             Báo danh sách trống
#         Ngược lại
#             Hiển thị menu sắp xếp

#             Nếu chọn sắp xếp
#                 Sắp xếp danh sách

#             Nếu chọn trích xuất
#                 Hiển thị 3 bài hát đầu tiên

#     Nếu chọn 5
#         Thoát chương trình

#     Ngược lại
#         Báo lỗi lựa chọn không hợp lệ

playlist = []

while True:
    print("\n========== PLAYLIST MANAGEMENT ==========")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và Trích xuất danh sách")
    print("5. Thoát chương trình")
    print("=========================================")

    choice = input("Nhập lựa chọn: ")

    match choice:

        # Chức năng 1
        case "1":
            print("\n1. Thêm bài hát vào cuối danh sách")
            print("2. Chèn bài hát vào vị trí bất kỳ")

            sub_choice = input("Nhập lựa chọn: ")

            match sub_choice:

                case "1":
                    song_name = input("Nhập tên bài hát: ")

                    playlist.append(song_name)

                    print("Thêm bài hát thành công!")
                    print(f"Số lượng bài hát hiện tại: {len(playlist)}")

                case "2":
                    song_name = input("Nhập tên bài hát: ")

                    try:
                        index = int(input("Nhập vị trí muốn chèn: "))

                        if index < 0 or index > len(playlist):
                            print("Vị trí không hợp lệ.")
                        else:
                            playlist.insert(index, song_name)

                            print("Thêm bài hát thành công!")
                            print(f"Số lượng bài hát hiện tại: {len(playlist)}")

                    except ValueError:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

                case _:
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

        # Chức năng 2
        case "2":

            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\n===== DANH SÁCH PHÁT =====")

                for i in range(len(playlist)):
                    print(f"{i + 1}. {playlist[i]}")

        # Chức năng 3
        case "3":

            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
                continue

            print("\n1. Xóa theo tên bài hát")
            print("2. Xóa theo vị trí")

            sub_choice = input("Nhập lựa chọn: ")

            match sub_choice:

                case "1":
                    song_name = input("Nhập tên bài hát cần xóa: ")

                    if song_name in playlist:
                        playlist.remove(song_name)
                        print(f"Đã xóa bài hát {song_name} khỏi danh sách")
                    else:
                        print("Không tìm thấy bài hát trong danh sách phát.")

                case "2":

                    try:
                        index = int(input("Nhập vị trí cần xóa: "))

                        if index < 1 or index > len(playlist):
                            print("Vị trí không hợp lệ.")
                        else:
                            removed_song = playlist.pop(index - 1)

                            print(f"Đã xóa bài hát {removed_song} khỏi danh sách")

                    except ValueError:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

                case _:
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

        # Chức năng 4
        case "4":

            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
                continue

            print("\n1. Sắp xếp theo bảng chữ cái")
            print("2. Nghe thử 3 bài hát đầu tiên")

            sub_choice = input("Nhập lựa chọn: ")

            match sub_choice:

                case "1":

                    playlist.sort()

                    print("\nDanh sách sau khi sắp xếp:")

                    for i in range(len(playlist)):
                        print(f"{i + 1}. {playlist[i]}")

                case "2":

                    print("\n3 bài hát đầu tiên:")

                    for song in playlist[:3]:
                        print(song)

                case _:
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

        # Chức năng 5
        case "5":
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")