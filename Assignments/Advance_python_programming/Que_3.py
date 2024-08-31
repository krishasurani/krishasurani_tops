# Write a Python program to append text to a file and display the text.

file = open("Que_3.txt",'w')
file.write("python is object oriented programming language") 
file.close()

file = open("Que_3.txt",'a')
file.write("\npython is interpreted programming language")
file.close()