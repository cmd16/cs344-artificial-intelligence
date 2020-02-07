from gps import gps

problem = {
    "start": ["wolf at a", "goat at a", "cabbage at a", "farmer at a"],
    "finish": ["wolf at b", "goat at b", "cabbage at b", "farmer at b"],

    "ops": [
        {
            "action": "move wolf from a to b",
            "preconds": [
                "wolf at a",
                "farmer at a"
            ],
            "add": [
                "wolf at b",
                "farmer at b"
            ],
            "delete": [
                "wolf at a",
                "farmer at a"
            ]
        },
        {
            "action": "move goat from a to b",
            "preconds": [
                "goat at a",
                "farmer at a"
            ],
            "add": [
                "goat at b",
                "farmer at b"
            ],
            "delete": [
                "goat at a",
                "farmer at a"
            ]
        },
        {
            "action": "move cabbage from a to b",
            "preconds": [
                "cabbage at a",
                "farmer at a"
            ],
            "add": [
                "cabbage at b",
                "farmer at b"
            ],
            "delete": [
                "cabbage at a",
                "farmer at a"
            ]
        },
        {
            "action": "move wolf from b to a",
            "preconds": [
                "wolf at b",
                "farmer at b"
            ],
            "add": [
                "wolf at a",
                "farmer at a"
            ],
            "delete": [
                "wolf at b",
                "farmer at b"
            ]
        },
        {
            "action": "move goat from b to a",
            "preconds": [
                "goat at b",
                "farmer at b"
            ],
            "add": [
                "goat at a",
                "farmer at a"
            ],
            "delete": [
                "goat at b",
                "farmer at b"
            ]
        },
        {
            "action": "move cabbage from b to a",
            "preconds": [
                "cabbage at b",
                "farmer at b"
            ],
            "add": [
                "cabbage at a",
                "farmer at a"
            ],
            "delete": [
                "cabbage at b",
                "farmer at b"
            ]
        },
    ]
}