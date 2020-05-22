Quickstart
===========================================
System Requirements
-------------------

This README is currently tailored to Unix-like systems (MacOS, Linux).

For FunctionHub developers and users, the following additional software
must be installed:

-  pip - Python standard package manager

Using FunctionHub
-----------------

Creating a development environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Fork and clone the repository.
2. Setup a virtual environment. ``python3 -m venv venv``
3. Install requirements to the virtual env.
   ``venv/bin/pip install -r requirements.txt``
4. Activate et the virtual env. ``. venv/bin/activate``
5. Enable the CLI to respond with the command cli instead of python
   cli.py. ``pip install --editable .``

*make changes and verify with the local cli*

User account & Navigation
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a user account on `FunctionHub <https://cloudstash.io>`__
2. Navigate through the website to discover different options for
   functions

Pushing functions to FunctionHub using CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a project. ``cli create exampleProject``
2. Move to the project directory. ``cd exampleProject``
3. Set the configuration file *config.ini* with your parameters.
   (example of *config.ini* can be found in `test <test/>`__ directory)
4. Store a function and compress it as myfunction.zip
5. Deploy the function to `FunctionHub <https://cloudstash.io>`__.
   ``cli deploy myfunction.zip``
6. Check the function has been uploaded on the selected repository
   (temporary unavailable)ß