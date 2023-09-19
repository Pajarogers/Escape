# Paja Rogers
#Course: CSC373
# Assignment: Your second application


# function to call the title of the program
def display_title_sceen():
    print("\n\n\n              ***** Escape Apartment 313 *****\n")

# function for the game rules


def rules_to_game():
    # game rules
    rules = ("""\n  You have to escape from apartment 313 before the time runs out! 
             \n  You only have 60 minutes to escape or will be locked in for ever.
             \n  Find the Clues to find the key to unlocked the door. """)
    print(rules)

    # function for user name


def get_user_name():
    user_name = input(" What is your name?")
    return user_name

# function passing an argument


def welcome_message(user_name):
    print(" Hi " + user_name)

# introduction to the program


def introduction():
    print("""\n\n           You was just told by your supervisor 'Mary' to go to apartment 313 and do a checklist on the apartment. 
          \n She have 3 appointments in the morning to show the apartment layout starting @ 8 am. 313 is only used for to show the 1 bedroom apartment layout.
          \n You only been working there now for 1 month and you have heard the horrors about 313. Anyone that goes up there after office hours never return 
          \n or quite. It only should take about 10 you though. You grab your work bag that includes:
          \n Pen - pocket flashlight - your phone - box cutter - 3 paper clips - radio - bag of chips and 1/2 of sandwich from lunch.
          \n It is now 4:35 pm and the office close @ 5 you go to the elevator and it on the 12 floor. So decide to take the stairs
          \n You jsut made to the door of the apartment. You look at your phone and it is now 4:45. You hear a voice it's Mr.Smug.
          \n Can you help me please? It will only take a minutes. You turn around and asked...What can I help you with Mrs.Smug?
          \n Can you help me bring my bags in and put them on the counter. She open the door and you grab 2 bags and then return to grab the other 2.
          \n As you was walking away she said put these in the top cabinet for me I can not reach it. You put the floor in the cabinet and turn to leave. 
          \n Before you please help me change the light bub in my room maintanence will be able to do it until tomorrow. Finally you done and you leave. 
          \n You walk to 313 put the key in and turned the lock. As you walked in the door you turned around and looked at the clock on the hall wall and it
          \n is now 5 pm... The door close.\n""")


# function for game
def game():

    # user choice
    print("""\n      It's pitch black and you cant see your can't see you hand in front of you and you hear a voice 'YOU ONLY HAVE 60 MINUTES!!!' 
        \n What will you do?
        \n (1) Call for help on the radio                     (2) Scam until someone hear you 
        \n (3) Beat on the door until someone open it         (4) Look for the light switch?""")

    user_choice = input(" Please enter your choice..\n")
    user_input = int(user_choice)
    user_time = 60

    if user_input == 1:
        print("**** Help can someone hear me? A very lite voice said go to the open the window for light. Just walk straight ahead. Don't turn around keep walking")
        print(" You remember you had a pocket flashlight. As you turn it on your hands begin to shake and you moved turn the window ")

    elif user_input == 2:
        print(" \n Bad choice you been scamming now for 10 minutes\n")
        user_time = user_time - 10
        print("Time left:")
        print(user_time)

    elif user_input == 3:
        print("No one can hear you! You wasted 20 minutes!")
        user_time = user_time - 20
        print("Time left:")
        print(user_time)
    elif user_input == 4:
        print("\n No light switch. -10 minutes")
        user_time = user_time - 10
        print("Time left:")
        print(user_time)

# 2nd part of the game


def apartment_game():
    # user choice
    print("\n You open the window. \n All minutes has been restored back to 60 minutes. \n What room will you look for the key?\n")
    print("""  What item will you Choose? 
        \n (1) bedroom                  (2) living room
        \n (3) kitchen                  (4) bathroom""")
    user_choice = input(" Please enter your choice..\n")
    user_input = int(user_choice)
    user_time = 60
    # if statement if the player choose the wrong item
    if user_input == 1:
        print(" You enter the bedroom and the door close you now locked in...")
        print("You remember that you have a paper clip and picked the locked.")
        print("You are now back in the main room.\n\n\n")

    elif user_input == 2:
        print(" \n You are trying to walk toard the table but you can't move your feet. You are sinking into the floor. \n")
        print(" It is a sinkhole.")
        user_time = user_time - 60
        print("Time left:")
        print(user_time)
        print("Game Over!!!\n\n\n")
    elif user_input == 3:
        print("You walk in the kitchen and see a Mrs.Snug. What are you doing here? She replied I am the key master!")
        print(" Can you help me get out! Only if you can solve the riddle.\n I am in the kitchen standing at the refrigerator.   What am I? ")
        print(" You think about it and 'Hungry' then you take out the bag of chip and 1/2 sandwich and give it to her.")
        print(" She hands you the key! Finally you can leave.")
        print(" You open the door to leave and as you walk out you look at the clock in the halway it is now 4:59 pm\n\n\n")
    elif user_input == 4:
        print("\n No it a black hole and you can never return!")
        print("Game Over!\n\n\n")


# main function
# call of function
def main():
    display_title_sceen()
    user_name = get_user_name()
    welcome_message(user_name)
    rules_to_game()
    introduction()
    game()
    apartment_game()


# start of program
if __name__ == "__main__":
    main()
