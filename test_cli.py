from pyGinit import main
from click.testing import CliRunner
from configparser import ConfigParser
from pathlib import Path
from os import path

config_obj = ConfigParser()
runner = CliRunner()

def test_set_token_command():
    result = runner.invoke(main.set_auth, ["test_token", "test_username"])
    parser = config_obj.read(path.join(Path.home(), ".pyGinitconfig.ini"))

    assert result.exit_code == 0
    assert config_obj["auth"]["token"] == "test_token"
    assert config_obj["auth"]["username"] == "test_username"


