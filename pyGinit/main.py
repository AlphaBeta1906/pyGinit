import click

from github import Github
from PyInquirer import prompt, style_from_dict, Token
from examples import custom_style_2
from colorama import init, Fore, Style
from configparser import ConfigParser

from pathlib import Path
from os import path


from .inquirer import questions
from .repo import create_repo, check_git_exist

init(autoreset=True)
config_obj = ConfigParser()
parser = config_obj.read(path.join(Path.home(), ".pyGinitconfig.ini"))

# TODO : add option command so user can initiazlize with only one line
# TODO : add ssh
# TODO : maybe add support for code host other than github,like gitlab,gitbucket etc


@click.group()
@click.version_option("0.3.1", help="Show version")
def pyginit():
    """pyGinit a simple cli automation tools
    to initalize both local and github remote repository

    version : 0.3.1
    """
    pass


@pyginit.command()
def init():
    """initialize local git repository and create remote github repository"""

    # check local repository are exist
    check_git_exist()
    answers = prompt(questions, style=custom_style_2)
    create_repo(
        answers.get("repo_name"),
        answers.get("description"),
        answers.get("remote_name"),
        answers.get("repo_type"),
        answers.get("readme_confirm"),
        answers.get("gitginore_template"),
        answers.get("license_name"),
        answers.get("additional_gitignore")
    )


@pyginit.command()
def remote():
    """create empty github repository only"""
    answers = prompt(questions[0:3], style=custom_style_2)
    create_repo(
        answers.get("repo_name"),
        answers.get("description"),
        answers.get("remote_name"),
        answers.get("repo_type"),
        None,
        None,
        None,
        None,
        command="remote",
    )


@pyginit.command()
@click.argument("token", metavar="<github_token>")
@click.argument("username", metavar="<github_username>")
def set_auth(token, username):
    """set your github token and username"""
    try:
        config_obj["auth"] = {"token": token, "username": username}
        with open(path.join(Path.home(), ".pyGinitconfig.ini"), "w") as conf:
            config_obj.write(conf)
    except Exception as e:
        print(e)
