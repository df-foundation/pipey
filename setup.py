from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pipey',
    version='0.0.1a4',
    license='GPLv3',
    description='Declarative syntactic sugar that enables piping in python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Joseph Moon',
    author_email='joseph@opendataframe.com',
    url='https://github.com/dataframehq/pipey',
    keywords=['pipe', 'declarative', 'python', 'data science'],
    packages=setuptools.find_packages(),
)
