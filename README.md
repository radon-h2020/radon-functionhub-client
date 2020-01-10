## FunctionHub client for interaction with cloudstash.io ##

Creating a development environment:

1. python3 -m venv venv (setup a virtual environment)
2. venv/bin/pip install -r requirements.txt (installing requirements to the virtual env)
3. . venv/bin/activate (activating the virtual env)
4. pip install --editable . (enabling the CLI to respond with the command cli instead of python cli.py)

Using the client:

1. Configure a config.ini file. You find an example in ```test/``` folder
2. Zip a folder with the Function and requirements
3. Run the command ```cli deploy <file.zip>```. Make sure the .ini files is present in your PWD


Contribute:

Read the [roadmap](ROADMAP.md)