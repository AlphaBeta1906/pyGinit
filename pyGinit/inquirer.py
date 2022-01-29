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
    {"type": "input", "name": "repo_name", "message": "Enter the name of your repo : "},
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
        "choices": [g.split(".")[0] for g in gitignore],
    },
    {
        "type": "list",
        "name": "license_name",
        "message": "choose a license",
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
        "message": "input your remote name name(default:origin)",
    },
]
