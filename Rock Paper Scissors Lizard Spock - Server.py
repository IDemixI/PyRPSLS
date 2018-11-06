# -*- coding: utf-8 -*-

import turtle                       # This imports the turtle module. (Was going to use with RPS)
import random                       # This imports the random module. (This is used for RPS)
import sys                          # This imports the sys module. (This is used for the test module)
import time                         # This imports the time module. (This is used for aspects of my multiplayer)
import socket                       # This imports the socket module. (This is used for aspects of my multiplayer)

showall = 0                         # This defines the global variable 'showall' and sets it to 0
player = None                       # A quick note: Global variables in python are considered bad practice.
gcount = 1                          # This defines the global variable 'gcount' and sets it to 1

dayList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']    # This is a list with 7 items (days of the week) indexed from 0 to 6

scores = {'Computer':[0,0,0]}   # This is a Dictionary with 1 'key' called computer. It's value is a list with 3 items '0,0,0' aka Wins Loses and Draws

""" Above are the imports for the modules being used throughout this assignment as well as
    a global list which will be used in several of the modules below."""


""" Below is the test function used to make sure each task of my assignment is functioning
    correctly. This is at the top as it will be used throughout the following assignment."""

def test(actual, expected):         # Test function defined with two parameters. actual and expected.

    """ Compare the actual to the expected value, and print a suitable message."""

    linenum = sys._getframe(1).f_lineno     # gets the caller’s line number.

    if (expected == actual):        # If the expected parameter matches the actual parameter then execute the following code

        msg = "Test on line {0} passed.". format(linenum)   # Uses 'format' to set {} as linenum

    else:                           # If it doesn't, then execute this code instead.

        msg = ("Test on line {0} failed. Expected ’{1}’, but got ’{2}’.". format(linenum, expected, actual))    #This uses format too but with 3 parameters.

    print(msg)                      # Prints the message, regardless of pass or fail of test.



""" First Function - Turn Clockwise using If and Elif statements.
    You can also create a similar function using a loop with a
    list containing N,E,S,W as well."""

def turn_clockwise(n):              # This is actually a messy (and not a very pythonic / efficient) way to do Question 1 but I wanted to use it as an example of nested If statements
                                    
    if n == "N" or n == "n":        # Checks to see if the parameter n is equal to n or N
        return "E"                  # If it does, it returns E
    elif n == "E" or n == "e":      # Checks to see if the parameter n is equal to e or E
        return "S"                  # If it does, it returns S
    elif n == "S" or n == "s":      # Checks to see if the parameter n is equal to s or S
        return "W"                  # If it does, it returns W
    elif n == "W" or n == "w":      # Checks to see if the parameter n is equal to w or W
        return "N"                  # If it does, it returns N
    else:                           
        return None                 # If n is none of those values it returns None.

##== Question One Answers ==##

def test_turn_clockwise():
    global showall                  # This sets the function to use the global variable 'showall'
    print("Returning Test results for Question One: " + '\n')   # A quick explaination of this is that it calls the function 'test'
    test(turn_clockwise("N"), "E")                              # with the parameter of said function it's testing and the expected
    test(turn_clockwise("W"), "N")                              # and actual outcome. There are other aspects to test too such as code
    test(turn_clockwise(42), None)                              # execution time, but I won't go into that.
    test(turn_clockwise("rubbish"), None)
    print('\n')                     # This simply leaves a new line.
    if showall == 0:                # If the global variable 'showall' is equal to 0 then execute:
        call_menu_item()            # Calls the function 'call_menu_item'


""" Second Function - Checks day_name for number then pulls day out of a list
    using a try catch/except block. If it cannot find the day in the list it
    then returns a Null value"""

def day_name(day):
    
    try:                            # Try catch statements are quite handy. This checks 'day' within the list
        return dayList[day]         # 'dayList' and if it cannot find the item within it will return None.
    except:
        return None

    
##== Question Two Answers ==##

def test_day_name():
    global showall                  # This sets the function to use the global variable 'showall'
    print("Returning Test results for Question Two: " + '\n')
    test(day_name(3), "Wednesday")
    test(day_name(6), "Saturday")
    test(day_name(42), None)
    print('\n')                     # This simply leaves a new line.
    if showall == 0:                # If the global variable 'showall' is equal to 0 then execute:
        call_menu_item()            # Calls the function 'call_menu_item'
        

