# Unfair Trivia

###### Code by: [Bryce B.](https://github.com/ProductionEXP) 
###### Idea by: [Gary K. Herberger Young Scholars Academy](https://herbergeracademy.asu.edu)

In the game of unfair tivia you do not know how many points each question is worth, it could be a positve or negitive number. You also do not know what the criteria is to win,  it could be who ever has the lowest score.
## Repository Info

This repo IS maintaianed, please submit an issue if you have a request or a bug.

---
## Rules

- Each team can either chose to keep or give points to another team, this will only happen if they get the question correct
    - A team can not give the points to themselves, that would be keeping the points not giving
- After a question is picked it is removed from the board no matter if they get it right or wrong
- Team numbers either go in ascending or descending order
    - Ascending, Ex. 1 > 2 | Descending, Ex. 2 > 1
- Once all questions are picked, you enter endgame, the game is over now time to determin a winner [Endgame](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#endgame)

---
## Setup
Either download the program from the green ```<>code``` button, [here](https://github.com/ProductionEXP/Unfair-Trivia), or from the newest relese, [here](https://github.com/ProductionEXP/Unfair-Trivia/releases). Once that is done unpack the zip file in your specified location, if you dont have python download the latest version from [here](https://www.python.org/downloads/). Once you have both python and the program installed you need to install PySimpleGUI look [here](https://github.com/PySimpleGUI/PySimpleGUI#installing--) for instructions on how to do so. After all of the prerequisites are installed you are ready to start, double click the .py file (```main.py```), and you are in! Upon starting you are asked to make a grid for the number of questions you have, see [Addding/Changing Questions](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#addingchanging-questions).

###### As of V4 this table is only useful for ```play.py```
| Tag       | Expination                        | Example       |
| --------- | --------------------------------- | ------------- |
| (int.)    | Integer                           | 1             |
| (y/n)     | Yes(y) or No(n)                   | y             |
| (a/d)     | Ascending(a) or Descending(d)     | a             |
| (a/n)     | Adding or New                     | n             |
| (k/g)     | Keep(k) or Give (g)               | k             |
| (str.)    | Just a plain string of text       | Hello World   |
| (anw.)    | User anwser, can be int or str    | USA           |

After every input you must press enter to continue, or the submit button. 

The first think the program promts you with is a text size selector, if you wish to keep it at 12 you can just hit submit, once you have chosen your font size, hit submit. This font size will not change untill you close the program and select a new font size.

---
###### Adding members / team names

I need to do this.

---
## Running The Game
Once setup is compleate the game will display available questions and what teams is up to pick a question. After the team picks a question, it will then display the team # and the question #, then ask if they are keeping or giving the points, if they are giving it will then ask the team that they are giving the points to. After that it will display What team is up, what question, if they are keeping or giving the points, and to who, then what the question is and it's answer, it will then ask you if they got the question correct. It is within your own judgement if the anwser is correct, the computer will only display one possible anwser. This prosses repeats until there is no more questions. 

---
## UI
###### Understanding the UI

I need to do this.

---
## Endgame
Upon entering engame, the game will end and it will display the scores, team name, and team members of each team. It will then show a endgame note, if one was provided in the config file, ```config.json```. To add an endgame note look [here](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#Config).

With this endgame note, let's use ```If the dice rolls 1 or 4 highest score wins, if the dice rolls 2 or 5 lowest score wins, and if it rolls 5 or 6 closest score to a prime number wins``` as an example, all you would have to do is roll a dice and look at the scores to determin a winner, and then congrats you have just played the game of unfair trivia!

---
## Playing the game
Instead of running the game you can play it, the prosess to do this is the same as if you where running the game, you will do setup the same, but instead of running ```main.py``` you need to run ```play.py```. after that everything is the same. Once you get to playing the game part instead of telling you the anwser it will ask you for the anwser, your anwser can be right but the anwser might not be in the data base, you can manually add points by typing ```madd``` when it asks you ```What question do you pick?``` it will then ask you for a team # and then how many points you want to add or remove, you can remove points by putting a negitve sign in front of the number you input.  

### ```play.py``` IS TIPICALY AN OLDER VERSION OF ```main.py```
#### As of the UI update (V4) ```play.py``` has NOT been updated

---
## Config
###### Setting up the config file

I need to do this.

---
## Adding/Changing Questions
###### Changing Questions
By defualt the code comes with two questions:

```
[
    {
        "question#": 1,
        "question": "What is 1+1?",
        "answer": ["2"],
        "points": -5
    },
    {
        "question#": 2,
        "question": "What is the sqrt of 4?",
        "answer": ["2"],
        "points": 5
    },
    {
        "question#": "done"
    }
]
```
In order to change them or add more you need to open the file "questions.json" this is under the "Data" folder in the programs folder. Once the file is open you can change things like the question it's anwser and how many points it is worth.
```
[
    {
        "question#": 1,
        "question": "What is python?",
        "answer": ["A programing language"],
        "points": 6
    },
    {
        "question#": 2,
        "question": "What is the sqrt of 4?",
        "answer": ["2"],
        "points": 5
    },
    {
        "question#": "done"
    }
]
```
Spot the diffrence?

---
###### Adding Questions

If you are going to add questions here is your template:
```
    {
        "question#": #,
        "question": "",
        "answer": [""],
        "points": #
    },
```
Let's say I want to add a question asking:
```"What are the first 3 digits of pi?"```

And the anwser being:
```"3.14"```

With a points value of: 
```-10```

And let's say that it is the 3rd question. The code for that would be:
```
    {
        "question#": 3,
        "question": "What are the first 3 digits of pi?",
        "answer": ["3.14"],
        "points": -10
    },
```

Now let's add that to our old list:
```
[
    {
        "question#": 1,
        "question": "What is python?",
        "answer": ["A programing language"],
        "points": 6
    },
    {
        "question#": 2,
        "question": "What is the sqrt of 4?",
        "answer": ["2"],
        "points": 5
    },
    {
        "question#": 3,
        "question": "What are the first 3 digits of pi?",
        "answer": ["3.14"],
        "points": -10
    },
    {
        "question#": "done"
    }
]
```
And you are done! Adding more questions past that is as easy as that. 

---
###### Adding multiple anwsers to one question

When running in player mode (play.py vs main.py) to increase accuracy you can have multiple anwsers to one question, this is done by useing the list in the questions.json file. 
```
[
    {
        "question#": 1,
        "question": "What is python?",
        "answer": ["A programing language"],
        "points": 6
    },
    {
        "question#": 2,
        "question": "What is the sqrt of 4?",
        "answer": ["2"],
        "points": 5
    },
    {
        "question#": 3,
        "question": "What are the first 3 digits of pi?",
        "answer": ["3.14"],
        "points": -10
    },
    {
        "question#": "done"
    }
]
```
If we take our previous file, under the anwser part of each question you can have multiple anwsers, here is an example:

```
    {
        "question#": 2,
        "question": "What is the sqrt of 4?",
        "answer": ["2", "two"],
        "points": 5
    },
```

We can do this for any question, if this is added to our previous list it would look like:

```
[
    {
        "question#": 1,
        "question": "What is python?",
        "answer": ["A programing language"],
        "points": 6
    },
    {
        "question#": 2,
        "question": "What is the sqrt of 4?",
        "answer": ["2", "two"],
        "points": 5
    },
    {
        "question#": 3,
        "question": "What are the first 3 digits of pi?",
        "answer": ["3.14"],
        "points": -10
    },
    {
        "question#": "done"
    }
]
```

If adding text based anwsers, you can not use capital letters otherwise the anwser will always be wrong.

---
## Versions

### [V1](https://github.com/ProductionEXP/Unfair-Trivia/releases/tag/V1)
###### Release Date: 8/21/2023
###### Contubitors: [ProductionEXP](https://github.com/ProductionEXP) 
## 

First release of the "game". Just the base.

---
### [V2 - The game update](https://github.com/ProductionEXP/Unfair-Trivia/releases/tag/V2)
###### Release Date: 8/23/2023
###### Contubitors: [ProductionEXP](https://github.com/ProductionEXP)
##
In this update I added the ability to "play" the game, in the previous version you could only run the game for another group of people, but in this update I added ```play.py``` it is an adtaptaion of the game ment to be played, see  [Playing the game](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#playing-the-game). 

---
### [V2.1 - Json Score Update](https://github.com/ProductionEXP/Unfair-Trivia/releases/tag/V2.1)
###### Release Date: 8/24/2023
###### Contubitors: [ProductionEXP](https://github.com/ProductionEXP)
##
In this update I added a JSON system for scores vs individual .txt files for every team. This was added to  bot ```main.py``` and ```play.py```.

---
### [V3 - The Names Update](https://github.com/ProductionEXP/Unfair-Trivia/releases/tag/V3)
###### Release Date: 8/30/2023
###### Contubitors: [ProductionEXP](https://github.com/ProductionEXP)
##

Multiple things where added in this update. Here is a short changelog:

- General updates
    - Added Members
    - Added Team Names
    - Updates to how teams.json (renamed from scores.json) is writen 
    - Intigrated all previous updates to ```play.py```

- Technical Updates
    - Added ```yesorno()```
    - Added ```test.py```

###### Members
Added the ability to add name (members) to teams, this is not required.

You can add members after you have entered how many teams are playing, you can add members in any order to any number of teams. To exit adding team names and continue with the program, when it asks you ```Would you like to add members to teams?``` enter ```exit```. For more information look [here](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#adding-members).

###### Team Names
Added the ability to add team names to every team, this is not required.

You can add team names after you have either added or skiped adding members, you can add team names in any order to any number of teams. To exit adding team names and continue with the program, when it asks you ```Would you like to add team names to teams?``` enter ```exit```. For more information look [here](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#adding-team-names).

###### Scoring
Renamed ```scores.json``` to ```teams.json```. And added ```members``` and ```teamname```. For furthur information on how this file is formated, look [here](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#Endgame)

###### Updated ```play.py```
Updated play.py with every new fetures, full list:

- Updated from ```scores.json``` to ```teams.json```
    - Added ```teamname```
    - Added ```members```
    - Changed formating
- Added ```printmembers```, ```yesorno```, ```addmembers```, ```addteamname```
- Updated ```printteams```, ```genscorefile```, ```a full rework of the interface of the Unfair-Trivia program```
- Updated all code for ```teams.json```
- Added the ability to add team names and members

###### Technical Changes
Added a function to see if a user input is either a or b (See [setup](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#setup) for full list of two character inputs). Function name ```yesorno()```.

Added ```test.py``` for development of new features before they are added to either ```main.py``` or ```play.py```, then bugfixed. This is an internal development file, serves no outside purpose.   

---
### [V4 - The UI Update](https://github.com/ProductionEXP/Unfair-Trivia/releases/tag/V4.1)
###### Release Date: 10/6/2023 (projected)
###### Contubitors: [ProductionEXP](https://github.com/ProductionEXP)
###### Special thanks: [PySimpleGUI](https://github.com/PySimpleGUI)
##

In short, a rework of the whole system.

Shortened Changelog:

- General Updates
    - Removed all command promt interaction, all done through [UI](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#UI) now
    - Added the ability to pre-load data, see [Config](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#Config) for more information

- Notes
    - UI update will be brought to ```play.py``` in [V4.1](https://github.com/ProductionEXP/Unfair-Trivia/releases/tag/V4)

###### UI
The main focus of this update is moving away from a command promt interface to a graphical user interface. The primary reason for this is to make this program more user-friendly. All of the UI was done through [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI), because of this it is required, if not already installed, to install PySimpleGUI, to see how to do this look [here](https://github.com/PySimpleGUI/PySimpleGUI#installing--).

For more information on this section, look [here](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#UI)

###### Config
This is a file, ```config.json``` under the ```Data``` folder, that stores a set of json data that is loaded at the begening of the program, as of right now all of the data the user would have to enter durring the startup of the program must EITHER be in ```config.json``` or be entered through the program. This will be fixed in a latter update.

This allows the user to skip the setup and start running the game faster. 

See [Config](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#Config) for more information, and how to set up this file.