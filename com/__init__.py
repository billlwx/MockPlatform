#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2019/1/17
from flask import Flask

app = Flask(__name__, template_folder='../templates',static_folder="",static_url_path="")