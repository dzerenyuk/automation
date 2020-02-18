#first task
user_name = input('Please enter your name:')
age = input('Please enter your age:')
print(f'Hello {user_name} your age is {age}')

#second task
number = int(input('Enter your number: '))
print(f'{number ** 132} - entered number in power 132, {number ** 132 % 3} - remainder from division')

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




