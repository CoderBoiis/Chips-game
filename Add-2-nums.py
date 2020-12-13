user_range = int(input("Times program runs(if infinite, type 0. When you want the loop to end, type 0 again): "))

def getNums():
  number1 = int(input("Enter a number: "))
  number2 = int(input("Enter a number: "))
  return number1, number2

if user_range == 0:
  while True:
    print("Enter 0 for both numbers if you want to end the loop.")
    number1, number2 = getNums()
    number_sum = number1 + number2
    if number_sum == 0:
      print("Thanks for using our program! Bye!")
      break
    print("Your sum is " + str(number_sum))
else:  # 'u' in the next line stands for 'user_range'
  for u in range(1, user_range + 1):
    number1, number2 = getNums()
    number_sum = number1 + number2
    print("Your sum is " + str(number_sum))
