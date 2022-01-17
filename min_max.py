# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 1/16/2022

# Description: Write a program that asks the user how many integers they would like to enter. You can assume that
# this initial input will be an integer >= 1. The program will then prompt the user to enter that many integers.
# After all the numbers have been entered, the program should display the largest and smallest of those numbers (no,
# you cannot use lists, or any other material we haven't covered).

# asking the user how many integers they would like to enter.
print("How many integers would you like to enter?")
# prompting the user to enter desired integers.
num_1 = int(input())
# checking if value for integers is a positive real number different from zero.
# if number is greater than zero, then proceed to collect integers.
if num_1 >= 1:
    # asking user to enter the desired number of integers.
    print("Please enter", num_1, "integers.")
    # initializing variables to store minimum and maximum values.
    minimum = int(input())
    maximum = minimum
    # initializing loop to compare every single entered integer to the previous one.
    for i in range(1, num_1):
        # variable number takes the value of the entered integer.
        number = int(input())
        # comparing just entered number to previous maximum number.
        # if just entered number is greater than last value for maximum,
        # then maximum value takes the value of just entered number.
        if number > maximum:
            maximum = number
        # comparing just entered number to previous minimum number.
        # if just entered number is smaller than last value for minimum,
        # then minimum value takes the value of just entered number.
        if number < minimum:
            minimum = number
    # printing results.
    print("min: ", minimum)
    print("max: ", maximum)
# if number is zero or less, then program would ask to enter a different number for integers.
else:
    print("Incorrect Value, please enter a number greater than zero.")
