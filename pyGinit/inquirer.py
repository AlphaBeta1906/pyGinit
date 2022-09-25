from prompt_toolkit.validation import Validator, ValidationError
from .gitignoreList import gitignore

  licenses = [
    "None",
    "MIT",
    "Gnu gpl v3",
    "Apache license 2.0",
    "Gnu AGPL v3",
    "Mozilla public license 2.0",
]

questions = [
    {
        "type": "input", 
        "name": "repo_name", 
        "message": "Enter the name of your repo : ",
        "validate": lambda result: len(result) > 0,
        "invalid_message": "repo name cannot empty",
        "transformer": lambda result: result.replace(" ","-")
    },
    {
        "type": "input",
        "name": "description",
        "message": "Enter description of your repo (optional) : ",
    },
    {
        "type": "list",
        "name": "repo_type",
        "message": "Select your github repo type",
        "choices": ["public", "private"],
    },
    {
        "type": "list",
        "name": "gitginore_template",
        "message": "Select gitginore template for your repo",
        "choices": [g.split(".")[0] for g in gitignore],
    },
    {
        "type": "input",
        "name": "additional_gitignore",
        "message": "Additional gitignore separated by comma(e.g: dist/,file.py,*.py)skip if gitgnore template is None : ",
        "when": lambda result: result["gitginore_template"] != "None",
    },
    {
        "type": "list",
        "name": "license_name",
        "message": "Choose a license",
        "choices": licenses,
    },
    {
        "type": "confirm",
        "name": "readme_confirm",
        "message": "Do you want to create readme for your repo ? ",
    },
    {
        "type": "input",
        "name": "remote_name",
        "message": "input your remote name name(default:origin) : ",
    },
]
