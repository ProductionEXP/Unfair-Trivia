# Defults for all vars
searchcycles = 0; grid = False; rows = 0; grid1 = False; grid2 = False; columns = 0; rowcylce = 0; rownum = 1; num = 1; columncylce = 0; pickednums = []; temptf = False; dt = 1

# Imports
import os
import json

# Auto Path and clearscreen assainment
if os.name == 'nt':
    main = os.path.dirname(__file__)
    question = os.path.join(main, 'Data\\questions.json')
    gridfile = os.path.join(main, 'Data\\grid.txt')
    teaminfo = os.path.join(main, 'Data\\teaminfo\\')
    CleanScreen = 'cls'

elif os.name == 'posix':
    question = 'Data\\questions.json'
    grid = 'Data\\grid.txt'
    teaminfo = 'Data\\teaminfo\\'
    CleanScreen = 'clear'

# It should never get to this else loop, but if it some how does we exit so the program does not crash mid use
else:
    print('OS Not supported')
    exit()

# Function to clear the screen
def cs() -> None:
    os.system(CleanScreen)

# Function to generate a new table without the numbers that have already been selected
def newtable(gridfile: str, columns: int, rows: int, pickednums: list | None = [], rowcylce: int | None = 0, columncylce: int | None = 0, num: int | None = 1) -> None:
    with open(gridfile, 'w') as openfile:
        while int(rowcylce) < int(columns):
            while int(columncylce) < int(rows):
                if int(num) not in pickednums:
                    openfile.writelines(str(num) + '   ')
                num = num + 1
                columncylce = columncylce + 1
            rowcylce = rowcylce + 1
            columncylce = 0
            openfile.writelines('\n')
        openfile.close
    
# Determins how many questions reamin to be picked
def numofquestionsremain(numofquestions: int, pickednums: list | None = []) -> int:
    return numofquestions - len(pickednums) 

# Prints the latest version of the table 
def printtable(gridfile: str) -> None:
    with open(gridfile, 'r') as openfile:
        openfile.seek(0)
        print(openfile.read())

# Prints all of the teams scores
def printteams(teaminfo: str, numofteams: int, doneteams: int | None = 1) -> None:
    while int(doneteams) <= int(numofteams):
        with open(str(teaminfo) + 'team' +str(doneteams) + '.txt', 'r') as openfile:
            print('Team ' + str(doneteams) + ': ' + str(openfile.read()))
        doneteams = doneteams + 1
    
cs()    

# Figures out how many questions we have
with open(question, 'r') as openfile:
    sol = json.load(openfile)
    while sol[searchcycles]['question#'] != 'done':
        searchcycles = searchcycles + 1
    numofquestions = searchcycles
    openfile.close

cs()

# Tells the user how many questions there is
print('Number of questions: ' + str(numofquestions))

# Has the user make a grid for the number of questions
while grid != True:
    # Has the user enter rows, and checks if it is a number
    while grid1 != True:
        print('How many rows do you want?')
        row = input('(int.) ')
        if row.isnumeric():
            rows = row
            grid1 = True
        else:
            print('That is not a number or is not an int., try again')
            continue

    # Has the user enter columns, and checks if it is a number
    while grid2 != True:
        print('How many columns do you want?')
        column = input('(int.) ')
        if column.isnumeric():
            columns = column
            grid2 = True
        else:
            print('That is not a number or is not an int., try again')
            continue

    # After the user has entered both rows and columns we multiply them 
    # To find out if the table would be to large or to small for the 
    # Number or questions
    if int(columns)*int(rows) > numofquestions:
        print('Grid is to large, try again')
        grid1 = False
        grid2 = False 
        continue

    elif int(columns)*int(rows) < numofquestions:
        print('Grid is to small, try again')
        grid1 = False
        grid2 = False 
        continue

    # Tells the user the size of the grid and has them confirm the 
    # Size or reenter the dimentions
    print('Grid is: ' + str(columns) + 'x' + str(rows))
    print('Please confirm\nenter "y" for yes\nenter "n" to enter new values')
    yorn = input('(y/n) ')

    if yorn.lower() == 'n':
        grid1 = False
        grid2 = False 
        continue
    elif yorn.lower() == 'y':
        grid = True
    else:
        print(str(yorn) + ' Is not a accepted value, try again')

