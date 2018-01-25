# -*- coding: utf-8 -*-
# @Time    : 18-1-25 下午3:42
# @Author  : xuan
# @File    : forms.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), 广州比呀比信息科技有限公司
# @Contact : zhangxuan@biyabi.com
# @Site    : http://m.biyabi.com/index.html
import re

from flask_wtf import Form
from wtforms import StringField,TextField,ValidationError
from wtforms.validators import DataRequired,Length


class CommentForm(Form):
    name = StringField(
        'Name',
        validators=[DataRequired(),Length(max=25)]
        )
    text = TextField(u'Comment', validators=[DataRequired()])


# def custom_email(form_object, field_object):
#     """Define a vaildator"""
#     if not re.match(r"[^@+@[^@]+\.[^@]]+", field_object.data):
#         raise ValidationError('Field must be a valid email address.')