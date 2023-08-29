searchcycles = 0; grid = False; rows = 0; grid1 = False; grid2 = False; columns = 0; rowcylce = 0; rownum = 1; num = 1; columncylce = 0; pickednums = []; temptf = False; dt = 1; numofteams = 0; teammemadd = ''; temptf2 = False

import os
import json

# Files for the program
if os.name == 'nt':
    main = os.path.dirname(__file__)
    question = os.path.join(main, 'Data\\questions.json')
    gridfile = os.path.join(main, 'Data\\grid.txt')
    teamlist = os.path.join(main, 'Data\\teams.json')
    CleanScreen = 'cls'

elif os.name == 'posix':
    question = 'Data\\questions.json'
    grid = 'Data\\grid.txt'
    teamlist = 'Data\\teams.json'
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
def printteams(numofteams: int, doneteams: int | None = 1, teamlist: str | None = teamlist) -> None:
    with open(teamlist) as openfile:
        scoresnteams = json.load(openfile)
        while int(doneteams) <= int(numofteams):
            print('Team ' + scoresnteams[doneteams-1]['team'] + ': ' + scoresnteams[doneteams-1]['score'])
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
    
# Checks if an input is y or n
def yesorno(yorn: str, y: str | None = 'y', n: str | None = 'n') -> bool:
    if yorn.lower() == n:
        return False
    elif yorn.lower() == y:
        return True
    else:
        print(str(yorn) + ' Is not a accepted input, try again')
    
# Generates score file
def genscoerfile(numofteams: int | None = numofteams, teamsdone: int | None = 0, teamlist: str | None = teamlist) -> None:
    with open(teamlist, 'w') as openfile:
        openfile.write('[\n')
        while int((teamsdone+1)) < int(numofteams):
            scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","score": "0","members": []}'
            jsondata = json.loads(scoreset)
            openfile.write(json.dumps(jsondata, indent=4))
            openfile.write(',\n')
            teamsdone = teamsdone+1
        if int((teamsdone+1)) == int(numofteams):
            scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","score": "0","members": []}'
            jsondata = json.loads(scoreset)
            openfile.write(json.dumps(jsondata, indent=4))
        openfile.write('\n]')
        openfile.close()
    with open(teamlist) as f:
        data = json.load(f)
    with open(teamlist, 'w') as f:
        json.dump(data, f, indent=4)

# Addes a score to a team
def addscorejson(team: int, teamnumpicked: int, teamlist: str | None = teamlist, question: str | None = question) -> str:
    with open(teamlist) as f:
        data = json.load(f)
        with open(question, 'r') as openfile:   
            questions = json.load(openfile)
            nscore = int(data[int(team)-1]['score']) +  int(questions[int(teamnumpicked)-1]['points'])
        data[int(team)-1]['score'] = str(str(data[int(team)-1]['score']).replace(str(data[int(team)-1]['score']), str(nscore)))
    with open(teamlist, 'w') as f:
        json.dump(data, f, indent=4)

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
    temptf = False 
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
    while temptf != True:
        print('Grid is: ' + str(columns) + 'x' + str(rows))
        print('Please confirm\nenter "y" for yes\nenter "n" to enter new values')
        yorn = input('(y/n) ')
        yorntf = yesorno(yorn)
        if yorntf:
            grid = True
            temptf = True
        elif yorntf == False:
            grid1 = False
            grid2 = False
            temptf = True
            continue
        else:
            temptf = False 
    temptf = False 

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
genscoerfile(numofteams)

# Adds mebers to teams
while temptf != True:
    print('\nWould you like to add members to teams?')
    addmem = input('(y/n) ')
    temp = yesorno(addmem)
    if temp:
        while teammemadd.lower() != 'exit':
            while temptf2 != True:
                print('\nWhat team are you adding members to?')
                teammemadd = input('(int.) ')
                if teammemadd.lower() == 'exit':
                    break 
                if isint(teammemadd) and teammemadd <= numofteams:
                    temptf2 = True
                elif teammemadd > numofteams:
                    print('Value is to large, try again')
                    temptf2 = False
            temptf2 = False
            cs()
            if teammemadd.lower() != 'exit':
                #addnames(teammemadd)
        temptf = True
        cs()
    elif temp == False:
        temptf = True
    else:
        temptf = False    
temptf = False

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
    if yesorno(direction, 'a', 'd'):
        direction = 'a'
        temptf = True
    else:
        direction = 'd'
        temptf = True
temptf = False

# Defines first team
currentteam = startteam
with open(question, 'r') as openfile:
    questions = json.load(openfile)
    while int(numofquestions - len(pickednums)) > 0:
        # Resets all values
        teamnumpicked = 0; korg = ''; temptf = False; giveteam = ''; keepgive = ''; teamquescorrect = ''; prevscore = 0

        # Generates new table
        newtable(gridfile, columns, rows, pickednums)
        cs()

        # Displays avalible questions, what team is up, and asks what question that team picks
        while temptf != True:
            print('Avalible questions:')
            printtable(gridfile)
            print('\nTeam ' + str(currentteam) + ' is up!\nWhat question do they pick?')
            teamnumpicked = input('(int.) ')
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
                printteams(numofteams)
                input('\n\nPress enter to continue')
                cs()
                continue
        temptf = False
        cs()

        # Figure out if the team is keeping or giving the points
        while temptf != True:
            print('Team ' + str(currentteam) + ' picked question ' + str(teamnumpicked))
            print('\nDo they want to keep(k) or give away(g) the points?')
            korg = input('(k/g) ')
            if yesorno(korg, 'k', 'g'):
                temptf = True
                korg = True
            else:
                temptf = True
                korg = False
        temptf = False

        # If the team is giving the points, figure out to who
        if korg == False:
            while temptf != True:
                print('\nWho is team ' + str(currentteam) + ' giving the points to?')
                giveteam = input('(int.) ')
                if isint(giveteam):
                    if int(giveteam) <= int(numofteams):
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
            anwsera = questions[int(teamnumpicked)-1]['answer']
            print('\nAnswer: \n' + str(anwsera[0]))
            print('\nDid they get the question right?')
            teamquescorrect = input('(y/n) ')
            if yesorno(teamquescorrect):
                teamquescorrect = True 
                temptf = True
            else:
                teamquescorrect = False
                temptf = True
        temptf = False

        # Updates the correct team's score for either keeping or giving points
        if teamquescorrect == True and korg == True:
            addscorejson(currentteam, teamnumpicked)

        elif teamquescorrect == True and korg == False:
            addscorejson(giveteam, teamnumpicked)
 
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
printteams(numofteams)
input('Press endter to exit')