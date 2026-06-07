"""
(1) Phân tích thiết kế hàm
Hàm 1: calculate_average(student)
Input
student: dict

Ví dụ:

{
    "student_id": "SV001",
    "name": "Nguyễn Văn A",
    "math": 8.5,
    "physics": 7.0,
    "chemistry": 9.0
}
Output
float
Pseudocode
Nhận dictionary sinh viên
Lấy điểm Toán, Lý, Hóa
Tính trung bình
Trả về kết quả
Hàm 2: get_rank(average)
Input
average: float
Output
str
Pseudocode
Nếu average >= 8
    trả về "Giỏi"

Nếu average >= 6.5
    trả về "Khá"

Nếu average >= 5
    trả về "Trung bình"

Ngược lại
    trả về "Yếu"
Hàm 3: display_grades(records)
Input
records: list
Output
None
Pseudocode
Nếu danh sách rỗng
    thông báo chưa có dữ liệu

Duyệt từng sinh viên
    tính ĐTB bằng calculate_average()
    lấy học lực bằng get_rank()
    hiển thị thông tin
Hàm 4: update_student_score(records)
Input
records: list
Output
None
Pseudocode
Nhập mã sinh viên
Chuẩn hóa mã

Tìm sinh viên

Nếu không tìm thấy
    thông báo lỗi

Nếu tìm thấy
    chọn môn học

    nhập điểm mới

    kiểm tra điểm hợp lệ

    cập nhật điểm

    thông báo thành công
Hàm 5: generate_report(records)
Input
records: list
Output
None
Pseudocode
Nếu danh sách rỗng
    thông báo chưa có dữ liệu

Đếm số sinh viên đỗ
Đếm số sinh viên trượt

Tính phần trăm

In báo cáo
Hàm 6: find_valedictorian(records)
Input
records: list
Output
None
Pseudocode
Nếu danh sách rỗng
    thông báo chưa có dữ liệu

Tìm sinh viên có ĐTB lớn nhất

In thông tin thủ khoa
Hàm phụ trợ find_student_by_id(records, student_id)
Input
records: list
student_id: str
Output
dict hoặc None
Pseudocode
Duyệt danh sách

Nếu tìm thấy mã
    trả về dictionary sinh viên

Không tìm thấy
    trả về None
Hàm phụ trợ input_score()
Input

Không có

Output
float
Pseudocode
Lặp vô hạn

Nhập điểm

Nếu nhập chữ
    báo lỗi

Nếu ngoài 0-10
    báo lỗi

Nếu hợp lệ
    return điểm
(2) Source Code Hoàn Chỉnh
"""

# ==========================
# DỮ LIỆU BAN ĐẦU
# ==========================

student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


# ==========================
# HÀM PHỤ TRỢ
# ==========================

def calculate_average(student):
    """
    Tính điểm trung bình của sinh viên
    """
    return (
        student["math"]
        + student["physics"]
        + student["chemistry"]
    ) / 3


def get_rank(average):
    """
    Xếp loại học lực
    """
    if average >= 8:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def find_student_by_id(records, student_id):
    """
    Tìm sinh viên theo mã
    """
    for student in records:
        if student["student_id"] == student_id:
            return student

    return None


def input_score():
    """
    Nhập điểm hợp lệ từ 0 đến 10
    """
    while True:

        try:
            score = float(input("Nhập điểm mới: "))

            if 0 <= score <= 10:
                return score

            print(
                "Điểm số không hợp lệ. "
                "Vui lòng nhập từ 0 đến 10!"
            )

        except ValueError:
            print(
                "Điểm số không hợp lệ. "
                "Vui lòng nhập từ 0 đến 10!"
            )


# ==========================
# CHỨC NĂNG 1
# ==========================

def display_grades(records):

    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):

        average = calculate_average(student)
        rank = get_rank(average)

        print(
            f"{index}. "
            f"[{student['student_id']}] "
            f"{student['name']} | "
            f"Toán: {student['math']} | "
            f"Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | "
            f"ĐTB: {average:.2f} - {rank}"
        )

    print("---------------------------")


# ==========================
# CHỨC NĂNG 2
# ==========================

def update_student_score(records):

    student_id = input(
        "Nhập mã sinh viên cần cập nhật: "
    ).strip().upper()

    student = find_student_by_id(
        records,
        student_id
    )

    if student is None:
        print(
            f"Không tìm thấy sinh viên mang mã "
            f"{student_id} trong hệ thống!"
        )
        return

    while True:

        print("1. Toán")
        print("2. Lý")
        print("3. Hóa")

        subject = input(
            "Chọn môn học (1-Toán, 2-Lý, 3-Hóa): "
        )

        if subject in ["1", "2", "3"]:
            break

        print("Lựa chọn không hợp lệ!")

    score = input_score()

    if subject == "1":
        student["math"] = score
        subject_name = "Toán"

    elif subject == "2":
        student["physics"] = score
        subject_name = "Lý"

    else:
        student["chemistry"] = score
        subject_name = "Hóa"

    print(
        f">> Đã cập nhật điểm {subject_name} "
        f"của sinh viên "
        f"'{student['name']}' "
        f"thành {score}."
    )


# ==========================
# CHỨC NĂNG 3
# ==========================

def generate_report(records):

    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)

    passed = 0
    failed = 0

    for student in records:

        average = calculate_average(student)

        if average >= 5:
            passed += 1
        else:
            failed += 1

    pass_percent = (passed / total) * 100
    fail_percent = (failed / total) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(
        f"Số lượng qua môn (ĐTB >= 5.0): "
        f"{passed} sinh viên "
        f"(Chiếm {pass_percent:.2f}%)"
    )
    print(
        f"Số lượng trượt (ĐTB < 5.0): "
        f"{failed} sinh viên "
        f"(Chiếm {fail_percent:.2f}%)"
    )
    print("----------------------")


# ==========================
# CHỨC NĂNG 4
# ==========================

def find_valedictorian(records):

    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = records[0]
    highest_average = calculate_average(records[0])

    for student in records[1:]:

        average = calculate_average(student)

        if average > highest_average:
            highest_average = average
            top_student = student

    print("\n--- VINH DANH THỦ KHOA ---")
    print(
        f"Sinh viên: "
        f"{top_student['name']} "
        f"(Mã: {top_student['student_id']})"
    )
    print(
        f"Điểm Trung Bình: "
        f"{highest_average:.2f}"
    )
    print(
        "Chúc mừng sinh viên đã đạt "
        "thành tích xuất sắc nhất khóa!"
    )
    print("--------------------------")


# ==========================
# MENU
# ==========================

def display_menu():

    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")
    print("======================================================")


# ==========================
# MAIN
# ==========================

def main():

    while True:

        display_menu()

        choice = input(
            "Chọn chức năng (1-5): "
        ).strip()

        if choice == "1":
            display_grades(student_records)

        elif choice == "2":
            update_student_score(student_records)

        elif choice == "3":
            generate_report(student_records)

        elif choice == "4":
            find_valedictorian(student_records)

        elif choice == "5":
            print(
                "Cảm ơn bạn đã sử dụng hệ thống!"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ!"
            )


main()