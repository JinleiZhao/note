#update db 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
形式：
Model.query.all()/db.session.query.all()

修改表中的值
1、player_db = Player.query.filter(
    Player.invite_code == new_code).first()  #获取对应行的对象

player_db.code = old_code  #重新给对应列赋值
                or
2、player_db = Player.query.filter(Player.code == new_code)\
    .update({'code': old_code})   #直接用update更新

                findly
db.session.commit()  最后提交

获取指定的列的值（first返会元组，all返回列表元组）
a = db.session.query(Page.title, Page.page[，...])[.filter(...)].all()/first()/scalar(){如果有则返回第一条数据}
b = Page.query.with_entities(Page.title, Page.page[，...])[.filter(...)].all()/first()

获取前十列的id[limit]并按照id倒叙,db.desc(xxx)  <==> xxx.desc()
Player.query.with_entities(Player.id).order_by(db.desc(Player.id)).limit(10).all()
Player.query.with_entities(Player.id).order_by(Player.id.desc()).limit(10).all()

设置查询的偏移offset
>> > Promoter.query.with_entities(Promoter.id).order_by(Promoter.id).limit(10).all()
[(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
>> > Promoter.query.with_entities(Promoter.id).order_by(Promoter.id).limit(10).offset(5).all()
[(6,), (7,), (8,), (9,), (10,), (11,), (12,), (13,), (14,), (15,)]

slice切片（索引0开始，前闭后开）
>> > Promoter.query.with_entities(Promoter.id).order_by(Promoter.id).slice(1, 6).all()
[(2,), (3,), (4,), (5,), (6,)]
>> > Promoter.query.with_entities(Promoter.id).order_by(Promoter.id).all()[1:6]
[(2,), (3,), (4,), (5,), (6,)]


