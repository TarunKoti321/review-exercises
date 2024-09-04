# Define a list
lst = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]

# II. Iterate using a for loop
print("Iterating using a for loop:")
for item in lst:
    print(item)

# III. Iterate using for loop and range
print("\nIterating using for loop and range:")
for i in range(len(lst)):
    print(lst[i])

# IV. List Comprehension
print("\nList Comprehension:")
comprehension = [item for item in lst]
print(comprehension)

# V. Enumerate
print("\nUsing Enumerate:")
for index, value in enumerate(lst):
    print(f"Index: {index}, Value: {value}")

# VI. Iter function and next function
print("\nUsing Iter and Next:")
it = iter(lst)
print(next(it))
print(next(it))

# VII. Map function
print("\nUsing Map function to square elements:")
squared = list(map(lambda x: x**2, lst))
print(squared)

# VIII. Using zip
print("\nUsing zip:")
lst2 = [9876, 5432, 1098]
for item1, item2 in zip(lst, lst2):
    print(item1, item2)

# IX. Using NumPy Module
print("\nUsing NumPy Module:")
import numpy as np
np_lst = np.array(lst)
print(np_lst)
