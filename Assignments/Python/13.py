# Write a Python program to count the number of characters (character frequency) in a string



def count_characters_set(test_str):
    res = {char: test_str.count(char) for char in set(test_str)}
    return res

input_string = "Helloworld"
result_set = count_characters_set(input_string)
print("Character frequencies using set() and count():")
print(result_set)
