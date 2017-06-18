#!/usr/bin/env python

import versioneer
from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name="awsebcli",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description="Command Line Interface for AWS EB.",
    long_description="Command Line Interface for AWS EB.",

    url="http://aws.amazon.com/elasticbeanstalk/",

    author="AWS Elastic Beanstalk",
    author_email="aws-eb-cli@amazon.com",

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=[
        "blessed>=1.9.5",
        "botocore>=1.0.1",
        "cement==2.8.2",
        "colorama==0.3.7",
        "docker-py>=1.1.0,<=1.7.2",
        "dockerpty>=0.3.2,<=0.4.1",
        "docopt>=0.6.1,<0.7",
        "pathspec==0.5.0",
        "pyyaml>=3.11",
        "requests>=2.6.1,<=2.9.1",
        "semantic-version==2.5.0",
        "setuptools>=20.0",
        "tabulate==0.7.5",
        "termcolor==1.1.0",
        "websocket-client>=0.11.0,<1.0",
    ],

    entry_points={
        'console_scripts': [
            "eb=ebcli.core.ebcore:main",
            "ebp=ebcli.core.ebpcore:main",
        ],
    },
)
