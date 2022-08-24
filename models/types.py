from database import db

class TypesModel(db.Model):
    __tabelaname__ = 'types'

    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20))

    def __init__(self, type_id, type_name):
        self.type_id = type_id
        self.type_name = type_name

    def json(self):
        return {
            'type_id': self.type_id,
            'type_name': self.type_name
        }

    @classmethod
    def find_by_name(cls, type_name):
        return cls.query.filter_by(type_name=type_name).first()

