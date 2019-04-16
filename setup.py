import pynex
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

requirements = [
    'logzero'
]

setup(
    name='pynex',
    version=pynex.__version__,
    description='A MCBE Python Server',
    long_description=readme,
    author='BFBTeam',
    author_email='bfbteam.mcpe@gmail.com',
    url='https://github.com/BFBTeam-PE/PyNEX',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'pynex = pynex.__main__:main'
        ]
    },
    install_requires=requirements
)