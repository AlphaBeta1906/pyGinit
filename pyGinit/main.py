import click
from PyInquirer import prompt
from examples import custom_style_2
from .inquirer import questions
from github import Github
from github.GithubException import GithubException, BadCredentialsException
from colorama import init, Fore, Style
from configparser import ConfigParser
from pathlib import Path
from os import path
import requests.exceptions


init()
config_obj = ConfigParser()


@click.group()
@click.version_option("v0.1")
def pyGinit():
    pass


def add_readme(add_readme, description=""):
    if add_readme:
        file = open("README.md", "w")
        file.write(description)
        file.close()
    else:
        pass


def add_gitignore(gitginore_template):
    """need fix """
    gitginore_template = gitginore_template.rstrip("\n")  # remove trailing newline

    if not gitginore_template == "None":
        url = (
            "https://raw.githubusercontent.com/github/gitignore/master/"
            + gitginore_template.strip(" ")
            + ".gitignore"
        )
        """ download gitignore template from github repository """
        dowonload = requests.get(url)
        open(".gitignore", "wb").write(dowonload.content)
    elif gitginore_template == ".gitignore":
        open(".gitignore").close()
    else:
        pass


@pyGinit.command()
def init():
    """initialize local git repo and create remote github repository for it"""
    answers = prompt(questions, style=custom_style_2)
    private = True if answers.get("repo_type") == "private" else False
    # print(answers.get("description"))
    parser = config_obj.read(path.join(Path.home(),".pyGinitconfig.ini"))
    print(config_obj["auth"]["token"])

    try:
        gh = Github(config_obj["auth"]["token"])

        add_readme(answers.get("readme_confirm"), answers.get("description"))
        add_gitignore(answers.get("gitginore_template"))

        # user = gh.get_user()
        # repo = user.create_repo(answers.get("repo_name"), description = answers.get("description"),private = private)

        click.echo(Fore.GREEN + Style.BRIGHT + "Repository succesfully created 🎉🎉")
    except BadCredentialsException:
        click.echo(Fore.RED + Style.BRIGHT + "Error : authrization error")
    except KeyError:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error : github token not found use set-token command to set your token"
        )
    except AssertionError:
        pass
    except TypeError:
        pass
    except GithubException:
        click.echo(Fore.RED + Style.BRIGHT + "Error : repo name too short")
    except requests.exceptions.ConnectionError:
        click.echo(Fore.RED + Style.BRIGHT + "Error : connection error")
    except requests.exceptions.ConnectTimeout:
        click.echo(Fore.RED + Style.BRIGHT + "Error : connection timeout")


@pyGinit.command()
@click.argument("token")
@click.argument("username")
def set_auth(token,username):
    """ set your github token and username """
    # https://scuzzlebuzzle:<MYTOKEN>@github.com/scuzzlebuzzle/ol3-1.git
    try:
        config_obj["auth"] = {"token": token,"username" : username}
        with open(path.join(Path.home(),".pyGinitconfig.ini"), "w") as conf:
            config_obj.write(conf)
    except Exception as e:
        print(e)
