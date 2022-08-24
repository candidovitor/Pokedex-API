from flask import Flask
from flask_restful import Api 
from resources.regions import Region, All_Regions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(All_Regions, '/regions')
api.add_resource(Region, '/region/<string:region_name>')


@app.before_first_request
def creat_database():
    db.create_all()

if __name__ == "__main__":
    from database import db
    db.init_app(app)
    app.run(debug=True)