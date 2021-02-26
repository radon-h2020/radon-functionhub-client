from typing import Match
from functionhub.main import fuhub
from click.testing import CliRunner
from click.exceptions import ClickException
import pytest
import os
import shutil

test_folder = 'example'

def test_create_folder():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['create','test'])

    assert result.output == f"project test successfully created\n"
    #CLEANUP
    shutil.rmtree('test')

def test_create_existing_folder():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['create',test_folder])

    assert result.exception

def test_create_package():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['package',test_folder])

    assert result.exit_code == 0
    #CLEANUP
    os.remove(f"{test_folder}.zip")

def test_create_nonexisting_package():
        runner = CliRunner()
        result = runner.invoke(fuhub, ['package', 'nofolder'])
        assert result.exit_code == 2

def test_upload_package():
    runner = CliRunner()
    runner.invoke(fuhub, ['package',test_folder])
    result = runner.invoke(fuhub, ['-f', 'example/config.ini', 'upload',f"{test_folder}.zip"])

    assert result.output == f"upload function hello-world to repository my-public-functions\nauthentication error\n"
    #CLEANUP
    os.remove(f"{test_folder}.zip")

def test_upload_nonexisting_package():
    runner = CliRunner()
    result = runner.invoke(fuhub, ['-f', 'example/config.ini', 'upload',f"{test_folder}.zip"])

    assert result.exception

def test_upload_package_with_missing_config_file():
    runner = CliRunner()
    runner.invoke(fuhub, ['package',test_folder])
    result = runner.invoke(fuhub, ['upload',f"{test_folder}.zip"])
    assert result.output == "Error: Config file could not be found\n"
