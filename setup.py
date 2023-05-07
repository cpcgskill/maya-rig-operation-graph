#!/usr/bin/python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function
import setuptools

lib_name = 'maya-rig-operation-graph'

author = 'cpcgskill',
author_email = 'cpcgskill@outlook.com'

version = '0.7.1'

description = 'maya计算图的实现'
with open("README.rst", "rb") as f:
    long_description = f.read().decode(encoding='utf-8')

project_homepage = 'https://github.com/cpcgskill/maya-rig-operation-graph'
project_urls = {
    'Bug Tracker': 'https://github.com/cpcgskill/maya-rig-operation-graph/issues',
}
license = 'Apache Software License (Apache 2.0)'

packages = ['rig_operation_graph']
python_requires = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*'
install_requires = [
    'maya-rig-core>=0.2.4',
]

setuptools.setup(
    name=lib_name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url=project_homepage,
    project_urls=project_urls,
    license=license,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    package_dir={"": "src"},
    packages=packages,
    package_data={'rig_operation_graph': ['*.pyi']},
    python_requires=python_requires,
    # 指定依赖
    install_requires=install_requires,
)
