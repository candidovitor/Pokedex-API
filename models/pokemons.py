from database import db

class PokemonModel(db.Model):
    __tablename__ = 'pokemons'

    number_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    evolution = db.Column(db.Boolean, default=True) # corrigir se esta certo

    type_id = db.Column(db.Integer, db.ForeignKey('types_model.type_id')) 
    region_id = db.Column(db.Integer, db.ForeignKey('region_model.region_id'))
    attack_id_1 = db.Column(db.Integer, db.ForeignKey('attack_model.attack_id'))
    attack_id_2 = db.Column(db.Integer, db.ForeignKey('attack_model.attack_id'))

    hit_point = db.Column(db.Integer)

    def __init__(self, number_id, name, evolution, type_id, region_id, attack_id, hit_point):

        self.number_id = number_id
        self.name = name
        self.evolution = evolution
        self.type_id = type_id
        self.region_id = region_id
        self.attack_id = attack_id
        self.hit_point = hit_point

    def json(self):
        return {
            'pokedex number': self.number_id,
            'pokemon name': self.name,
            'evolution': self.evolution,
            'type_id': self.type_id,
            'region_id': self.region_id,
            'attack_id': self.attack_id,
            'hit_point': self.hit_point
        }