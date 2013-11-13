# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

# initialize global variables used in your code
# The secret number generated by program
g_secret_number = 0
# Upper bound of the secret number, excluded
g_upper_bound   = 100
# Lower bound of the secret number, included
g_lower_bound   = 0
# Max guess can be performed by the player
g_max_guess     = 7
# Number of guess performed by now
g_current_guess = 0

# helper function to start and restart the game
def new_game():
    global g_secret_number, g_max_guess, g_lower_bound, g_upper_bound
    g_secret_number = random.randrange(g_lower_bound, g_upper_bound)
    g_current_guess = 0
    print "\nNew Game Started, good luck ........."
    print "Secret number set to I_AM_A_SECRET_NUMBER_ (^_^)"
    print "Please guess a number between", g_lower_bound , "(include) and", g_upper_bound, "(exclude)"
    print "I will give you", g_max_guess, "chances to guess\n"
    
def set_upper(upper):
    global g_upper_bound,g_max_guess
    g_upper_bound = upper;
    if(upper == 100):
        g_max_guess = 7
    elif(upper == 1000):
        g_max_guess = 10
    print "Range set to [ 0 ," , g_upper_bound , ")"
    print "Max number of guess set to", g_max_guess
    new_game()

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    set_upper(100)
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    set_upper(1000)
    
def input_guess(guess):
    # main game logic goes here	
    global g_secret_number, g_current_guess
    guess_int = int(guess)
    print "You guessed" , guess_int
    if (guess_int == g_secret_number):
        print "Bingo, you got me!"
        print "I am truely",g_secret_number
        print "Be a very SERIOUS guess the number robert"
        print "I will give you a even more difficult test"
        print "Please be prepared for that:"
        new_game()
        return
    elif (guess_int > g_secret_number):
        print "I am actually lower than you thought"
    else:
        print "I am actually higher than you thought"            
    g_current_guess = g_current_guess + 1
    if (g_current_guess == g_max_guess):
        print "\nAll", g_max_guess , "changes has been used"
        print "But you still havn't got me :( :( :("
        print "Guess what? I'm magic", g_secret_number
        print "We will give you another try!"
        print "Please be prepared for that:"
        new_game()
    else:
        print "You still have", g_max_guess - g_current_guess, "guess chance(s) to get me\n"
    
# create frame

frame = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements
frame.add_button("Range [0, 100)", range100, 200)
frame.add_button("Range [0, 1000)", range1000, 200)
frame.add_input("Who am I?", input_guess, 75)

# call new_game and start frame
frame.start()
new_game()

# always remember to check your completed program against the grading rubric
