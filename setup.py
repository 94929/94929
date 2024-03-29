from os import path

from setuptools import setup, find_packages


def get_readme():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
        readme = readme_file.read()
        return readme


setup(
    name='jinsung',
    version='0.2.0',
    author='Jinsung Ha',
    author_email='jsung5381@naver.com',
    description='Who is Jinsung Ha?',
    long_description='Who is Jinsung Ha? \n' + get_readme(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/94929/94929',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
