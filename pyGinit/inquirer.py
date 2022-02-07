from prompt_toolkit.validation import Validator, ValidationError
from .gitignoreList import gitignore

class InputValidator(Validator):
    def validate(self,document):
        if not document.text:
            raise ValidationError(
                message="Repo name must not empty",
                cursor_position=len(document.text))  # Move cursor to end            

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
        "validate": InputValidator
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
