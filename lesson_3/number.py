import random

# int (Integer): Kiểu số nguyên
x1 = 10
x2 = -10
x3 = 123793817491273
print("x1 =", type(x1))
print("x2 =", type(x2))
print("x3 =", type(x3))

# float (Floating point number): Kiểu số thực
y1 = 10.5
y2 = 10.0
y3 = -10.5
y4 = 10.213123172387912739
print("y1 =", type(y1))
print("y2 =", type(y2))
print("y3 =", type(y3))
print("y4 =", type(y4))

print("Result of 35e3 == 35000:", 35e3 == 35000)
print("Result of 35E3 == 35000:", 35E3 == 35000)
print("Result of 35e-3 == 0.035:", 35e-3 == 0.035)

# complex (Complex number): Kiểu số phức
z = 10 + 5j
print ("z =", type(z))

# Random number
random_number = random.randint(1, 100)
# Giống với (alias): random.randrange(1, 100 + 1)
print("Random number:", random_number)

random_range = random.randrange(1, 100)
print("Random range:", random_range)



