"""
(1) Phân tích và thiết kế giải pháp
1. Các hàm cần xây dựng
Hàm display_menu()

Chức năng: Hiển thị menu.

Input: Không có

Output: Không có (None)

Hàm display_students(student_list)

Chức năng: Hiển thị danh sách học viên.

Input:

student_list: list

Output:

None
Hàm validate_score(score_input)

Chức năng: Kiểm tra điểm có hợp lệ hay không.

Input:

score_input: str

Output:

True  -> hợp lệ
False -> không hợp lệ
Hàm find_student_by_id(student_list, student_id)

Chức năng: Tìm vị trí học viên theo mã.

Input:

student_list: list
student_id: str

Output:

index (int) nếu tìm thấy
-1 nếu không tìm thấy
Hàm add_student(student_list)

Chức năng: Thêm học viên mới.

Input:

student_list: list

Output:

None
Hàm update_score(student_list)

Chức năng: Cập nhật điểm.

Input:

student_list: list

Output:

None
Hàm get_rank(average_score)

Chức năng: Xếp loại học lực.

Input:

average_score: float

Output:

str

Ví dụ:

"Giỏi"
"Khá"
"Trung bình"
"Yếu"
Hàm evaluate_students(student_list)

Chức năng: Đánh giá học lực toàn bộ học viên.

Input:

student_list: list

Output:

None
2. Vì sao nên tách thành nhiều hàm?
Nếu viết một file dài hàng trăm dòng:

❌ Khó đọc

❌ Khó tìm lỗi

❌ Khó tái sử dụng

❌ Khó nâng cấp

Khi tách thành nhiều hàm:

✔ Mỗi hàm chỉ làm một việc

✔ Dễ kiểm thử

✔ Dễ bảo trì

✔ Có thể tái sử dụng

✔ Tuân thủ nguyên tắc Clean Code

Ví dụ:

validate_score()

được dùng lại ở:

Thêm học viên
Cập nhật điểm

không cần viết lại nhiều lần.

(2) Source Code Hoàn Chỉnh

"""
# =========================
# DỮ LIỆU BAN ĐẦU
# =========================

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]


# =========================
# HIỂN THỊ MENU
# =========================

def display_menu():
    """
    Hiển thị menu chính
    """
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")


# =========================
# KIỂM TRA ĐIỂM
# =========================

def validate_score(score_input):
    """
    Kiểm tra điểm hợp lệ từ 0 đến 10
    """
    try:
        score = float(score_input)

        if 0 <= score <= 10:
            return True

        return False

    except:
        return False


# =========================
# TÌM HỌC VIÊN THEO MÃ
# =========================

def find_student_by_id(student_list, student_id):
    """
    Trả về index học viên
    """
    for i in range(len(student_list)):
        if student_list[i]["student_id"] == student_id:
            return i

    return -1


# =========================
# HIỂN THỊ DANH SÁCH
# =========================

def display_students(student_list):
    """
    Hiển thị danh sách học viên
    """

    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    for i, student in enumerate(student_list, start=1):
        print(
            f"{i}. Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"Toán: {student['math_score']} | "
            f"Anh: {student['english_score']}"
        )


# =========================
# NHẬP ĐIỂM
# =========================

def input_score(message):
    """
    Nhập điểm có kiểm tra hợp lệ
    """

    while True:
        score = input(message)

        if validate_score(score):
            return float(score)

        print("Điểm không hợp lệ, phải là số từ 0 đến 10")


# =========================
# THÊM HỌC VIÊN
# =========================

def add_student(student_list):
    """
    Thêm học viên mới
    """

    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()

        if find_student_by_id(student_list, student_id) != -1:
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        else:
            break

    while True:
        name = input("Nhập tên học viên: ").strip()

        if name == "":
            print("Tên học viên không được để trống!")
        else:
            name = name.title()
            break

    math_score = input_score("Nhập điểm Toán: ")
    english_score = input_score("Nhập điểm Anh: ")

    student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }

    student_list.append(student)

    print("Thêm học viên thành công!")


# =========================
# CẬP NHẬT ĐIỂM
# =========================

def update_score(student_list):
    """
    Cập nhật điểm học viên
    """

    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()

    index = find_student_by_id(student_list, student_id)

    if index == -1:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return

    print("Nhập điểm mới:")

    math_score = input_score("Điểm Toán: ")
    english_score = input_score("Điểm Anh: ")

    student_list[index]["math_score"] = math_score
    student_list[index]["english_score"] = english_score

    print("Cập nhật điểm thành công!")


# =========================
# XẾP LOẠI HỌC LỰC
# =========================

def get_rank(average_score):
    """
    Trả về xếp loại học lực
    """

    if average_score >= 8:
        return "Giỏi"

    elif average_score >= 6.5:
        return "Khá"

    elif average_score >= 5:
        return "Trung bình"

    else:
        return "Yếu"


# =========================
# ĐÁNH GIÁ HỌC LỰC
# =========================

def evaluate_students(student_list):
    """
    Đánh giá học lực toàn bộ học viên
    """

    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    print("\n===== KẾT QUẢ ĐÁNH GIÁ =====")

    for student in student_list:

        average = (
            student["math_score"]
            + student["english_score"]
        ) / 2

        rank = get_rank(average)

        print(
            f"Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"ĐTB: {average:.2f} | "
            f"Xếp loại: {rank}"
        )


# =========================
# CHƯƠNG TRÌNH CHÍNH
# =========================

while True:

    display_menu()

    choice = input("Nhập lựa chọn: ").strip()

    if choice == "1":
        display_students(students)

    elif choice == "2":
        add_student(students)

    elif choice == "3":
        update_score(students)

    elif choice == "4":
        evaluate_students(students)

    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")