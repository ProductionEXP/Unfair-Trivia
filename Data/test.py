import json
import os
CleanScreen = 'cls'
main = os.path.dirname(__file__)
teamlist = os.path.join(main, 'teams.json')

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
