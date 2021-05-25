from configparser import ConfigParser
from pathlib import Path
from os import path, system, devnull
from subprocess import Popen, call, STDOUT, PIPE
import git


def execute_git():
    command = 'git init; git add .;git commit -m "initial commit"  '

    if call(["git", "branch"], stderr=STDOUT, stdout=open(devnull, "w")) != 0:
        process = Popen(command, shell=True, stdout=PIPE)
    else:
        print("git already initialize")
        exit()
# https://scuzzlebuzzle:<MYTOKEN>@github.com/scuzzlebuzzle/ol3-1.git
def remote_git(username,token,repo_name):
	url = "https://{username}:{token}@github.com/{username}/{repo_name}.git".format(username=username,token=token,repo_name = repo_name)
	command = "git remote add origin " + url
	process = Popen(command, shell=True, stdout=PIPE)
