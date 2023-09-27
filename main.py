searchcycles = 0; grid = False; rows = 0; grid1 = False; grid2 = False; columns = 0; rowcylce = 0; rownum = 1; num = 1; columncylce = 0; pickednums = []; temptf = False; dt = 1; numofteams = 0; teammemadd = []; temptf2 = False; teamnameadd = []; gridd = False; teamnum = False; members = False; names = False

import os
import json
import PySimpleGUI as sg

sg.theme('DarkBlack')

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
def printtable(gridfile: str | None = gridfile, p: bool | None = True) -> str:
	with open(gridfile, 'r') as openfile:
		openfile.seek(0)
		if p:
			print(openfile.read())
		else:
			return str(openfile.read())

# Prints current list of members for a single team 
def printmembers(targetteam: int, teamlist: str | None = teamlist) -> None:
	with open(teamlist) as openfile:
		scoresnteams = json.load(openfile)
		print('Members:')
		while int(len(scoresnteams[int(targetteam)]['members'])) > 0:
			memberslist = scoresnteams[int(targetteam)]['members']
			print(memberslist.pop())
		print()

# Prints current lits of teams and scores
def printteams(numofteams: int, doneteams: int | None = 1, teamlist: str | None = teamlist) -> None:
	with open(teamlist) as openfile:
		scoresnteams = json.load(openfile)
		while int(doneteams) <= int(numofteams):
			if str(scoresnteams[doneteams-1]['teamname']) == '':
				print('Team ' + scoresnteams[doneteams-1]['team'] + ': ' + scoresnteams[doneteams-1]['score'])
				if scoresnteams[doneteams-1]['members'] != []:
					printmembers(doneteams-1)
				doneteams = doneteams + 1
			elif str(scoresnteams[doneteams-1]['teamname']) != '':
				print(scoresnteams[doneteams-1]['teamname'] + ': ' + scoresnteams[doneteams-1]['score'])
				if scoresnteams[doneteams-1]['members'] != []:
					printmembers(doneteams-1)
				doneteams = doneteams + 1     

# Check if a string (any) is an integer
def isint(number: any, printi: bool | None = True) -> bool:
	flag = True
	try:
		int(number)
	except ValueError:
		flag = False

	if flag:
		return True
	else:
		if printi == True:
			print('That is not a integer, try again')
		return False
	
# Checks if an input is y or n
def yesorno(yorn: str, y: str | None = 'y', n: str | None = 'n') -> bool:
	if yorn.lower == n:
		return False
	elif yorn.lower == y:
		return True
	else:
		print(str(yorn) + ' Is not a accepted input, try again')

# Generates score file
def genscoerfile(numofteams: int | None = numofteams, teamsdone: int | None = 0, teamlist: str | None = teamlist) -> None:
	with open(teamlist, 'w') as openfile:
		openfile.write('[\n')
		while int((teamsdone+1)) < int(numofteams):
			scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "0","members": []}'
			jsondata = json.loads(scoreset)
			openfile.write(json.dumps(jsondata, indent=4))
			openfile.write(',\n')
			teamsdone = teamsdone+1
		if int((teamsdone+1)) == int(numofteams):
			scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "0","members": []}'
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

# Adds members to a team
def addmembers(numofteams: int | None = numofteams, targetteam: int | None = 0, teamsdone: int | None = 0, teamlist: str | None = teamlist, temptf: bool | None = False, nmembers: list | None = '') -> None:
	with open(teamlist) as f:
		prevdata = json.load(f)
	with open(teamlist, 'w') as openfile:
		openfile.write('[\n')
		while int((teamsdone+1)) < int(numofteams):
			if teamsdone+1 != targetteam:
				scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members'])).replace("'", '"') + '}'
				jsondata = json.loads(scoreset)
				openfile.write(json.dumps(jsondata, indent=4))
				openfile.write(',\n')
				teamsdone = teamsdone+1
			if teamsdone+1 == targetteam and int((teamsdone+1)) < int(numofteams):
				while temptf != True:
					nmembers = nmembers.replace(' ', '", "')
					nmembers = '["' + nmembers + '"]'
				temptf = False
				scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(nmembers) + '}'
				jsondata = json.loads(scoreset)
				openfile.write(json.dumps(jsondata, indent=4))
				openfile.write(',\n')
				teamsdone = teamsdone+1
		if int((teamsdone+1)) == int(numofteams) and teamsdone+1 != targetteam:
			scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members']).replace("'", '"')) + '}'
			jsondata = json.loads(scoreset)
			openfile.write(json.dumps(jsondata, indent=4))
			openfile.write('\n]')
		if teamsdone+1 == targetteam and int((teamsdone+1)) == int(numofteams):
			while temptf != True:
				nmembers = nmembers.replace(' ', '", "')
				nmembers = '["' + nmembers + '"]'
			temptf = False
			scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(nmembers) + '}'
			jsondata = json.loads(scoreset)
			openfile.write(json.dumps(jsondata, indent=4))
			openfile.write('\n]')    
	with open(teamlist) as f:
		data = json.load(f)
	with open(teamlist, 'w') as f:
		json.dump(data, f, indent=4)

