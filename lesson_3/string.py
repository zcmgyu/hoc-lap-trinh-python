# String

x = "Hello, World!"
y = 'Hello, World!'

print("x =", x)
print("y =", y)

#  I'm Win
# name = 'I'm Win'
name1 = "I'm Win"
print("name1 =", name1)
name2 = 'I\'m Win' # escape character
print("name2 =", name2)
name3 = """I'm Win"""
print("name3 =", name3)

# Multiline string
introduction = """

I'm Win

I'm a student

I'm a developer"""

print("introduction =", introduction)

# Strings are arrays
strs = "Hello, World!"

print("strs[0] =", strs[0])
print("strs[1] =", strs[1])
print("strs[2] =", strs[2])
print("strs[3] =", strs[3])
print("strs[4] =", strs[4])

for str in strs:
    print('str =', str)

print("strs length =", len(strs))


# Check string
document = "To check if a certain phrase or character is present in a string, we can use the keyword in."

print("Win in document =", "Win" in document)
print("character in document =", "character" in document)

if "character" in document:
    print("character is present in document")
else:
    print("character is not present in document")

if "Win" not in document:
    print("Win is not present in document")
else:
    print("Win is present in document")


