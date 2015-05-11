#coding=u8

from setuptools import setup, find_packages
setup(
    name="yangcongsdk",
    version="1.9",
    description="洋葱官方python sdk",
    author="Secken",
    url="http://www.yangcong.com",
    license="LGPL",
    packages=find_packages(),
    scripts=["yangcong/yangcong.py"],
)