""" Third Function - Checks day_num for day then pulls day out of a list
    using a try catch/except block. If it cannot find the day in the list it
    then returns a Null value. This is similar to Function 2, but it uses the
    lists index so that it can return a number rather than a string."""

def day_num(day):

    try:                            # This works exactly the same way as the other Try Catch, but
        return dayList.index(day)   # It uses the lists Index rather than the variable in the list.
    except:
        return None
    

##== Question Three Answers ==##

def test_day_num():
    global showall                  # This sets the function to use the global variable 'showall'
    print("Returning Test results for Question Three: " + '\n')
    test (day_num('Friday'), 5)
    test (day_num('Sunday'), 0)
    test (day_num(day_name(3)), 3)
    test (day_name(day_num('Thursday')), 'Thursday')
    test (day_num('Halloween'), None)
    print('\n')                     # This simply leaves a new line.
    if showall == 0:                # If the global variable 'showall' is equal to 0 then execute:
        call_menu_item()            # Calls the function 'call_menu_item'


""" Fourth (and most difficult imo) Function - This takes two variables 'today' and
    'day' with which it has to find out what day it will be 'day' amount of days from
    now. I shall explain this one a little on the lines below."""

def day_add(today = None, day = None):      # Declares the function as normal but sets the two parameters to 'None' to begin with.

    if today == None and day == None:       # This is done to see if the user has called day_add or the test. If the values are 'None' do the following:
        today = input("What day is it today? ")     # Show the user an input asking them what day today is.
        day = int(input("How many days is it until you go on holiday? "))   # Show the user an input asking them how many days until their holiday.

    t = int(day_num(today)) + int(day%7)    # This part baffled me for a while. now t is equal to the parameter 'today' once it's been ran through
    t = t%7                                 # the function 'day_num'. This is then added to the parameter 'day' but not before 'day' has had modular 
                                            # division applied to it - %7. Next, t is checked to make sure it's not 7 or it would throw us a Null
                                            # value when we run the next part. If it is equal to 7 we make it 0, because our list is 0-6 not 1-7.
        
    results = day_name(t)                   # This runs the results of 't' through the module 'day_name' giving us our final answer

    return results                          # Finally, the answer is returned and the function ends.

##== Question Four Answers ==##

def test_day_add():
    global showall                  # This sets the function to use the global variable 'showall'
    print("Returning Test results for Question Four: " + '\n')
    test(day_add("Monday",4), "Friday")
    test(day_add("Tuesday",0), "Tuesday")
    test(day_add("Tuesday",14), "Tuesday")
    test(day_add("Sunday",100), "Tuesday")
    print('\n')                     # This simply leaves a new line.
    if showall == 0:                #If the global variable 'showall' is equal to 0 then execute:
        call_menu_item()            #Calls the function 'call_menu_item'

##== Question Five Answers ==##
        
"""Question 5 works simply because the modular division can go both ways. It's done
   in such a way that the answer will be worked out correctly no matter what number
   is placed within the test case."""

def test_day_add_neg():
    global showall                  #This sets the function to use the global variable 'showall'
    print("Returning Test results for Question Five: " + '\n')
    test(day_add("Sunday", -1), "Saturday")
    test(day_add("Sunday", -7), "Sunday")
    test(day_add("Tuesday", -100), "Sunday")
    print('\n')                     #This simply leaves a new line.
    if showall == 0:                #If the global variable 'showall' is equal to 0 then execute:
        call_menu_item()            #Calls the function 'call_menu_item'


""" Fifth Function - This function simply converts hours into seconds then adds minutes, which have also been
    convered into seconds and then finally seconds to give the user the total number of seconds."""

def to_secs(hours,mins,secs):       #Function defined with 3 parameters.
    
    total = ((hours * 3600) + (mins * 60) + (secs))     #A basic sum calculated utilising parentheses.
    
    return total                    #Returns the sum of 'total'