cs()

# Generates the first table 
newtable(gridfile, columns, rows, pickednums)

# Prints that table for the user to see
printtable(gridfile)

# Prints to the user the number of remaining questions
print(str(numofquestionsremain(numofquestions, pickednums)) + ' Questions Remain')

# Has the user enter how many teams are playing and checks 
# If it is a int.
while temptf != True:
    print('\nHow many teams are playing?')
    numofteams = input('(int.) ')
    if numofteams.isnumeric():
        temptf = True
    else:
        print('That is not a number, try again')
        temptf = False
temptf = False

# Generates all the teams score text (.txt) files
while int(dt) <= int(numofteams):
    with open(str(teaminfo) + 'team' +str(dt) + '.txt', 'w') as openfile:
        openfile.write('0')
        openfile.close()
    dt = dt + 1

# Asks the user what team will start the game
# And checks if it is a int. and is a team
# that is playing
while temptf != True:
    print('\nWhat team will be starting?')
    startteam = input('(int.) ')
    if startteam.isnumeric():
        temptf = True
    else:
        print('That is not a number, try again')
        temptf = False
temptf = False

# Figures out the direction (order) of the teams
# Asks the user for a direction then checks if
# It is a supported anwser
while temptf != True:
    print('\nWhat direction are we going in?\nAscending(a), Ex. 1 > 2\nDescending(d), Ex. 2 > 1')
    direction = input('(a/d) ')
    if direction.lower() == 'a':
        direction = 'a'
        temptf = True
    elif direction.lower() == 'd':
        direction = 'd'
        temptf = True
    else:
        print('That is not a acceptable input, try again')
        temptf = False
temptf = False

