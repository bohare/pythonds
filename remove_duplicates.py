# Create a list of letters from the words in wordlist and delete the dup[licates, if any.

wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

org = ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
org_set = list(set(org))
print(org_set)
