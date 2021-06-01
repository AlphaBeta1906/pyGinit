import click
from PyInquirer import prompt
from examples import custom_style_2
from github import Github
from github.GithubException import GithubException, BadCredentialsException
from colorama import init, Fore, Style
from configparser import ConfigParser
from pathlib import Path
from os import path, system, devnull
from subprocess import Popen, call, STDOUT, PIPE
import requests
import time

from .gitCommand import execute_git
from .inquirer import questions

init()
config_obj = ConfigParser()


@click.group()
@click.version_option("0.1.3", help="Show version")
def pyGinit():
    """title"""
    pass


def add_readme(add_readme, description=""):
    if add_readme:
        file = open("README.md", "w")
        file.write(description)
        file.close()
    else:
        pass


def add_gitignore(gitginore_template):
    gitginore_template = gitginore_template.rstrip("\n")  # remove trailing newline

    if not gitginore_template == "None":
        url = (
            "https://raw.githubusercontent.com/github/gitignore/master/"
            + gitginore_template.strip(" ")
            + ".gitignore"
        )
        """ download gitignore template from github repository(yeah...repository github account itself) """
        dowonload = requests.get(url)
        open(".gitignore", "wb").write(dowonload.content)
    elif gitginore_template == ".gitignore":
        open(".gitignore").close()
    else:
        pass


@pyGinit.command()
def init():
    """ initialize local git repository and create remote github repository """
    answers = prompt(questions, style=custom_style_2)
    private = True if answers.get("repo_type") == "private" else False
    # print(answers.get("description"))
    parser = config_obj.read(path.join(Path.home(), ".pyGinitconfig.ini"))

    try:
        # check both remote and local repository are exist
        # if not program will continue

        """
        if statment must tell if one or both local and remote already exist
        example : if local yes & remote no => create remote only
                  if local no  & remote yes => create local only
                  if both yes => program will stop...
        ...maybe in future

        for now let's just use this code below
        """
        url_check = "https://github.com/{username}/{repo_name}".format(
            username=config_obj["auth"]["username"], repo_name=answers.get("repo_name")
        )
        if (
            call(["git", "branch"], stderr=STDOUT, stdout=open(devnull, "w")) != 0
            or not requests.get(url_check).status_code
        ):
            pass
        else:
            click.echo(
                "Local repository already exists, you can use pyGinit remote to create remote only"
            )
            click.echo("program stopped")

            exit()

        """  
        main parts where remote repositorty are created 
        if exception happen(connection error,wrong inpu etc) repository(local and remote)
        is not created
        """
        gh = Github(config_obj["auth"]["token"])
        # uncomment only when testing
        user = gh.get_user()
        repo = user.create_repo(
            answers.get("repo_name"),
            description=answers.get("description"),
            private=private,
        )

    except KeyError:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error : github token not found,use set-auth command to set your token and username"
        )


    #  two exception below are throw when some prompt are not filled or user abort the command
    except AssertionError:
        exit()
    except TypeError:
        exit()

    except BadCredentialsException:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error : authrization error. have you entered the correct token and username?"
        )

    except GithubException:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error : repository name too short, minimum name length is 1 character"
        )

    except requests.exceptions.ConnectionError:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error : Connection error.Are you connnect to internet?"
        )
    except requests.exceptions.ConnectTimeout:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error : Connection timeout.Please check your internet connetion"
        )
    except requests.exceptions.ReadTimeout:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error : Connection timeout.Please check your internet connetion"
        )
    except AttributeError:
        pass
    else:
        add_readme(answers.get("readme_confirm"), answers.get("description"))
        add_gitignore(answers.get("gitginore_template"))
        execute_git(
            config_obj["auth"]["username"],
            config_obj["auth"]["password"],
            answers.get("repo_name"),
        )
        click.echo(Fore.GREEN + Style.BRIGHT + "Repository succesfully created 🎉🎉")


# should i create this ?
@pyGinit.command()
def init_remote():
    """ only create empty github repository """
    click.echo("initialize remote repo only")


@pyGinit.command(options_metavar="<options>")
@click.argument("token", metavar="<github_token>")
@click.argument("username", metavar="<github_username>")
@click.argument("password", metavar="<github_password>")
def set_auth(token, username, password):
    """ set your github token and username """
    try:
        config_obj["auth"] = {
            "token": token,
            "username": username,
            "password ": password,
        }
        with open(path.join(Path.home(), ".pyGinitconfig.ini"), "w") as conf:
            config_obj.write(conf)
    except Exception as e:
        print(e)
