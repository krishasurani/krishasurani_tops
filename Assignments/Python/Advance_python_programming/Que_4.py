# Write a Python program to read first n lines of a file. 

number = int(input("Enter number of line you want to read: "))

file = open("Que_4.txt",'r')

for line in range(number):
    print(file.readline())
file.close()