from src import main
from click.testing import CliRunner
from configparser import ConfigParser
from pathlib import Path
from os import path
import git

config_obj = ConfigParser()
runner = CliRunner()

def test_set_token_command():
    result = runner.invoke(main.set_auth, ["test_token", "test_username","test_password"])
    parser = config_obj.read(path.join(Path.home(), ".pyGinitconfig.ini"))

    assert result.exit_code == 0
    assert config_obj["auth"]["token"] == "test_token"
    assert config_obj["auth"]["username"] == "test_username"
    assert config_obj["auth"]["password"] == "test_password"

def test_version_output():
	result =  runner.invoke(main.pyGinit,["--version"] )
	assert result.exit_code == 0
	assert '0.1.7' in result.output