# Adds team name to a team
def addteamname(numofteams: int | None = numofteams, targetteam: int | None = 0, teamsdone: int | None = 0, teamlist: str | None = teamlist, temptf: bool | None = False, teamname: str | None = '') -> None:
	with open(teamlist) as f:
		prevdata = json.load(f)
	with open(teamlist, 'w') as openfile:
		openfile.write('[\n')
		while int((teamsdone+1)) < int(numofteams):
			if teamsdone+1 != targetteam:
				scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "' + str(prevdata[teamsdone]['teamname']) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members'])).replace("'", '"') + '}'
				jsondata = json.loads(scoreset)
				openfile.write(json.dumps(jsondata, indent=4))
				openfile.write(',\n')
				teamsdone = teamsdone+1
			if teamsdone+1 == targetteam and int((teamsdone+1)) < int(numofteams):
				scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "' + str(teamname) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members'])).replace("'", '"') + '}'
				jsondata = json.loads(scoreset)
				openfile.write(json.dumps(jsondata, indent=4))
				openfile.write(',\n')
				teamsdone = teamsdone+1
		if int((teamsdone+1)) == int(numofteams) and teamsdone+1 != targetteam:
			scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "' + str(prevdata[teamsdone]['teamname']) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members']).replace("'", '"')) + '}'
			jsondata = json.loads(scoreset)
			openfile.write(json.dumps(jsondata, indent=4))
			openfile.write('\n]')
		if teamsdone+1 == targetteam and int((teamsdone+1)) == int(numofteams):
			scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "' + str(teamname) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members'])).replace("'", '"') + '}'
			jsondata = json.loads(scoreset)
			openfile.write(json.dumps(jsondata, indent=4))
			openfile.write('\n]')    
	with open(teamlist) as f:
		data = json.load(f)
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
while gridd == False:
	griduilayout =  [[sg.Text('Welcome to Unfair Trvia!')],
					 [sg.Text(str('Number of questions: ' + str(numofquestions)))],
					 [sg.Text('To Start fill out the feilds below: \n')],
					 [sg.Text('How many rows do you want?')],
					 [sg.Input('', enable_events=True,  key='rows', )],
					 [sg.Text('Input can not be blank\n', key='rowsfail',  text_color='red')],
					 [sg.Text('How many columns do you want?')],
					 [sg.Input('', enable_events=True,  key='columns', )],
					 [sg.Text('Input can not be blank\n', key='columnsfail', text_color='red')],
					 [sg.Text(key='fail', text_color='red')],
					 [sg.Button('Submit', visible=True, bind_return_key=True)]
					]
	griduiwindow = sg.Window('Unfair Trivia - Grid Setup', griduilayout)

	while True:
		event, values = griduiwindow.read()
		if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
		if len(values['rows']) and values['rows'][-1] not in ('0123456789'):
			griduiwindow['rows'].update(values['rows'][:-1])
		if len(values['columns']) and values['columns'][-1] not in ('0123456789'):
			griduiwindow['columns'].update(values['columns'][:-1])
		if values['rows'] == '' or isint(values['rows'], False) == False:
			griduiwindow['rowsfail'].update('Input can not be blank\n')
		if values['rows'] == '0':
			griduiwindow['rowsfail'].update('Input can not be 0\n')   
		elif values['rows'] != '0' and values['rows'] != '':
			griduiwindow['rowsfail'].update('')
		if values['columns'] == '' or isint(values['columns'], False) == False:
			griduiwindow['columnsfail'].update('Input can not be blank\n')   
		if values['columns'] == '0':
			griduiwindow['columnsfail'].update('Input can not be 0\n')   
		elif values['columns'] != '0' and values['columns'] != '':
			griduiwindow['columnsfail'].update('')       
		if isint(values['rows'], False) and isint(values['columns'], False) and int(values['rows'])*int(values['columns']) != int(numofquestions):
			if int(values['rows'])*int(values['columns']) > int(numofquestions):
				griduiwindow['fail'].update('Grid too large, try again')
			elif int(values['rows'])*int(values['columns']) < int(numofquestions):
				griduiwindow['fail'].update('Grid too small, try again')
		else:
			griduiwindow['fail'].update('')
		if isint(values['rows'], False) and isint(values['columns'], False): 
			if event == 'Submit' and int(values['rows'])*int(values['columns']) == int(numofquestions):
				griduiwindow['fail'].update('')
				print('You have submited a grid of ' + str((int(values['rows'])*int(values['columns']))) + ' questions.\nIn a grid of ' + values['rows'] + 'x' + values['columns'])
				columns = values['columns']
				rows = values['rows']
				break
	griduiwindow.close()

	newtable(gridfile, columns, rows, pickednums)
	with open(gridfile, 'r') as openfile:
		grid = openfile.read()
		openfile.close()

	gridcheckuilayout = [[sg.Text(grid)],
						 [sg.Text('\nYou entered a grid of ' + str(rows) + 'x' + str(columns))],
						 [sg.Text('Please confrim that this grid is correct')],
						 [sg.Button('Yes', visible=True, bind_return_key=True), sg.Button('No', visible=True)]
						]

	gridcheckuiwindow = sg.Window('Unfair Trivia - Grid Confirmation', gridcheckuilayout)

	while True:
		event, values = gridcheckuiwindow.read()
		if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
		if event == 'Yes':
			gridd = True
			gridcheckuiwindow.close()
			break
		elif event == 'No':
			gridd = False
			gridcheckuiwindow.close()
			break


