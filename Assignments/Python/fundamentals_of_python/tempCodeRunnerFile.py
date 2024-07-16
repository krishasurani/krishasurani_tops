    num = int(input("Enter the number: "))
    if num<0:
        print("Please enter positive number !!")
        continue

    fact = 1
    for i in range(1,num+1) :
        fact = fact * i
        
    print("factorial of {num} is: ",fact)
