first_set = {1, 2, 3, 5, 1, 8, 7}
second_set = {1, 2, 3, 4, 6, 2, 0}
print(f"List with unique elements from {first_set} and {second_set} is "
      f"{list((first_set.union(second_set)))}")
