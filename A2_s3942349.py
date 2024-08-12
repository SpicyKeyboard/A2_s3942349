#COSC1519 Introduction to Programming
#A2 Programming Project
#Student name: Heath Yates
#Student number: 3942349

#IMPORTED MODULES
import random

#PROGRAM FUNCTIONS
#begins the start game text and asks the first question of the game
def game_start():
    #assigns text to the variables text_game_start and options_entrance to be printed to the user
    text_game_start = 'You are a world class spy on a mission of utmost importance \n'
    text_game_start += 'To complete your mission you must successfully extract from \n'
    text_game_start += 'the enemy base with the three pieces of information inside.\n'
    text_game_start += 'You begin already inside the entrance to the enemy base but\n'
    text_game_start += 'first must get your way through entrance security.\n \n'
    options_entrance = 'There is only one guard in the entrance that you must get past, what do you do? \n'
    options_entrance += '   1: Sneak past him using your spy stealth training \n'
    options_entrance += '   2: Shoot him! \n'
    options_entrance += '   3: Perform a silent takedown [good option]\n'
    print(text_game_start + options_entrance)
    user_entrance_option = input('What do you do?: ')
    while user_entrance_option != '3': #loops until user makes the '3' choice to progress game
        if user_entrance_option == '1':
            print('Unfortunately you were spotted and the entire base is on high alert as the guard rang the alarm')
            print('Maybe next time it is a better idea not to try sneak around in a place that is well lit.')
        if user_entrance_option == '2':
            print('You successfully downed the guard, however now every other guard knows that you are there too.')
        print('Try again \n' + options_entrance)
        user_entrance_option = input('What do you do?: ')
    print('Your takedown was successful and you managed to silently take down the guard and hide his body.')
    print('You now progress to the next room which is a three way fork.')

#tells the user what options are available and asks what they want to pick up
def game_middle_fork():
    #assigns variables text_game_middle and options_middle some text to be printed to the user
    text_game_middle = 'There are two different tools resting upon the wall of just before the fork, how lucky!\n'
    text_game_middle += 'One is a toolset consisting of screwdrivers, wire-cutters, a hammer and other helpful tools\n'
    text_game_middle += 'The other is a toy hulk hand, as you only have space for one more tool as your spy gear\n'
    text_game_middle += 'already takes up most of your holding capacity, which tool will you choose?: \n \n'
    options_middle = '    1: The toolset\n'
    options_middle += '    2: The Hulk hand\n'
    print(text_game_middle + options_middle)
    user_tool_choice = input('Which tool will you choose?: ')
    while True: #loops forever until break command is reached via using correct input of '1' or '2'
        if user_tool_choice == '1' or user_tool_choice == '2':
            break
        print(options_middle)
        user_tool_choice = input('Which tool will you choose?: ')
    if user_tool_choice == '1':
        item_inventory.append('Toolset')
    elif user_tool_choice == '2':
        item_inventory.append('Hulk Hand')
    print('Item obtained \''+item_inventory[0]+'\'!\n')
    game_hallway_choice()

#asks the user what hallway they are going to go down along with ridding the choices of hallways that they have already
#been down as this function will be called three times during the game. The last call may be redundant as the user only
#has one choice however I decided to keep it as it was annoying to make.
def game_hallway_choice():
    #hallway_annex is a list variable that contains all three options (left, middle, right) and will remove these variables
    #if the user has previously chosen them, eg: the user already went down left hallway_annex would now only contain
    #middle and right, this can be seen in the code at lines 85, 89 and 93 where depending on user input it removes the
    #option from hallway_annex
    if len(hallway_annex) == 3: #checks the length of hallway annex to see if user has gone down a hall yet, if len == 3
                                #it means that user has not gone down any hall yet, so will provide all options
        print('Now you must make a choice, \n')
        text_game_hallway = 'Do you go down the left hallway, the middle hallway or progress down the right hallway?'
    elif len(hallway_annex) == 2: #means that user has selected one hall previously and will only provide two options now
        text_game_hallway = 'Do you go down the ' + hallway_annex[0] + ' hallway or the ' + hallway_annex[1] + ' hallway?'
    else: #means that user has selected two halls and will now only show options for last hall
        text_game_hallway = 'Now for the final hallway, the ' + hallway_annex[0] + ' hallway.'
    print(text_game_hallway)
    options_hallway = ''
    #three if statements adding option text based on the choices available
    if 'left' in hallway_annex:
        options_hallway += '1: Left hallway\n'
    if 'middle' in hallway_annex:
        options_hallway += '2: Middle hallway\n'
    if 'right' in hallway_annex:
        options_hallway += '3: Right hallway\n'
    print(options_hallway)
    user_hallway_choice = input('Which hallway do you choose?: ')
    while True: #creates a loop asking for user input until user inputs correct string then it will break the loop
        if user_hallway_choice == '1':
                hallway_annex.remove('left') #here is an example of hallway_annex having a list item removed
                user_direction = 'left'
                break
        elif user_hallway_choice == '2':
                hallway_annex.remove('middle')
                user_direction = 'middle'
                break
        elif user_hallway_choice == '3':
                hallway_annex.remove('right')
                user_direction = 'right'
                break
        user_hallway_choice = input('Which hallway do you choose?: ')
    print('You choose the ' + user_direction + ' hallway.\n')
    #based off user input, progresses game to a different state
    if user_direction == 'left':
        game_left()
    elif user_direction == 'middle':
        game_middle()
    else:
        game_right()

