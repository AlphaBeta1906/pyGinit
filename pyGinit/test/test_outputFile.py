from pyGinit.main import add_readme, add_gitignore
import os

def test_add_readme():
	add_readme(True,"Test")
	assert open("README.md").read() == "Test"
	os.remove("README.md")

def tes_add_gitignore():
	add_gitignore("Ada")
	assert open(".gitignore").read() != "__pycache__/"