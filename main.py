searchcycles = 0; grid = False; rows = 0; grid1 = False; grid2 = False; columns = 0; rowcylce = 0; rownum = 1; num = 1; columncylce = 0; pickednums = []; temptf = False; dt = 1; numofteams = 0; teammemadd = []; temptf2 = False; teamnameadd = []; gridd = False; teamnum = False; members = False; names = False; directiontf = False; startteamtf = False; exitsec = False; output = ''

from math import floor
import os
import json
import nicegui as ui

sg.theme('DarkBlack')

# Files for the program
if os.name == 'nt':
	main = os.path.dirname(__file__)
	question = os.path.join(main, 'Data\\questions.json')
	gridfile = os.path.join(main, 'Data\\grid.txt')
	teamlist = os.path.join(main, 'Data\\teams.json')
	configdata = os.path.join(main, 'Data\\config.json')

elif os.name == 'posix':
	question = 'Data\\questions.json'
	grid = 'Data\\grid.txt'
	teamlist = 'Data\\teams.json'
	configdata = 'Data\\config.json'
	
# String conversion to list
def Convert(string: str | None = False) -> list:
	li = list(string.split(","))
	return li

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
def returnmembers(targetteam: int, teamlist: str | None = teamlist, output: str | None = '') -> str:
	with open(teamlist) as openfile:
		scoresnteams = json.load(openfile)
		output = output + 'Members:'
		while int(len(scoresnteams[int(targetteam)]['members'])) > 0:
			memberslist = scoresnteams[int(targetteam)]['members']
			output = output + (memberslist.pop())
		output = output + '\n'
	return output 
				
# Prints current lits of teams and scores
def returnteams(numofteams: int, doneteams: int | None = 1, teamlist: str | None = teamlist, output: str | None = '') -> str:
	with open(teamlist) as openfile:
		scoresnteams = json.load(openfile)
		while int(doneteams) <= int(numofteams):
			if str(scoresnteams[doneteams-1]['teamname']) == '':
				output = output + ('\nTeam ' + str(scoresnteams[doneteams-1]['team']) + ': ' + str(scoresnteams[doneteams-1]['score']))
				if scoresnteams[doneteams-1]['members'] != []:
					output = output + returnmembers(doneteams-1)
				doneteams = doneteams + 1
			elif str(scoresnteams[doneteams-1]['teamname']) != '':
				output = output + ('\n' + str(scoresnteams[doneteams-1]['teamname']) + ': ' + str(scoresnteams[doneteams-1]['score']))
				if scoresnteams[doneteams-1]['members'] != []:
					output = output + returnmembers(doneteams-1)
				doneteams = doneteams + 1   
	return output  


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
		nmembers = str(nmembers)
		while int((teamsdone+1)) < int(numofteams):
			if teamsdone+1 != targetteam:
				scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members'])).replace("'", '"') + '}'
				jsondata = json.loads(scoreset)
				openfile.write(json.dumps(jsondata, indent=4))
				openfile.write(',\n')
				teamsdone = teamsdone+1
			if teamsdone+1 == targetteam and int((teamsdone+1)) < int(numofteams):
				nmembers = nmembers.replace("'", '"')
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
			nmembers = nmembers.replace("'", '"')
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

print('Number of questions: ' + str(numofquestions))


# If a user has a config file and wants to use the settings from that instead of entering new ones we grab the data from the file
with open(configdata, 'r') as openfile:
	loadedconfigdata = json.load(openfile)
	endgame = loadedconfigdata[0]['endgame']
if loadedconfigdata[0]['use'] == 'True':
	newtable(gridfile, int(loadedconfigdata[1]['grid'][1]), int(loadedconfigdata[1]['grid'][0]))
	columns = int(loadedconfigdata[1]['grid'][1])
	rows = int(loadedconfigdata[1]['grid'][0])
	numofteams = int(loadedconfigdata[1]['numofteams'])
	genscoerfile(numofteams)
	currentteam = int(loadedconfigdata[1]['startteam'])
	direction = str(loadedconfigdata[1]['direction'])
	if str(loadedconfigdata[1]['members']) == 'True':
		teammemnum = loadedconfigdata[2]['teammebersteams']
		teammemstr = loadedconfigdata[2]['teammebers']
		for currteam in teammemstr: 
			tarteam = teammemnum.pop(0)
			addmembers(targetteam = tarteam, nmembers = currteam, numofteams = numofteams)	
	if str(loadedconfigdata[1]['teamnames']) == 'True':
		teamnemnum = loadedconfigdata[3]['teamnamesteams']
		teamnemstr = loadedconfigdata[3]['teamnames']
		for currteam in teamnemstr: 
			tarteam = teamnemnum.pop(0)
			addteamname(targetteam = tarteam, teamname = currteam, numofteams = numofteams)
	useconfigdata = True
