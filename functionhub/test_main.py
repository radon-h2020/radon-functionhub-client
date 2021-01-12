from functionhub.main import fuhub, Global
from click.testing import CliRunner

test_folder = 'test'

def test_create_folder():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['create','test'])

    assert result.output == f"project {test_folder} successfully created\n"

def test_create_package():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['package','test'])

    assert result.exit_code == 0

def test_upload_package():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['upload',f"{test_folder}.zip"])

    assert result.output == f"upload function  to repository \n502\n"