from flask_restful import Resource, reqparse
from models.types import TypesModel
from database import db

class Type(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('type_id', type=int, required=True)
    parser.add_argument('type_name', type=str)

    def post(self, type_name):
    
        data = Type.parser.parse_args()
        type_id = data['type_id']
        
        type_name = TypesModel(type_id, type_name)
        print(type_name)
        
        
        
        