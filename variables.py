# Variables
name = "Win" # letter
old = 12 # number
print("Name: " + name) # Name: Win
print("Old: " + str(old)) # Old: 12, str = string
print("--------------------------------")
# Reassign variables
x = "Win"
x = 12
print("x: " + str(x))
print("--------------------------------")
# Casting (ép kiểu)
x = str(3)    # x will be '3'
print("Type of x: " + str(type(x)))
y = int(3)    # y will be 3
print("Type of y: " + str(type(y)))
z = float(3)  # z will be 3.0
print("Type of z: " + str(type(z)))
print("--------------------------------")
# Case-sensitive
name = "Win 1"
Name = "Win 2"
print("name: " + name)
print("Name: " + Name)
print("--------------------------------")
# Variable names
# Valid
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# Invalid
# 2myvar = "John"
# my-var = "John"
# my var = "John"
print("--------------------------------")
myvariablename = "john"
# Camel Case (Lạc đà)
myVariableName = "john"
# Pascal Case (Pascal) <<<
MyVariableName = "john"
# Snake Case (Rắn) <<<
my_variable_name = "john"
# UPPER CASE (Chữ hoa) <<< Constant (hằng số)
MY_VARIABLE_NAME = "john"
print("--------------------------------")
# Many Values to Multiple Variables
# x = "Orange"
# y = "Banana"
# z = "Cherry"
x, y, z = "Orange", "Banana", "Cherry"
print("x: " + x)
print("y: " + y)
print("z: " + z)
print("--------------------------------")
# One Value to Multiple Variables
x = y = z = "Orange"
print("One value x: " + x)
print("One value y: " + y)
print("One value z: " + z)
print("--------------------------------")
# Unpack a Collection
classmates = ["Alice", "Bob", "Charlie"] # list, array (danh sách)
# x = classmates[0] # 0 là vị trí của phần tử trong danh sách
# y = classmates[1] # 1 là vị trí của phần tử trong danh sách
# z = classmates[2] # 2 là vị trí của phần tử trong danh sách
x, y, z = classmates # unpack a collection (giải nén một tập hợp)
print("Unpack a collection x: " + x)
print("Unpack a collection y: " + y)
print("Unpack a collection z: " + z)
print("--------------------------------")
# Output Variables
x = 5
y = 10
print(x + y)
print(str(x) + str(y)) # x = "5", y = "10"

print("x:", x)
print("y:", y)
print("--------------------------------")

# Global Variables (Biến toàn cục)
x = "awesome"
def my_func():
    x = "fantastic" # local variable (biến cục bộ) -> Không có nghĩa là reassign
    y = "fantastic" # local variable (biến cục bộ)
    print("Python is " + x)
    print("Y:", y)
my_func()
print("Python is " + x)

print("--------------------------------")
# The global Keyword: Giúp khai báo biến toàn cục bên trong hàm
def my_func_global_keyword():
    global foo
    foo = "fantastic"
my_func_global_keyword()
print("foo:", foo)
print("--------------------------------")
