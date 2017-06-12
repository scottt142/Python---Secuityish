def main():
    total = int(input("Enter total time:"))
    laps = int(input("Enter number of laps:"))

    try:
        average = total / laps      # put the dangerous line of code in the try block
    except:
        average = 0              # handle the error by giving average a default value
        print("ERROR - Average could not be calculated.")      # display helpful info

    print("Your average lap time was", average) # this line of code is still executed

main()