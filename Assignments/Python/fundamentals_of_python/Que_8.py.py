#  Write a Python program to test whether a passed letter is a vowel or not


def is_vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False

letter = input("Enter a letter: ")
if is_vowel(letter):
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")





