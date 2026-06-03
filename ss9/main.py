# students = []

# number_sv = int(input("Nhập số lượng sinh viên: "))

# for i in range(number_sv):
#     name_sv = input(f"Nhập tên sinh viên thứ {i + 1}: ")
#     students.append(name_sv)

# for sv in students:
#     print(sv)

# for index,value in enumerate(students, start=0):
#     print(f"sinh viên thứ {index}: {value} ")


# numbers = ["khiêm", "hưng", "tài"]

# sv = input("Nhập tên sinh viên: ")

# if sv in numbers:
#     print("Đã tìm thấy sinh viên ở vị trí", numbers.index(sv))
# else:
#     print("Không tìm thấy sinh viên")


numbers = ["khiêm", "hưng", "tài"]

sv = input("Nhập tên sinh viên: ")
found = False

for i in range(len(numbers)):
    if sv in numbers[i]:
        print(f"da tim thay {numbers[i]} ơ vị tri {i}")
        found = True
        break

if found == False:
    print("Không tìm thấy sinh viên")

