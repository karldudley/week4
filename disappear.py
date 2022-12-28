# # get a sentence from the user and the characters to remove
sentence = input("Please write a cool sentence:\t")
characters = input("What characters do you want to remove from the sentence?\t")

# convert characters to a list
list_of_chars = characters.split()

# Create a translation table to map the characters
transtab = str.maketrans('', '', ''.join(list_of_chars))

# remove the characters and print old and new sentences
new_sentence = sentence.translate(transtab)
print(sentence)
print(new_sentence)
