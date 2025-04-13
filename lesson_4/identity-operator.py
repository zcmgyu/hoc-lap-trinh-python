# Identity Operator

## is operator
x1 = 10 # primitive type kiểu nguyên thuỷ
y1 = 10

print("x1 is y1 = ", x1 is y1)

x2 = [1, 2, 3] # reference type kiểu tham chiếu
y2 = [1, 2, 3]
z2 = x2 # z2 reference to x2 (z2 tham chiếu đến x2)

print("x2 is y2 = ", x2 is y2)
print("x2 == y2 = ", x2 == y2)

# RAM memory: [x2, ......, y2]

print("x2 is z2 = ", x2 is z2)

# not is operator
# opposite of is operator

x1 = 10 # primitive type kiểu nguyên thuỷ
y1 = 10

print("x1 is not y1 = ", x1 is not y1)

x2 = [1, 2, 3] # reference type kiểu tham chiếu
y2 = [1, 2, 3]
z2 = x2 # z2 reference to x2 (z2 tham chiếu đến x2)

print("x2 is not y2 = ", x2 is not y2)

# RAM memory: [x2, ......, y2]

print("x2 is not z2 = ", x2 is not z2)
