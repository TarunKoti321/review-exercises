from itertools import combinations, permutations

# Define lists
A = [1, 2]
B = [3, 4]
C = [5, 6]
D = [7, 8]
E = [9, 0]

# Compute all combinations
print("Combinations:")
for combination in combinations(A + B + C + D + E, 3):
    print(combination)

# Compute all permutations
print("\nPermutations:")
for perm in permutations(A + B + C + D + E, 3):
    print(perm)
