# •	Write a Python program to copy the contents of a file to another file. 


try:
    with open('Que_11.txt','r') as file:
        content = file.read()
    with open('Que_12.txt','w') as file2:
        file2.write(content)
    print('file copied successfully')
except FileNotFoundError:
    print('file not exists')