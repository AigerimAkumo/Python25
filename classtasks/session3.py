
# for num in range (101):
#     print(num)

#print only even number all the way to 10

# for num in range (11):
#     if num % 2 == 0:
#         print (num)

#Character counter
#take an input of the word/senetence
#calculate how many A characters are in the word/sentece
#input: aKumosolutions

# word = input("Please, provide a word or sentence: ")
# counter = 0
# for char in word:
#     if char == "a":
#         counter = counter + 1
# print(counter)

#instead of taking letter "a" let the user choose the letter
#sentence or character should be cases insensetive (hint: use str.lower or str.upper)

word = input("Please, provide a word or sentence: ")
word2 = input("Choose any letter from your word or sentence: ")
word3 = input("Choose second letter from your word or sentence: ")

counter = 0
counter2 = 0

if len(word2) == 1 and len(word3) == 1:
    for char in word:
        if char == word2:
            counter = counter + 1
        elif char == word3:
            counter = counter2 + 1
    print(f"{word2} = {counter}")
    print(f"{word3} = {couner2}")
    
else:
    print ("Character input is more than 1")

print(counter)