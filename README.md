# FunctionHub client 

| Items                    | Contents                                                     |
| ------------------------ | ------------------------------------------------------------ |
| **Short Description**    | The FunctionHub-cli provides interaction with [FunctionHub](https://cloudstash.io) for storing and accessing reusable functions. FunctionHub is child of [Cloudstash](https://cloudstash.io), a broader cloud based storage unit for functions and artifacts. |
| **Documentation** | https://functionhub-cli.readthedocs.io/|
| **Video** | WPI  |
| **Licence** | [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0) |
| **Contact**              | <ul><li> Praqma ([@naesheim](https://github.com/naesheim)) </li></ul> |

## System Requirements
This README is currently tailored to Unix-like systems (MacOS, Linux). 

For FunctionHub developers and users, the following additional software must be installed: 

 - pip - Python standard package manager 
 

## Using  FunctionHub
### Creating a development environment

1.  Fork and clone the repository.
2.  Setup a virtual environment. ``python3 -m venv venv``
3.  Install requirements to the virtual env. 
``venv/bin/pip install -r requirements.txt`` 
5. Activate et the virtual env.		``. venv/bin/activate`` 
6. Enable the CLI to respond with the command cli instead of python cli.py.
``pip install --editable .``

_make changes and verify with the local cli_

### User account & Navigation
1.  Create a user account on [FunctionHub](https://cloudstash.io)  
2.  Navigate through the website to discover different options for functions

### Pushing functions to FunctionHub using CLI

1. Create a project. ``cli create exampleProject`` 
2. Move to the project directory. ``cd exampleProject`` 
3. Set the configuration file _config.ini_ with your parameters. (example of _config.ini_ can be found  in [test](test/) directory)
4. Store a function and compress it as myfunction.zip
5. Deploy the function to [FunctionHub](https://cloudstash.io). ``cli deploy myfunction.zip`` 
6. Check the function has been uploaded on the selected repository (temporary unavailable)



## Contribution
We encourage contributions from everyone who finds interest in this project!

For any ideas, bugs or new features use our issue tracker at our  [GitHub](https://github.com/radon-h2020/functionHub-client/issues)  project.

When contributing, fork the repository and commit work through pull requests.





Read the [roadmap](ROADMAP.md)
