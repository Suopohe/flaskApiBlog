# -*- coding: utf-8 -*-
# @Time    : 18-1-25 下午3:51
# @Author  : xuan
# @File    : fake_data.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), 广州比呀比信息科技有限公司
# @Contact : zhangxuan@biyabi.com
# @Site    : http://m.biyabi.com/index.html

import random
import datetime
from uuid import uuid4

from models import db,User,Post,Tag

user = User(id=str(uuid4()), username='jmilkfan', password='fanguiju')
db.session.add(user)
db.session.commit()

user = db.session.query(User).first()
tag_one = Tag(id=str(uuid4()), name='Python')
tag_two = Tag(id=str(uuid4()), name='Flask')
tag_three = Tag(id=str(uuid4()), name='SQLALchemy')
tag_four = Tag(id=str(uuid4()), name='JMilkFan')
tag_list = [tag_one, tag_two, tag_three, tag_four]

s = "EXAMPLE TEXT"
for i in range(100):
    new_post = Post(id=str(uuid4()),title="Post"+str(i))
    new_post.user_id = user.id
    new_post.publish_date = datetime.datetime.now()
    new_post.text = ' '.join([s,str(i)])
    new_post.tags = random.sample(tag_list, random.randint(1, 3))
    db.session.add(new_post)

db.session.commit()
