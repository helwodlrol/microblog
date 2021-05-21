# -*- coding: UTF-8 -*-
"""
    @Project ：microblog 
    @Author  ：cong.jin
    @Date    ：2021/5/21 10:25 
"""
from flask import Flask

app = Flask(__name__)

from app import routes
