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
        {"input": [3], "answer": 7.07},
        {"input": [2, 2], "answer": 4},
        {"input": [2, 3], "answer": 6},
        {"input": [3, 5, 4], "answer": 6.0},
        {"input": [1.5, 2.5, 2], "answer": 1.5},
    ],
    "Extra": [
        {"input": [1], "answer": 0.79},
        {"input": [1000], "answer": 785398.16},
        {"input": [1, 10], "answer": 10},
        {"input": [1000, 1000], "answer": 1000000},
        {"input": [1, 1, 1], "answer": 0.43},
        {"input": [10, 2, 9], "answer": 8.18},
        {"input": [100, 200, 200], "answer": 9682.46},
        {"input": [10, 8, 6], "answer": 24},
        {"input": [3.14], "answer": 7.74},
        {"input": [0.58, 0.21], "answer": 0.12},
        {"input": [6.7, 3.14, 5.77], "answer": 9.05},
    ]
}
