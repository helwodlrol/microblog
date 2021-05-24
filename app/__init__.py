# -*- coding: UTF-8 -*-
"""
    @Project ：microblog 
    @Author  ：cong.jin
    @Date    ：2021/5/21 10:25 
"""
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# app
app = Flask(__name__, template_folder='../templates')
# config
app.config.from_object(Config)
# db
db = SQLAlchemy(app)
# migrate
migrate = Migrate(app, db)
# login
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
