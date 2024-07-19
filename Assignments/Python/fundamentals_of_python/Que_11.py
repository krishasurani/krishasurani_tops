#  Write a python program to sum of the first n positive integers


def sum_of_integers(n):
    return n * (n + 1) // 2


num = int(input("Enter a positive integer: "))
if num > 0:
    sum_n = num * (num + 1) / 2  
    print("The sum of the first",num, "positive integers is:", sum_n)
else:
    print("Please enter a positive integer.")