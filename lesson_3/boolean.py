a = 100
# b = 200
b = 100

if (a > b): # false
    print("a is greater than b")
elif (a == b): # true
    print("a is equal to b")
else:
    print("b is greater than a")

# Evaluate values and variables

# True values
x1 = "Hello" # true
x2 = 15

print("bool(x1) =", bool(x1))
print("bool(x2) =", bool(x2))

# False values
x3 = 0
x4 = "" # false
x5 = None
x6 = ()
x7 = []
x8 = {}

print("bool(x3) =", bool(x3))
print("bool(x4) =", bool(x4))
print("bool(x5) =", bool(x5))
print("bool(x6) =", bool(x6))
print("bool(x7) =", bool(x7))
print("bool(x8) =", bool(x8))

input_string = ""

if (len(input_string) > 0):
    print("input_string is not empty")
else:
    print("input_string is empty")

# Same as
if (bool(input_string)):
    print("input_string is not empty")
else:
    print("input_string is empty")

# Functions can Return a Boolean

def compare_two_numbers(a, b) -> bool:
    return a > b

if (compare_two_numbers(10, 20)):
    print("10 is greater than 20")
else:
    print("20 is greater than 10")

# Check instance

foo = 20.0

if (isinstance(foo, int)):
    print("foo is an integer")
elif (isinstance(foo, float)):
    print("foo is a float")
else:
    print("foo is not an integer or a float")

# Check if a string is a number



