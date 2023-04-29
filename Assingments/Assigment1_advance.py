
import numpy as np

correct_letter = "java"
count = 6
wrong_guess = 0

guessed_array = []
used_letter = []
flag = 0
temp = 1
print(f"You have {count} tries left")
print("Used letter: ")
print("Word: _ _ _ _")
while count != 0:
    flag = 0
    letter = input("Guess a letter: ")
    for i in range(len(correct_letter)):
        if correct_letter[i] ==letter: # check the estimating letter is equal to correct one
            guessed_array.insert(i,letter) # if it is true than we adding this letter to correct place
            flag = 1
    if flag == 0:
        count = count - 1
        wrong_guess = + 1

    used_letter.insert(temp,letter) # to see used letter
    temp = temp + 1
           
    print(f"You have {count} tries left")
    print("Used letter: ", used_letter)
    print("Word: ", guessed_array)
    if len(guessed_array) == len(correct_letter): # if you guess 5 times you cant do anymore
        flag =5
        break

if flag == 5:
    print("You guessed the word java !")
else:
    print("you lost the game")
    