from typing import List

class Menus:
    main: list = [
        "1. Standard\n",
        "2. Scientific\n",
        "8. Previous History\n",
        "9. Exit Program\n"
    ]

    standard: list = [
        "1. Addition", 
        "2. Subtraction",
        "3. Multiplication",
        "4. Division",
        "5. Square Root",
        "6. Percent",
        "7. Go Back",
        "8. Exit Program"
    ]
    
    scientific: List[dict] = [
        {
            "id": 1,
            "name": "Exponential",
            "options": [
                {
                    "id": 1,
                    "name": "exponentation",
                    "formula": "x^y"
                },
                {
                    "id": 2,
                    "name": "square",
                    "formula": "x^2"
                },
                {
                    "id": 3,
                    "name": "cube",
                    "formula": "x^3"
                },
                {
                    "id": 4,
                    "name": "cube root",
                    "formula": "³√x"
                },
                {
                    "id": 5,
                    "name": "n-th root",
                    "formula": "x^(1/n)"
                },
                {
                    "id": 6,
                    "name": "euler's number raise to the power x",
                    "formula": "e^x"
                }
            ]
        }
    ]
