#first task
user_name = input('Please enter your name:')
age = input('Please enter your age:')
print(f'Hello {user_name} your age is {age}')
# TODO: space after # is not present

#second task
number = int(input('Enter your number: '))
print(f'{number ** 132} - entered number in power 132, {number ** 132 % 3} - remainder from division')
# TODO: line with instruction is bigger then 79 symbols

#third task
first_number = int(input())
second_number = int(input())
print(first_number + second_number) # addition
print(first_number - second_number) # substraction
print(first_number * second_number) # multiplication
print(first_number // second_number) # division with no remainder
print(first_number / second_number) # division with remainder
print(first_number % second_number) #remainder from division
print(first_number ** second_number) #powering
# TODO: space after # is not present
# TODO: 2 spaces after code before comment should be present
# TODO: No description about output in console

# region fourth task
a, b, c = [int(x) for x in input('Enter three values: ').split()]
print( (2 * a - 8 * b) / (a + b +c ))
# TODO: ZeroDivisionError: division by zero
# TODO: Please take a look on PEP 8:
# TODO: Excess space present after '('
# TODO: Space after arithmetical operation is not present
# TODO: Blocking operation inside list comprehension. Best practice is to
#  prevent blocking operations inside
#  functions/methods/generators/coroutines/comprehensions

#fifth task
string = input()
number = int(input())
print(string * number)
# TODO: space after # is not present
# TODO: No description about input parameters

#sixth task
number_first = 125
number_second = 437
print(number_first % 2, number_first % 3, number_first % 10, number_first % 22)
print(number_second % 2, number_second % 3, number_second % 10, number_second % 22)
# TODO: Space after arithmetical operation is not present
# TODO: line with instruction is bigger then 79 symbols
# TODO: No description about output in console
# TODO: code duplication with literals 2, 3, 10, 22

#seventh task
first = int(input())
second = int(input())
print(first // second, second // first)
# TODO: Space after arithmetical operation is not present
# TODO: No description about output in console
# TODO: No description about input parameters


#eigth task
print(" ".join([x for x in input('Enter three values: ').split()]))
# TODO: Space after arithmetical operation is not present
# TODO: Blocking operation inside input parameters of builtin function
# TODO: Blocking operation inside list comprehension

#ninth task
first = 15
second = 43
first, second = second, first
print(first, second)
# TODO: Space after arithmetical operation is not present

#tenth task
from decimal import Decimal
a = 100.23459879
b = 2.09870983745
# converting to decimal incorrect result of multiplying
msg_0 = "Converting result of float mult:"
print(f"{msg_0.ljust(40)} | {Decimal(a * b )}")

msg_1 = "Mult float numbers:"
msg_2 = "Mult float number in decimal container:"
msg_3 = "Valid conversion to decimal:"

print(f"{msg_1.ljust(40)} | {a * b}")
print(f"{msg_2.ljust(40)} | {Decimal(a) * Decimal(b)}")
print(f"{msg_3.ljust(40)} | {Decimal(str(a)) * Decimal(str(b))}")
# TODO: Space after arithmetical operation is not present
# TODO: Modules level import is not at top of current module: PEP 8
# TODO: Excessive space after 'b'
# TODO: Please take a look on comparison of operations with decimal types

# TODO: Common todo. Please split tasks by different modules. Since there is
#  a lot of blocking input operations and it is hard to read code i such
#  style.