# Prints first table
printtable()

# Prints how many questions remain
print(str(numofquestions - len(pickednums)) + ' Questions Remain')

# Figure out how many teams are playing
while teamnum == False:
	numberofteamslayout =   [[sg.Text('How many teams are playing?')],
							 [sg.Input('', enable_events=True,  key='numoteam', )],
							 [sg.Text('Input can not be blank\n', key='teamnumfail',  text_color='red')],
							 [sg.Button('Submit', visible=True, bind_return_key=True)]
							]
	numberofteamswindow = sg.Window('Unfair Trivia - Number Of Teams', numberofteamslayout)

	while True:
		event, values = numberofteamswindow.read()
		if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
		if len(values['numoteam']) and values['numoteam'][-1] not in ('0123456789'):
			numberofteamswindow['numoteam'].update(values['numoteam'][:-1])
		if values['numoteam'] == '' or isint(values['numoteam'], False) == False:
			numberofteamswindow['teamnumfail'].update('Input can not be blank\n')   
		if values['numoteam'] == '0':
			numberofteamswindow['teamnumfail'].update('Input can not be 0\n')   
		elif values['numoteam'] != '0' and values['numoteam'] != '':
			numberofteamswindow['teamnumfail'].update('')
		if event == 'Submit' and values['numoteam'] != '' and values['numoteam'] != '0':
			numofteams = int(values['numoteam'])
			break
	numberofteamswindow.close()    
	teamnum = True

# Generate a score file for each team
genscoerfile(numofteams)

