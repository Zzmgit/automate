# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zhangzheming
@Version        :
------------------------------------
@File           :  setup.py
@Description    :
@CreateTime     :  2019/10/29 9:14
------------------------------------
@ModifyTime     :
"""
from setuptools import setup

setup(
    name='sdk',
    version='0.1',
    author='Zzm',
    description=('Keywords for automatic retrieval'),
    long_description=('README.md'),
    keyword=('GitHub search '),
    license='GNU GPLv3',
    packages=['', 'conf', 'util'],
    url='https://github.com/Zzmgit/automate',
    download_url='https://github.com/Zzmgit/automate.git',
    platforms='Python3',
    include_package_data=True,
    install_requires=[
        'selenium>=3.9.0',
        'urllib3>=1.25.6',
    ],
    zip_safe=False
)
