# Write a Python program to read last n lines of a file

num = int(input("Enter number of lines to read from last: "))

with open('Que_5.txt','r') as file:
    data = file.readlines()
    data1 = data[::-1]
    for i in range(num):
        print(data1[i])