# -*- coding: UTF-8 -*-
"""
    @Project ：microblog 
    @Author  ：cong.jin
    @Date    ：2021/6/7 11:22 
"""
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes