from database import db

class ChargerAttackModel(db.Model):
    __tabelaname__ = 'charger_attacks'

    charger_attack_id = db.Column(db.Integer, primary_key=True)
    charger_attack_name = db.Column(db.String(50))
    damage = db.Column(db.Integer)

    type_id = db.Column(db.Integer, db.ForeignKey('types_model.type_id'))

    #charger_attack_pokemon = db.relationship("PokemonModel")

    def __init__(self, charger_attack_id, charger_attack_name, damage, type_id):
        self.charger_attack_id = charger_attack_id
        self.charger_attack_name = charger_attack_name
        self.damage = damage
        self.type_id = type_id

    def json(self):
        return {
            'charger_attack_id': self.charger_attack_id,
            'charger_attack_name': self.charger_attack_name,
            'damage': self.damage,
            'type_id': self.type_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_attack(self):
        db.session.delete(self)
        db.session.commit()

    def update_attack(self, charger_attack_name, damage, type_id):
        self.charger_attack_name = charger_attack_name
        self.damage = damage
        self.type_id = type_id

    @classmethod
    def find_by_id(cls, charger_attack_id):
        return cls.query.filter_by(charger_attack_id=charger_attack_id).first()

    @classmethod
    def find_all_attacks(cls):
        return cls.query.all()