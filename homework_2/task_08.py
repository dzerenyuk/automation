# Дан кортеж из N элементов и список из N элементов вывести элементы
# которые есть как в кортеже так и в списке.
first_set = (1, 25, 45, 16, 21, 3, 4, 8, 65)
second_set = [1, 8, 25, 65, 32, 97, 30, 44, 9]
print(f"List of elememnts both in {first_set} and {second_set} is "
      f"{list(set(first_set).intersection(set(second_set)))}")