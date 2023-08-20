# Unfair Trivia

###### Code by: [Bryce B.](https://github.com/ProductionEXP) 
###### Idea by: [Gary K. Herberger Young Scholars Academy](https://herbergeracademy.asu.edu)

In the game of unfair tivia you do not know how many points each question is worth, it could be a positve or negitive number. You also do not know what the criteria is to win,  it could be who ever has the lowest score.

## Rules

- Each team can either chose to keep or give points to another team, this will only happen if they get the question correct
    - A team can not give the points to themselves, that would be keeping the points not giving
- After a question is picked it is removed from the board no matter if they get it right or wrong
- Team numbers either go in ascending or descending order
    - Ascending, Ex. 1 > 2 | Descending, Ex. 2 > 1
- Once all questions are picked, you enter endgame, the game is over now time to determin a winner [Endgame]()

## Setup
Either download the program from the green code button, [here](https://github.com/ProductionEXP/Unfair-Trivia), or from the newest relese, [here](https://github.com/ProductionEXP/Unfair-Trivia/releases). Once that is done unpack the zip file in your spescifided location, if you dont have python download the latest version from [here](https://www.python.org/downloads/). Once you have both python and the program installed you are ready to start, double click the .py file (main.py), and you are in! Upon starting you are asked to make a grid for the number of questions you have, see [Addding/Changing Questions](), the "(int.) " before your cursor tells you what type of input is required.
| Tag       | Expination                    | Example   |
| --------- | ----------------------------- | --------- |
| (int.)    | Integer                       | 1         |
| (y/n)     | Yes(y) or No(n)               | y         |
| (a/d)     | Ascending(a) or Descending(d) | a         |
| (k/g)     | Keep(k) or Give (g)           | k         |

After every input you must press enter to continue. Before it askes you "How many teams are playing?", it will show you the current table and how many questions remain. After you enter the number of teams playing it will ask what team is starting, this number must be less than or equal to the number of teams. After that you chose the direction, once that is done setup is compleate.

## Playing The Game
Once setup is compleate the game will display available questions and what teams is up to pick a question. After the team picks a question, it will then display the team # and the question #, then ask if they are keeping or giving the points, if they are giving it will then ask the team that they are giving the points to. After that it will display What team is up, what question, if they are keeping or giving the points, and to who, then what the question is and it's answer, it will then ask you if they got the question correct. This prosses repeats until there is no more questions. 

If at any point you want to see the scores of the teams, when it asks "What question do they pick?" just type "score", and it will display the scores.

## Endgame
Upon entering engame the code will display the scores and then exit, if the terminal closes the scores are located in "Data\teaminfo\" in here you will find .txt files for every team, the number stored in there is the score of that team.

This is where the programs stops it's job and you have to do yours.

Before the game started you should have picked some winnging critrea now is the time to figure out the winner, let's say that your criteria was, ```If the dice rolls 1 or 4 highest score wins, if the dice rolls 2 or 5 lowest score wins, and if it rolls 5 or 6 closest score to a prime number wins```. All you would have to do is roll a dice and look at the scores to determin a winner. Congrats you have just played the game of unfair trivia!

## Adding/Changing Questions
###### Changing Questions
By defualt the code comes with two questions:

```
[
    {
        "question#": 1,
        "question": "What is 1+1?",
        "answer": "2",
        "points": -5
    },
    {
        "question#": 2,
        "question": "What is the sqrt of 4?",
        "answer": "2",
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
        "answer": "A programing language",
        "points": 6
    },
    {
        "question#": 2,
        "question": "What is the sqrt of 4?",
        "answer": "2",
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
        "answer": "",
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
        "answer": "3.14",
        "points": -10
    },
```

Now let's add that to our old list:
```
[
    {
        "question#": 1,
        "question": "What is python?",
        "answer": "A programing language",
        "points": 6
    },
    {
        "question#": 2,
        "question": "What is the sqrt of 4?",
        "answer": "2",
        "points": 5
    },
    {
        "question#": 3,
        "question": "What are the first 3 digits of pi?",
        "answer": "3.14",
        "points": -10
    },
    {
        "question#": "done"
    }
]
```
And you are done! Adding more questions past that is as easy as that. 