def test_to_secs():
    global showall                  #This sets the function to use the global variable 'showall'
    print("Returning Test results for Question Six: " + '\n')
    test(to_secs(2, 30, 10), 9010)
    test(to_secs(2, 0, 0), 7200)
    test(to_secs(0, 2, 0), 120)
    test(to_secs(0, 0, 42), 42)
    test(to_secs(0, -10, 10), -590)
    print('\n')                     #This simply leaves a new line.
    if showall == 0:                #If the global variable 'showall' is equal to 0 then execute:
        call_menu_item()            #Calls the function 'call_menu_item'

def hours_in(sec):

    answer = (sec // 3600)
    
    return answer

def minutes_in(sec):

    answer = ((sec % 3600) // 60)

    return answer

def seconds_in(sec):

    answer = ((sec % 3600) % 60)
    
    return answer

def test_himisi():
    global showall                  #This sets the function to use the global variable 'showall'
    print("Returning Test results for Question Seven: " + '\n')
    test(hours_in(9010), 2)
    test(minutes_in(9010), 30)
    test(seconds_in(9010), 10)
    print('\n')                     #This simply leaves a new line.
    if showall == 0:                #If the global variable 'showall' is equal to 0 then execute:
        call_menu_item()            #Calls the function 'call_menu_item'

def compare(a,b):
    if a > b:                       #Simple function. If a is bigger than b then:
        return 1
    elif a == b:                    #If a is equal to b then:
        return 0
    elif a < b:                     #If a is smaller than b then:
        return -1
    else:                           #Some may say an else here is overkill, but it stops things
        return None                 #from breaking if someone enters something other than numbers.

def test_compare():
    global showall                  #This sets the function to use the global variable 'showall'
    print("Returning Test results for Question Eight: " + '\n')
    test(compare(5, 4), 1)
    test(compare(7, 7), 0)
    test(compare(2, 3), -1)
    test(compare(42, 1), 1)
    print('\n')                     #This simply leaves a new line.
    if showall == 0:                #If the global variable 'showall' is equal to 0 then execute:
        call_menu_item()            #Calls the function 'call_menu_item'



def rpsrules(retry = None):
    gobk = {'back':rpsls,'Back':rpsls}
    global player
    global gcount
    rules =('Scissors cut paper.','Paper covers rock.','Rock crushes lizard.','Lizard poisons Spock.','Spock smashes scissors.','Scissors decapitate lizard.','Lizard eats paper.','Paper disproves Spock.','Spock vaporizes rock.','Rock crushes scissors.')
    if retry == None or retry == 2:
        print ("Here are the rules, " + player+ "!\n")
        for item in rules:
            print(item)
        if retry == None:
            print('\nType "back" to return to the main menu.')
        else:
            print('\nType "back" to return to the game.')
    goto = input()
    if goto in gobk:
        if retry == 2:
            newrps(retry = gcount)
        else:
            gobk[goto]()
    else:
        print ("Command not recognised. Try again.\n")
        rpsrules(retry = 1)
    

def cname():
    global player
    tempplayer = player
    player = input("Enter your new name: ")
    scores[player] = scores.pop(tempplayer)
    print ('\nName successfully changed!\n\nNow returning you to the Options menu:\n')
    rpsopt(retry = 2)

def reset():
    global gcount
    for i in scores.keys():
        scores[i] = [0,0,0]
    gcount = 1
    print('The scores and game count have been reset!\n\nNow returning you to the Options menu:\n')
    rpsopt(retry = 2)

def rpsopt(retry = None):
    opsd = {'cname':cname,'reset':reset,'back':rpsls}
    opsm = ('cname - Change Name','reset - Reset Score & Game Number', 'back - Go Back')
    if retry == None:
        print("Below are the avaliable options: \n")
        for item in opsm:
            print(item)
        print('\n')
    elif retry == 2:
        for item in opsm:
            print(item)
        print('\n')
    goto = input()
    if goto in opsd:
        opsd[goto]()
    else:
        print ("Command not recognised. Try again.\n")
        rpsopt(retry = 1)

def newrps(retry = 1, c = 'Yes'):
    weapons = {'Rock':0,'rock':0,'R':0,'r':0,'Paper':1,'paper':1,'P':1,'p':1,'Scissors':2,'scissors':2,'S':2,'s':2,'Lizard':3,'lizard':3,'L':3,'l':3,'Spock':4,'spock':4,'SP':4,'sp':4}
    wepd = ('Rock','Paper','Scissors','Lizard','Spock')     #Indexed at 0,1,2,3,4 - In reference to the above dictionary
    wpr1 = {'rr':'Both Players picked Rock',
            'rp':'Paper Smothers Rock',
            'rs':'Rock Crushes Scissors',
            'rl':'Rock Crushes Lizard',
            'rsp':'Spock Vaporizes Rock',
            'pp':'Both Players picked Paper',
            'ps':'Scissors Cuts Paper',
            'pl':'Lizard Eats Paper',
            'psp':'Paper Disproves Spock',
            'ss':'Both Players picked Scissors',
            'sl':'Scissors Decapitates Lizard',
            'ssp':'Spock Melts Scissors',
            'll':'Both Players picked Lizard',
            'lsp':'Lizard Poisons Spock',
            'spsp':'Both Players picked Spock'}
    wpr2 = {'w':(player + ' Wins!'),'l':'Computer Wins!','d':"It's a Draw!",'sp':'Live Long and Prosper! (Draw)'}
    wepcount = []
    smartcpu = set(wepcount)
    global gcount
    comp = None
    
    while c == 'y' or c == 'Y' or c == 'yes' or c == 'Yes':
        if retry == 1:
            print("The game begins, " + player + "! Pick your weapon!\nRemember, you can choose from Rock, Paper, Scissors, Lizard or Spock! :")
        else:
            print('\nThis is game number ' + str(retry) + '! Type Rules for full list!\n')
        pweap = input()
        if pweap in weapons:
            fpweap = (wepd[weapons[pweap]])
            wepcount.append(str(fpweap))
            finecpu = [x for x in smartcpu if all([wepcount.count(x) >= wepcount.count(y) for y in smartcpu])]
            if not finecpu:
                pass
            else:
                g = random.randrange(0,101)
                if g > 40:                          # This is a 60% chance of taking players previous choice into consideration (so it's more spontanious)
                    if len(finecpu) > 1:            # If finecpu has two top items then:
                        h = random.randrange(0,2)   # Randomly select the index of one of them.
                        key = finecpu[h]            
                    else:
                        key = finecpu[0]            # If there is one top item, pick this one.
                        
                    if key in weapons:
                        ai = 1                      # This is set to 1 so a print statement later can determine how to display.

                        if key == wepd[0]:
                            smart = random.choice(['Paper', 'Spock'])
                        if key == wepd[1]:
                            smart = random.choice(['Scissors', 'Lizard'])
                        if key == wepd[2]:
                            smart = random.choice(['Rock', 'Spock'])
                        if key == wepd[3]:
                            smart = random.choice(['Rock', 'Scissors'])
                        if key == wepd[4]:
                            smart = random.choice(['Paper', 'Lizard'])
                            
                        comp = (wepd[weapons[smart]])

                else:
                    pass
                    
            if comp == None:                        # If by this point comp is still equal to None then
                comp = random.randrange(0,5)        # This will return 0-4
                ai = 0                              # This is set to 0 so a print statement later can determine how to display.
                
            print ('Player Choice: ' + fpweap)
            time.sleep(1)

            if ai == 0:
                print('Computer Choice: ' + wepd[comp] + '\n')
            else:
                print('Computer Choice: ' + comp + '\n')
                comp = wepd.index(comp)
                
            a = wpr1
            b = wpr2
            c = ' - '
            win = [1,0,0]
            lose = [0,1,0]
            draw = [0,0,1]
            time.sleep(2)
            if weapons[pweap] == 0:
                if comp == 0:
                    print(a['rr'] + c + b['d'])
                    scores[player] = [x + y for x, y in zip(scores[player], draw)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], draw)]
                if comp == 1:
                    print(a['rp'] + c + b['l'])
                    scores[player] = [x + y for x, y in zip(scores[player], lose)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], win)]
                if comp == 2:
                    print(a['rs'] + c + b['w'])
                    scores[player] = [x + y for x, y in zip(scores[player], win)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], lose)]
                if comp == 3:
                    print(a['rl'] + c + b['w'])
                    scores[player] = [x + y for x, y in zip(scores[player], win)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], lose)]
                if comp == 4:
                    print(a['rsp'] + c + b['l'])
                    scores[player] = [x + y for x, y in zip(scores[player], lose)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], win)]
            if weapons[pweap] == 1:
                if comp == 0:
                    print(a['rp'] + c + b['w'])
                    scores[player] = [x + y for x, y in zip(scores[player], win)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], lose)]
                if comp == 1:
                    print(a['pp'] + c + b['d'])
                    scores[player] = [x + y for x, y in zip(scores[player], draw)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], draw)]
                if comp == 2:
                    print(a['ps'] + c + b['l'])
                    scores[player] = [x + y for x, y in zip(scores[player], lose)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], win)]
                if comp == 3:
                    print(a['lp'] + c + b['l'])
                    scores[player] = [x + y for x, y in zip(scores[player], lose)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], win)]
                if comp == 4:
                    print(a['psp'] + c + b['w'])
                    scores[player] = [x + y for x, y in zip(scores[player], win)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], lose)]
            if weapons[pweap] == 2:
                if comp == 0:
                    print(a['rs'] + c + b['l'])
                    scores[player] = [x + y for x, y in zip(scores[player], lose)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], win)]
                if comp == 1:
                    print(a['ps'] + c + b['w'])
                    scores[player] = [x + y for x, y in zip(scores[player], win)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], lose)]
                if comp == 2:
                    print(a['ss'] + c + b['d'])
                    scores[player] = [x + y for x, y in zip(scores[player], draw)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], draw)]
                if comp == 3:
                    print(a['sl'] + c + b['w'])
                    scores[player] = [x + y for x, y in zip(scores[player], win)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], lose)]
                if comp == 4:
                    print(a['ssp'] + c + b['l'])
                    scores[player] = [x + y for x, y in zip(scores[player], lose)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], win)]
            if weapons[pweap] == 3:
                if comp == 0:
                    print(a['rl'] + c + b['l'])
                    scores[player] = [x + y for x, y in zip(scores[player], lose)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], win)]
                if comp == 1:
                    print(a['lp'] + c + b['w'])
                    scores[player] = [x + y for x, y in zip(scores[player], win)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], lose)]
                if comp == 2:
                    print(a['sl'] + c + b['l'])
                    scores[player] = [x + y for x, y in zip(scores[player], lose)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], win)]
                if comp == 3:
                    print(a['ll'] + c + b['d'])
                    scores[player] = [x + y for x, y in zip(scores[player], draw)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], draw)]
                if comp == 4:
                    print(a['lsp'] + c + b['w'])
                    scores[player] = [x + y for x, y in zip(scores[player], win)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], lose)]
            if weapons[pweap] == 4:
                if comp == 0:
                    print(a['rsp'] + c + b['w'])
                    scores[player] = [x + y for x, y in zip(scores[player], win)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], lose)]
                if comp == 1:
                    print(a['psp'] + c + b['l'])
                    scores[player] = [x + y for x, y in zip(scores[player], lose)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], win)]
                if comp == 2:
                    print(a['ssp'] + c + b['w'])
                    scores[player] = [x + y for x, y in zip(scores[player], win)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], lose)]
                if comp == 3:
                    print(a['lsp'] + c + b['l'])
                    scores[player] = [x + y for x, y in zip(scores[player], lose)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], win)]
                if comp == 4:
                    print(a['spsp'] + c + b['sp'])
                    scores[player] = [x + y for x, y in zip(scores[player], draw)]
                    scores['Computer'] = [x + y for x, y in zip(scores['Computer'], draw)]
            #print('\nList of Player Choices: \n')
            #for item in wepcount:
            #    print (item)
            #print("\nYou've picked " + fpweap + " " + str(wepcount.count(fpweap)) + ' times!\n')
            time.sleep(1)
            print('\n  W, L, D \n', scores[player], '\n')
            smartcpu = set(wepcount)
            retry += 1
            gcount = retry
            comp = None
            time.sleep(2)
            c = input('Would you like to play again? Yes or No: ')
        elif pweap == 'rules' or pweap == 'Rules':
            rpsrules(retry = 2)
        else:
            print("You've picked an invalid weapon type!")
            rt = input('Would you like to try again? Yes to try, No to exit: ')
            if rt == 'Yes' or rt == 'yes' or rt == 'Y' or rt == 'y':
                newrps(retry = gcount)
            elif rt == 'No' or rt == 'no' or rt == 'N' or rt == 'n':
                print('\nReturning to main game menu\n')
                rpsls()
            else:
                print('\nLearn to type, noob!\n')
                rpsls()
    gcount = retry
    print('\nReturning to the main game menu\n')
    rpsls()
    

