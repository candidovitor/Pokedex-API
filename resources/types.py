from flask_restful import Resource, reqparse
from models.types import TypesModel
from database import db

class Types(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('type_id', type=int, required=True)
    parser.add_argument('type_name', type=str)

    def get(self, type_name):
        types = TypesModel.find_by_name(type_name)
        if types:
            return types.json()
        else:
            return {'Message':'Type not found'}, 404

    def put(self, type_name):
        try:
            data = Types.parser.parse_args()
            types = TypesModel.find_by_name(type_name)
            #print(types)

            if types:

                new_type_id = data['type_id']
                new_type_name = data['type_name']
                types.update_type(new_type_id, new_type_name)
        
                types.save_to_db()
                return types.json(), 200
            
            else:
                return {'Message':'Type could not be updated'}, 404 

        except:
            return {'Message': 'An error occurred while editing some type'}, 500

    def post(self, type_name):
        #print(type_name)

        try:
            data = Types.parser.parse_args()
            type_id = data['type_id']
            
            types = TypesModel(type_id, type_name)
            types.save_to_db()
            return types.json()
            #print('ok')
        except:
            return {'Message':'An error occurred while inserting the type'}, 500

    def delete(self, type_name):
        try:
            types = TypesModel.find_by_name(type_name)
            if types:
                types.delete_type()
                return {'Message':'Type deleted'}, 200
        except:
            return {'Message':'An error occurred while deleting type'}, 500

class AllTypes(Resource):
    def get(self):
        return {"Types": [types.json() for types in TypesModel.find_all_types()]}


        

        
        
        
        
        
        
        