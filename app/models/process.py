from app.models import db
from datetime import datetime
import pytz
import time
import random

process_headers = db.Table(
    'process_headers',
    db.Column('process_id', db.Integer, db.ForeignKey('processes.id',
              ondelete='CASCADE')),
    db.Column('header_id', db.Integer, db.ForeignKey('headers.id',
              ondelete='CASCADE')))


class Process(db.Model):
    """Request model class"""

    __tablename__ = 'processes'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime(timezone=True),
                     default=datetime.now(pytz.utc))
    method = db.Column(db.String)
    path = db.Column(db.String)
    query = db.Column(db.String)
    body = db.Column(db.String)
    headers = db.relationship(
        'Header', secondary=process_headers,
        backref=db.backref('processes', lazy='dynamic'))
    duration = db.Column(db.String)

    def __init__(self, time=None, method=None, path=None, query=None,
                 body=None, headers=None):
        self.time = time
        self.method = method
        self.path = path
        self.query = query
        self.body = body
        if headers is None:
            self.headers = []
        else:
            self.headers = headers
        self.duration = self.time_duration()

    def time_duration(self):
        then = time.time()
        time.sleep(random.randint(15, 30))
        now = time.time()
        return now - then

    def __repr__(self):
        return '<Request %r>' % self.id

    def __str__(self):
        return self.__repr__()