# Defines the first team
currentteam = startteam
with open(question, 'r') as openfile:
    questions = json.load(openfile)

    # Starts a loop around all of the teams untill there are no questions left
    while int(numofquestionsremain(numofquestions, pickednums)) > 0:

        # Resets the values, we dont need to do this 
        # Just an extra layer of protection
        teamnumpicked = 0; korg = ''; temptf = False; giveteam = ''; keepgive = ''; teamquescorrect = ''; prevscore = 0

        # Generates a new table after every cycle 
        # to remove the last question picked
        newtable(gridfile, columns, rows, pickednums)
        cs()

        # Displays the avalible questions and what team
        # Is up to pick, then asks for the question that
        # They pick, the checks that that question has 
        # Not been picked yet and is a number and is
        # A question that exists, if the user enters
        # Score vs a number it will display the current
        # Scores of all of the teams then it will restart
        # That teams turn
        while temptf != True:
            print('Avalible questions:')
            printtable(gridfile)
            print('\nTeam ' + str(currentteam) + ' is up!\nWhat question do they pick?')
            teamnumpicked = input('(int.) ')
            if teamnumpicked.lower() != 'score':
                if teamnumpicked.isnumeric():
                    if int(teamnumpicked) <= int(numofquestions):
                        if int(teamnumpicked) not in pickednums:
                            teamnumpicked = teamnumpicked
                            temptf = True
                        else:
                            print('Number was already picked, try again')
                            temptf = False
                    else:
                        print('Question does not exist, try again')
                        temptf = False
                else:
                    print('That is not a number, try again')
                    temptf = False
            else:
                printteams(teaminfo, numofteams)
                input('\n\nPress enter to continue')
                cs()
                continue
        temptf = False
        cs()

        # After we have the question that the team 
        # Picked we need to figure out if they are
        # Going to keep or give the points, we ask
        # The user for an input and then check to 
        # Make sure the input is acceptable
        while temptf != True:
            print('Team ' + str(currentteam) + ' picked question ' + str(teamnumpicked))
            print('\nDo they want to keep(k) or give away(g) the points?')
            korg = input('(k/g) ')
            if korg.lower() == 'k':
                temptf = True
                korg = True
            elif korg.lower() == 'g':
                temptf = True
                korg = False
            else:
                print('That is not a acceptable input, try again')
                temptf = False
        temptf = False

        # If the team is giveing the points away we
        # Need to find out what team they are giving
        # The points to, we ask the user for an input
        # And then we check to make sure that the input
        # is a number and is a team
        if korg == False:
            while temptf != True:
                print('\nWho is team ' + str(currentteam) + ' giving the points to?')
                giveteam = input('(int.) ')
                if giveteam.isnumeric():
                    if giveteam <= numofteams:
                        temptf = True
                    else:
                        print('That is not a team, try again')
                        temptf = False
                else:
                    print('That is not a number, try again')
                    temptf = False
            temptf = False

        # Generating the text for if they are giving the
        # Points and to who or if they are just keeping 
        # the points
        if korg == True:
            keepgive = 'keeping the points'
        if korg == False:
            keepgive = 'giving the points to ' + str(giveteam)
        cs()

        # After the team has picked the question and has determined
        # If they are keeping or giving the points we show the user
        # What team is up, What question they picked, if they are 
        # Keeping or giving the points, and to who, the question,
        # And the anwser to the question, then we ask the user,
        # If they got the question right or wrong, then we check
        # The user's input to make sure it is an acceptable input
        while temptf != True:
            print('Team ' + str(currentteam) + ' picked question ' + str(teamnumpicked) + ' - And are ' + str(keepgive))
            print('\n\nQuestion: \n' + str(questions[int(teamnumpicked)-1]['question']))
            print('\nAnswer: \n' + str(questions[int(teamnumpicked)-1]['answer']))
            print('\nDid they get the question right?')
            teamquescorrect = input('(y/n) ')
            if teamquescorrect.lower() == 'y':
                teamquescorrect = True 
                temptf = True
            elif teamquescorrect.lower() == 'n':
                teamquescorrect = False
                temptf = True
            else:
                print('That is not a acceptable input, try again')
                temptf = False
        temptf = False

        # After the team has anwsered and we know if they got it right or 
        # Wrong we have to get their old score and add it to the ammount 
        # Of points they lost or gained
        if teamquescorrect == True and korg == True:
            with open(str(teaminfo) + 'team' + str(currentteam) + '.txt', 'r') as openfile:
                prevscore = openfile.read()
                openfile.close()
            newscore = int(prevscore) + int(questions[int(teamnumpicked)-1]['points'])

            with open(str(teaminfo) + 'team' + str(currentteam) + '.txt', 'w') as openfile:
                openfile.write(str(newscore))
                openfile.close()

        # If they got the question right but they chose to give the points
        # Away we must now add the points lost or earned to the team that 
        # Was gifted the points
        elif teamquescorrect == True and korg == False:
            with open(str(teaminfo) + 'team' + str(giveteam) + '.txt', 'r') as openfile:
                prevscore = openfile.read()
                openfile.close()
            newscore = int(prevscore) + int(questions[int(teamnumpicked)-1]['points'])

            with open(str(teaminfo) + 'team' + str(giveteam) + '.txt', 'w') as openfile:
                openfile.write(str(newscore))
                openfile.close()
        
        # Affter we have added scores (or not) we must add the question
        # that was picked to the list of pickednums to then regnerate 
        # The table with out that question and to prevent others from
        # Picking that question again
        pickednums.append(int(teamnumpicked))

        # After we have added the question to the list of pickednums
        # We have to select the next team based off of the direction 
        # Picked earlier, we also must make sure that the next team
        # Exsits
        if direction == 'a':
            if int(currentteam) != numofteams:
                currentteam = int(currentteam) + 1
            elif int(currentteam) == numofteams:
                currentteam = 1
        elif direction == 'd':
            if int(currentteam) != 1:
                currentteam = int(currentteam) - 1
            elif int(currentteam) == 1:
                currentteam = numofteams

# After all of the questions have been picked we must
# Display all of the teams scores before the program ends
cs()
print('Endgame!\nCurrent scores are:')
printteams(teaminfo, numofteams)