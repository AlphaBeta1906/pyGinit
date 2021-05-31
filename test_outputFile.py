from pyGinit import main
import os
import git

def test_add_readme():
    main.add_readme(True, "Test")
    assert open("README.md").read() == "Test"
    os.remove("README.md")


def test_add_gitignore():
    main.add_gitignore("Python")
    assert "__pycache__/" in open(".gitignore").read() 