def score(retry = None):
    gobk = {'back':rpsls,'Back':rpsls}
    if retry == None:
        print('Player  \t|\tScore - Win/Lose/Draw\n________\t|\t________\n')
        for key in scores.keys():
            print("%s       \t|\t%s" %(key, scores[key]))
        print('\nType "back" to return to the main menu.')
    goto = input()
    if goto in gobk:
        gobk[goto]()
    else:
        print ("Command not recognised. Try again.\n")
        score(retry = 1)

def rpsls(retry = None):
    global player
    rpsmenu = {'new':newrps,'New':newrps,'options':rpsopt,'Options':rpsopt,'rules':rpsrules,'Rules':rpsrules,'score':score,'Score':score,'back':main_menu_reload,'Back':main_menu_reload}
    rpsmenudes = ('New - Starts New Game', 'Options - Opens Option Menu', 'Rules - Lists the rules for Rock, Paper, Scissors, Lizard, Spock', 'Score - Shows a list of the High Scores', 'Back - Goes back to the main menu')
    if player == None:
        player = input("Welcome to Rock, Paper, Scissors, Lizard, Spock! Please enter your name: ")
        scores[player] = [0,0,0]
    if retry == None: 
        print("\nWelcome " + player + "! Pick an option: \n")
        for item in rpsmenudes:
            print(item)
        print('\n')
    main = None
    main = input()
    if main in rpsmenu:
        if main == 'new':
            rpsmenu[main](retry = gcount)
        else:
            rpsmenu[main]()       
    else:
        print ("Command not recognised. Try again.\n")
        rpsls(retry = 1)


