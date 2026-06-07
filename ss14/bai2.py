"""
(1) Phân tích lỗi
Câu 1: total_points là biến Global hay Local?
total_points = 100

Đây là biến toàn cục (Global Variable) vì nó được khai báo bên ngoài mọi hàm.

Biến global có thể được đọc từ bất kỳ đâu trong chương trình.

Câu 2: Giải thích lỗi UnboundLocalError

Đoạn code gây lỗi:

def add_reward_points(points_earned):
    total_points = total_points + points_earned

Khi Python thấy:

total_points = ...

nó hiểu rằng:

"À, total_points là một biến cục bộ (local) của hàm này."

Nhưng ở vế phải lại có:

total_points + points_earned

Python phải đọc giá trị của total_points trước.

Vấn đề là biến local này chưa được gán giá trị nào cả, nên Python báo:

UnboundLocalError:
local variable 'total_points' referenced before assignment

Có thể hình dung như sau:

def add_reward_points(points_earned):
    # Python nghĩ total_points là local
    total_points = total_points + points_earned

↓

def add_reward_points(points_earned):
    local_total_points = local_total_points + points_earned

Biến local_total_points chưa tồn tại nên lỗi.

Câu 3: Nếu chỉ đọc biến thì có lỗi không?

Không.

Ví dụ:

total_points = 100

def show_points():
    print(total_points)

show_points()

Kết quả:

100

Vì hàm chỉ đọc biến global chứ không gán lại giá trị cho nó.

Câu 4: Cách sửa 1 - Dùng từ khóa global

Từ khóa cần dùng là:

global total_points

Ví dụ:

total_points = 100

def add_reward_points(points_earned):
    global total_points
    total_points = total_points + points_earned

Lúc này Python hiểu rằng:

Hãy sử dụng biến total_points ở bên ngoài hàm.

Câu 5: Cách sửa 2 (Khuyến nghị)

Một hàm tốt nên:

Nhận dữ liệu qua tham số.
Tính toán.
Trả kết quả bằng return.

Ví dụ:

def add_reward_points(current_points, points_earned):
    return current_points + points_earned

return giúp trả lại tổng điểm mới cho chương trình.

(2) Source Code Đúng Chuẩn (Cách 2)
"""

# Tổng điểm hiện tại của khách hàng
total_points = 100

# Hàm cộng điểm thưởng
def add_reward_points(current_points, points_earned):
    return current_points + points_earned


# Khách được thưởng 50 điểm
total_points = add_reward_points(total_points, 50)

print("Đã cộng thêm 50 điểm.")
print("Tổng điểm hiện tại của khách hàng:", total_points)