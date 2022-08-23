from flask_restful import Resource, reqparse
from models.regions import RegionModel


class Region(Resource):
    parser = reqparse.RequestParser()
    #parser.add_argument('region_id')
    #parser.add_argument('region_name', type=str, required=True)
    

    def post(self, region_name):
        """ region = RegionModel.find_by_name(region_name)
        
        if region:
            region = region.json()
            return (
                {"Message": f"An region with name '{region['region_name']}' already exists"}
            )

        
        region = RegionModel(region_name)

        try:
            region.save_to_database()
        except:
            return {"message": "Erro"}
        
        return region.json(), 201 """
        "seu post esta dando erro, terá que começar de novo para ficar bom igual você espera conseguir deixar"


""" class All_Regions(Resource):
    def get(self):
        return {"regions": [region.json() for region in RegionModel.find_all_regions()]} """
    
