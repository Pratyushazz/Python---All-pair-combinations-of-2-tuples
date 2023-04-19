# input
tuple1 = (4, 5)
tuple2 = (7, 8)

# initialize an empty list to store the filtered tuples
filtered_tuples = []

# iterate over each element in tuple 1
for element1 in tuple1:
    # iterate over each element in tuple 2
    for element2 in tuple2:
        # append a tuple of the two elements to the filtered list
        filtered_tuples.append((element1, element2))
        # append a tuple of the two elements in reverse order to the filtered list
        filtered_tuples.append((element2, element1))

# output
print(filtered_tuples)
