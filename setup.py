#coding=u8

from setuptools import setup, find_packages
setup(
    name="yangcongsdk",
    version="1.0",
    description="洋葱官方python sdk",
    author="Secken",
    url="http://www.yangcong.com",
    license="LGPL",
    packages=find_packages(),
    scripts=["sdk/yangcong.py"],
)
