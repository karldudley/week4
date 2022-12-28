# get a word from user
word = input("Please enter a word:\t")
new_word1 = ""

# loop through word and change to upper and lower
for i in range(len(word)):
    if (i % 2 == 0):
        new_word1 += word[i].upper()
    else:
        new_word1 += word[i].lower()
# print edited word
print(new_word1)

words = word.split()
new_word2 = ""
for i in range(len(words)):
    if (i % 2 == 0):
        new_word2 += words[i].lower() + " "
    else:
        new_word2 += words[i].upper() + " "
# print edited word
print(new_word2)
