# -*- coding: utf-8 -*-
# @Time    : 18-1-25 下午12:30
# @Author  : xuan
# @File    : config.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), 广州比呀比信息科技有限公司
# @Contact : zhangxuan@biyabi.com
# @Site    : http://m.biyabi.com/index.html


class Config(object):
    """基础配置类"""
    SECRET_KEY = 'you never guess key'


class ProConfig(Config):
    """生产环境配置"""
    pass


class DevConfig(Config):
    """开发环境 配置 class."""
    # Open the DEBUG
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:biyabi@127.0.0.1:3306/flaskblog'