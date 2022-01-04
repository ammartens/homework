list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
other_number = 69
last_number = 420
for number in list_of_numbers:
  print(number * other_number)
  if number * other_number > last_number:
    print("this number is greater than " + str(last_number))
