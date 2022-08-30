from database import db

class TypesModel(db.Model):
    __tabelaname__ = 'types'

    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20))

    #type_fast_attack = db.relationship("FastAttackModel", lazy="dynamic") 
    #type_charger_attack = db.relationship("ChargerAttackModel", lazy="dynamic")

    #type_pokemon = db.relationship("PokemonModel", lazy="dynamic")

    
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

    @classmethod
    def find_by_id(cls, type_id):
        return cls.query.filter_by(type_id=type_id).first()

    @classmethod
    def find_all_types(cls):
        return cls.query.all()

    def delete_type(self):
        db.session.delete(self)
        db.session.commit()

    def update_type(self, type_id, type_name):
        self.type_id = type_id
        self.type_name = type_name


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
