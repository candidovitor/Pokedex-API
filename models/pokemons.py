from database import db

class PokemonModel(db.Model):
    __tablename__ = 'pokemons'

    number_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    evolution = db.Column(db.String(3))

    type_id = db.Column(db.Integer, db.ForeignKey('types_model.type_id')) 
    region_id = db.Column(db.Integer, db.ForeignKey('region_model.region_id'))
    fast_attack = db.Column(db.Integer, db.ForeignKey('fast_attack_model.attack_id'))
    charger_attack = db.Column(db.Integer, db.ForeignKey('charger_attack_model.attack_id'))

    hit_point = db.Column(db.Integer)

    def __init__(self, number_id, name, evolution, type_id, region_id, fast_attack, charger_attack,hit_point):

        self.number_id = number_id
        self.name = name
        self.evolution = evolution
        self.type_id = type_id
        self.region_id = region_id
        self.fast_attack = fast_attack
        self.charger_attack = charger_attack
        self.hit_point = hit_point

    def json(self):
        return {
            'number_id': self.number_id,
            'name': self.name,
            'evolution': self.evolution,
            'type_id': self.type_id,
            'region_id': self.region_id,
            'fast_attack': self.fast_attack,
            'charger_attack': self.charger_attack,
            'hit_point': self.hit_point
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_pokemon(self):
        db.session.delete(self)
        db.session.commit()

    def update_pokemon(self, name, evolution, type_id, region_id, attack_id_1, attack_id_2, hit_point):
            self.name = name
            self.evolution = evolution
            self.type_id = type_id
            self.region_id = region_id
            self.attack_id_1 = attack_id_1
            self.attack_id_2 = attack_id_2
            self.hit_point = hit_point
        

    @classmethod
    def find_by_id(cls, number_id):
        return cls.query.filter_by(number_id=number_id).first()

    