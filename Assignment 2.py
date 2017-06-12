import random as r

def main():
    original = input("Enter a 4-letter word: ").lower()

    letters = isolate_letters(original)
    obsfucate_letters(letters)
    obfuscated = recompose_obfuscated_letters(letters)

    print("Original:  ", original)
    print("Obfuscated:", obfuscated)


def isolate_letters(original):
    letters = list(original)
    return letters


def obsfucate_letters(letters):
    symbols = (["!", "%", "*", "#", "@"])
    if r.randint(0,100) <=90:
        letters[0] = r.choice(symbols)
    else:
        letters[0] = letters[0]

    if r.randint(0,100) <=90:
        letters[1] = r.choice(symbols)
    else:
        letters[1] = letters[1]

    if r.randint(0,100)  <=90:
        letters[2] = r.choice(symbols)
    else:
        letters[2] = letters[2]

    if r.randint(0,100)  <=90:
        letters[3] = r.choice(symbols)
    else:
        letters[3] = letters[3]
    return letters



def recompose_obfuscated_letters(letters):
     obfuscated = (''.join(map(str, letters)))
     return obfuscated

main()