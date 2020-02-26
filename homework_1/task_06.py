number_one = 125
number_two = 437
print(f"Remainder of the division {number_one} by 2 is {number_one % 2} \n"
      f"Remainder of the division {number_one} by 3 is {number_one % 3} \n"
      f"Remainder of the division {number_one} by 10 is {number_one % 10} \n"
      f"Remainder of the division {number_one} by 22 is {number_one % 22}"
      )
print(f"Remainder of the division {number_two} by 2 is {number_two % 2} \n"
      f"Remainder of the division {number_two} by 3 is {number_two % 3} \n"
      f"Remainder of the division {number_two} by 10 is {number_two % 10} \n"
      f"Remainder of the division {number_two} by 22 is {number_two % 22}"
      )
# NOT_FOR_REWORK: You could render duplicate code into variables and
# mathematical formulas easy to read as they are
# For example:
# a, b, c, d, e, f = 55, 3, 2, 3, 10, 22
#
# print(f"{a} % {c} = {a % c}")
# print(f"{a} % {d} = {a % d}")
# print(f"{a} % {e} = {a % e}")
# print(f"{a} % {f} = {a % f}")
#
# print(f"{b} % {c} = {b % c}")
# print(f"{b} % {d} = {b % d}")
# print(f"{b} % {e} = {b % e}")
# print(f"{b} % {f} = {b % f}")

# variant with iterating is more comfortable when you need to iterate a lot
# of arguments with same operaions
# devidables = [55, 3]
# dividers = [2, 3, 10, 22]
#
# for devidable in devidables:
#     for divider in dividers:
#         print(f"{devidable} % {divider} = {devidable % divider}")
