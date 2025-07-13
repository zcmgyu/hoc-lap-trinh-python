# Lists

# List is a collection of items
list = [1, 2, 3, 4, 5]

# Accessing elements
print("Accessing first item: ", list[0])

print("Accessing last item: ", list[len(list) - 1])
print("Accessing last item: ", list[-1])

# Modifying elements
list[0] = 10
print("Modifying item: ", list)

# Adding elements
list.append(6)
print("Adding item: ", list)

# Removing elements
list.remove(6)
print("Removing item: ", list)

# Remove last item
list.pop()
print("Removing last item: ", list)
list.pop()
print("Removing last item: ", list)

# Remove first item
list.pop(0)
print("Removing first item: ", list)

# Remove item at index
list.pop(1)
print("Removing item at index 1: ", list)


# Range of Indexes
pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

reads = pages[0:5]

print("Read pages: ", reads)

todayPages = pages[5:]
print("Today's pages: ", todayPages)

# Changes a range of items
newList = [10, 20, 30, 40, 50]
newList[1:3] = [1, 2, 3, 4]
print("New list: ", newList)

# Insert a range of items
danhSachLop = ["Nguyen Van A", "Nguyen Van B", "Nguyen Van C", "Nguyen Van D", "Nguyen Van E"]

danhSachLop.insert(3, "Nguyen Dang Doanh")

print("Danh sach lop: ", danhSachLop)

# Extend a list
lop6_3 = ["Nguyen Van A", "Nguyen Van B", "Nguyen Van C", "Nguyen Van D", "Nguyen Van E"]
lop6_4 = ["Nguyen Van F", "Nguyen Van G", "Nguyen Van H", "Nguyen Van I", "Nguyen Van J"]

print("Danh sach lop 6.3 BEFORE: ", lop6_3)
lop6_3.extend(lop6_4)

print("Danh sach lop AFTER: ", lop6_3)


# Loop

list = ['A', 'B', 'C', 'D', 'E']

for item in list:
    print(item + '+')


# While loop

number_of_candies = 30
while number_of_candies > 0: # Condition (boolean): true/false. true: run, false: stop
# while True:
    # Phat khoi
    print("Phát kẹo!!!")
    # number_of_candies = number_of_candies - 1
    number_of_candies -= 1
    print("Số kẹo còn lại: ", number_of_candies)
    # Không có điều kiện để dừng
    # Chạy vô tận
    # if number_of_candies == 0:
        # break
print("Hết kẹo")

fruits = ["apple", "banana", "cherry", "avocado"]

# Print a list
i = 0
print("Print a list")
while i < len(fruits):
    print(fruits[i])
    i += 1
print("Stopped!!!")

# Reverse a list
print("Reverse a list")
j = len(fruits) - 1
while j >= 0:
  print(fruits[j])
  j -= 1
print("Stopped!!!")

# Shortest way to print a list
# for fruit in fruits:
#     print(fruit)
print("Use the for loop")
[print(fruit) for fruit in fruits]

# List comprehension
print("List comprehension")
print("Print fruits that start with 'a'")
[print(fruit) for fruit in fruits if fruit[0] == 'a']
new_fruits = [fruit for fruit in fruits if fruit[0] == 'a']
print("New fruits: ", new_fruits)


# Pass by reference | Pass by value
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# Clone new list
# new_fruits = [x for x in fruits]
# Reference to list
new_fruits = fruits


new_fruits[0] = "avocado"

print("Fruits: ", fruits)
print("New Fruits: ", new_fruits)

# Sort a list
print("--------------------------------")
print("Sort a list")
fruits.sort()
print("Fruits: ", fruits)

# Sort a list in descending order
print("Sort a list in descending order")
fruits.sort(reverse=True)
print("Reversed Fruits: ", fruits)

# Find all indexes of a fruit in list
print("--------------------------------")
print("Find all indexes of a fruit in list")
fruits = ["banana", "banana", "Orange", "Kiwi", "cherry", "banana"]

print([i for i, fruit in enumerate(fruits) if fruit == "banana"])
