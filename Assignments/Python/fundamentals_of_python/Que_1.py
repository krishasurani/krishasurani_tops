#  Write a Python program to check if a number is positive, negative or zero.

while(1):

    number = int(input("enter the number: "))
    print(number)

    if number>=0 :
        print("the number is positive") 
    elif number==0 :
        print("the number is zero ")
    else :
        print("the number is negative")