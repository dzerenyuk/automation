length_of_fibo = 7
first_number = 0
second_number = 1
count = 0
if length_of_fibo <= 0:
    print("Invalid value")
elif length_of_fibo == 1:
    print(f"Fibonacci sequence is {length_of_fibo}")
else:
    print("Fibonacci sequence:")
    while count < length_of_fibo:
        print(first_number)
        temp = first_number + second_number
        first_number = second_number
        second_number = temp
        count += 1
