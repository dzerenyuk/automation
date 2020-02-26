numbers = [0, 12, 4, 98, 32, 11, 64, 3, -5, 11]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(f"Sorted list is {numbers}")
