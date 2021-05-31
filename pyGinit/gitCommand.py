
from configparser import ConfigParser
from pathlib import Path
from os import path, system, devnull
from subprocess import Popen, call, STDOUT, PIPE
import git

config_obj = ConfigParser()
parser = config_obj.read(path.join(Path.home(), ".pyGinitconfig.ini"))
def execute_git(username,password,repo_name):
    url = "https://{username}:{password}@github.com/{username}/{repo_name}.git".format(
        username=username, repo_name=repo_name,password=password
    )
    repo = git.Repo.init()
    repo.git.add('--all')
    print(url)
    repo.index.commit("initial commit")
    repo.git.push(url,'HEAD:master')