searchcycles = 0; grid = False; rows = 0; grid1 = False; grid2 = False; columns = 0; rowcylce = 0; rownum = 1; num = 1; columncylce = 0; pickednums = []; temptf = False; dt = 1

import os
import json

# Files for the program
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

else:
    print('OS Not supported')
    exit()

# Clearscreen
def cs() -> None:
    os.system(CleanScreen)

# Generates a new table of questions
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

# Prints current table
def printtable(gridfile: str) -> None:
    with open(gridfile, 'r') as openfile:
        openfile.seek(0)
        print(openfile.read())

# Prints current lits of teams and scores
def printteams(teaminfo: str, numofteams: int, doneteams: int | None = 1) -> None:
    while int(doneteams) <= int(numofteams):
        with open(str(teaminfo) + 'team' +str(doneteams) + '.txt', 'r') as openfile:
            print('Team ' + str(doneteams) + ': ' + str(openfile.read()))
        doneteams = doneteams + 1

# Checks if a number is and integer
def isint(number: any) -> bool:
    flag = True
    try:
        int(number)
    except ValueError:
        flag = False

    if flag:
        return True
    else:
        print('That is not a integer, try again')
        return False
    
# Addes a score to a team    
def addscore(team: int, teamnumpicked: int, addpoints: int | None = 0, teaminfo: str | None = teaminfo, question: str | None = question, prevscore = 0, newscore = 0, ) -> None:
    with open(question, 'r') as openfile:   
        questions = json.load(openfile)
        with open(str(teaminfo) + 'team' + str(team) + '.txt', 'r') as openfile:
            prevscore = openfile.read()
            openfile.close()
        if teamnumpicked != 'add':
            newscore = int(prevscore) + int(questions[int(teamnumpicked)-1]['points'])
        else:
            newscore = addpoints

        with open(str(teaminfo) + 'team' + str(team) + '.txt', 'w') as openfile:
            openfile.write(str(newscore))
            openfile.close()
        openfile.close()

# Figures out how many questions there are
with open(question, 'r') as openfile:
    sol = json.load(openfile)
    while sol[searchcycles]['question#'] != 'done':
        searchcycles = searchcycles + 1
    numofquestions = searchcycles
    openfile.close

cs()

print('Number of questions: ' + str(numofquestions))

# Has the user make a grid
while grid != True:
    while grid1 != True:
        print('How many rows do you want?')
        row = input('(int.) ')
        if isint(row):
            rows = row
            grid1 = True
        else:
            continue

    while grid2 != True:
        print('How many columns do you want?')
        column = input('(int.) ')
        if isint(column):
            columns = column
            grid2 = True
        else:
            continue

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

    # Has user confirm grid
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

# Generates first table
newtable(gridfile, columns, rows, pickednums)

# Prints first table
printtable(gridfile)

# Prints how many questions remain
print(str(numofquestions - len(pickednums)) + ' Questions Remain')

# Figure out how many teams are playing
while temptf != True:
    print('\nHow many teams are playing?')
    numofteams = input('(int.) ')
    if isint(numofteams):
        temptf = True
temptf = False

# Generate a score file for each team
while int(dt) <= int(numofteams):
    with open(str(teaminfo) + 'team' +str(dt) + '.txt', 'w') as openfile:
        openfile.write('0')
        openfile.close()
    dt = dt + 1

# Figure out the starting team
while temptf != True:
    print('\nWhat team will be starting?')
    startteam = input('(int.) ')
    if isint(startteam):
        temptf = True
temptf = False

# Figure out direction
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

