from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='functionhub',
    version='0.1.7',
    author="naesheim",
    description="A client for CloudStash.io interaction",
    url="https://cloudstash.io",
    packages=find_packages(),
    package_data = {'functionhub': ['config.ini']},
    include_package_data=True,
    install_requires=[
        'Click','requests','chardet','urllib3'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        fuhub=functionhub.main:fuhub
    '''
)
