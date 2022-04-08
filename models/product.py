from db import db

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False )


    def __init__(self ,name, price, title):
        self.name = name
        self.title = title
        self.price = price



    def __repr__(self):
        return f'ProductModel(name={self.name}, title{self.title}, price={self.price})'
   
    
    def json(self,):
        return {
            'name':self.name,
            'title':self.title,
            'price':self.price
        }

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls,):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


