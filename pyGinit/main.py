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

# TODO : add ssh
# TODO : user can custom remote name

@click.group()
@click.version_option("0.2.0", help="Show version")
def pyGinit():
    """pyGinit a simple cli automation tools
    to initalize both local and remote repository

    version : 0.2.0
    """
    pass


def add_readme(add_readme, title, description=""):
    """
    add  readme if description parameter is not null
    """
    if add_readme:
        file = open("README.md", "w")
        file.writelines(["# " + title + "\n", "\n" + description])
        file.close()
    else:
        pass


def add_gitignore(gitginore_template):
    """
    add gitignore template if the parameter is not equal None

            parameters :
                gitginore_template(str) : gitignore template name e.g python,javascript etc         
    """
    gitginore_template = gitginore_template.rstrip("\n")  # remove trailing newline
    try:
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
    except requests.exceptions.ConnectionError:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error:Connection error when downloading .gitginore template"
        )
        exit()


@pyGinit.command()
def init():
    """ initialize local git repository and create remote github repository """
    answers = prompt(questions, style=custom_style_2)
    private = True if answers.get("repo_type") == "private" else False
    parser = config_obj.read(path.join(Path.home(), ".pyGinitconfig.ini"))
    url_check = "https://github.com/{username}/{repo_name}".format(
        username=config_obj["auth"]["username"], repo_name=answers.get("repo_name")
    )
    if call(["git", "branch"], stderr=STDOUT, stdout=open(devnull, "w")) != 0:
        pass
    else:
        if call(["git", "branch"], stderr=STDOUT, stdout=open(devnull, "w")) != 0:
            click.echo(
                "Local repository already exists"
            )
        click.echo("program stopped")
        exit()
    try:
        # check both remote and local repository are exist
        # if not program will continue

        """
        if statment must tell if one or both local and remote already exist
        example :
                if local yes & remote no => create remote only
                if local no  & remote yes => create local only
                        if both yes => program will stop...
        ...maybe in future
        for now let's just use these code below
        """

        """  
        main parts where remote repositorty are created 
        if exception happen(connection error,wrong inpu etc) repository(local and remote)
        is not created
        """

        # add readme
        add_readme(
            answers.get("readme_confirm"),
            answers.get("repo_name"),
            answers.get("description"),
        )

        add_gitignore(answers.get("gitginore_template"))# add gitignore

        #github authorization
        gh = Github(config_obj["auth"]["token"])
        user = gh.get_user()
        # create github repo
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
    #? How to get github error message?
    except GithubException as e:
        click.echo(Fore.RED + Style.BRIGHT + "Error when creating remote repository")
        raise e

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
        click.echo("creating repository...Please wait")
        click.echo("pushing file to remote")
        execute_git(
            config_obj["auth"]["username"],
            config_obj["auth"]["token"],
            answers.get("repo_name"),
        )
        click.echo(Fore.GREEN + Style.BRIGHT + "Repository succesfully created 🎉🎉")


@pyGinit.command(options_metavar="<options>")
@click.argument("token", metavar="<github_token>")
@click.argument("username", metavar="<github_username>")
def set_auth(token, username):
    """ set your github token and username """
    try:
        config_obj["auth"] = {
            "token": token,
            "username": username,
        }
        with open(path.join(Path.home(), ".pyGinitconfig.ini"), "w") as conf:
            config_obj.write(conf)
    except Exception as e:
        print(e)
