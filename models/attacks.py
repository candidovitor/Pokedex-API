from database import db

class AttackModel(db.Model):
    __tabelaname__ = 'attacks'

    attack_id = db.Column(db.Integer, primary_key=True)
    attack_name = db.Column(db.String(50))
    damage = db.Column(db.Integer)

    type_id = db.Column(db.Integer, db.ForeignKey('types_model.type_id'))
    #terá uma ou duas informações que sairão daqui para a tabela pokemon

    def __init__(self, attack_id, attack_name, damage, type_id):
        self.attack_id = attack_id
        self.attack_name = attack_name
        self.damage = damage
        self.type_id = type_id

    def json(self):
        return {
            'attack_id': self.attack_id,
            'attack_name': self.attack_name,
            'damage': self.damage,
            'type_id': self.type_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_attack(self):
        db.session.delete(self)
        db.session.commit()

    def update_attack(self, attack_name, damage, type_id):
        self.attack_name = attack_name
        self.damage = damage
        self.type_id = type_id

    @classmethod
    def find_by_id(cls, attack_id):
        return cls.query.filter_by(attack_id=attack_id).first()

    @classmethod
    def find_all_attacks(cls):
        return cls.query.all()

    
        
