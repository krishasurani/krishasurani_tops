# Write a Python program to get the Fibonacci series of given range. 

# def Fibonacci(number):
#            if(number == 0):
#                       return 0
#            elif(number == 1):
#                       return 1
#            else:
#                       return (Fibonacci(number - 2)+ Fibonacci(number - 1))
# number = int(input("Enter the Number upto which fibonacci series has to to print : "))
# for n in range(0, number):
#            print(Fibonacci(n))

a = 0
b = 1
num = int(input("range of fibonacci series: "))
print(a,b,end=" ")
for i in range(1,(num+1)-2):
    sum = a+b
    a = b
    b = sum
    print(sum,end=" ")