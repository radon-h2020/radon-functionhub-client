from functionhub.main import fuhub
from click.testing import CliRunner

test_folder = 'example'

def test_create_folder():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['create','test'])

    assert result.output == f"project test successfully created\n"

def test_create_existing_folder():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['create',test_folder])

    assert result.exception

def test_create_package():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['package',test_folder])

    assert result.exit_code == 0

def test_create_nonexisting_package():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['package', 'nofolder'])

    assert result.exception

def test_upload_package():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['-f', 'example/config.ini', 'upload',f"{test_folder}.zip"])

    assert result.output == f"upload function hello-world to repository my-public-functions\nSize limitation, consider a paid subscription\n"

def test_upload_package_with_missing_config_file():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['upload',f"{test_folder}.zip"])

    assert result.exception
