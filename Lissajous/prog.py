import matplotlib.pyplot as pl
import matplotlib.animation as animation
import numpy as np
from lissajous import Lissajous
import random

# main menu
while True:
    print ("""
  Welcome to Lissajous Curve  
            MENU
------------------------------
1. Play
2. View
3. Quit

Your option (1-3) :""")

# check input 
    while True:
        menu = input()
        try : 
            menu = int(menu)
            break
        except ValueError:
            print ('please input a number.')
            print ('Your option (1-3): ')

# the Play menu
    if (menu == 1):
        radius_1 = 1
        radius_2 = 1

# randoming the first and second circle speed and prevent the same number for both speed
        while True:    
            speed_1 = random.randint(1,10)
            speed_2 = random.randint(1,10)
            if (speed_1 != speed_2):
                break
# setting the play menu
        repeat = 'N'
        repeat_count = 1

# comment
        print ("please close the matplotlib window to proceed (after you know the guess number).")

# animate the curve
        lissajous = Lissajous(radius_1,radius_2,speed_1,speed_2)
        lissajous.get_curve(repeat_count)
        lissajous.animate(repeat)

# the guess menu (play)
        print ("""
Guess the speed:
---------------------------
""")

# validate the first circle speed guess
        while True :
            print ("First circle Speed  (1-10):")
            guess_speed_1 = input()
            try:
                guess_speed_1 = int(guess_speed_1)
                if (guess_speed_1 > 10 or guess_speed_1 < 1):
                    print ("Range of Guess is only from 1 to 10")
                else :
                    break
            except ValueError :
                print ("Please input a number between 1 - 10:")
# validate the second circle speed guess
        while True :
            print ("Second circle Speed  (1-10):")
            guess_speed_2 = input()
            try:
                guess_speed_2 = int(guess_speed_2)
                if (guess_speed_2 > 10 or guess_speed_2 < 1):
                    print ("Range of Guess is only from 1 to 10")
                else :
                    break
            except ValueError :
                print ("Please input a number between 1 - 10:")
                
# checking the answer
        if (guess_speed_1 == speed_1 and guess_speed_2 == speed_2):
            print (" YOU WIN ! ")
        elif (guess_speed_1 == speed_1 or guess_speed_2 == speed_2):
            if (guess_speed_1 == speed_1):
                print (" YOU LOSE ! Try more. Your first guess are correct!")
                print ("The correct second guess is",speed_2)
            else:
                print (" YOU LOSE ! Try more. Your second guess are correct!")
                print ("The correct first guess is",speed_1)
        else :
            print (" YOU LOSE ! Try more. Both of your guess are wrong!")
            print ("The correct first guess is",speed_1)
            print ("The correct second guess is",speed_2)
        
# the view menu
    elif (menu == 2):

#validate the inputs
        while True:
            radius_1 = input("input the first circle radius: ")
            try:
                radius_1 = int(radius_1)
                break
            except:
                print ("please input a number")
        while True:
            radius_2 = input("input the second circle radius: ")
            try:
                radius_2 = int(radius_2)
                break
            except:
                print ("please input a number")
        while True:
            speed_1 = input("input the first circle rotation speed:")
            try:
                speed_1 = int(speed_1)
                break
            except:
                print ("please input a number")
        while True:
            speed_2 = input("input the second circle rotation speed:")
            try:
                speed_2 = int(speed_2)
                break
            except:
                print ("please input a number")

# Validate the repeat choice
        while True:
            repeat = input("Do you want the curve drawn repeatedly ? (y/N)")
            if not(repeat.lower() == "y" or repeat.lower() == "n"):
                print ("please input (y/N).")
            else:
                if repeat.lower() == "y":
                # validate the repeat_count
                    while True:
                        repeat_count = input("How many times you want to repeat the CURVE : ")
                        try:
                            repeat_count = int(repeat_count)
                            if (repeat_count <= 1):
                                print("please input more than 1.")
                            else:
                                break
                        except :
                            print("please input a number")
                    break
                else:
                    repeat_count = 1 
                    break

# comment
        print ("please close the matplotlib window to proceed.")

# animate the curve
        lissajous = Lissajous(radius_1,radius_2,speed_1,speed_2)
        lissajous.get_curve(repeat_count)
        lissajous.animate(repeat)
    
# exit 
    elif (menu == 3):
        exit()
# input beside 1, 2, and 3
    else : 
        print ('Wrong Input, please input between 1 and 3.')
