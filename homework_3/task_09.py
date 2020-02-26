number = 23
# prime number is a number that is divisible only by itself without a remainder
if number > 1:
    # check for factors
    for i in range(2, number):
        if number % i == 0:
            print(F"{number} isn't a prime number")
            break
    else:
        print(f"{number} is prime")
else:
    print(f"{number} isn't prime")
