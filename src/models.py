from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_

db = SQLAlchemy()

class SearchResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String)
    summary = db.Column(db.String())

    def __repr__(self):
        return "<SearchResult {}>".format(self.title)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @property
    def counter(self):
        result =  SearchCounter.query.filter(SearchCounter.result_id == self.id).first()
        if not result:
            result = SearchCounter.create(result_id=self.id, count=0)
        return result

    def increment_counter(self):
         return self.counter.increment()

    @classmethod
    def create(cls, **kwargs):
        new_data = SearchResult(**kwargs)
        new_data.save()

    @classmethod
    def search(cls,search_string):
        split_result = search_string.split(" ")
        result_title = [cls.title.contains(search_item) for search_item in split_result]
        result_summary = [cls.summary.contains(search_item) for search_item in split_result]
        query_1 = cls.query.filter(and_(*result_title)).all()
        query_2 = cls.query.filter(and_(*result_summary)).all()
        result = cls.query.filter(or_(*result_summary)).all()
        if len(result) > 0:
             for i in result:
                 i.increment_counter()
        return result

    @classmethod
    def populate_with_data(cls):
        data = {
        "title": "Jinja",
        "url": "/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=0ahUKEwi6zevKr_7TAhUJiSwKHblZAeUQFgghMAA&amp;url=http%3A%2F%2Fjinja.pocoo.org%2F&amp;usg=AFQjCNFKiObWsstA_tSpH_tNsUK_VKY4EA&amp;sig2=eFKaff1ZCmdBpLeG3og3Uw",
        "summary": """<div class="s">
                    <div>
                        <div class="f kv _SWb" style="white-space:nowrap"><cite class="_Rm">jinja.pocoo.org/</cite>
                            <div class="action-menu ab_ctl"><a class="_Fmb ab_button" href="#" id="am-b0" aria-label="Result details" aria-expanded="false"
                                    aria-haspopup="true" role="button" jsaction="m.tdd;keydown:m.hbke;keypress:m.mskpe" data-ved="0ahUKEwi6zevKr_7TAhUJiSwKHblZAeUQ7B0IIjAA"><span class="mn-dwn-arw"></span></a>
                        </div>
                        </div><span class="st"><em>Jinja</em> is Beautiful. {% extends "layout.html" %} {% block body %} &lt;ul&gt; {% for user in users %} &lt;li&gt;&lt;a href="{{ user.url }}"&gt;{{ user.username }}&lt;/a&gt;&lt;/li&gt; {% endfor&nbsp;...</span></div>
                </div>"""
        }
        inst = cls(**data)
        inst.save()

class SearchCounter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    result_id = db.Column(db.Integer, db.ForeignKey('search_result.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def create(cls, **kwargs):
        new_data = SearchCounter(**kwargs)
        new_data.save()
        return new_data

    def increment(self):
        self.count += 1
        self.save()

    def reset_counter(self):
        self.count = 0
        self.save()