numbers = [1, 8, 14, 32, 11, 24, 16, 7, 5, 96]
count_even_numbers = 0
for number in numbers:
    if not number % 2 :
        count_even_numbers += 1
print(f"Total of even numbers in the list is {count_even_numbers}")
