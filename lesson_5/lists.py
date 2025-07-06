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
