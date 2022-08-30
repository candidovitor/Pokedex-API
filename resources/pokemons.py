from flask_restful import Resource, reqparse
from models.pokemons import PokemonModel
from models.attacks import AttackModel
from models.types import TypesModel
from models.regions import RegionModel

from database import db

class Pokemon(Resource):
    parser = reqparse.RequestParser()
    #parser.add_argument('number_id', type=int, required=True)
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('evolution', type=str, required=True)
    parser.add_argument('type_id', type=int, required=True)
    parser.add_argument('region_id', type=int, required=True)
    parser.add_argument('attack_id_1', type=int, required=True)
    parser.add_argument('attack_id_2', type=int, required=True)
    parser.add_argument('hit_point', type=int, required=True)

    def post(self, number_id):
        #print(number_id)
        try: 
            pokemon = PokemonModel.find_by_id(number_id)
            if pokemon:
                return {'Message':'Id already in use'}, 404
            else: 
                data = Pokemon.parser.parse_args()
        
                name = data['name']
                evolution = data['evolution']

                type_id = data['type_id']
                region_id = data['region_id']
                attack_id_1 = data['attack_id_1']
                attack_id_2 = data['attack_id_2']
                hit_point = data['hit_point']

                pokemon = PokemonModel(number_id, name, evolution, type_id, region_id, attack_id_1, attack_id_2, hit_point)

                pokemon.save_to_db()
                return pokemon.json()
        except:
            return {'Message':'An error occurred while adding pokemon'}, 500
    
    def get(self, number_id):
        
        pokemon = PokemonModel.find_by_id(number_id)

        if pokemon:
            pokemon = pokemon.json()
            type_id = pokemon['type_id']
            print(type_id)
            results_type = db.session.query(TypesModel, PokemonModel).join(PokemonModel).filter_by(type_id=type_id)
            for typ,poke in results_type:
                #print(f' i = {typ.type_name}')
                pokemon.pop('type_id', None)
                pokemon ['type_name'] = typ.type_name


            print(results_type)
            #type_dict = []


            return pokemon
        else:
            return {'Message':'Pokemon number not found in pokedex'}, 404 
        
        

    def delete(self, number_id):
        try:
            pokemon = PokemonModel.find_by_id(number_id)
            if pokemon:
                pokemon.delete_pokemon()
                return {'messege':'Pokemon deleted from your pokedex'}, 200
            else:
                return {'messege':'Pokemon not found in your pokedex'}, 404
        except:
            return {'messege':'An internal error acourred'}, 500
    
    def put(self, number_id):
        try:
            data = Pokemon.parser.parse_args()

            pokemon = PokemonModel.find_by_id(number_id)
            if pokemon:
                
                new_name = data['name']
                new_evolution = data['evolution']
                new_type_id = data['type_id']
                new_region_id = data['region_id']
                new_attack_id_1 = data['attack_id_1']
                new_attack_id_2 = data['attack_id_2']
                new_hit_point = data['hit_point']

                pokemon.update_pokemon(new_name, new_evolution, new_type_id, new_region_id, new_attack_id_1, new_attack_id_2, new_hit_point) 
                pokemon.save_to_db()
                return pokemon.json(), 200
            
            else:
                return {"Message": "Could not find this ID"}, 404
        except:
            return {'messege':'An internal error acourred'}, 500


    

