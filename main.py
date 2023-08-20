searchcycles = 0; grid = False; rows = 0; grid1 = False; grid2 = False; columns = 0; rowcylce = 0; rownum = 1; num = 1; columncylce = 0; pickednums = []; temptf = False; dt = 1

import os
import json

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

def cs() -> None:
    os.system(CleanScreen)

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
    
def numofquestionsremain(numofquestions: int, pickednums: list | None = []) -> int:
    return numofquestions - len(pickednums) 

def printtable(gridfile: str) -> None:
    with open(gridfile, 'r') as openfile:
        openfile.seek(0)
        print(openfile.read())

def printteams(teaminfo: str, numofteams: int, doneteams: int | None = 1) -> None:
    while int(doneteams) <= int(numofteams):
        with open(str(teaminfo) + 'team' +str(doneteams) + '.txt', 'r') as openfile:
            print('Team ' + str(doneteams) + ': ' + str(openfile.read()))
        doneteams = doneteams + 1
    
cs()    

with open(question, 'r') as openfile:
    sol = json.load(openfile)
    while sol[searchcycles]['question#'] != 'done':
        searchcycles = searchcycles + 1
    numofquestions = searchcycles
    openfile.close

cs()

print('Number of questions: ' + str(numofquestions))

while grid != True:
    while grid1 != True:
        print('How many rows do you want?')
        row = input('(int.) ')
        if row.isnumeric():
            rows = row
            grid1 = True
        else:
            print('That is not a number or is not an int., try again')
            continue

    while grid2 != True:
        print('How many columns do you want?')
        column = input('(int.) ')
        if column.isnumeric():
            columns = column
            grid2 = True
        else:
            print('That is not a number or is not an int., try again')
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

newtable(gridfile, columns, rows, pickednums)

printtable(gridfile)

print(str(numofquestionsremain(numofquestions, pickednums)) + ' Questions Remain')

while temptf != True:
    print('\nHow many teams are playing?')
    numofteams = input('(int.) ')
    if numofteams.isnumeric():
        temptf = True
    else:
        print('That is not a number, try again')
        temptf = False
temptf = False

while int(dt) <= int(numofteams):
    with open(str(teaminfo) + 'team' +str(dt) + '.txt', 'w') as openfile:
        openfile.write('0')
        openfile.close()
    dt = dt + 1

while temptf != True:
    print('\nWhat team will be starting?')
    startteam = input('(int.) ')
    if startteam.isnumeric():
        temptf = True
    else:
        print('That is not a number, try again')
        temptf = False
temptf = False

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

currentteam = startteam
with open(question, 'r') as openfile:
    questions = json.load(openfile)
    while int(numofquestionsremain(numofquestions, pickednums)) > 0:
        teamnumpicked = 0; korg = ''; temptf = False; giveteam = ''; keepgive = ''; teamquescorrect = ''; prevscore = 0
        newtable(gridfile, columns, rows, pickednums)
        cs()

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

        if korg == True:
            keepgive = 'keeping the points'
        if korg == False:
            keepgive = 'giving the points to ' + str(giveteam)

        cs()
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

        if teamquescorrect == True and korg == True:
            with open(str(teaminfo) + 'team' + str(currentteam) + '.txt', 'r') as openfile:
                prevscore = openfile.read()
                openfile.close()
            newscore = int(prevscore) + int(questions[int(teamnumpicked)-1]['points'])

            with open(str(teaminfo) + 'team' + str(currentteam) + '.txt', 'w') as openfile:
                openfile.write(str(newscore))
                openfile.close()

        elif teamquescorrect == True and korg == False:
            with open(str(teaminfo) + 'team' + str(giveteam) + '.txt', 'r') as openfile:
                prevscore = openfile.read()
                openfile.close()
            newscore = int(prevscore) + int(questions[int(teamnumpicked)-1]['points'])

            with open(str(teaminfo) + 'team' + str(giveteam) + '.txt', 'w') as openfile:
                openfile.write(str(newscore))
                openfile.close()
        
        pickednums.append(int(teamnumpicked))

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

cs()
print('Endgame!\nCurrent scores are:')
printteams(teaminfo, numofteams)