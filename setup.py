import codecs
import re
from os import path
from setuptools import setup, find_packages


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-lazy-tags',
    version=find_version('lazy_tags', '__init__.py'),
    description='A Django app for lazy loading template tags over AJAX',
    long_description=read('README.rst'),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='ajax, django, templatetag',
    author='Grant McConnaughey',
    author_email='grantmcconnaughey@gmail.com',
    url='https://github.com/grantmcconnaughey/django-lazy-tags/',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
)
