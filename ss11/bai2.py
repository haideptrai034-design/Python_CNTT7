"""
(1) Phân tích lỗi
1. Dictionary employee gồm những key nào?
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

Các key gồm:

employee_id
full_name
department
status
2. Vì sao dòng sau gây lỗi?
employee_id = employee[0]

Dictionary truy cập dữ liệu bằng key, không phải bằng index.

Python sẽ tìm key có tên 0:

employee[0]

Nhưng dictionary không có key nào là 0, nên sinh lỗi:

KeyError: 0
3. Dictionary có truy cập phần tử bằng index giống list không?

❌ Không.

Ví dụ:

List
numbers = [10, 20, 30]

print(numbers[0])

Kết quả:

10
Dictionary
employee = {
    "employee_id": "NV001"
}

print(employee["employee_id"])

Kết quả:

NV001

Dictionary luôn truy cập bằng key.

4. Muốn lấy mã nhân viên "NV001" cần viết thế nào?
employee_id = employee["employee_id"]
5. Vì sao dòng sau gây lỗi?
full_name = employee["name"]

Dictionary không có key:

"name"

Nó chỉ có:

"full_name"

nên sẽ báo:

KeyError: 'name'
6. Key đúng để lấy họ tên nhân viên là gì?
full_name

Câu lệnh đúng:

full_name = employee["full_name"]
7. Vì sao dòng sau chưa cập nhật đúng trạng thái?
employee["employee_status"] = "official"

Lệnh này không cập nhật key cũ.

Nó tạo thêm một key mới:

{
    "status": "probation",
    "employee_status": "official"
}

Trong khi yêu cầu là sửa giá trị của key:

status
8. Muốn cập nhật trạng thái nhân viên cần dùng key nào?
employee["status"] = "official"
9. Vì sao dòng sau gây lỗi?
employee.append("base_salary", 15000000)

append() chỉ dùng cho list.

Ví dụ:

numbers = []

numbers.append(10)

Dictionary không có phương thức append().

Nên Python báo:

AttributeError
10. Dictionary có phương thức append() không?

❌ Không.

11. Muốn thêm lương cơ bản base_salary = 15000000 cần viết thế nào?

Cách 1:

employee["base_salary"] = 15000000

Cách 2:

employee.update({"base_salary": 15000000})
12. Vì sao dòng sau gây lỗi?
del employee["team"]

Dictionary không có key:

"team"

nên Python báo:

KeyError: 'team'
13. Muốn xóa thông tin phòng ban cần dùng key nào?

Key đúng là:

department

Câu lệnh:

del employee["department"]

Hoặc:

employee.pop("department")
(2) Sửa lỗi
"""

# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên
employee_id = employee["employee_id"]

# Lấy họ tên nhân viên
full_name = employee["full_name"]

# Cập nhật trạng thái nhân viên
employee["status"] = "official"

# Thêm lương cơ bản
employee["base_salary"] = 15000000

# Xóa phòng ban
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)