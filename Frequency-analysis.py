letter_frequency = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

text = input("enter text").lower()

alphabet ='abcdefghijklmnopqrstuvwxyz'
common_letters = 'etaoinshrdlcumwfgypbukjxqz'

for letter in text:
    if letter.isalpha():
        letter_frequency[letter] += 1

def key_func(text):
    return text[1]

unsort = letter_frequency.items()
sort = sorted(unsort, key = key_func)

ordered = reversed(sort)
reverse = list(ordered)

inordered = list()
for char in reverse:
    inordered.append(char)

tup = list()

for i in inordered:
    tup += i

s = str(tup)

' '.join(str(i) for i in tup)
print(tup)

freqtoletter = {}
for freq in freqtoletter:
    freqtoletter[freq].sort(key=common_letters.find, reverse = True)
    freqtoletter[freq] = ' '.join(freqtoletter[freq])
    print (freqtoletter)