#asks the user what they want to do and has different game progressions based on the user selection. One of the user
#selections from a previous question has an effect on the results of one of the choices.
def game_left():
    text_hallway_left = 'You travel down the left hallway, soon finding the room that it ends in,\n'
    text_hallway_left += 'inside you find one of the pieces of information that you require, it\n'
    text_hallway_left += 'is in a glass box, however you could probably just break it using\n'
    text_hallway_left += 'your ' + str(item_inventory[0])
    if item_inventory[0] == 'Toolset':
        text_hallway_left += '\'s hammer.'
    else:
        text_hallway_left += '.'
    print(text_hallway_left)
    options_left_hallway = '1: Smash the glass! [good option]\n'
    options_left_hallway += '2: Dont do anything\n'
    options_left_hallway += '3: Leave the enemy base [ends game]\n'
    print(options_left_hallway)
    user_left_hallway = input('What will you do?: ')
    glass_box_health = 50
    time_until_found = 0
    while True: #creates a loop that will run until user inputs the correct input to progress the game
        if user_left_hallway == '1': #conditional for '1' input
            if item_inventory[0] == 'Toolset':
                while True: #creates a loop that will run until the variable glass_box_health is =< 0
                    if glass_box_health > 0:
                        input('Smash it!: ')
                        glass_box_health = glass_box_health - random.randint(10, 30)
                        print('The glass box health is now ' + str(glass_box_health) + '.')
                    elif glass_box_health <= 0:
                        print('The glass box has shattered.')
                        print('You collect the information that was inside the once whole glass box and go back to the fork in the hallway.')
                        break

                break
            else:
                print('You clobbered that glass box with your hulk hand, smashing it to bits in one hit!')
                print('You collect the information that was inside the once whole glass box and go back to the fork in the hallway.')
                break
        elif user_left_hallway == '2': #condition for '2' input
            if time_until_found == 2:
                print('You have been found by the patrolling guards, perhaps try something else next time')
                print('Try again\n')
                time_until_found = 0
            user_left_hallway = input('What will you do?: ')
            time_until_found += 1
        elif user_left_hallway == '3': #conditional for '3' input
            print('You have failed your mission by leaving the enemy base without all the information.')
            quit()
        else: #conditional to rerun the input if input was not satisfactory
            user_left_hallway = input('What will you do?: ')

#asks the user what they want to do and has different game progressions based on the user selection. One of the user
#selections from a previous question has an effect on the results of one of the choices.
def game_middle():
    text_hallway_middle = 'You travel down the middle hallway, soon finding the room that it ends in,\n'
    text_hallway_middle += 'inside you find one of the pieces of information that you require, it\n'
    text_hallway_middle += 'is behind a metal plate that has been screwed on tight.\n'
    #if/else statement that changes options based on the previous options the user has made
    if item_inventory[0] == 'Toolset':
        text_hallway_middle += 'You should be able to unscrew it with the screwdrivers in your Toolset.'
        options_middle_hallway = '1: Unscrew one of the screws [good option]\n'
    else:
        text_hallway_middle += 'You should be able to smash that plate using your hulk hand.'
        options_middle_hallway = '1: Smash that plate!! [good option]\n'
    print(text_hallway_middle)
    options_middle_hallway += '2: Dont do anything\n'
    options_middle_hallway += '3: Leave the enemy base [ends game]\n'
    print(options_middle_hallway)
    user_middle_hallway = input('What will you do?: ')
    screws_left = 4
    time_until_found = 0
    while True: #creates a loop that will continue until satisfactory input is given otherwise will run input again
        if user_middle_hallway == '1':
            if item_inventory[0] == 'Toolset':
                while True: #creates a loop that will run until variable screws_left is = 0
                    if screws_left > 0:
                        input('Unscrew one of the screws: ')
                        screws_left -= 1
                        print('There are now ' + str(screws_left) + ' screws left.')
                    elif screws_left <= 0:
                        text_game_middle_tool ='You unscrewed all 4 screws and took the metal plate off revealing the information inside.\n'
                        text_game_middle_tool += 'You collect the information that was inside and go back to the fork in the hallway.'
                        print(text_game_middle_tool)
                        break
                break
            else:
                text_game_middle_hulk = 'You clobbered that metal plate with your hulk hand, smashing it in one hit!\n'
                text_game_middle_hulk += 'You collect the information that was inside and go back to the fork in the hallway.'
                print(text_game_middle_hulk)
                break
        elif user_middle_hallway == '2':
            if time_until_found == 2:
                print('You have been found by the patrolling guards, perhaps try something else next time')
                print('Try again\n')
                time_until_found = 0
            user_middle_hallway = input('What will you do?: ')
            time_until_found += 1
        elif user_middle_hallway == '3':
            print('You have failed your mission by leaving the enemy base without all the information.')
            quit()
        else:
            user_middle_hallway = input('What will you do?: ')

