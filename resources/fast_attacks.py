from flask_restful import Resource, reqparse
from models.fast_attacks import FastAttackModel
from models.types import TypesModel

from database import db

class All_FAst_Attacks(Resource):
    def get(self):
        return {"fast_attacks": [attacks.json() for attacks in FastAttackModel.find_all_attacks()]}

class Attack(Resource):
    parser = reqparse.RequestParser()
    #parser.add_argument('attack_id', type=int, required=True, help="This field cannot be left blank")
    parser.add_argument('fast_attack_name', type=str, required=True)
    parser.add_argument('damage', type=int, required=True)
    parser.add_argument('type_id', type=float, required=True)
    

    def post(self, attack_id):
        #print(attack_id)
        attack = AttackModel.find_by_id(attack_id)
        if attack:
            return {"Message": "Id already in use"}, 404

        try:
            data = Attack.parser.parse_args()
            
            fast_attack_name = data['fast_attack_name']
            damage = data['damage']
            type_id = data['type_id']

            attack = FastAttackModel(fast_attack_id, fast_attack_name, damage, type_id)

            attack.save_to_db()
        except:
            return {"Message": "Internal error accoured"}, 500
        
        return attack.json()

    def delete(self, attack_id):
        try:
            attack = FastAttackModel.find_attack_by_id(attack_id)
            if attack:
                attack.delete_attack()
                return {"Message": "Attack deleted"}, 200
            else:
                return {"Message": "Could not delete this attack"}, 404 
        except:
            return {"Message": "Internal error accoured"}, 500

    def get(self, attack_id):

        attack = AttackModel.find_by_id(attack_id)
        if attack:
            return attack.json()
        else:
            return {"Message": "Could not find this ID"}, 500

    def put(self, attack_id):
        try:
            data = Attack.parser.parse_args()
            attack = AttackModel.find_by_id(attack_id)
            if attack:
                new_attack_name = data['attack_name']
                new_damage = data['damage']
                new_type_id = data['type_id']
                attack.update_attack(new_attack_name, new_damage, new_type_id)
                attack.save_to_db()
                return attack.json(), 201
            else:
                return {"Message": "Could not find this ID"}, 404
        except:
            return {"Message": "Internal error accoured"}, 500

class Attack_by_type(Resource):
    def get(self, type_id):
        print(type_id)
        try:
            attacks = AttackModel.query.filter_by(type_id=type_id)
            
            type_attack = TypesModel.find_by_id(type_id)
            type_attack = type_attack.json()
            print(type_attack)
            type_name = type_attack['type_name']

            type_attack = AttackModel.query.filter_by(type_id=type_id).first()

            return {f'attacks from {type_name}': [x.json() for x in attacks]}
        except:
            return {'Message': 'An error occurred while to try filter all attacks by type {type_id}'}, 500



        
