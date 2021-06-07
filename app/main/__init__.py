# -*- coding: UTF-8 -*-
"""
    @Project ：microblog 
    @Author  ：cong.jin
    @Date    ：2021/6/7 13:57 
"""
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
