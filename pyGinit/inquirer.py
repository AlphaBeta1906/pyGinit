from prompt_toolkit.validation import Validator, ValidationError
from .gitignoreList import gitignore
import os
import sys

questions = [
    {
        "type": "input",
        "name": "repo_name",
        "message": "Enter the name of your repo : ",
    },
    {
        "type": "input",
        "name": "description",
        "message": "Enter description of your repo (optional) : ",
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
        "choices": gitignore,
    },
    {
        "type": "confirm",
        "name": "readme_confirm",
        "message": "Do you want to create readme for your repo ? ",
    },
]
