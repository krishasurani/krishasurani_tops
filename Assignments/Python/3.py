# Write a Python program to get the Fibonacci series of given range. 


#  fibonacci_series(n):
#         fib_sequence = [0, 1]
#     while len(fib_sequence) < n:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence


def Fibonacci(number):
           if(number == 0):
                      return 0
           elif(number == 1):
                      return 1
           else:
                      return (Fibonacci(number - 2)+ Fibonacci(number - 1))
number = int(input("Enter the Number upto which fibonacci series has to to print : "))
for n in range(0, number):
           print(Fibonacci(n))