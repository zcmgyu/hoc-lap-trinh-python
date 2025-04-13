# Python Logical Operators

## AND Operator

x1 = True
y1 = True
z1 = True

print("x1 and y1 and z1 = ", x1 and y1 and z1)

x2 = True
y2 = False
z2 = True

print("x2 and y2 and z2 = ", x2 and y2 and z2)

x3 = False
y3 = False
z3 = False

print("x3 and y3 and z3 = ", x3 and y3 and z3)

# Example
# Kiểm tra xem học sinh có phải là học sinh cấp 2 hay không

# Lấy input data lớp của sinh viên:
class_level = int(input("Nhập lớp của học sinh: "))

# Kiểm tra xem lớp có phải là lớp cấp 2 hay không
# [6, 7, 8, 9]
if class_level >= 6 and class_level <= 9:
    print("Học sinh là học sinh cấp 2")
else:
    print("Học sinh KHÔNG phải là học sinh cấp 2")

# OR Operator

x4 = True
y4 = False
z4 = False

print("x4 or y4 or z4 = ", x4 or y4 or z4)

x5 = False
y5 = False
z5 = False

print("x5 or y5 or z5 = ", x5 or y5 or z5)

x6 = True
y6 = True
z6 = True

print("x6 or y6 or z6 = ", x6 or y6 or z6)

## NOT Operator

x7 = True

print("not x7 = ", not x7)

x8 = False

print("not x8 = ", not x8)




