def fizz_buzz(number):
    if number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    elif (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    else:
        return number


k = fizz_buzz(9)
print(k)
