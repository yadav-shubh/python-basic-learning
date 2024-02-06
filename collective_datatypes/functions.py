import math


def welcome(name):
    print(f"Welcome to {name}")


def square(number):
    return math.pow(number, 2), f"The square of {number} is {math.pow(number, 2)}"


user_input = input("What is your name? ")
welcome(user_input)

user_input = input("Type a number to see the square: ")
square_of_number, message = square(number=int(user_input))
print(square_of_number, message, sep=", ")
