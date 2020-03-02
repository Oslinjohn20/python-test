for x in range (101):
    print(x)
number= int(input("type a number here:"))
if number % 3 == 0:
    print("Fizz")

if number % 5 == 0:
    print("Buzz")

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")