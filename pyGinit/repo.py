import click

from github import Github
from github.GithubException import GithubException, BadCredentialsException
from colorama import init, Fore, Style
from os import path, system, devnull
from subprocess import Popen, call, STDOUT, PIPE
from bs4 import BeautifulSoup
import requests

from configparser import ConfigParser
from pathlib import Path
from os import path, system, devnull
from subprocess import Popen, call, STDOUT, PIPE

from .gitCommand import execute_git

init(autoreset=True)
config_obj = ConfigParser()
parser = config_obj.read(path.join(Path.home(), ".pyGinitconfig.ini"))
gh = Github(config_obj["auth"]["token"])
license_dict = {
    "MIT": "mit",
    "Gnu gpl v3": "gpl-3.0",
    "Apache license 2.0": "apache-2.0",
    "Gnu AGPL v3": "agpl-3.0",
    "Mozilla public license 2.0": "mpl-2.0",
}


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


def add_gitignore(gitginore_template,addtional_gitignore,test=False):
    """
    add gitignore template if the parameter is not equal None

            parameters :
                gitginore_template(str) : gitignore template name e.g python,javascript etc
    """
    gitginore_template = gitginore_template.rstrip("\n")  # remove trailing newline
    additional = "\n".join(addtional_gitignore.split(","))
    try:
        if not gitginore_template == "None" and not gitginore_template == "Blank":
            """ download gitignore template from github repository(yeah...repository github account itself) """
            url = f'https://raw.githubusercontent.com/github/gitignore/master/{gitginore_template.strip(" ")}.gitignore'
            gitignore = requests.get(url)
            if test:
                return gitignore.status_code
            open(".gitignore", "w").write(gitignore.content.decode("utf-8")  + additional)
                # gitignore.write()
        elif gitginore_template == "Blank" and not gitginore_template == "None":
            open(".gitignore","w").write(additional if additional else "")
        else:
            pass
    except requests.exceptions.ConnectionError:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error:Connection error when downloading gitginore template"
        )
        exit()


def addLicense(license, test=False):
    try:
        if license != "None":
            url = requests.get(
                f"https://choosealicense.com/licenses/{license_dict[license]}/"
            )
            # if test is true function only return http status code from the url
            if test:
                return url.status_code
            html = BeautifulSoup(url.content, "html.parser")
            license_content = html.find(id="license-text").get_text()
            open("LICENSE", "w").write(license_content)
    except requests.ConnectionError:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error:Connection error when downloading gitginore template"
        )
        exit()


def check_git_exist():
    """
    check wether local git is exist or not
    """
    if call(["git", "branch"], stderr=STDOUT, stdout=open(devnull, "w")) != 0:
        pass
    else:
        if call(["git", "branch"], stderr=STDOUT, stdout=open(devnull, "w")) != 0:
            click.echo("Local repository already exists")
        click.echo(
            "Local repository already exists, pyGinit only accept directory without git"
        )
        exit()


def push_to_remote(repo_name, remote_name):
    # initialize local git and push it to remote
    # if user cancel the pushing process,
    # only remote repository are created(empty repo)
    click.echo("creating repository...Please wait")
    click.echo("pushing file to remote")
    execute_git(
        config_obj["auth"]["username"],
        config_obj["auth"]["token"],
        repo_name,
        remote_name,
    )


def create_repo(*args, command="all"):
    (
        repo_name,
        description,
        remote_name,
        private,
        readme_confirm,
        gitginore_template,
        license,
        additional_gitignore
    ) = args
    private = False if private != "private" else True

    try:
        parser = config_obj.read(path.join(Path.home(), ".pyGinitconfig.ini"))

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

        try:
            repo = gh.get_repo(config_obj["auth"]["username"] + "/" + repo_name)
        except:
            pass  # if repository not exist/get exception it means program can continue
        else:
            click.echo(
                Fore.YELLOW
                + Style.BRIGHT
                + "Remote repository already exist at: "
                + repo.clone_url
            )
            click.echo(Fore.YELLOW + Style.BRIGHT + "Program stopped")
            exit()

        """  
        main parts where remote repositorty are created 
        if exception happen(connection error,wrong inpu etc) repository(local and remote)
        is not created
        """
        # github authorization
        user = gh.get_user()
        # create github repo
        repo = user.create_repo(repo_name, description=description, private=private)
        if command == "all":
            add_readme(readme_confirm, repo_name, description)
            add_gitignore(gitginore_template,additional_gitignore)
            addLicense(license)
        # create_repo(answers.get("repo_name"), answers.get("description"), private)

    except KeyError:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error : github token not found,use set-auth command to set your token"
            " and username"
        )

    #  two exception below are throw when some prompt are not filled or user abort the command
    except AssertionError as e:
        exit()
    except TypeError as e:
        raise e
        exit()
    except BadCredentialsException:
        click.echo(
            Fore.RED
            + Style.BRIGHT
            + "Error : authrization error. have you entered the correct token and"
            " username?"
        )
    # ? How to get github error message?
    except GithubException as e:
        click.echo(Fore.RED + Style.BRIGHT + "Error when creating remote repository")
        click.echo(e)

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

    except AttributeError as e:
        print(e)
    else:

        if repo_name:
            if command == "all":
                push_to_remote(repo_name, remote_name)

            click.echo(
                "repository succesfully created at :"
                + f'https://github.com/{config_obj["auth"]["username"]}/{repo_name.replace(" ","-")}.git'
            )
            click.echo(Fore.GREEN + Style.BRIGHT + "Repository succesfully created 🎉🎉")
        else:
            click.echo("repo name empty")