#asks the user what they want to do and has different game progressions based on the user selection. One of the user
#selections from a previous question has an effect on the results of one of the choices.
def game_right():
    #assining variables text that explains what the user is doing to be printed later
    text_hallway_right = 'You travel down the right hallway, soon finding the room that it ends in,\n'
    text_hallway_right += 'inside you find one of the pieces of information that you require, it\n'
    text_hallway_right += 'is behind iron bars that has a digital lock on it.\n'
    text_hallway_right += 'It seems you will have to do some mathematical equations to release the bars.\n'
    print(text_hallway_right)
    options_right_hallway = '1: Enter the mathematical equations [good option]\n'
    options_right_hallway += '2: Dont do anything\n'
    options_right_hallway += '3: Leave the enemy base [ends game]\n'
    print(options_right_hallway)
    user_right_hallway = input('What will you do?: ')
    time_until_found = 0
    while True: #creates a loop that runs until it reaches a break command via receiving correct user input
        if user_right_hallway == '1':
            if item_inventory[0] == 'Toolset':
                #code to allow user input int, store the int, and do some math with the int
                math_right_first = random.randint(2,5)
                math_right_second = random.randint(3,6)
                math_right_answer = math_right_first * math_right_second
                text_user_answer_first = 'Enter the multiplier of ' + str(math_right_first) + ' to get the product of ' + str(math_right_answer) + ': '
                user_right_first_math = input(text_user_answer_first)
                while int(user_right_first_math) != math_right_second: #creates loop until question answered correctly
                    print('Incorrect, please try again.')
                    user_right_first_math = input(text_user_answer_first)
                print('Correct answer, proceed to next question.')
                #code to allow user input float, store float and do something with the float
                math_right_hundred = random.randint(1,99)
                math_right_decimal = math_right_hundred / 100
                user_right_second_math = input('Please enter ' + str(math_right_hundred) + ' divided by 100: ')
                while float(user_right_second_math) != math_right_decimal: #creates loop until question answered correctly
                    print('Incorrect, please try again')
                    user_right_second_math = input('Please enter ' + str(math_right_hundred) + ' divided by 100: ')
                text_right_math_complete = 'Correct answer, now releasing the bars...\n'
                text_right_math_complete += 'The bars lower and you can now obtain the information inside.\n'
                text_right_math_complete += 'After you have the information you return to the fork in the hallway.\n'
                print(text_right_math_complete)
                break
            else:
                print('Wait why are you trying to do math when you can just hulk smash those bars. HULK SMASH!!')
                print('You collect the information that was inside and go back to the fork in the hallway.')
                break
        elif user_right_hallway == '2':
            if time_until_found == 2:
                print('You have been found by the patrolling guards, perhaps try something else next time')
                print('Try again\n')
                time_until_found = 0
            user_right_hallway = input('What will you do?: ')
            time_until_found += 1
        elif user_right_hallway == '3':
            print('You have failed your mission by leaving the enemy base without all the information.')
            quit()
        else:
            user_right_hallway = input('What will you do?: ')

#after the user has gone through the three rooms and completed all story this code will run, it is just some text
#stating that the mission is complete and the game has ended
def game_end():
    #when code is ran it assigns text to variables and prints, this is the last run code of the game, so it finishes here.
    text_game_end = 'You have successfully obtained all of the information from the enemy base, as you are\n'
    text_game_end += 'extracting from the base you wonder what the information is about, so you take a look...\n'
    text_game_end += '\"THE SECRET COOKIE RECIPE FORMULA\"\n'
    text_game_end += '\'bruh\' you muttered.\n'
    text_game_end += 'END OF GAME'
    print(text_game_end)

#MAIN PROGRAM
item_inventory = [] #creates list for user input
hallway_annex = ['left', 'middle', 'right'] #assigns list items to be used in program
game_start()
game_middle_fork()
game_hallway_choice()
game_hallway_choice()
game_end()