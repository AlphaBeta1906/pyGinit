from prompt_toolkit.validation import Validator, ValidationError
import os
import sys

file = open(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "gitignore-list.txt"), "r"
)
arr = []
for text in file:
    arr.append(text.replace(".gitignore", " "))


questions = [
    {
        "type": "input",
        "name": "repo_name",
        "message": "Enter the name for your repo : ",
    },
    {
        "type": "input",
        "name": "description",
        "message": "Enter description of your repo (leave blank if you dont have one) : ",
    },
    {
        "type": "list",
        "name": "repo_type",
        "message": "select your github repo type",
        "choices": ["public", "private"],
    },
    {
        "type": "list",
        "name": "gitginore_template",
        "message": "Select gitginore template for your repo",
        "choices": arr,
    },
    {
        "type": "confirm",
        "name": "readme_confirm",
        "message": "Do you want to create readme for your repo ? ",
    },
]
