from flask import request
from flask_restplus import Resource, fields



from models.product import ProductModel
from schemas.product import ProductSchema

from server.instance import server

product_ns = server.products_ns

product_schema = ProductSchema()
product_list_schema = ProductSchema(many=True)


ITEM_NOT_FOUND = 'Product not fund.'

item = product_ns.model('Product',{
    'name': fields.String(description='Product name'),
    'title': fields.String(description='Product title'),
    'price': fields.Float(description='Product price')
})


class Product(Resource):
    
    def get(self, id):
        product_data = ProductModel.find_by_id(id)
        if product_data:
            return product_schema.dump(product_data), 200
        return {'message': ITEM_NOT_FOUND}, 400

    @product_ns.expect(item)
    def put(self, id):
        product_data = ProductModel.find_by_id(id)
        product_json = request.get_json()

        product_data.name = product_json['name']
        product_data.title = product_json['title']
        product_data.price = product_json['price']

        product_data.save_to_db()
        return product_schema.dump(product_data), 200

    def delete(self, id):

        product_data = ProductModel.find_by_id(id)
        if product_data:
            product_data.delete()
            return '', 204
        return {'message': ITEM_NOT_FOUND}



class Productlist(Resource):
    def get(self,):
        return product_list_schema.dump(ProductModel.find_all()), 200 


    @product_ns.expect(item)
    @product_ns.doc('Create itens')
    def post(self, ):
        product_json = request.get_json()
        product_data = product_schema.load(product_json)
        
        product_data.save_to_db()
        


        return product_schema.dump(product_data), 201
        
        


