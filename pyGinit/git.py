from configparser import ConfigParser
from pathlib import Path
from os import path, system, devnull
from subprocess import Popen, call, STDOUT, PIPE


def execute_git():
    command = 'git init; git add .;git commit -m "initial commit"  '

    if call(["git", "branch"], stderr=STDOUT, stdout=open(devnull, "w")) != 0:
        process = Popen(command, shell=True, stdout=PIPE)
    else:
        print("git already initialize")
        exit()
