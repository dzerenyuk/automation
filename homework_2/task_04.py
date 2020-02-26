# Дан список из N элементов, пользователь вводит 2 целых числа, вывести часть
  # списка индекс начала которого равен первому введенному числу, а конец равен
   # индексу второго введенного числа.
user_list = [1, 25, 14, 85, 15, -4, 235, 17, 56, 4]
first_index = 3
last_index = 7
print(f'List with begin index {first_index} and last index {last_index}'
       f' is {user_list[first_index: last_index + 1]}')