import click
import configparser
import requests
import os
import base64
import zipfile
import errno

from configparser import Error

# global class with all global data
class Global(object):
    def __init__(self, endpoint, debug):
        self.endpoint = endpoint
        self.debug = debug

def read_config(config_file):
    try:
        config = configparser.ConfigParser()
        config.read(config_file)
        return config
    except:
        configparser.Error('error')

def package_function(filename):
    if os.path.isdir(filename):
        print('pack repo')
        # replace with zip - maybe not essential at the moment
    else:
        raise click.ClickException(f"folder {filename} cannot be found")


# Defining the main command group (cli) and global options (e.g. --debug)
@click.group()
@click.option('--endpoint', '-e', envvar='FH_ENDPOINT', default='https://repo.cloudstash.io', help='Endpoint URL for your FunctionHub')
@click.option('--debug', '-d', envvar='FH_DEBUG', default=False, help='Enable debug output')
# enabling the built in --version option. Uses the version from setup.py
@click.version_option()
# pass the main command context to other subcommands
@click.pass_context
def cli(ctx, endpoint, debug):
    # add a Global object to the context that will be passed to all subcommands
    ctx.obj = Global(endpoint, debug)

# subcommnad for deploy operation
@cli.command(name='deploy')
@click.argument('zip_file', type=click.Path(exists=True,resolve_path=True))
@click.pass_obj
def deploy_function(global_config, zip_file):
    pass
    if not os.path.exists('config.ini'):
        raise click.ClickException(f"Config file could not be found")
        
    config = read_config('config.ini')
    payload = {}
    try:
        payload['artifactName'] = config.get('FUNCTION','name')
        payload['version'] = config.get('FUNCTION','version')
        payload['repositoryName'] = config.get('REPOSITORY','repository')
        payload['organization'] = config.get('REPOSITORY','org')
        payload['provider'] = config.get('RUNTIME','provider')
        payload['runtime'] = config.get('RUNTIME','runtime')
        with open(zip_file,'rb') as binfile:
            encoded = base64.b64encode(binfile.read())
        payload['file'] = encoded.decode()
    except:
        raise KeyError("unsupported key")

    click.secho(f"deploy function {payload['artifactName']} to repository {payload['repositoryName']}", bold=True)
    
    try:
        r = requests.post(
            global_config.endpoint,
            json=payload,
            headers={'content-type':'application/json'}
        )
        click.echo(r.status_code)
    except requests.exceptions.RequestException as e:
            click.echo(e)

@cli.command(name='create')
@click.argument('package_name', type=click.Path(exists=False))
@click.argument('desired_dir', required=False, default=os.getcwd(), type=click.Path(exists=True,resolve_path=True, writable=True))
@click.pass_obj
def create_function(global_config, package_name, desired_dir):
    pass
    try:
        target_dir=os.path.join(desired_dir,package_name)
        os.mkdir(target_dir)
        config_file = open('.resources/config.ini', 'r')
        project_config = open(f"{target_dir}/config.ini", 'w')
        for line in config_file.readlines():
            project_config.write(line)
        
        config_file.close()
        project_config.close()
        click.echo(f"project {package_name} successfully created")

    except OSError as err:
        if err.errno == errno.EEXIST:
            raise click.ClickException("Project already exist")
        else:
            os.rmdir(target_dir)
            raise click.ClickException(err)         