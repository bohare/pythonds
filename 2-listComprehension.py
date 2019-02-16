# Create a list of letters from the words in wordlist and delete the duplicates, if any. Do this using list comprehensions.
# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)


letters = list(set([letter for word in wordlist for letter in word]))
print(letters)
