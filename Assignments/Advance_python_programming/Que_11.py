# Write a Python program to write a list to a file. 

my_list = [
    {'name': 'krisha',
     'age' : 16,
     'contact' : 123456},
     {'name': 'kruti',
      'age' : 18,
      'contact' : 987654}
]

file = open('Que_11.txt','w')
for i in my_list:
    file.write(str(i) + '\n')
file.close()