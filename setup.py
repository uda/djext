import os

from setuptools import setup, find_packages

import djext


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='djext',
    version=djext.__version__,
    description='Quick tools for Django',
    author='Yehuda Deutsch',
    author_email='yeh@uda.co.il',

    license='MIT',
    url='https://gitlab.com/uda/djext',
    keywords='django http wsgi quick tools models forms views templates templatetags',
    packages=find_packages(),
    include_package_data=True,
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    extras_require={
        'dev': ['django'],
        'test': ['coverage'],
        'json': ['jsonschema'],
    },
    python_requires='>=3.5',
)
