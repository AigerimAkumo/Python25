
# Task 1: Word Counter
# Ask the user to enter a sentence. Calculate the length of the sentence.


# take input from the user
sentence = input("please eneter a sentence: ")

# split() the sentence into words
words = sentence.split()

# len() will 
word_count = len(words)

print(word_count)