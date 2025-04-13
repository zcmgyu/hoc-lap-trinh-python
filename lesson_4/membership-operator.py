# Membership Operator


print("3 in [1, 2, 3, 4, 5] = ", 3 in [1, 2, 3, 4, 5])

print("3 not in [1, 2, 3, 4, 5] = ", 3 not in [1, 2, 3, 4, 5])

print("'a' in 'Hello' = ", 'a' in 'Hello')

# Example: 
# Kiểm tra học sinh Nguyễn Đăng Doanh có trong danh sách học sinh hay không

students = ["Nguyen Van A", "Nguyen Van B", "Nguyen Van C", "Nguyen Van D"]

name = "Nguyen Dang Doanh"

if name in students:
    print("Học sinh Nguyễn Đăng Doanh có trong danh sách")
else:
    print("Học sinh Nguyễn Đăng Doanh KHÔNG có trong danh sách")

# not in operator
