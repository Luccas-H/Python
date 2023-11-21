import string 
letters = string.ascii_lowercase
 

word = str(input("Type something for encrypt in Caesar Cipher: ")).lower()

list_letters = []
for letter in letters:
    list_letters.append(letter)

list_word = []
for split in word:
    list_word.append(split)

list_word_splitted = []
for splitted_alpha in list_word:
    if splitted_alpha.isalpha():
        list_word_splitted.append(splitted_alpha)


list_cesar = []
timing = 3
timing_reverse = 23
for word_letter in list_word_splitted:
    if list_letters.index(word_letter) >= 23:
        print(list_letters[abs(list_letters.index(word_letter) - timing_reverse)], end = "")
    
    elif word_letter in list_letters:
        print(list_letters[list_letters.index(word_letter) + timing], end = "")

