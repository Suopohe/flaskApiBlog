# -*- coding: utf-8 -*-
# @Time    : 18-1-25 下午12:33
# @Author  : xuan
# @File    : main.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), 广州比呀比信息科技有限公司
# @Contact : zhangxuan@biyabi.com
# @Site    : http://m.biyabi.com/index.html
from flask import Flask

from config import DevConfig
import forms


app = Flask(__name__)

# 导入视图
views = __import__('views')

# 加载配置环境
app.config.from_object(DevConfig)


if __name__ == '__main__':
    app.run()