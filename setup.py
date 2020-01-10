from setuptools import setup

setup(
    name='functionhub',
    version='v0.1.0',
    py_modules=['cli'],
    install_requires=[
        'Click','requests'
    ],
    entry_points='''
        [console_scripts]
        cli=cli:cli
    ''',
)
