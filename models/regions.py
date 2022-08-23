from database import db

class RegionModel(db.Model):
    __tabelaname__ = 'regions'

    region_id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(20))

    def __init__(self,  region_name):
        self.region_name = region_name
        self.region_id = region_id

    def json(self):
        return {
            'region_name': self.region_name,
            'region_id': self.region_id
        }
    
    @classmethod
    def find_by_id(cls, region_id):
        region = cls.query.filter_by(region_id=region_id).first()
        return region
        

    @classmethod
    def find_by_name(cls, region_name):
        region = cls.query.filter_by(region_name=region_name).first()
        return region

    
    def find_all_regions(cls):
        return cls.query.all()

    
    def save_to_database(self):
        db.session.add(self)
        db.session.commit()