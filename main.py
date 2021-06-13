_author_ = "Amna Shahbaz"
_date_ = "Monday, May 31st, 2021"
_version_ = "1.0"
_filename_ = "Shahbaz_Amna_Assignment-3.py"
_description_ = "Guessing if random values are higher, lower, or in between"

import random

#variables
user_input = " "
correct = 0
incorrect = 0

#Conditioned while loop
while (user_input == "higher" or "lower" or "other"):
  print ("\nWelcome to Hi-Lo-Other!")
  random_number_1 = random.randint (1, 13)
  random_number_2 = random.randint (1, 13)
  print ("The first random value generated is", random_number_1)
  print ("The second random value generated is", random_number_2)
  print ("********")
  print ("Now what you have to do is guess whether the third random generated value is higher than the first two random numbers, lower,or other, which is in between the random generated numbers or the same number if both the random numbers are the same.")
  print ("###########")
  user_input = input("Is the third generated number: higher, lower, other? Or quit? ")
  if user_input == "quit":
    break
  #Check to see user enters valid input
  elif user_input == "higher" or user_input== "lower" or user_input== "other":
    random_number_3 = random.randint (1, 13)
    print ("The third random value generated is", random_number_3)
    if user_input == "higher" and random_number_3 > random_number_1 and random_number_3 > random_number_2:
      print ("Well done! You got it right!\n")
      correct +=1
    elif user_input == "lower" and random_number_3 < random_number_1 and random_number_3 < random_number_2:
      print ("Well done! You got it right!\n")
      correct +=1
    elif user_input == "other" and random_number_3 >= min(random_number_1, random_number_2)  and random_number_3 <= max(random_number_1, random_number_2):
      print ("Well done! You got it right!\n")
      correct +=1
    else:
      print ("Better luck next time!\n")
      incorrect +=1
    #If guess is correct, "Correct" counter increases, vice versa
    print ("Correct:", correct)
    print ("Incorrect:", incorrect)
  #print if invalid input is given
  else:
    print ("Please enter: higher, lower, or other\n")