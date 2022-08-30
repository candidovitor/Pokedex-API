from flask_restful import Resource, reqparse
from models.charger_attacks import ChargerAttackModel
from models.types import TypesModel

from database import db

class All_Charger_Attacks(Resource):
    def get(self):
        return {"cherger_attacks": [attacks.json() for attacks in ChargerAttackModel.find_all_attacks()]}

class ChargerAttack(Resource):
    parser = reqparse.RequestParser()
    #parser.add_argument('charger_attack_id', type=int, required=True, help="This field cannot be left blank")
    parser.add_argument('charger_attack_name', type=str, required=True)
    parser.add_argument('damage', type=int, required=True)
    parser.add_argument('type_id', type=float, required=True)
    

    def post(self, charger_attack_id):
        print(charger_attack_id)

        attack = ChargerAttackModel.find_by_id(charger_attack_id)
        if attack:
            return {"Message": "Id already in use"}, 404

        try:
            data = ChargerAttack.parser.parse_args()
            
            charger_attack_name = data['charger_attack_name']
            damage = data['damage']
            type_id = data['type_id']

            attack = ChargerAttackModel(charger_attack_id, charger_attack_name, damage, type_id)

            attack.save_to_db()
        except:
            return {"Message": "Internal error accoured"}, 500
        
        return attack.json()

    def delete(self, charger_attack_id):
        try:
            attack = ChargerAttackModel.find_by_id(charger_attack_id)
            if attack:
                attack.delete_attack()
                return {"Message": "Attack deleted"}, 200
            else:
                return {"Message": "Could not delete this attack"}, 404 
        except:
            return {"Message": "Internal error accoured"}, 500

    def get(self, charger_attack_id):

        attack = ChargerAttackModel.find_by_id(charger_attack_id)
        if attack:
            return attack.json()
        else:
            return {"Message": "Could not find this ID"}, 500

    def put(self, charger_attack_id):
        #try:
        data = ChargerAttack.parser.parse_args()
        attack = ChargerAttackModel.find_by_id(charger_attack_id)
        if attack:
            new_attack_name = data['charger_attack_name']
            new_damage = data['damage']
            new_type_id = data['type_id']
            attack.update_attack(new_attack_name, new_damage, new_type_id)
            attack.save_to_db()
            return attack.json(), 201
        else:
            return {"Message": "Could not find this ID"}, 404
        #except:
            #return {"Message": "Internal error accoured"}, 500

class Charger_Attack_by_type(Resource):
    def get(self, type_id):
        #print(type_id)
        try:
            attacks = ChargerAttackModel.query.filter_by(type_id=type_id)
            
            type_attack = TypesModel.find_by_id(type_id)
            type_attack = type_attack.json()
            #print(type_attack)
            type_name = type_attack['type_name']

            type_attack = ChargerAttackModel.query.filter_by(type_id=type_id).first()

            return {f'attacks from {type_name}': [x.json() for x in attacks]}
        except:
            return {'Message': 'An error occurred while to try filter all attacks by type {type_id}'}, 500