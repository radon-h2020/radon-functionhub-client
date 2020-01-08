from setuptools import setup

setup(
    name='functionhub',
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'Click','requests'
    ],
    entry_points='''
        [console_scripts]
        cli=cli:main
    ''',
)