# Defines first team
currentteam = startteam
with open(question, 'r') as openfile:   
    questions = json.load(openfile)

    while int(numofquestions - len(pickednums)) > 0:
        # Resets all values
        teamnumpicked = 0; korg = ''; temptf = False; giveteam = ''; keepgive = ''; prevscore = 0; override = False; useranwser = ''; anwsera = []
        teampointsadd = 0; teampointsaddnum = 0; temptf2 = False

        # Generates new table
        newtable(gridfile, columns, rows, pickednums)
        cs()

        # Displays avalible questions, what team is up, and asks what question that team picks
        while temptf != True:
            print('Avalible questions:')
            printtable(gridfile)
            print('\nTeam ' + str(currentteam) + ' is up!\nWhat question do you pick?')
            teamnumpicked = input('(int.) ')
            if teamnumpicked.lower() != 'madd':
                if teamnumpicked.lower() != 'score':
                    if isint(teamnumpicked):
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
                    # Prints all team's scores 
                    printteams(teaminfo, numofteams)
                    input('\n\nPress enter to continue')
                    cs()
                    continue
            else:
                cs()
                # Manully adding points 
                while temptf2 != True:
                    print('What team are we adding points to?')
                    teampointsadd = input('(int.) ')
                    if isint(teampointsadd):
                        if int(teampointsadd) <= int(numofteams) and int(teampointsadd) > 0:
                            temptf2 = True
                            teampointsadd = int(teampointsadd)
                        else:
                            print('That it not a team, try again')
                            temptf2 = False
                temptf2 = False
                cs()

                while temptf2 != True:
                    print('How many points are we adding or removing?')
                    teampointsaddnum = input('(int.) ')
                    if isint(teampointsaddnum) == True:
                        addscore(teampointsadd, 'add', int(teampointsaddnum))
                        temptf2 = True
                continue
        temptf = False
        cs()

        # Figure out if the team is keeping or giving the points
        while temptf != True:
            print('Team ' + str(currentteam) + ' picked question ' + str(teamnumpicked))
            print('\nDo you want to keep(k) or give away(g) the points?')
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

        # If the team is giving the points, figure out to who
        if korg == False:
            while temptf != True:
                print('\nWho is team ' + str(currentteam) + ' giving the points to?')
                giveteam = input('(int.) ')
                if isint(giveteam):
                    if giveteam <= numofteams:
                        temptf = True
                    else:
                        print('That is not a team, try again')
                        temptf = False
            temptf = False

        # Generates text for keeping and giving
        if korg == True:
            keepgive = 'keeping the points'
        if korg == False:
            keepgive = 'giving the points to ' + str(giveteam)
        cs()

        # Displays question, team number, keeping or giving points, and anwser to the question, then asks the user if
        # the team got the question right
        while temptf != True:
            print('Team ' + str(currentteam) + ' picked question ' + str(teamnumpicked) + ' - And are ' + str(keepgive))
            print('\n\nQuestion: \n' + str(questions[int(teamnumpicked)-1]['question']))
            useranwser = input('(anw.) ')
            anwsera = questions[int(teamnumpicked)-1]['answer'] 
            if useranwser.lower() in anwsera:
                useranwser = True 
                temptf = True
            elif useranwser.lower() not in anwsera:
                useranwser = False
                temptf = True
            else:
                print('That is not a acceptable input, try again')
                temptf = False
        temptf = False

        # Updates the correct team's score for either keeping or giving points
        if useranwser == True and korg == True:
            addscore(currentteam, teamnumpicked)

        elif useranwser == True and korg == False:
            addscore(giveteam, teamnumpicked)

        # Remove the question from the table
        pickednums.append(int(teamnumpicked))

        # Figure out the next team
        if direction == 'a':
            if int(currentteam) != int(numofteams):
                currentteam = int(currentteam) + 1
            elif int(currentteam) == int(numofteams):
                currentteam = 1
        elif direction == 'd':
            if int(currentteam) != 1:
                currentteam = int(currentteam) - 1
            elif int(currentteam) == 1:
                currentteam = int(numofteams)
                
# Display fianl scores
cs()
print('Endgame!\nCurrent scores are:')
printteams(teaminfo, numofteams)
input('Press endter to exit')