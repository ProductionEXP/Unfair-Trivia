searchcycles = 0; grid = False; rows = 0; grid1 = False; grid2 = False; columns = 0; rowcylce = 0; rownum = 1; num = 1; columncylce = 0

import os
import random
import json
import sys

if os.name == 'nt':
    main = os.path.dirname(__file__)
    question = os.path.join(main, 'questions.json')
    gridfile = os.path.join(main, 'grid.txt')
    CleanScreen = 'cls'

elif os.name == 'posix':
    question = 'questions.json'
    grid = 'grid.txt'
    CleanScreen = 'clear'

def cs():
    os.system(CleanScreen)
    
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
        row = input()
        if row.isnumeric():
            rows = row
            grid1 = True
        else:
            print('That is not a number or is not an int., try again')
            continue

    while grid2 != True:
        print('How many columns do you want?')
        column = input()
        if column.isnumeric():
            columns = column
            grid2 = True
        else:
            print('That is not a number or is not an int., try again')
            continue

    if int(columns)*int(rows) > numofquestions:
        print('Grid is to large try again')
        grid1 = False
        grid2 = False 
        continue

    if int(columns)*int(rows) < numofquestions:
        print('Grid is to small try again')
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
        print(str(yorn) + ' Is not a accepted value try again')

cs()

with open(gridfile, 'w') as openfile:
    while int(rowcylce) < int(columns):
        while int(columncylce) < int(rows):
            openfile.writelines(str(num) + '   ')
            num = num + 1
            columncylce = columncylce + 1
        rowcylce = rowcylce + 1
        columncylce = 0
        openfile.writelines('\n')
    openfile.close

with open(gridfile, 'r') as openfile:
    openfile.seek(0)
    print(openfile.read())