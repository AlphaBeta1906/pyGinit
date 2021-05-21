from setuptools import setup

setup(
    name='pyGinit',
    version='0.1',
    author= 'fariz',
    license= 'MIT',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pyGinit=main:pyGinit
    ''',
)