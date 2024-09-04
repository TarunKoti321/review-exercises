import itertools

# Define the list
list_elements = [1, 2, 3, 4]

# Compute permutations
print("Permutations using itertools:")
permutations_list = list(itertools.permutations(list_elements))
print(permutations_list)

# Compute combinations
print("\nCombinations using itertools:")
combinations_list = list(itertools.combinations(list_elements, 2))
print(combinations_list)
