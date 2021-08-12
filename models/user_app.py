from db import db

class UserAppModel(db.Model):

    __tablename__ = 'users_app'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    rut = db.Column(db.Integer)
    campus = db.Column(db.String(80))
    career = db.Column(db.Integer)
    permission = db.Column(db.String(80))
    def __init__(self, name, permission):
        self.name = name
        self.permission = permission
    
    def json(self):
        #return {'name':self.name, 'permission': self.permission}
        return {'name':self.name}
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
    @classmethod
    def find_by_rut(cls,rut):
        return cls.query.filter_by(rut=rut).first()
    @classmethod
    def find_by_campus(cls,campus):
        return cls.query.filter_by(campus=campus)
    @classmethod
    def find_by_career(cls,career):
        return cls.query.filter_by(career=career)
    @classmethod
    def find_by_career_campus(cls, career, campus):
        return cls.query.filter_by(career=career).filter_by(campus=campus)
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()