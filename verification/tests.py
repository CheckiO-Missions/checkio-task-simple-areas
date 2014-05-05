"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": 7.07, "answer": [3]},
{"input": 4, "answer": [2, 2]},
{"input": 6, "answer": [2, 3]},
{"input": 6.0, "answer": [3, 5, 4]},
{"input": 1.5, "answer": [1.5, 2.5, 2]},
    ],
    "Extra": [
        {
            "input": [6, 3],
            "answer": 9,
            "explanation": "6+3=?"
        },
        {
            "input": [6, 7],
            "answer": 13,
            "explanation": "6+7=?"
        }
    ]
}
