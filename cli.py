import click
import configparser
import requests
import os
import zipfile

function_hub = 'https://repo.cloudstash.io'

def read_config():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config
    except:
        configparser.Error('error')


def deploy_function(filename):
    config = read_config()
    try:
        CONFIG_NAME = config.get('FUNCTION','name')
        CONFIG_VERSION = config.get('FUNCTION','version')
        CONFIG_REPO = config.get('REPOSITORY','repository')
        CONFIG_ORG = config.get('REPOSITORY','org')
        CONFIG_PROVIDER = config.get('RUNTIME','provider')
        CONFIG_RUNTIME = config.get('RUNTIME','runtime')
    except:
        raise KeyError("unsupported key")

    click.secho(f"deploy function {CONFIG_NAME} to repository {CONFIG_REPO}", bold=True)
    
    try:
        r = requests.put(
            f"{function_hub}/{CONFIG_ORG}/{CONFIG_REPO}/{CONFIG_PROVIDER}/{CONFIG_RUNTIME}/{CONFIG_NAME}/{CONFIG_VERSION}/{CONFIG_NAME}-{CONFIG_VERSION}.zip",
            files={'file': open(filename,'rb')},
            headers={'content-type':'application/zip'}
        )
        click.echo(r.text)
    except:
        requests.exceptions.RequestException

def package_function(filename):
    if os.path.isdir(filename):
        print('pack repo')
    else:
        raise click.ClickException(f"folder {filename} cannot be found")

def create_function(filename):
    try:
        os.mkdir(filename)
        config_file = open('resources/config.ini', 'r')
        # project_config = open(f"{filename}/config.ini", 'w')
        for line in config_file.readlines():
            # project_config.write(line)
            print(line)
        
        config_file.close()
        # project_config.close()
    except FileExistsError():
        raise click.ClickException('project already exist')
    except OSError as err:
        raise click.ClickException(err)

        
@click.command()
@click.argument('method')
@click.argument('filename')
def main(method,filename):
    if method.lower() == 'deploy':
        deploy_function(filename)
    elif method.lower() == 'package':
        package_function(filename)
    elif method.lower() == 'create':
        create_function(filename)
    else:
        raise click.ClickException("wrong parameter. Supported parameter is deploy")
