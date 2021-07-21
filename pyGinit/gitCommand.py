from configparser import ConfigParser
from pathlib import Path
from os import path, system, devnull
from subprocess import Popen, call, STDOUT, PIPE
import git

config_obj = ConfigParser()
parser = config_obj.read(path.join(Path.home(), ".pyGinitconfig.ini"))


def execute_git(username, token, repo_name,remote_name):
    """
    initialize git repository and push to remote
    """
    remote_name = "origin" if not remote_name else remote_name
    url = "https://{username}:{token}@github.com/{username}/{repo_name}.git".format(
        username=username, repo_name=repo_name.replace(" ", "-"), token=token
    )
    repo = git.Repo.init()
    repo.git.add("--all")
    repo.index.commit("initial commit")
    repo.git.push(url, "HEAD:master")
    repo.create_remote(remote_name, url)
    print("remote name :"+ remote_name+ "\nurl :" + url)
