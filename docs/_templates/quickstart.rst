Quickstart
---------------------------------------------

System Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This README is currently tailored to Unix-like systems (MacOS, Linux).

For FunctionHub developers and users, the following additional software
must be installed:

-  pip3 - Python3 standard package manager


Download the Function Hub client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. pip3 install functionhub

**make changes and verify with the local cli**

User account & Navigation
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a user account on `FunctionHub <https://cloudstash.io>`__
2. Store the deploy-token given to you
3. Create a new repository
4. Navigate through the website to discover different options for
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
   handler =

   
4. Create a zipped folder containing your function and libraries if necessary.
5. Upload the function to `FunctionHub <https://cloudstash.io>`__.
   ``fuhub --token <deploy-token> upload myfunction.zip``



Retreiving Functions from FunctionHub 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Browse `FunctionHub <https://cloudstash.io>`__ and find the Function of your choice.
2. Copy the ArtifacId.
3. In terminal do ``curl -o function.zip https://cloudstash.io/artifact_download/*ArtifactId*``
