# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='ingookey', # package name
    version='0.1',   # package version
    keywords=('setup', 'ingookey'),
    description='setup ingookey',
    long_description='setup ingookey for test',
    license='MIT',
    install_requires=[], # 3rd packages
    author='Ingookey',
    author_email='ingookey@163.com',
    packages=find_packages(),
    platforms='any',
    url='', # project link
    include_package_data = True,
    entry_points={
        'console_scripts':[
            'ingookey=run:main'
        ]
    },
)