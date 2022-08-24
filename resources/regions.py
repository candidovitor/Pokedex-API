from flask_restful import Resource, reqparse
from models.regions import RegionModel
from database import db

class Region(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('region_id', type=int, required=True)
    parser.add_argument('region_name', type=str)
    

    def get(self, region_name):       
        try:
            region = RegionModel.find_by_name(region_name)
            if region:
                return region.json()
            return{"messege": "Region not found"}, 404
        except Exception:
            return {'Message': 'An error occurred while getting the region'}, 500

    def post(self, region_name):
        region = RegionModel.find_by_name(region_name)
        #print(region)
        if region:
            return (
                {"Message": f"An region with name '{region_name}' already exists"}
            )
        data = Region.parser.parse_args()
        region_id = data['region_id']

        region = RegionModel(region_id, region_name)
    
        try:
            region.save_to_db()
        except:
            return {'Message': f'An error occurred while inserting the region'}, 500
        return region.json(), 201

    def put(self, region_name):
        try:
            data = Region.parser.parse_args()
            region = RegionModel.find_by_name(region_name)
            #print(region)
            
            if region:
                #print(data)
                new_region_id = data['region_id']
                new_region_name = data['region_name']
                region.update_region(new_region_id, new_region_name)

                region.save_to_db()
                return region.json(), 200
            else:
                region = RegionModel(region_name, **data)
            region.save_to_db()
            return region.json(), 200
        except:
            return {'Message': 'An error occurred while editing the region'}, 500
         

    def delete(self, region_name):
 
        region = RegionModel.find_by_name(region_name)
        if region:
            try:
                region.delete_region()
            except:
                return {'messege': 'An internal error ocurred trying to dalete region.'}, 500
            return {'messesge': 'Region deleted'}, 200
        else:
            return {'messesge': 'Region not found'}, 404
        
 


class All_Regions(Resource):
    def get(self):
        return {"regions": [region.json() for region in RegionModel.find_all_regions()]}
    
