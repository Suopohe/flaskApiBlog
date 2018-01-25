# -*- coding: utf-8 -*-
# @Time    : 18-1-25 下午1:02
# @Author  : xuan
# @File    : manage.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), 广州比呀比信息科技有限公司
# @Contact : zhangxuan@biyabi.com
# @Site    : http://m.biyabi.com/index.html
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

import main
import models

# 初始化对象
manager = Manager(main.app)

# 初始化数据迁移
migrate = Migrate(main.app, models.db)

manager.add_command("server",Server())
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=main.app,
                db = models.db,
                User = models.User,
                Post = models.Post,
                Comment = models.Comment,
                Tag = models.Tag,
                )

if __name__ == '__main__':
    manager.run()