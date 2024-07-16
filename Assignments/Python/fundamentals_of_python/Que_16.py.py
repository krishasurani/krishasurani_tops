#  Write a Python program to count the occurrences of each word in a given sentence 


# def word_frequency(sentence):
#     words = sentence.split()
#     frequency = {}
#     for word in words:
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#     return frequency


def word_count(sentence):
    counts = {}
    words = sentence.split()
    for word in words:
        word = word.lower() 
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# Example usage:
sentence = "I am persuing backend technology with python at Tops technology Surat.This is the place from  where I will get knowledge of IT field"
word_frequencies = word_count(sentence)
for word, count in word_frequencies.items():
    print(f"{word}: {count}")

