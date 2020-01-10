import click
import configparser
import requests
import os
import zipfile
import errno

# global class with all global data
class Global(object):
    def __init__(self, endpoint, debug):
        self.endpoint = endpoint
        # self.config = read_config(os.path.abspath(config))
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
@click.argument('package_dir', type=click.Path(exists=True,resolve_path=True))
@click.pass_obj
def deploy_function(global_config, package_dir):
    pass
    config_file=os.path.join(package_dir,'config.ini')
    if not os.path.exists(config_file):
        raise click.ClickException(f"{config_file} Couldn't be found")
        
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

@cli.command(name='create')
@click.argument('package_name', type=click.Path(exists=False))
@click.argument('desired_dir', required=False, type=click.Path(exists=True,resolve_path=True, writable=True))
@click.pass_obj
def create_function(global_config, package_name, desired_dir=os.getcwd()):
    pass
    try:
        target_dir=os.path.join(desired_dir,package_name)
        os.mkdir(target_dir)
        config_file = open('resources/config.ini', 'r')
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