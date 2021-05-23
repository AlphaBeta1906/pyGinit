from pyGinit import main
import os

def test_add_readme():
	main.add_readme(True,"Test")
	assert open("README.md").read() == "Test"
	os.remove("README.md")

def tes_add_gitignore():
	main.add_gitignore("Ada")
	assert open(".gitignore").read() != "__pycache__/"