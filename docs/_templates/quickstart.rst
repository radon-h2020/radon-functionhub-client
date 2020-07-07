Quickstart
---------------------------------------------

System Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This README is currently tailored to Unix-like systems (MacOS, Linux).

For FunctionHub developers and users, the following additional software
must be installed:

-  pip - Python standard package manager


Download the Function Hub client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. pip install functionhub

**make changes and verify with the local cli**

User account & Navigation
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a user account on `FunctionHub <https://cloudstash.io>`__
2. Create a new repository
3. Navigate through the website to discover different options for
   functions

Pushing functions to FunctionHub using CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a project. ``fuhub create exampleProject``
2. Move to the project directory. ``cd exampleProject``
3. Set the configuration file *config.ini* with your parameters.
   (example of *config.ini* can be found in `test <https://github.com/radon-h2020/functionHub-client/tree/master/test>`__ directory)

::

   [REPOSITORY]
   org =
   repository =

   [FUNCTION]
   name =
   version =
   description = 

   [RUNTIME]
   provider =
   runtime =

   
4. Store a function and compress it as myfunction.zip
5. Deploy the function to `FunctionHub <https://cloudstash.io>`__.
   ``fuhub deploy myfunction.zip``
6. Check the function has been uploaded on the selected repository
   (temporary unavailable)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~