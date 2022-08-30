from flask import Flask
from flask_restful import Api 
from resources.regions import Region, All_Regions
from resources.types import Types, AllTypes
#from resources.fast_attacks import Attack, AllAttacks, Attack_by_type
#from resources.pokemons import Pokemon

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(All_Regions, '/regions')
api.add_resource(Region, '/region/<string:region_name>')

api.add_resource(AllTypes, '/types')
api.add_resource(Types, '/type/<string:type_name>')

api.add_resource(All_Fast_Attacks, '/attacks')
api.add_resource(Fast_Attack, '/attack/<int:attack_id>')
api.add_resource(Fast_Attack_by_type, '/attack_by_type/<int:type_id>')

#api.add_resource(Pokemon, '/pokemon/<int:number_id>')
#api.add_resource(Pokemons, '/pokemons')

@app.before_first_request
def creat_database():
    db.create_all()

if __name__ == "__main__":
    from database import db
    db.init_app(app)
    app.run(debug=True)