# Adds members to teams
while members == False and names == False:
	#displays1 (display section 1)
	displays1 = []; teamsdone = 0; teamup = 1; columnteams = []
	while teamsdone < numofteams/2:
		[templist1, templist2] = [[], []]
		templist1.append(sg.Text(str('\nTeam ' + str(int(teamup)) + '\nMembers: ' + str() + '\nTeam Name: ' + str())))
		templist1.append(sg.Text('\nWould you like to add a team name or team members?'))
		templist2.append(sg.Checkbox('Team Name', key = (str('tn' + str(int(teamup)))), tooltip = str('Add a Team name to team ' + str(int(teamup)))))
		templist2.append(sg.Checkbox('Team Members', key = (str('tm' + str(int(teamup)))), tooltip = str('Add a Team members to team ' + str(int(teamup)))))
		displays1.append(templist1)
		displays1.append(templist2) 
		columnteams.append(int(teamup))
		teamup = teamup + 1
		teamsdone = teamsdone + 1

	#displays2 (display section 2)
	displays2 = []; teamsdone = 0; teamup = int((numofteams/2)+1)
	while teamsdone < numofteams/2:
		[templist1, templist2] = [[], []]
		templist1.append(sg.Text(str('\nTeam ' + str(int(teamup)) + '\nMembers: ' + str() + '\nTeam Name: ' + str())))
		templist1.append(sg.Text('\nWould you like to add a team name or team members?'))
		templist2.append(sg.Checkbox('Team Name', key = (str('tn' + str(int(teamup)))), tooltip = str('Add a Team name to team ' + str(int(teamup)))))
		templist2.append(sg.Checkbox('Team Members', key = (str('tm' + str(int(teamup)))), tooltip = str('Add a Team members to team ' + str(int(teamup)))))
		displays2.append(templist1)
		displays2.append(templist2)
		columnteams.append(int(teamup))
		teamup = teamup + 1
		teamsdone = teamsdone + 1


	teamnamememberslayout = [[sg.Text('Unfair Trivia - Adding Team Names and Members'), sg.Button('Skip', tooltip = 'Skip this section')],
							 [sg.Button('Submit', visible=True, bind_return_key=True, tooltip = 'Submit the data for this section')],
							 [sg.Column(displays1, scrollable = True, vertical_scroll_only = True, size_subsample_height = 1.25, vertical_alignment = 'center', expand_x = True, sbar_background_color = 'black', expand_y = True), 
							  sg.Column(displays2, scrollable = True, vertical_scroll_only = True, size_subsample_height = 1.25, vertical_alignment = 'center', expand_x = True, sbar_background_color = 'black', expand_y = True)
							 ]
							]

	[templist1, templist2, displays1, displays2s] = [[], [], [], []]
	
	teamnamememberswindow = sg.Window('Unfair Trivia - Team Names and Members', teamnamememberslayout, resizable = True)

	while True:
		event, values = teamnamememberswindow.read()
		if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
		if event == 'Skip': teamnamememberswindow.close(); break
		if event == 'Submit':
			for item in columnteams:
				targettn = str('tn' + str(int(item)))
				targettm = str('tm' + str(int(item)))
				if values[targettm] == True:
					teammemadd.append(int(item))
				if values[targettn] == True:
					teamnameadd.append(int(item))
			teamnamememberswindow.close()	
			break
		
	displays1 = []; displays2 = []; memberadd = []; nameadd = []; teammemaddstr = []; teamnameaddstr = []

	if int(len(teammemadd)) + int(len(teamnameadd)) > 0:
		for currteam in teamnameadd:
			[templist1, templist2] = [[], []]
			templist1.append(sg.Text(str('\nTeam ' + str(int(currteam)))))
			templist1.append(sg.Text('\nTeam Name: '))
			templist2.append(sg.Input(key = (str('tna' + str(int(currteam)))), tooltip = str('Add a Team name to team ' + str(int(currteam)))))
			displays1.append(templist1)
			displays1.append(templist2)
			memberadd.append(int(teamup))
		
		for currteam in teammemadd:
			[templist1, templist2] = [[], []]
			templist1.append(sg.Text(str('\nTeam ' + str(int(currteam)))))
			templist1.append(sg.Text('\nTeam Members: (Seperate by commas (,))'))
			templist2.append(sg.Input(key = (str('tma' + str(int(currteam)))), tooltip = str('Add a Team name to team ' + str(int(currteam)))))
			displays2.append(templist1)
			displays2.append(templist2)
			nameadd.append(int(teamup))
		
		namesandmemlayout =	[[sg.Text('Unfair Trivia - Adding Team Names and Members')],
							 [sg.Button('Submit', visible=True, bind_return_key=True, tooltip = 'Submit the data for this section')],
							 [sg.Column(displays1, scrollable = True, vertical_scroll_only = True, size_subsample_height = 1.25, vertical_alignment = 'center', expand_x = True, sbar_background_color = 'black', expand_y = True), 
							  sg.Column(displays2, scrollable = True, vertical_scroll_only = True, size_subsample_height = 1.25, vertical_alignment = 'center', expand_x = True, sbar_background_color = 'black', expand_y = True)
							 ]
							]
	
		namesandmemwindow = sg.Window('Unfair Trivia - Team Names and Members', namesandmemlayout, resizable = True)
		
		while True:
			event, values = namesandmemwindow.read()
			if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
			if event == 'Submit':
				for item in memberadd:
					targettm = str('tma' + str(int(item)))
				for item in nameadd:
					targettn = str('tna' + str(int(item)))
					teammemaddstr.append(values[targettm]) 
				namesandmemwindow.close()	
				break

		nmembers = ''; tname = ''
		for currteam in teammemaddstr: 
			nmembers = '1' + str(currteam)
			addmembers(targetteam = int(currteam), nmembers = nmembers)
		members = True

		for currteam in teamnameaddstr: 
			tname = '1' + str(currteam)
			addteamname(targetteam = int(currteam), teamname = tname)
		names = True
		
	input()
	
# Addes Names to team (Team Names)
while temptf != True:
	print('\nWould you like to add team names to teams?')
	addname = input('(y/n) ')
	temp = yesorno(addname)
	if temp:
		while teamnameadd.lower() != 'exit':
			while temptf2 != True:
				print('\nWhat team are you adding a team name to?')
				teamnameadd = input('(int.) ')
				if teamnameadd.lower() == 'exit':
					break 
				if isint(teamnameadd):
					if teamnameadd <= numofteams:
						temptf2 = True
					else:
						print('Value is to large, try again')
						temptf2 = False   
			temptf2 = False
			cs()
			if teamnameadd.lower() != 'exit':
				addteamname(numofteams, int(teamnameadd))
			if teamnameadd.lower() == 'exit':
				temptf2 = True
				temptf = True
				break 
	else:
		temptf = True
temptf2 = True
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
			printtable()
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
newtable(gridfile, columns, rows, pickednums)
cs()
print('Endgame!\nCurrent scores are:')
printteams(numofteams)
input('Press enter to exit')