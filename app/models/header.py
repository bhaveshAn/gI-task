from app.models import db


class Header(db.Model):
    """Header model class"""

    __tablename__ = 'headers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Header %r>' % self.name

    def __str__(self):
        return self.__repr__()
