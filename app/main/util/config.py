#!/usr/bin/python
from configparser import ConfigParser

conf = ConfigParser()
conf.read("app/main/util/config.ini")

def config():
    return conf