else: useconfigdata = False

layout =	[
			 [sg.Text('Unfair Trvia - Font Size selector')],
		 	 [sg.Text('Sample text', size=(20, 1), key='-text-')],
	         [sg.Slider((6, 50), default_value=12, size=(14, 20), orientation='h', key='-slider-', change_submits=True),
    	      sg.Text('Font size', key = 'fs')],
        	 [sg.Text('Font string = ', key = 'fs1'), sg.Text('', size=(25, 1), key='-fontstring-')],
	         [sg.Button('Submit')]
			]

window = sg.Window('Unfair Trvia - Font string builder', layout)
font_string = 'Helvitica 12'
while True:
	event, values = window.read()
	if event in (sg.WIN_CLOSED, 'Submit'): break
	font_string = 'Helvitica '
	font_string += str(int(values['-slider-']))
	window['-text-'].update(font=font_string)
	window['-fontstring-'].update('"'+font_string+'"')
window.close()

if useconfigdata != True:
	# Has the user make a grid
	while gridd == False:
		griduilayout =  [[sg.Text('Welcome to Unfair Trvia!', font = font_string)],
						 [sg.Text(str('Number of questions: ' + str(numofquestions)), font = font_string)],
						 [sg.Text('To Start fill out the feilds below: \n', font = font_string)],
						 [sg.Text('How many rows do you want?', font = font_string)],
						 [sg.Input('', enable_events=True,  key='rows', font = font_string)],
						 [sg.Text('Input can not be blank\n', key='rowsfail',  text_color='red', font = font_string)],
						 [sg.Text('How many columns do you want?', font = font_string)],
						 [sg.Input('', enable_events=True,  key='columns', font = font_string)],
						 [sg.Text('Input can not be blank\n', key='columnsfail', text_color='red', font = font_string)],
						 [sg.Text(key='fail', text_color='red', font = font_string)],
						 [sg.Button('Submit', visible=True, bind_return_key=True, font = font_string)]
						]
		griduiwindow = sg.Window('Unfair Trivia - Grid Setup', griduilayout)
	
		while True:
			event, values = griduiwindow.read()
			if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
			if len(values['rows']) and values['rows'][-1] not in ('0123456789'): griduiwindow['rows'].update(values['rows'][:-1])
			else:
				if values['rows'] == '' or isint(values['rows'], False) == False: griduiwindow['rowsfail'].update('Input can not be blank\n')
				else:
					if values['rows'] == '0': griduiwindow['rowsfail'].update('Input can not be 0\n') 
					else:
						griduiwindow['rowsfail'].update('')
			if len(values['columns']) and values['columns'][-1] not in ('0123456789'): griduiwindow['columns'].update(values['columns'][:-1])
			else:
				if values['columns'] == '' or isint(values['columns'], False) == False: griduiwindow['columnsfail'].update('Input can not be blank\n')   
				else:
					if values['columns'] == '0': griduiwindow['columnsfail'].update('Input can not be 0\n')   
					else:
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
	
		gridcheckuilayout = [[sg.Text(grid, font = font_string)],
							 [sg.Text('\nYou entered a grid of ' + str(rows) + 'x' + str(columns), font = font_string)],
							 [sg.Text('Please confrim that this grid is correct', font = font_string)],
							 [sg.Button('Yes', visible=True, bind_return_key=True, font = font_string), sg.Button('No', visible=True, font = font_string)]
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
		numberofteamslayout =   [[sg.Text('How many teams are playing?', font = font_string)],
								 [sg.Input('', enable_events=True,  key='numoteam', font = font_string)],
								 [sg.Text('Input can not be blank\n', key='teamnumfail',  text_color='red', font = font_string)],
								 [sg.Button('Submit', visible=True, bind_return_key=True, font = font_string)]
								]
		numberofteamswindow = sg.Window('Unfair Trivia - Number Of Teams', numberofteamslayout)
	
		while True:
			event, values = numberofteamswindow.read()
			if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
			if len(values['numoteam']) and values['numoteam'][-1] not in ('0123456789'): numberofteamswindow['numoteam'].update(values['numoteam'][:-1])
			else:
				if values['numoteam'] == '' or isint(values['numoteam'], False) == False: numberofteamswindow['teamnumfail'].update('Input can not be blank\n')   
				else:
					if values['numoteam'] == '0': numberofteamswindow['teamnumfail'].update('Input can not be 0\n')   
					else:
						numberofteamswindow['teamnumfail'].update('')
			if event == 'Submit' and values['numoteam'] != '' and values['numoteam'] != '0':
				numofteams = int(values['numoteam'])
				break
		numberofteamswindow.close()    
		teamnum = True
	
	# Generate a score file for each team
	genscoerfile(numofteams)
	
	# Sees if the user wants to add members and team names to the teams
	# If the the user wants to they will then be able to add them to the corrasponding team
	while members == False and names == False:
		#displays1 (display section 1)
		displays1 = []; teamsdone = 0; teamup = 1; columnteams = []
		while teamsdone < numofteams/2:
			[templist1, templist2] = [[], []]
			templist1.append(sg.Text(str('\nTeam ' + str(int(teamup)) + '\nMembers: ' + str() + '\nTeam Name: ' + str()), font = font_string))
			templist1.append(sg.Text('\nWould you like to add a team name or team members?', font = font_string))
			templist2.append(sg.Checkbox('Team Name', key = (str('tn' + str(int(teamup)))), tooltip = str('Add a Team name to team ' + str(int(teamup))), font = font_string))
			templist2.append(sg.Checkbox('Team Members', key = (str('tm' + str(int(teamup)))), tooltip = str('Add a Team members to team ' + str(int(teamup))), font = font_string))
			displays1.append(templist1)
			displays1.append(templist2) 
			columnteams.append(int(teamup))
			teamup = teamup + 1
			teamsdone = teamsdone + 1
	
		#displays2 (display section 2)
		displays2 = []; teamsdone = 0
		while teamsdone < floor(numofteams/2):
			[templist1, templist2] = [[], []]
			templist1.append(sg.Text(str('\nTeam ' + str(int(teamup)) + '\nMembers: ' + str() + '\nTeam Name: ' + str()), font = font_string))
			templist1.append(sg.Text('\nWould you like to add a team name or team members?', font = font_string))
			templist2.append(sg.Checkbox('Team Name', key = (str('tn' + str(int(teamup)))), tooltip = str('Add a Team name to team ' + str(int(teamup))), font = font_string))
			templist2.append(sg.Checkbox('Team Members', key = (str('tm' + str(int(teamup)))), tooltip = str('Add a Team members to team ' + str(int(teamup))), font = font_string))
			displays2.append(templist1)
			displays2.append(templist2)
			columnteams.append(int(teamup))
			teamup = teamup + 1
			teamsdone = teamsdone + 1
	
		if numofteams <= 2: ssh1 = 1
		if numofteams > 2: ssh1 = 1.25
		if numofteams >= 20: ssh1 = 2
		if numofteams >= 50: ssh1 = 5
		if numofteams >= 100: ssh1 = 10
	
		teamnamememberslayout = [[sg.Text('Unfair Trivia - Adding Team Names and Members', font = font_string), sg.Button('Skip', tooltip = 'Skip this section', font = font_string)],
								 [sg.Button('Submit', visible=True, bind_return_key=True, tooltip = 'Submit the data for this section', font = font_string)],
								 [sg.Column(displays1, scrollable = True, vertical_scroll_only = True, size_subsample_height = ssh1, vertical_alignment = 'center', expand_x = True, sbar_background_color = 'black', expand_y = True), 
								  sg.Column(displays2, scrollable = True, vertical_scroll_only = True, size_subsample_height = ssh1, vertical_alignment = 'center', expand_x = True, sbar_background_color = 'black', expand_y = True)
								 ]
								]
	
		[templist1, templist2, displays1, displays2s] = [[], [], [], []]
		
		teamnamememberswindow = sg.Window('Unfair Trivia - Team Names and Members', teamnamememberslayout, resizable = True)
	
		while True:
			event, values = teamnamememberswindow.read()
			if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
			if event == 'Skip': teamnamememberswindow.close(); exitsec = True ;break
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
			
		if exitsec == True: members = False; names = False; break
			
		displays1 = []; displays2 = []; memberadd = []; nameadd = []; teammemaddstr = []; teamnameaddstr = []
	
		if int(len(teammemadd)) + int(len(teamnameadd)) > 0:
			for currteam in teamnameadd:
				[templist1, templist2] = [[], []]
				templist1.append(sg.Text(str('\nTeam ' + str(int(currteam))), font = font_string))
				templist1.append(sg.Text('\n\nTeam Name: ', font = font_string))
				templist2.append(sg.Input(key = (str('tna' + str(int(currteam)))), tooltip = str('Add a Team name to team ' + str(int(currteam))), font = font_string))
				displays1.append(templist1)
				displays1.append(templist2)
				nameadd.append(int(currteam))
			
			for currteam in teammemadd:
				[templist1, templist2] = [[], []]
				templist1.append(sg.Text(str('\nTeam ' + str(int(currteam))), font = font_string))
				templist1.append(sg.Text('\n\nTeam Members: (Seperate by commas (,))', font = font_string))
				templist2.append(sg.Input(key = (str('tma' + str(int(currteam)))), tooltip = str('Add a Team members to team ' + str(int(currteam))), font = font_string))
				displays2.append(templist1)
				displays2.append(templist2)
				memberadd.append(int(currteam))
			
			if int(len(teammemadd)) + int(len(teamnameadd)) <= 2: ssh = 1
			if int(len(teammemadd)) + int(len(teamnameadd)) > 2: ssh = 1.25
			if int(len(teammemadd)) + int(len(teamnameadd)) >= 20: ssh = 2
			if int(len(teammemadd)) + int(len(teamnameadd)) >= 50: ssh = 5
			if int(len(teammemadd)) + int(len(teamnameadd)) >= 100: ssh = 10
		
			namesandmemlayout =	[[sg.Text('Unfair Trivia - Adding Team Names and Members', font = font_string)],
								 [sg.Button('Submit', visible=True, bind_return_key=True, tooltip = 'Submit the data for this section', font = font_string)],
								 [sg.Column(displays1, scrollable = True, vertical_scroll_only = True, size_subsample_height = ssh, vertical_alignment = 'center', expand_x = True, sbar_background_color = 'black', expand_y = True), 
								  sg.Column(displays2, scrollable = True, vertical_scroll_only = True, size_subsample_height = ssh, vertical_alignment = 'center', expand_x = True, sbar_background_color = 'black', expand_y = True)
								 ]
								]
		
			namesandmemwindow = sg.Window('Unfair Trivia - Team Names and Members', namesandmemlayout, resizable = True)
	
			while True:
				event, values = namesandmemwindow.read()
				if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
				if event == 'Submit':
					for item in memberadd:
						targettm = str('tma' + str(int(item)))
						teammemaddstr.append(Convert(values[targettm]))
					for item in nameadd:
						targettn = str('tna' + str(int(item)))
						teamnameaddstr.append(values[targettn]) 
					namesandmemwindow.close()
					break
				
			for currteam in teammemaddstr: 
				tarteam = memberadd.pop(0)
				addmembers(targetteam = tarteam, nmembers = currteam, numofteams = numofteams)
			members = True
	
			for currteam in teamnameaddstr: 
				tarteam = nameadd.pop(0)
				addteamname(targetteam = tarteam, teamname = currteam, numofteams = numofteams)
			names = True
			
	while startteamtf != True:
		stuilayout =	[[sg.Text('Unfair Trivia - Starting Team', font = font_string)],
						 [sg.Button('Submit', visible=True, bind_return_key=True, tooltip = 'Submit the data for this section', font = font_string)],
						 [sg.Text('What team will be starting?', font = font_string)],
						 [sg.Input(key = 'startteamui')],
						 [sg.Text('Input can not be blank\n', key='stfail',  text_color='red', font = font_string)],
						]
		
		stuiwindow = sg.Window('Unfair Trivia - Starting Team', stuilayout, resizable = True)
		while True:
			event, values = stuiwindow.read()
			if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
			if len(values['startteamui']) and values['startteamui'][-1] not in ('0123456789'): stuiwindow['startteamui'].update(values['startteamui'][:-1])		
			else:
				if values['startteamui'] == '': stuiwindow['stfail'].update('Input can not be blank\n')  
				else:
					if int(values['startteamui']) > numofteams: stuiwindow['stfail'].update('Input can not be above the number of teams\n') 
					else: 
						if int(values['startteamui']) <= 0: stuiwindow['stfail'].update('Input can not be 0\n')
						else: 
							stuiwindow['stfail'].update('')	
							if event == 'Submit':
								startteam = int(values['startteamui'])
								stuiwindow.close()
								startteamtf = True
								break
							
	while directiontf != True:
		directionuilayout = [[sg.Text('Unfair Trivia - Direction', font = font_string)],
							 [sg.Button('Submit', visible=True, bind_return_key=True, tooltip = 'Submit the data for this section', font = font_string)],
							 [sg.Radio("Ascending", "ad", key='ada', enable_events=True, default=True, font = font_string), sg.Radio("Descending", "ad", key='add', enable_events=True, font = font_string)] 
							]
		
		directionuiwindow = sg.Window('Unfair Trivia - Team direction', directionuilayout, resizable = True)
		while True:
			event, values = directionuiwindow.read()
			if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()	
			if event == 'Submit':
				if values['ada'] == True: direction = 'a'
				elif values['add'] == True: direction = 'd'
				directionuiwindow.close()
				directiontf = True
				break
	# Defines first team
	currentteam = startteam

while int(numofquestions - len(pickednums)) > 0:
	with open(question, 'r') as openfile:
		questions = json.load(openfile)
	newtable(gridfile, columns, rows, pickednums)

	mainloopuilayout =	[
						 [sg.Text('Unfair Trivia - The Game', font = font_string), sg.Push(), sg.Text(returnteams(numofteams), key = 'score', font = font_string)],
						 [sg.Text('\nCurrent Grid:', font = font_string)],
						 [sg.Text(printtable(p = False), key = 'grid', font = font_string)],
	 					 [sg.Text('\nTotal Questions remaining: ' + str(numofquestions - len(pickednums)), key = 'tqr', font = font_string)],
	 					 [sg.Text('\nTeam ' + str(currentteam) + ' is up!\nWhat question do they pick?', key = 'tnumup', font = font_string)],
	 					 [sg.Input('', enable_events = True, key = 'quespick', font = font_string), sg.Button('Submit', visible=True, bind_return_key=True, tooltip = 'Submit the data for this section', font = font_string)],
						 [sg.Text('Input can not be blank\n', key='quespickfail',  text_color='red', font = font_string)]
						]

	mainloopuiwindow = sg.Window('Unfair Trvia - The Game', mainloopuilayout, resizable = True)

	while True:
		event, values = mainloopuiwindow.read()
		if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
		if len(values['quespick']) and values['quespick'][-1] not in ('0123456789'): mainloopuiwindow['quespick'].update(values['quespick'][:-1])		
		else:
			if values['quespick'] == '': mainloopuiwindow['quespickfail'].update('Input can not be blank\n')  
			else:
				if int(values['quespick']) in pickednums: mainloopuiwindow['quespickfail'].update('Question was already picked\n') 
				else: 
					if int(values['quespick']) > int(numofquestions): mainloopuiwindow['quespickfail'].update('Question does not exist\n') 
					else:
						if int(values['quespick']) <= 0: mainloopuiwindow['quespickfail'].update('Input can not be 0\n')
						else: 
							mainloopuiwindow['quespickfail'].update('')	
							if event == 'Submit':
								mainloopuiwindow.close()
								teamnumpicked = int(values['quespick'])
								break			

	mainloopuilayoutquestionsettings =  [
										 [sg.Text('Unfair Trivia - The Game', font = font_string), sg.Push(), sg.Text(returnteams(numofteams), key = 'score', font = font_string)],
										 [sg.Text('\nTeam ' + str(currentteam), key = 'tnumup', font = font_string)],
										 [sg.Text('Do they chose to give the points away or keep the points?', font = font_string)],
										 [sg.Radio("Keep", "korg", key='keep', enable_events=True, default=True, font = font_string), sg.Radio("Give", "korg", key='give', enable_events=True, font = font_string)],
										 [sg.Button('Submit', visible=True, bind_return_key=True, tooltip = 'Submit the data for this section', font = font_string)],

										 [sg.Text('\nTeam ' + str(currentteam) + ' is giving the points away!\nWho are they giving the points to?', visible=False, key = 's1', font = font_string)],
										 [sg.Input('', enable_events = True, visible=False, key = 'givepointspick', font = font_string), sg.Button('Next!', visible=False, bind_return_key=True, tooltip = 'Submit the data for this section', font = font_string)],
										 [sg.Text('Input can not be blank\n', key='givepointspickfail',  text_color='red', visible=False, font = font_string)]
										]

	mainloopuiwindowquestionsettings = sg.Window('Unfair Trvia - The Game', mainloopuilayoutquestionsettings, resizable = True)

	while True:
		event, values = mainloopuiwindowquestionsettings.read()
		if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
		if event == 'Submit':
			if values['keep'] == False:
				korg = True
				mainloopuiwindowquestionsettings['s1'].update(visible=True)
				mainloopuiwindowquestionsettings['givepointspick'].update(visible=True)
				mainloopuiwindowquestionsettings['Next!'].update(visible=True)
				mainloopuiwindowquestionsettings['givepointspickfail'].update(visible=True)
				event, values = mainloopuiwindowquestionsettings.read()
			else:
				korg = False
				mainloopuiwindowquestionsettings['s1'].update(visible=False)
				mainloopuiwindowquestionsettings['givepointspick'].update(visible=False)
				mainloopuiwindowquestionsettings['Next!'].update(visible=False)
				mainloopuiwindowquestionsettings['givepointspickfail'].update(visible=False)
				mainloopuiwindowquestionsettings.close()
				break

		if values['keep'] == False:
				if len(values['givepointspick']) and values['givepointspick'][-1] not in ('0123456789'): mainloopuiwindowquestionsettings['givepointspick'].update(values['givepointspick'][:-1])		
				else:
					if values['givepointspick'] == '': mainloopuiwindowquestionsettings['givepointspickfail'].update('Input can not be blank\n')  
					else:
						if int(values['givepointspick']) > numofteams: mainloopuiwindowquestionsettings['givepointspickfail'].update('Input can not be above the number of teams\n') 
						else:
							if int(values['givepointspick']) <= 0: mainloopuiwindowquestionsettings['givepointspickfail'].update('Input can not be 0\n')
							else: 
								if int(values['givepointspick']) == currentteam: mainloopuiwindowquestionsettings['givepointspickfail'].update('The team can' + "'" + 't give points to themselves\n')
								else: 
									mainloopuiwindowquestionsettings['givepointspickfail'].update('')
									if event == 'Next!': 
										giveteam = int(values['givepointspick'])
										mainloopuiwindowquestionsettings.close()
										break

	if korg == False:
			keepgive = 'keeping the points'
	if korg == True:
		keepgive = 'giving the points to ' + str(giveteam)
	anwsera = questions[int(teamnumpicked)-1]['answer']

	mainloopuilayoutquestionresponse = 	[
										 [sg.Text('Unfair Trivia - The Game', font = font_string), sg.Push(), sg.Text(returnteams(numofteams), key = 'score', font = font_string)],
										 [sg.Text('Team ' + str(currentteam) + ' picked question ' + str(teamnumpicked) + ' - And are ' + str(keepgive), key = 'tnumup', font = font_string)],
										 [sg.Text('\n\nQuestion: \n' + str(questions[int(teamnumpicked)-1]['question']), key = 'question', font = font_string)],
										 [sg.Text('\nAnswer: \n' + str(anwsera[0]), key = 'awnserinput', font = font_string)],
										 [sg.Text('\nDid they get the question right?', font = font_string)],
										 [sg.Radio("Yes", "qesright", key='y', enable_events=True, default=True, font = font_string), sg.Radio("No", "qesright", key='n', enable_events=True, font = font_string)],
										 [sg.Button('Submit', visible=True, bind_return_key=True, tooltip = 'Submit the data for this section', font = font_string)]
										]	
	
	mainloopuiwindowquestionresponse = sg.Window('Unfair Trvia - The Game', mainloopuilayoutquestionresponse, resizable = True)

	while True:
		event, values = mainloopuiwindowquestionresponse.read()
		if event in (None, 'Exit') or event == sg.WINDOW_CLOSED: exit()
		if event == 'Submit': 
			if values['y'] == True: teamquescorrect = True 
			elif values['n'] == True: teamquescorrect = False 
			mainloopuiwindowquestionresponse.close()
			break

	# Updates the correct team's score for either keeping or giving points
	if teamquescorrect == True and korg == False:
		addscorejson(currentteam, teamnumpicked)
	elif teamquescorrect == True and korg == True:
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

# Display Final scores
newtable(gridfile, columns, rows, pickednums)
print('Endgame!\nCurrent scores are:')
print(returnteams(numofteams))
print('Your endgame note: ' + str(endgame))
input('Press enter to exit')