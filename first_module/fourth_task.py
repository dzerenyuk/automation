#fourth task
a, b, c = [int(x) for x in input('Enter three values: ').split()]
print( (2 * a - 8 * b) / (a + b +c ))


#fifth task
string = input()
number = int(input())
print(string * number)

#sixth task
number_first = 125
number_second = 437
print(number_first % 2, number_first % 3, number_first % 10, number_first % 22)
print(number_second % 2, number_second % 3, number_second % 10, number_second % 22)

#seventh task
first = int(input())
second = int(input())
print(first // second, second // first)


#eigth task
print(" ".join([x for x in input('Enter three values: ').split()]))

#ninth task
first = 15
second = 43
first, second = second, first
print(first, second)

#tenth task

from decimal import Decimal
a = 100.23459879
b = 2.09870983745
print(Decimal(a * b ))