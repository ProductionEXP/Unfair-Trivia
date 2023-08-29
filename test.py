import json
import os
CleanScreen = 'cls'
main = os.path.dirname(__file__)
teamlist = os.path.join(main, 'Data\\teams.json')

numofteams = 2

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
    
def cs() -> None:
    os.system(CleanScreen)
    
def yesorno(yorn: str, y: str | None = 'y', n: str | None = 'n') -> bool:
    if yorn.lower() == n:
        return False
    elif yorn.lower() == y:
        return True
    else:
        print(str(yorn) + ' Is not a accepted input, try again')

def addmembers(numofteams: int | None = numofteams, targetteam: int | None = 0, teamsdone: int | None = 0, teamlist: str | None = teamlist, temptf: bool | None = False) -> None:
    with open(teamlist) as f:
        prevdata = json.load(f)
    with open(teamlist, 'w') as openfile:
        openfile.write('[\n')
        while int((teamsdone+1)) < int(numofteams):
            if teamsdone+1 != targetteam:
                scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(prevdata[teamsdone]['members']) + '}'
                jsondata = json.loads(scoreset)
                openfile.write(json.dumps(jsondata, indent=4))
                openfile.write(',\n')
                teamsdone = teamsdone+1
            if teamsdone+1 == targetteam and int((teamsdone+1)) < int(numofteams):
                print('Who are the new members you want to add?')
                print('If multiple seperate names with a space')
                nmembers = input('(str.) ')
                nmembers = nmembers.replace(' ', '", "')
                nmembers = '["' + nmembers + '"]'
                while temptf != True:
                    print('\n' + str(nmembers) + ' Please confim that these are the names you want to add')
                    conf = input('(y/n) ')
                    if yesorno(conf):
                        temptf = True
                        cs()
                temptf = False
                scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(nmembers) + '}'
                jsondata = json.loads(scoreset)
                openfile.write(json.dumps(jsondata, indent=4))
                openfile.write(',\n')
                teamsdone = teamsdone+1
        if int((teamsdone+1)) == int(numofteams) and teamsdone+1 != targetteam:
            scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(prevdata[teamsdone]['members']) + '}'
            jsondata = json.loads(scoreset)
            openfile.write(json.dumps(jsondata, indent=4))
            openfile.write('\n]')
        if teamsdone+1 == targetteam and int((teamsdone+1)) == int(numofteams):
            print('Who are the new members you want to add?')
            print('If multiple seperate names with a space')
            nmembers = input('(str.) ')
            nmembers = nmembers.replace(' ', '", "')
            nmembers = '["' + nmembers + '"]'
            while temptf != True:
                print('\n' + str(nmembers) + ' Please confim that these are the names you want to add')
                conf = input('(y/n) ')
                if yesorno(conf):
                    temptf = True
                    cs()
            temptf = False
            scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(nmembers) + '}'
            jsondata = json.loads(scoreset)
            openfile.write(json.dumps(jsondata, indent=4))
            openfile.write('\n]')    
    with open(teamlist) as f:
        data = json.load(f)
    with open(teamlist, 'w') as f:
        json.dump(data, f, indent=4)

with open(teamlist) as f:
        data = json.load(f)
with open(teamlist, 'w') as f:
    json.dump(data, f, indent=4)

#addmembers(numofteams, 1)