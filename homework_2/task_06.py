first_set = {1, 8, 2, 1, 4, 6, 16, 15, 15, 2, 0, 3, 2, 32}
second_set = {12, 2, 85, 12, 4, 9, 32, 17, 0, 15, 1, 6, 31}
set_intersection = first_set.intersection(second_set)
set_to_list = list(set_intersection)
substraction = set_to_list[0] - set_to_list[-1]
print(f"Intersection of {first_set} and {second_set} is {set_intersection} \n"
      f"Substraction of first and last element of set {set_intersection} "
      f"is {substraction} ")



