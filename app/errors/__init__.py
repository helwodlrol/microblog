# -*- coding: UTF-8 -*-
"""
    @Project ：microblog 
    @Author  ：cong.jin
    @Date    ：2021/6/7 11:13 
"""
from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
