# Write a Python program to read a file line by line store it into a variable. 

file = open("Que_7.txt",'r')
file_list = file.readlines()

for line in file_list:
    print(line)
file.close()