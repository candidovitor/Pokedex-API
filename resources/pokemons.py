from flask_restful import Resource, reqparse
from models.pokemons import PokemonModel

from database import db

class Pokemon(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('number_id', type=int, required=True)
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('evolution', required=True)
    parser.add_argument('type_id', type=int, required=True)
    parser.add_argument('region_id', type=int, required=True)
    parser.add_argument('attack_id_1', type=int, required=True)
    parser.add_argument('attack_id_2', type=int, required=True)
    parser.add_argument('hit_point', type=int, required=True)