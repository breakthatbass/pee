from setuptools import setup, find_packages
from pee.__init__ import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
        name='pee',
        version=f'{__version__}',
        description='Display memory system information',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Taylor Gamache',
        author_email='gamache.taylor@gmail.com',
        url='https://github.com/breakthatbass/pee',
        packages=find_packages(),
        license='MIT',
        entry_points={
            'console_scripts':['pee = pee.pee:main']
            },
        python_requires='>=3.6'
    )
