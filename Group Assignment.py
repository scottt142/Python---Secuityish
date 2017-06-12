def main():

    # the main menu loop
    while True:

        # show the main menu and save their choice
        main_choice = main_menu()

        # when they choose to quit break out of the infinite while loop
        if main_choice == 'q':
            break

        # user chooses to cipher
        elif main_choice == 'c':
            print("STUDENTS TO IMPLEMENT.")

        # user chooses to decipher
        elif main_choice == 'd':
            print("STUDENTS TO IMPLEMENT.")

        else:
            print("Error - choice not recognised")


def cipher(method, text):
    if method == 'c':
        return caeser(text)

    if method == 'f':
        return error ("CANNOT USE FREQUENCY ANALYSIS TO ENCRPYT")
        choice = input("Choose").lower()

        if method == 'c':
            return caeser(text)
    return method, text


def decipher(method, text):

    if method == 'c':
        return caeser(text)

    if method == 'f': #Frequency Analysis
        return frequency_analysis(text)

    return text


def caesar(text):
    """ Summary:    Caesar shift a string by a given amount
        Parameters: text - The text to apply the shift to
        Returns:    A string containing the shifted text
    """

    return text






def frequency_analysis(text):
    frequency = {'a':0, 'b': 0, 'c':0, 'd':0, 'e': 0, 'f':0,'g':0,}
    return "STUDENTS TO IMPLEMENT."


def get_text(source):
    """ Summary:    Single access point to text source methods
        Parameters: source - A character representing where to get text from
                             "T" for user input, "F" for file
        Returns:    A string containing the file / typed text
    """

    return "STUDENTS TO IMPLEMENT."


def save_to_file(text):

    file = open("encryption.txt", "w")
    file.write(text)
    file.close()
    print("encryption.txt")

def load_from_file():
    try:
        file = open("encryption.txt", "r")
        string_text = file.read()
        file.close()
    except:
        print("File Cannot Open!")

    return file

def main_menu():
    print()
    print("Scott Taylor, Kieran Rowley, Dan Porter, James Swindell - 2016")
    print()
    print(".-MAIN MENU-----------------.")
    print("|                           |")
    print("|  (C) Cipher               |")
    print("|  (D) Decipher             |")
    print("|  (Q) Quit                 |")
    print("|                           |")
    print("`---------------------------'")

    return input("What would you like to do? ").lower()

def source_menu():

    return "STUDENTS TO IMPLEMENT."

def method_menu():
    return "STUDENTS TO IMPLEMENT."



main()