def qall():
    global showall                  # This sets the function to use the global variable 'showall'
    showall = 1                     # Sets the global variable 'showall' to 1
    test_turn_clockwise()           # The following lines simply call all 8 Questions Answers.
    test_day_name()
    test_day_num()
    test_day_add()
    test_day_add_neg()
    test_to_secs()
    test_himisi()
    test_compare()
    showall = 0                     # Sets the global variable 'showall' back to 0 now all 8 questions modules have been loaded
    call_menu_item()                # Calls the function 'call_menu_item'


#####
# I need to make a Master Listen server which accepts connections, adds the IP to a list, then disconnects the client. #
#####

def multi(retry = None):
    
    mp = socket.socket()        # Creates a socket object.
    host = socket.gethostname() # Gets the local machine's name.
    port = 54562                # Reserve a port for your service.
    opname = None               # Opponents Name.
    global player               # Calls Global variable 'player'.
    replay = 'Yes'
    oprep = 'Yes'
    ruledef = ['Rock','Paper','Scissors']
    ruledic = {'Rock':0,'rock':0,'R':0,'r':0,'Paper':1,'paper':1,'P':1,'p':1,'Scissors':2,'scissors':2,'S':2,'s':2}
    ys = ['Yes','yes','Y','y','Yeah','yeah','Yep','yep']
    win = [1,0,0]
    lose = [0,1,0]
    draw = [0,0,1]


    if retry == None:
        print('Welcome to the multiplayer (yes, you heard correctly) segment of the game!\n\n')
    
    while player == None or player == '':
        player = input('Enter your name: ')
        if not player == None or not player == '':
            scores[player] = [0,0,0]
            
    print ('\nLooking for opponents. If none can be found, a new game will be made...')
    time.sleep(3)

    try:
        mp.connect((host, port))
        print('\nGame Found! Joining now...')
        time.sleep(2)
        c = mp
    except ConnectionRefusedError:
        mp.close()
        mp = socket.socket()
        mp.bind((host, port))        # Bind to the port
        mp.listen(5)                 # Now wait for client connection.
        print ('\nNew Game Created!')
        time.sleep(2)
        print ('Waiting for opponents...\n')
        c, addr = mp.accept()     # Establish connection with client.
        print ('Opponent found!\n')

    print ('Connection made from: ', host, 'on port:', port, '\n')
    
    while replay in ys:
        #add some code to check if the opponent also picked replay!
        while not oprep in ys:
            print(oprep)
            print ('\nYour opponent has left! Connection Closed')
            print ('Final Scores go here')
            main_menu_reload()
        try:
            oprep = None
            
            if opname == None:
                c.send(player.encode())
                opname = c.recv(1024).decode() # first message needs to be player name
                scores[opname] = [0,0,0]
                print('Your opponent is ' + opname + ', Fight!')
                time.sleep(2)

            #make it so it sends random 1-100 and higher number goes first
            print ('Players rolling (1-100) to see who goes first!\n')
            firstp = random.randrange(0,101)
            c.send(str(firstp).encode())
            firsto = c.recv(1024).decode()

            time.sleep(2)
            
            a = int(firstp)
            b = int(firsto)

            if a < b:
                print(opname + ' (' + str(b) + ') ' + 'rolled higher than ' + player + ' (' + str(a) + ')! ' + opname + ' gets to pick first!')
                print ('\nWaiting for opponent...\n')
                opweap = c.recv(1024).decode()
                print (opname + " has picked! Now it's your turn!\n")
                pweap = input('Pick a weapon, ' + player + '!\n' + player + ' Weapon: ')
                print('\n')
                
                while not pweap in ruledic:
                    pweap = input('\n' + pweap + ' is not a valid weapon.\nPick again: ')
                    
                fpweap = str(ruledef[ruledic[pweap]])
                c.send(fpweap.encode())
                    
            elif a > b:
                print(player + ' (' + str(a) + ') ' + 'rolled higher than ' + opname + ' (' + str(b) + ')! ' + player + ' gets to pick first!')
                pweap = input('\nPick a weapon, ' + player + '!\n' + player + ' Weapon: ')
                
                while not pweap in ruledic:
                    pweap = input(pweap + ' is not a valid weapon , pick again: ')
                    
                fpweap = str(ruledef[ruledic[pweap]])
                c.send(fpweap.encode())
                    
                print ("\nYou've picked! Now it's " + opname + "'s turn!\n")
                print ('Waiting for opponent...')
                opweap = c.recv(1024).decode()
            else:
                # They rolled the same number out of 100 -_- what are the chances eh? tell 'em to re-roll.
                print('Need to roll again')

            
            #Game rules - what beats what goes here!
            pwin = str('You' + ' win the game! well done!')
            plose = str(opname + ' wins the game! bad luck!')
            
            # Local Player - Rock #    
            if fpweap == 'Rock' and opweap == 'Rock':
                print ("\nIt's a draw! both players picked", fpweap)
                scores[player] = [x + y for x, y in zip(scores[player], draw)]
                scores[opname] = [x + y for x, y in zip(scores[opname], draw)]
                
            if fpweap == 'Rock' and opweap == 'Paper':
                print ('\n' + opname + "'s " + opweap + ' smothers ' + 'your ' + fpweap + '!')
                print (plose)
                scores[player] = [x + y for x, y in zip(scores[player], lose)]
                scores[opname] = [x + y for x, y in zip(scores[opname], win)]
                
            if fpweap == 'Rock' and opweap == 'Scissors':
                print ('\nYour ' + fpweap + ' crushes ' + opname + "'s " + opweap + '!')
                print (pwin)
                scores[player] = [x + y for x, y in zip(scores[player], win)]
                scores[opname] = [x + y for x, y in zip(scores[opname], lose)]
                
            # Local Player - Paper #    
            if fpweap == 'Paper' and opweap == 'Rock':
                print ('\nYour ' + fpweap + ' smothers ' + opname + "'s " + opweap + '!')
                print (pwin)
                scores[player] = [x + y for x, y in zip(scores[player], win)]
                scores[opname] = [x + y for x, y in zip(scores[opname], lose)]
                
            if fpweap == 'Paper' and opweap == 'Paper':
                print ("\nIt's a draw! both players picked", fpweap)
                scores[player] = [x + y for x, y in zip(scores[player], draw)]
                scores[opname] = [x + y for x, y in zip(scores[opname], draw)]
                
            if fpweap == 'Paper' and opweap == 'Scissors':
                print ('\n' + opname + "'s " + opweap + ' cuts ' + 'your ' + fpweap + '!')
                print (plose)
                scores[player] = [x + y for x, y in zip(scores[player], lose)]
                scores[opname] = [x + y for x, y in zip(scores[opname], win)]
                
            # Local Player - Scissors #    
            if fpweap == 'Scissors' and opweap == 'Rock':
                print ('\n' + opname + "'s " + opweap + ' crushes ' + 'your ' + fpweap + '!')
                print (plose)
                scores[player] = [x + y for x, y in zip(scores[player], lose)]
                scores[opname] = [x + y for x, y in zip(scores[opname], win)]
                
            if fpweap == 'Scissors' and opweap == 'Paper':
                print ('\nYour ' + fpweap + ' cuts ' + opname + "'s " + opweap + '!')
                print (pwin)
                scores[player] = [x + y for x, y in zip(scores[player], win)]
                scores[opname] = [x + y for x, y in zip(scores[opname], lose)]
                
            if fpweap == 'Scissors' and opweap == 'Scissors':
                print ("\nIt's a draw! both players picked", fpweap)
                scores[player] = [x + y for x, y in zip(scores[player], draw)]
                scores[opname] = [x + y for x, y in zip(scores[opname], draw)]
                
            replay = input('\nWould you like to play again? Yes or No : ')
            c.send(replay.encode())
            oprep = c.recv(1024).decode()
            time.sleep(2)
            
        except:
            print('The connection has been lost\n')
            c.close()
            main_menu_reload()
            # Close the connection
            
    print ('\nConnection Closed - Game Over\n')
    print (player + ' won ' + str(scores[player][0]) + ' games!')
    print (opname + ' won ' + str(scores[opname][0]) + ' games!\n')
    main_menu_reload()


