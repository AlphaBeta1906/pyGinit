from pyGinit import main
from click.testing import CliRunner
from configparser import ConfigParser
from pathlib import Path
from os import path

config_obj = ConfigParser()
runner = CliRunner()

def test_set_token_command():
    result = runner.invoke(main.set_auth, ["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", "AlphaBeta1906"])
    parser = config_obj.read(path.join(Path.home(), ".pyGinitconfig.ini"))

    assert result.exit_code == 0
    assert config_obj["auth"]["token"] == "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"
    assert config_obj["auth"]["username"] == "AlphaBeta1906"

def test_version_output():
	result =  runner.invoke(main.pyGinit,["--version"] )
	assert result.exit_code == 0
	assert '0.1.3' in result.output




