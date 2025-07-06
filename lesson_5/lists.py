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


# Chưa học xong while loop
