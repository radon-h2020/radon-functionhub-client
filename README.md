![pypi](https://img.shields.io/pypi/v/pybadges.svg)
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)

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
### Install fuhub with 

1. ``pip install functionhub``


### User account & Navigation
1.  Create a user account on [FunctionHub](https://cloudstash.io)
2.  Store the deploy token given to you
3.  Navigate through the website to discover different options for functions

### Pushing functions to FunctionHub using CLI

1. Create a project. ``fuhub create exampleProject`` 
2. Change directory to the project directory. ``cd exampleProject``
3. Set the configuration file _config.ini_ with your parameters. (example of _config.ini_ can be found  in [test](test/) directory)
4. Create a zipped folder containing your function and libraries if necessary.
5. Upload the function to [FunctionHub](https://cloudstash.io). ``fuhub --token <deploy-token> upload myfunction.zip`` 

### Retreiving Functions from FunctionHub 

1. Browse [FunctionHub](https://cloudstash.io) and find the Function of your choice
2. Copy the ArtifacId
3. In terminal do ``curl -o function.zip https://cloudstash.io/artifact_download/<ArtifactId> ``


## Contribution
We encourage contributions from everyone who finds interest in this project!

For any ideas, bugs or new features use our issue tracker at our  [GitHub](https://github.com/radon-h2020/functionHub-client/issues)  project.

When contributing, fork the repository and commit work through pull requests.



Read the [roadmap](ROADMAP.md)
