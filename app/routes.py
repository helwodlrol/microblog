# -*- coding: UTF-8 -*-
"""
    @Project ：microblog 
    @Author  ：cong.jin
    @Date    ：2021/5/21 10:26 
"""
from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'
