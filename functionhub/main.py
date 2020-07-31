import click
import configparser
import requests
import os
import base64
import errno
import shutil

from configparser import Error, NoOptionError

# global class with all global data
class Global(object):
    def __init__(self, endpoint, debug, token):
        self.endpoint = endpoint
        self.debug = debug
        self.token = token

def read_config(config_file):
    try:
        config = configparser.ConfigParser()
        config.read(config_file)
        return config
    except Error as e:
        click.secho(f"{e}",fg='red')


# Defining the main command group (cli) and global options (e.g. --debug)
@click.group()
@click.option('--endpoint', '-e', envvar='FH_ENDPOINT', default='https://cloudstash.io/artifact', help='Endpoint URL for your FunctionHub')
@click.option('--debug', '-d', envvar='FH_DEBUG', default=False, help='Enable debug output')
@click.option('--token', '-at', envvar='ACCESS_TOKEN', default="", help='Set access token for publishing to private repositories')
# enabling the built in --version option. Uses the version from setup.py
@click.version_option()
# pass the main command context to other subcommands
@click.pass_context
def fuhub(ctx, endpoint, debug, token):
    # add a Global object to the context that will be passed to all subcommands
    ctx.obj = Global(endpoint, debug, token)

# subcommnad for upload operation
@fuhub.command(name='upload')
@click.argument('zip_file', type=click.Path(exists=True,resolve_path=True))
@click.pass_obj
def upload_function(global_config, zip_file):
    pass
    if not os.path.exists('config.ini'):
        raise click.ClickException(f"Config file could not be found")
        
    config = read_config('config.ini')
    payload = {}
    try:
        payload['artifact_name'] = config.get('FUNCTION','name')
        payload['version'] = config.get('FUNCTION','version')
        payload['description'] = config.get('FUNCTION','description')
        payload['repositoryName'] = config.get('REPOSITORY','repository')
        payload['organization'] = config.get('REPOSITORY','org')
        payload['provider'] = config.get('RUNTIME','provider')
        payload['runtime'] = config.get('RUNTIME','runtime')
        payload['applicationToken'] = global_config.token
        with open(zip_file,'rb') as binfile:
            encoded = base64.b64encode(binfile.read())
        payload['file'] = encoded.decode()

        click.secho(f"upload function {payload['artifact_name']} to repository {payload['repositoryName']}", bold=True)
        
        r = requests.post(
            global_config.endpoint,
            json=payload,
            headers={'content-type':'application/json'}
        )
        click.echo(r.status_code)

    except KeyError as ke:
        click.secho(f"{ke}",fg='red') 
    except NoOptionError as noe:
        click.secho(f"{noe}",fg='red')
    except requests.exceptions.RequestException as re:
            click.secho(f"{re}",fg='red')

@fuhub.command(name='create')
@click.argument('package_name', type=click.Path(exists=False))
@click.argument('desired_dir', required=False, default=os.getcwd(), type=click.Path(exists=True,resolve_path=True, writable=True))
@click.pass_obj
def create_function(global_config, package_name, desired_dir):
    try:
        target_dir=os.path.join(desired_dir,package_name)
        os.mkdir(target_dir)
        config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        config_file = open(config_file_path, 'r')
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

@fuhub.command(name='package')
@click.argument('package_dir', type=click.Path(exists=True, resolve_path=True,))
def package_function(package_dir):
    if os.path.isdir(package_dir):
        shutil.make_archive(os.path.join(os.getcwd(),os.path.basename(package_dir)), 'zip', os.path.dirname(package_dir))
    else:
        raise click.ClickException(f"folder {package_dir} cannot be found")