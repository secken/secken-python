#coding=u8

from setuptools import setup, find_packages
setup(
    name="secken-api",
    version="2.5",
    description="洋葱官方python sdk",
    author="Secken",
    url="http://www.secken.com",
    license="LGPL",
    packages=find_packages(),
    scripts=["secken.py"],
    py_modules=['secken']
)
