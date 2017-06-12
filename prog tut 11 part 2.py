def main():
    # dictionary of username : hashed_password
    users = {
        "mim" : 149,
        "mls" : 162,
        "bon" : 9
    }

    # attempt a login
    success = login(users)

    if success:
        print("Successful login")
    else:
        print("Could not login")



def login(users):

    # ask for a username and password
    username = input("Enter username:")
    password = input("Enter password for " + username)

    # compare the stored HASHED password to the HASHED password just entered
    if users.get(username) == hasher(password):
        return True   # successful login
    else:
        return False  # unsuccessful login



def hasher(password):
    import random
    ascii_value = sum([ord(char) for char in password])
    random.seed(ascii_value)
    hashed_password = (random.randint(0,255) + ascii_value) % 256
    return hashed_password



main()