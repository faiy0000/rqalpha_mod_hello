
# -*- coding: utf-8 -*-
try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements
from os.path import dirname, join
from setuptools import (
    find_packages,
    setup,
)

# requirements = [str(ir.req) for ir in parse_requirements("requirements.txt", session=False)]
requirements = parse_requirements("requirements.txt", session=False)
# requirements = list(install_reqs)
setup(
    # name='rqalpha-mod-hello',
    name='hello',
    version="0.1.0",
    description='RQAlpha Mod to say hello',
    packages=find_packages(exclude=[]),
    author='your name',
    author_email='your email address',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='https://github.com/johnsonchak/rqalpha-mod-hello',
    requirements = [str(ir.requirement) for ir in requirements],
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
    ],
)