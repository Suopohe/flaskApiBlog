# -*- coding: utf-8 -*-
# @Time    : 18-1-25 下午2:38
# @Author  : xuan
# @File    : views.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), 广州比呀比信息科技有限公司
# @Contact : zhangxuan@biyabi.com
# @Site    : http://m.biyabi.com/index.html
import datetime
from uuid import uuid4
from os import path

from flask import render_template,Blueprint
from sqlalchemy import func

from main import app
from models import db,User,Post,Tag,Comment,posts_tags
from forms import CommentForm

blog_blueprint = Blueprint(
    'blog',
    __name__,
    template_folder=path.join('templates/blog'),
    url_prefix='/blog'
)


def sidebar_data():
    # Get post of recent
    recent = db.session.query(Post).order_by(
        Post.publish_date.desc()
    ).limit(5).all()

    # Get the tags and sort by count of posts.
    top_tags = db.session.query(
        Tag, func.count(posts_tags.c.post_id).label('total')
    ).join(
        posts_tags
    ).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags


@app.route('/')
@app.route('/<int:page>')
def home(page = 1):
    posts = Post.query.order_by(
        Post.publish_date.desc()
    ).paginate(page,10)
    recent, top_tags = sidebar_data()
    return render_template('blog/home.html',
                           posts = posts,
                           recent=recent,
                           top_tags=top_tags
                           )


@app.route('/post/<string:post_id>',methods=('GET','POST'))
def post(post_id):
    """文章视图函数"""
    forms = CommentForm()
    if forms.validate_on_submit():
        new_comment = Comment(id=str(uuid4()),name=forms.name.data)
        new_comment.text = forms.text.data
        new_comment.date = datetime.datetime.now()
        new_comment.post_id = post_id
        db.session.add(new_comment)
        db.session.commit()
    post = Post.query.get_or_404(post_id)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent,top_tags = sidebar_data()
    return render_template('blog/post.html',
                           form = forms,
                           post=post,
                           tags=tags,
                           comments=comments,
                           recent=recent,
                           top_tags=top_tags)


@app.route('/tag/<string:tag_name>')
def tag(tag_name):
    """标签视图函数"""
    tag = Tag.query.filter_by(name=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()
    return render_template('tag.html',
                           tag=tag,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)