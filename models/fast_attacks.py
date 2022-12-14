from database import db

class FastAttackModel(db.Model):
    __tabelaname__ = 'fast_attacks'

    fast_attack_id = db.Column(db.Integer, primary_key=True)
    fast_attack_name = db.Column(db.String(50))
    damage = db.Column(db.Integer)

    type_id = db.Column(db.Integer, db.ForeignKey('types_model.type_id'))

    fast_attack_pokemon = db.relationship("PokemonModel")

    def __init__(self, fast_attack_id, fast_attack_name, damage, type_id):
        self.fast_attack_id = fast_attack_id
        self.fast_attack_name = fast_attack_name
        self.damage = damage
        self.type_id = type_id

    def json(self):
        return {
            'fast_attack_id': self.fast_attack_id,
            'fast_attack_name': self.fast_attack_name,
            'damage': self.damage,
            'type_id': self.type_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_attack(self):
        db.session.delete(self)
        db.session.commit()

    def update_attack(self, fast_attack_name, damage, type_id):
        self.fast_attack_name = fast_attack_name
        self.damage = damage
        self.type_id = type_id

    @classmethod
    def find_by_id(cls, fast_attack_id):
        return cls.query.filter_by(fast_attack_id=fast_attack_id).first()

    @classmethod
    def find_all_attacks(cls):
        return cls.query.all()

    
        
