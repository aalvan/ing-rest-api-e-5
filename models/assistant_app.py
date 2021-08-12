from db import db

class AssistantAppModel(db.Model):
    __tablename__ = 'assistants_app'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    rut = db.Column(db.Integer)
    range = db.Column(db.String(80))
    manager = db.Column(db.Integer)
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
    def find_by_range(cls,range):
        return cls.query.filter_by(range=range)
    @classmethod
    def find_by_manager(cls,manager):
        return cls.query.filter_by(manager=manager)
    @classmethod
    def find_by_manager_range(cls, manager, range):
        return cls.query.filter_by(manager=manager).filter_by(range=range)
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()