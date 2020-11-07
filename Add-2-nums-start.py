user_range = int(input("Times program runs(if infinite, type 0. When you want the loop to end, type 0 again): "))


if user_range == 0:
    while True:
        user_range += 1
        # Saketh your code should be before the print here, which will get the 2 numbers and find their sum
        number_sum =
        if number_sum == 0:
            break
        print("Your sum is " + str(number_sum))
else:  # 'u' in the next line stands for 'user_range'
    for u in range(1, user_range + 1):
        # Put your same input and sum code here
        number_sum =
        print("Your sum is " + str(number_sum))