def about():
    print('Programmed and designed by: \n')
    print("________                 .__        \n\______ \   ____   _____ |__|__  ___\n |    |  \_/ __ \ /     \|  \  \/  /\n |    `   \  ___/|  Y Y  \  |>    < \n/_______  /\___  >__|_|  /__/__/\_ \ \n       \/     \/      \/         \/\n\n")
    time.sleep(2)
    call_menu_item()

def main_menu_reload():
    print('Below is a list of items, type "help" to refresh the list' + '\n' + '\n')
    for k, d in zip(sorted(menu.keys()), mendef):       #using parameters k (for menu) and d (for mendef) execute the zip function, and sort 'menu' while it's at it.
        print(k + ' - ' + d)        #Print k and d - k being key and d being definition.
    print('\n')                     #This simply leaves a new line.
    call_menu_item()                #Calls the function 'call_menu_item'


def call_menu_item():               
    main = input()                  #Defines the local variable main and makes it a user input.
    if main in menu:                #If the users input aka main is within the dictionary 'menu' then:
        menu[main]()                #This pulls up a list of all items in the dictionary.
    elif main in menulc:            #This does the same thing but simply checks the lower case dictionary.
        menulc[main]()
    else:
        print ("Command not recognised. See 'help' for list.")
        call_menu_item()


menu = {'Q1':test_turn_clockwise,'Q2':test_day_name,'Q3':test_day_num,'Q4':test_day_add,'Q5':test_day_add_neg,'Q6':test_to_secs,'Q7':test_himisi,'Q8':test_compare,'Qall':qall,'RPS':rpsls,'exit': exit,'help':main_menu_reload}
menulc = {'q1':test_turn_clockwise,'q2':test_day_name,'q3':test_day_num,'q4':test_day_add,'q5':test_day_add_neg,'q6':test_to_secs,'q7':test_himisi,'q8':test_compare,'qall':qall,'rps':rpsls,'Exit': exit,'Help':main_menu_reload,'about':about,'multi':multi}
mendef = ['Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6', 'Question 7', 'Question 8', 'All Questions', 'Rock, Paper, Scissors, Lizard, Spock','Exit Application','Help Menu']

if __name__ == "__main__":          #This is called when the python file is executed. Like "main" in many other languages.
    
    print ("Welcome to Ryan Saunders's Python Assignment")
    input ('Press Enter to continue...\n')   #Please note: When opening the file alone, it will not work correctly unless you use raw_input, while idle is funny and dislikes raw_input!
    main_menu_reload()              #Calls the function 'main_menu_reload'


