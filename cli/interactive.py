from InquirerPy import prompt
from InquirerPy.base.control import Choice

def userQuaries():
    questions = [
        {
            "type": "list",
            "message": "what Backend framework are you using:",
            "choices": [
                Choice("express", name="Express (JavaScript)"),
                Choice("fastapi", name="FastAPI (Python)"),
                Choice("flask", name="Flask (Python)"),
            ],
            "name": "backend",
        },
        {
            "type": "list",
            "message": "what frontend framework are you using:",
            "choices": [
                Choice("react", name="React (JavaScript)"),
                Choice("nextjs", name="Next.js (JavaScript)"),
            ],
            "name": "frontend",
        },
    ]

    return prompt(questions)

def detectFramework():

    questions = [
        {
            "type": "confirm",
            "message": "Do you know which frameworks you are using",
            "name": "detect",
            "default": True,
        },
    ]

    return prompt(questions)["detect"]