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
Either download the program from the green ```<>code``` button, [here](https://github.com/ProductionEXP/Unfair-Trivia), or from the newest relese, [here](https://github.com/ProductionEXP/Unfair-Trivia/releases). Once that is done unpack the zip file in your spescifided location, if you dont have python download the latest version from [here](https://www.python.org/downloads/). Once you have both python and the program installed you are ready to start, double click the .py file (```main.py```), and you are in! Upon starting you are asked to make a grid for the number of questions you have, see [Addding/Changing Questions](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#addingchanging-questions), the ```(int.) ``` before your cursor tells you what type of input is required.
| Tag       | Expination                        | Example       |
| --------- | --------------------------------- | ------------- |
| (int.)    | Integer                           | 1             |
| (y/n)     | Yes(y) or No(n)                   | y             |
| (a/d)     | Ascending(a) or Descending(d)     | a             |
| (a/n)     | Adding or New                     | n             |
| (k/g)     | Keep(k) or Give (g)               | k             |
| (str.)    | Just a plain string of text       | Hello World   |
| (anw.)    | User anwser, can be int or str    | USA           |

After every input you must press enter to continue. Before it askes you ```How many teams are playing?```, it will show you the current table and how many questions remain. After you enter the number of teams playing it will ask what team is starting, this number must be less than or equal to the number of teams. After that you chose the direction, once that is done setup is compleate.

---
###### Adding members

If you want to add members to a team or all teams, after entering how many teams are playing the game will ask you, ```Would you like to add members to teams?```, after this all that has to be done is follow the instructions givin by the game. When you add members to a team it will remove all previous members, so remember to add all member vs just the new ones.

Once you are done adding team members, when the game asks you, ```What team are you adding members to?```, enter ```exit``` and you will be onto the next step.

---
###### Adding team names

After you either add team members or you chose to skip that step you are asked, ```Would you like to add team names to teams?```, if you want to add team names to any of the teams you can. When you add a team name it will remove the previous name and replace it with the new name.

Once you are done adding team names, when the game asks you, ```What team are you adding a team name to?```, enter ```exit``` and you will be onto the next step.

---
## Running The Game
Once setup is compleate the game will display available questions and what teams is up to pick a question. After the team picks a question, it will then display the team # and the question #, then ask if they are keeping or giving the points, if they are giving it will then ask the team that they are giving the points to. After that it will display What team is up, what question, if they are keeping or giving the points, and to who, then what the question is and it's answer, it will then ask you if they got the question correct. It is within your own judgement if the anwser is correct, the computer will only display one possible anwser. This prosses repeats until there is no more questions. 

If at any point you want to see the scores of the teams, when it asks ```What question do they pick?``` just type ```score```, and it will display the scores.

---
## Endgame
Upon entering engame the code will display the scores and then exit, if the terminal closes the scores are located in ```teams.json``` in here you will find a data set that has the team number and score for that team. It could look somthing like this:
```
[
    {
        "team": "1",
        "teamname": "The Dogs",
        "score": "21",
        "members": [
            "bob",
            "joE"
        ]
    },
    {
        "team": "2",
        "teamname": "The Cats",
        "score": "-5",
        "members": [
            "Ryan"
        ]
    }
]
```
The team and score for every team is dispalyed. Along with the team name and members if applicable. 

This is where the programs stops it's job and you have to do yours.

Before the game started you should have picked some winnging critrea now is the time to figure out the winner, let's say that your criteria was, ```If the dice rolls 1 or 4 highest score wins, if the dice rolls 2 or 5 lowest score wins, and if it rolls 5 or 6 closest score to a prime number wins```. All you would have to do is roll a dice and look at the scores to determin a winner. Congrats you have just played the game of unfair trivia!

---
## Playing the game 
Instead of running the game you can play it, the prosess to do this is the same as if you where running the game, you will do setup the same, but instead of running ```main.py``` you need to run ```play.py```. after that everything is the same. Once you get to playing the game part instead of telling you the anwser it will ask you for the anwser, your anwser can be right but the anwser might not be in the data base, you can manually add points by typing ```madd``` when it asks you ```What question do you pick?``` it will then ask you for a team # and then how many points you want to add or remove, you can remove points by putting a negitve sign in front of the number you input.  

### ```play.py``` IS TIPICALY AN OLDER VERSION OF ```main.py```

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
- Updated ```printteams```, ```genscorefile```, ```addscorejson```
- Updated all code for ```teams.json```
- Added the ability to add team names and members

###### Technical Changes
Added a function to see if a user input is either a or b (See [setup](https://github.com/ProductionEXP/Unfair-Trivia/tree/main#setup) for full list of two character inputs). Function name ```yesorno()```.

Added ```test.py``` for development of new features before they are added to either ```main.py``` or ```play.py```, then bugfixed. This is an internal development file, serves no outside purpose.   

---
### [V4 - The UI Update](https://github.com/ProductionEXP/Unfair-Trivia/releases/tag/V4)
###### Release Date: ?
###### Contubitors: [ProductionEXP](https://github.com/ProductionEXP)
##

This will be pain.