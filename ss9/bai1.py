"""
(1) Phân tích lỗi
1. Sau khi chạy dòng lệnh delivery_orders.insert(0, "GE000"), danh sách delivery_orders thay đổi như thế nào?
Danh sách sẽ được thêm phần tử "GE000" vào vị trí đầu tiên (index 0). Các phần tử đang có trong danh sách sẽ bị dịch sang phải 1 vị trí.
Danh sách trở thành: ['GE000', 'GE001', 'GE002', 'GE003-CANCEL', 'GE004'] (Giả định trước đó đã chạy lệnh append "GE004").

2. Vì sao dòng sau sửa sai đơn hàng cần cập nhật? delivery_orders[1] = "GE002-UPDATED"
Vì sau khi dùng lệnh insert ở trên, phần tử tại index 1 đã trở thành "GE001". Dòng lệnh này đang ghi đè sai dữ liệu lên đơn hàng "GE001" thay vì đơn hàng "GE002".

3. Sau khi chèn "GE000" vào đầu danh sách, "GE002" đang nằm ở index nào?
"GE002" đã bị dịch chuyển sang phải và hiện đang nằm ở index 2.

4. Vì sao dòng sau gây lỗi? delivery_orders.remove(3)
Vì trong danh sách không có phần tử nào có giá trị là số nguyên 3. Khi không tìm thấy giá trị này để xóa, Python sẽ báo lỗi ValueError.

5. Phương thức remove() xóa phần tử theo giá trị hay theo vị trí?
Phương thức remove() tìm và xóa phần tử theo giá trị (value), không phải theo vị trí (index).

6. Muốn xóa đơn hàng "GE003-CANCEL", cần viết lệnh như thế nào?
Cần viết: delivery_orders.remove("GE003-CANCEL")

7. Phương thức pop() có tác dụng gì?
Phương thức pop() có tác dụng xóa phần tử cuối cùng ra khỏi danh sách (nếu không truyền tham số index) và trả về chính phần tử vừa bị xóa đó.

8. Vì sao chương trình báo lỗi khi in biến transferred_order?
Vì biến transferred_order chưa từng được khởi tạo hay gán giá trị trước đó. Trình biên dịch không tìm thấy biến này trong bộ nhớ nên báo lỗi NameError.

9. Muốn lưu lại đơn hàng vừa lấy ra bằng pop(), cần viết lệnh như thế nào?
Cần viết: transferred_order = delivery_orders.pop()

(2) Sửa lỗi
"""
# Danh sách đơn hàng ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm "GE004" vào cuối danh sách
delivery_orders.append("GE004")

# Chèn "GE000" vào đầu danh sách
delivery_orders.insert(0, "GE000")

# Sửa mã "GE002" thành "GE002-UPDATED" (GE002 đang ở index 2)
delivery_orders[2] = "GE002-UPDATED"

# Xoá mã “GE003-CANCEL” theo đúng giá trị
delivery_orders.remove("GE003-CANCEL")

# Lấy đơn hàng cuối cùng ra khỏi danh sách và lưu vào biến
transferred_order = delivery_orders.pop()

# In kết quả
print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)