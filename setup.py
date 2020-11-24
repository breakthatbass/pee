from setuptools import setup, find_packages
from pee.__init__ import __version__

setup(
        name='pee',
        version=f'{__version__}',
        description='Display memory system information',
        author='Taylor Gamache',
        author_email='gamache.taylor@gmail.com',
        url='https://github.com/breakthatbass/pee',
        packages=find_packages(),
        license='MIT',
        entry_points={
            'console_scripts':['pee = pee.pee:main']
            }
    )
