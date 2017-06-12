letter_frequency = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

text = input("enter text").lower()

alphabet ='abcdefghijklmnopqrstuvwxyz'
common_letters = 'EATNIROSHLCDGUWPBFYMKVXZJQ'.lower()

text_as_list = list(text)
newletters = list()
finalletters = list()

def key_func(text):
    return text[1]

for letter in text:
    if letter.isalpha():
        letter_frequency[letter] += 1

unsort = letter_frequency.items()
sort = sorted(unsort, key = key_func, reverse = True)

amount = 0
for c, l in sort:
    common = (c,common_letters[amount])
    newletters.append(common)
    amount += 1

for char in text_as_list:
    if char.isalpha():
        for c,l in newletters :
            if char == c:
                replacing = char.replace(char,l)
                finalletters.append(replacing)
    else:
        finalletters.append(char)


text = "".join(finalletters)

print("Your message is - ", text)





