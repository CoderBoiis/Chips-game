# Gets the user's range at the starting so I know if the user wants this to be a never ending loop
user_range = int(input("Times program runs(if infinite, type 0. When you want the loop to end, type 0 again): "))


if user_range == 0:
    while True:
        user_range += 1
        # This is the code which I added, everything from line 8-10
        number1 = int(input("Give the first number you want to add: "))
        number2 = int(input("Give the second number you want to add: "))
        number_sum = number1 + number2
        # This breaks the code after printing the end messages if you input 0 again
        if number_sum == 0:
            print("Thanks for using our system. (❁´◡`❁)")
            break
        # Prints the sum if the code is not broken
        print("Your sum is " + str(number_sum))
else:  # Runs a for loop in the range of the user_range(user_range is not affected by the + 1 in the while loop above)
    # 'u' in the next line stands for 'user_range'
    for u in range(user_range):
        # I copied and pasted the code from above here, lines 18-20
        number1 = int(input("Give the first number you want to add: "))
        number2 = int(input("Give the second number you want to add: "))
        number_sum = number1 + number2
        # Prints the sum if the code is not broken
        print("Your sum is " + str(number_sum))
