"""
An implementation of the wolf goat cabbage problem (see https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem).
The farmer can carry one thing at a time from side a to side b (or side b to side a) and needs to carry all three things
from a to b without leaving the wolf alone with the goat or the goat alone with the cabbage.

Correct solution:
1. Take the goat to b
2. go to a
3. Take the wolf or cabbage to b
4. Take the goat to a
5. Take the thing that was not taken in step 3 to b
6. go to a
7. Take goat to b

gps can't figure out this one because step 4 doesn't make sense to the narrow-minded gps - you get further away from your goal.
"""

from gps import gps

problem = {
    "start": ["wolf at a", "goat at a", "cabbage at a", "farmer at a", "wolf with goat", "goat with cabbage"],
    "finish": ["wolf at b", "goat at b", "cabbage at b", "farmer at b"],

    "ops": [
        {
            "action": "move farmer from a to b",
            "preconds": [
                "farmer at a",
                "wolf not with goat",
                "goat not with cabbage"
            ],
            "add": [
                "farmer at b"
            ],
            "delete": [
                "farmer at a"
            ]
        },
        {
            "action": "move farmer from b to a",
            "preconds": [
                "farmer at b",
                "wolf not with goat",
                "goat not with cabbage"
            ],
            "add": [
                "farmer at a"
            ],
            "delete": [
                "farmer at b"
            ]
        },
        {
            "action": "move wolf from a to b when goat is at a",
            "preconds": [
                "wolf at a",
                "farmer at a",
                "goat at a",
                "goat not with cabbage"
            ],
            "add": [
                "wolf at b",
                "farmer at b",
                "wolf not with goat"
            ],
            "delete": [
                "wolf at a",
                "farmer at a",
                "wolf with goat"
            ]
        },
        {
            "action": "move wolf from a to b when goat is at b",
            "preconds": [
                "wolf at a",
                "farmer at a",
                "goat at a",
                "goat not with cabbage"
            ],
            "add": [
                "wolf at b",
                "farmer at b",
                "wolf with goat"
            ],
            "delete": [
                "wolf at a",
                "farmer at a",
                "wolf not with goat"
            ]
        },
        {
            "action": "move goat from a to b when wolf at a and cabbage at a",
            "preconds": [
                "goat at a",
                "farmer at a",
                "wolf at a",
                "cabbage at a"
            ],
            "add": [
                "goat at b",
                "farmer at b",
                "wolf not with goat",
                "goat not with cabbage"
            ],
            "delete": [
                "goat at a",
                "farmer at a",
                "wolf with goat",
                "goat with cabbage"
            ]
        },
        {
            "action": "move goat from a to b when wolf at a and cabbage at b",
            "preconds": [
                "goat at a",
                "farmer at a",
                "wolf at a",
                "cabbage at b"
            ],
            "add": [
                "goat at b",
                "farmer at b",
                "wolf not with goat"
                "goat with cabbage"
            ],
            "delete": [
                "goat at a",
                "farmer at a",
                "wolf with goat",
                "goat not with cabbage"
            ]
        },
        {
            "action": "move goat from a to b when wolf at b and cabbage at b",
            "preconds": [
                "goat at a",
                "farmer at a",
                "wolf at b",
                "cabbage at b"
            ],
            "add": [
                "goat at b",
                "farmer at b",
                "wolf with goat",
                "goat with cabbage"
            ],
            "delete": [
                "goat at a",
                "farmer at a",
                "wolf not with goat",
                "goat not with cabbage"
            ]
        },
        {
            "action": "move goat from a to b when wolf at b and cabbage at a",
            "preconds": [
                "goat at a",
                "farmer at a",
                "wolf at b",
                "cabbage at a"
            ],
            "add": [
                "goat at b",
                "farmer at b",
                "wolf with goat",
                "goat not with cabbage"
            ],
            "delete": [
                "goat at a",
                "farmer at a",
                "wolf not with goat",
                "goat with cabbage"
            ]
        },
        {
            "action": "move cabbage from a to b when goat at a",
            "preconds": [
                "cabbage at a",
                "farmer at a",
                "wolf not with goat",
                "goat at a"
            ],
            "add": [
                "cabbage at b",
                "farmer at b",
                "goat not with cabbage"
            ],
            "delete": [
                "cabbage at a",
                "farmer at a",
                "goat with cabbage"
            ]
        },
        {
            "action": "move cabbage from a to b when goat at b",
            "preconds": [
                "cabbage at a",
                "farmer at a",
                "wolf not with goat",
                "goat at b"
            ],
            "add": [
                "cabbage at b",
                "farmer at b",
                "goat with cabbage"
            ],
            "delete": [
                "cabbage at a",
                "farmer at a",
                "goat not with cabbage"
            ]
        },
        {
            "action": "move wolf from b to a when goat is at a",
            "preconds": [
                "wolf at b",
                "farmer at b",
                "goat at a",
                "goat not with cabbage"
            ],
            "add": [
                "wolf at a",
                "farmer at a",
                "wolf with goat"
            ],
            "delete": [
                "wolf at b",
                "farmer at b",
                "wolf not with goat"
            ]
        },
        {
            "action": "move wolf from b to a when goat is at b",
            "preconds": [
                "wolf at b",
                "farmer at b",
                "goat at b",
                "goat not with cabbage"
            ],
            "add": [
                "wolf at a",
                "farmer at a",
                "wolf not with goat"
            ],
            "delete": [
                "wolf at b",
                "farmer at b",
                "wolf with goat"
            ]
        },
        {
            "action": "move goat from b to a when wolf at a and cabbage at a",
            "preconds": [
                "goat at b",
                "farmer at b",
                "wolf at a",
                "cabbage at a"
            ],
            "add": [
                "goat at a",
                "farmer at a",
                "wolf with goat",
                "goat with cabbage"
            ],
            "delete": [
                "goat at b",
                "farmer at b",
                "goat not with wolf",
                "goat not with cabbage"
            ]
        },
        {
            "action": "move goat from b to a when wolf at a and cabbage at b",
            "preconds": [
                "goat at b",
                "farmer at b",
                "wolf at a",
                "cabbage at b"
            ],
            "add": [
                "goat at a",
                "farmer at a",
                "wolf with goat",
                "goat not with cabbage"
            ],
            "delete": [
                "goat at a",
                "farmer at a",
                "wolf not with goat",
                "goat with cabbage"
            ]
        },
        {
            "action": "move goat from b to a when wolf at b and cabbage at b",
            "preconds": [
                "goat at b",
                "farmer at b",
                "wolf at b",
                "cabbage at b"
            ],
            "add": [
                "goat at a",
                "farmer at a",
                "wolf not with goat",
                "goat not with cabbage"
            ],
            "delete": [
                "goat at a",
                "farmer at a",
                "wolf with goat",
                "goat with cabbage"
            ]
        },
        {
            "action": "move goat from b to a when wolf at b and cabbage at a",
            "preconds": [
                "goat at b",
                "farmer at b",
                "wolf at b",
                "cabbage at a"
            ],
            "add": [
                "goat at a",
                "farmer at a",
                "wolf not with goat",
                "goat with cabbage"
            ],
            "delete": [
                "goat at b",
                "farmer at b",
                "wolf with goat",
                "goat not with cabbage"
            ]
        },
        {
            "action": "move cabbage from b to a when goat at a",
            "preconds": [
                "cabbage at b",
                "farmer at b",
                "wolf not with goat",
                "goat at a"
            ],
            "add": [
                "cabbage at a",
                "farmer at a",
                "goat with cabbage"
            ],
            "delete": [
                "cabbage at b",
                "farmer at b",
                "goat not with cabbage"
            ]
        },
        {
            "action": "move cabbage from b to a when goat at b",
            "preconds": [
                "cabbage at b",
                "farmer at b",
                "wolf not with goat",
                "goat at b"
            ],
            "add": [
                "cabbage at a",
                "farmer at a",
                "goat not with cabbage"
            ],
            "delete": [
                "cabbage at a",
                "farmer at a",
                "goat with cabbage"
            ]
        },
    ]
}

def main():
    start = problem['start']
    finish = problem['finish']
    ops = problem['ops']
    actionSequence = gps(start, finish, ops)
    if actionSequence is None:
        print("plan failure...")
        return
    for action in actionSequence:
        print(action)

if __name__ == '__main__':
    main()
