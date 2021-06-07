# -*- coding: UTF-8 -*-
"""
    @Project ：microblog 
    @Author  ：cong.jin
    @Date    ：2021/5/21 11:08 
"""
from app import db, cli, create_app
from app.models import User, Post

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post
    }
