# •	Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

while True:
    try:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(f"{number} is an Even number!")
        else:
            print(f"{number} is an Odd number!")
        
        more_check = input("Do you want to check another number? (y/n): ").lower()
        if more_check != 'y':
            print("Exiting the program.")
            break
        
    except ValueError:
        print("Please enter a valid number!")


