import click
from PyInquirer import prompt
from examples import custom_style_3
from inquirer import questions
from github import Github
from github.GithubException import  GithubException
from colorama import init, Fore, Style
init()

@click.group()
def pyGinit():
	pass

@pyGinit.command()
def init():
	"""initialize local git repo and create remote github repository for it"""
	answers = prompt(questions, style=custom_style_3)
	username = answers.get("username")
	password = answers.get("password")
	repo_type = True if answers.get("repo_type") == "private" else False
	gh = Github(answers.get("token"))
	try:
		user = gh.get_user()
		repo = user.create_repo(answers.get("repo_name"), description = answers.get("description"),private = repo_type)
		click.echo(Fore.GREEN+Style.BRIGHT+"Repository succesfully created 🎉🎉")
	except GithubException:
		click.echo(Fore.RED+Style.BRIGHT+"Error : authrization error")