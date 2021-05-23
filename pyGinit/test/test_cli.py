from pyGinit.main import set_auth
from click.testing import CliRunner
from configparser import ConfigParser
from pathlib import Path
from os import path

config_obj = ConfigParser()
def test_set_token_command():
   runner = CliRunner()
   result = runner.invoke(set_auth, ['test_token','test_username'])
   parser = config_obj.read(path.join(Path.home(),".pyGinitconfig.ini"))

   assert result.exit_code == 0
   assert config_obj["auth"]["token"] == "test_token"
   assert config_obj["auth"]["username"] == "test_username"
   