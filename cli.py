import click
import configparser
import requests

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
    


@click.command()
@click.argument('method')
@click.argument('filename')
def main(method,filename):
    if method.lower() == 'deploy':
        deploy_function(filename)
    elif method.lower() == 'package':
        package_function(filename)
    else:
        raise click.ClickException("wrong parameter. Supported parameter is deploy")
