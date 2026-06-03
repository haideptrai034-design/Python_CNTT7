"""
(1) Phân tích lỗi
Câu 1

Sau khi chạy:

express_orders.insert(0, "GE100-FAST")

Danh sách thay đổi từ:

["GE101", "GE102-WRONG", "GE103-CANCEL", "GE104"]

thành:

["GE100-FAST", "GE101", "GE102-WRONG", "GE103-CANCEL", "GE104"]

Vì insert(0, value) chèn phần tử vào vị trí đầu tiên và đẩy toàn bộ phần tử cũ sang phải 1 vị trí.

Câu 2

Vì sao dòng sau sửa nhầm đơn hàng?

express_orders[1] = "GE102-UPDATED"

Sau khi dùng insert(0, "GE100-FAST"), danh sách là:

Index    Giá trị
0        GE100-FAST
1        GE101
2        GE102-WRONG
3        GE103-CANCEL
4        GE104

express_orders[1] là "GE101".

Nên lệnh trên đã sửa:

GE101

thành:

GE102-UPDATED
Câu 3

Sau khi chèn "GE100-FAST" vào đầu danh sách, "GE102-WRONG" nằm ở index nào?

Đáp án:

index = 2
Câu 4

Vì sao dòng sau không xóa đúng đơn hàng bị hủy?

express_orders.pop(3)

Sau khi sửa nhầm dữ liệu:

[
    "GE100-FAST",
    "GE102-UPDATED",
    "GE102-WRONG",
    "GE103-CANCEL",
    "GE104"
]

Index lúc này:

0 -> GE100-FAST
1 -> GE102-UPDATED
2 -> GE102-WRONG
3 -> GE103-CANCEL
4 -> GE104

Lệnh:

pop(3)

thực ra xóa đúng "GE103-CANCEL".

Nhưng lỗi trước đó đã làm dữ liệu sai nên kết quả cuối cùng vẫn sai nghiệp vụ.

Câu 5

Muốn xóa theo giá trị nên dùng:

express_orders.remove("GE103-CANCEL")

Ưu điểm:

Không cần nhớ index.
Xóa đúng theo mã đơn hàng.
Câu 6

pop() không truyền index sẽ lấy phần tử nào?

express_orders.pop()

Mặc định lấy:

phần tử cuối cùng

Ví dụ:

["A", "B", "C"]
pop()

Lấy:

"C"
Câu 7

Vì sao dòng sau lấy sai đơn hàng đang giao?

current_order = express_orders.pop()

Vì pop() lấy phần tử cuối danh sách.

Lúc đó phần tử cuối là:

GE104

nên:

current_order = "GE104"

Trong khi đơn cần giao trước là:

GE100-FAST
Câu 8

Muốn lấy đơn hàng đầu tiên để giao:

current_order = express_orders.pop(0)

pop(0) sẽ lấy phần tử ở đầu danh sách.

Câu 9

Những dòng cần sửa:

Sai
express_orders[1] = "GE102-UPDATED"
Đúng
express_orders[2] = "GE102-UPDATED"
Sai
current_order = express_orders.pop()
Đúng
current_order = express_orders.pop(0)
(2) Source Code Đúng
"""

# Danh sách đơn hàng ban đầu
express_orders = [
    "GE101",
    "GE102-WRONG",
    "GE103-CANCEL"
]

# Thêm đơn hàng mới
express_orders.append("GE104")

# Chèn đơn hỏa tốc
express_orders.insert(0, "GE100-FAST")

# Sửa mã đơn hàng bị nhập sai
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hàng bị hủy
express_orders.remove("GE103-CANCEL")

# Lấy đơn đầu tiên để giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)