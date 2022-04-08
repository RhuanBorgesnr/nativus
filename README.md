# REST API Nativus Salateria

API desenvolvida com o microfamework flask.


## Run the app

python app.py

## Get list of Products

### Request

`GET /products/`

curl -X 'GET' \
  'http://127.0.0.1:5000/api/products' \
  -H 'accept: application/json'


## Create another new Product

### Request

`POST /products/`

curl -X 'POST' \
  'http://127.0.0.1:5000/api/products' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Sanduíche de Pernil",
  "title": "Pão baquete, pernil suíno desfiado ao molho agridoce, salada de cenoura e repolho, alface, tomate e creme de queijo ou alho",
  "price": 15.49
}'

## Change a Product

### Request

`POST /products/id`

curl -X 'PUT' \
  'http://127.0.0.1:5000/api/product/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Fruit Bowl manga com maracujá",
  "title": "Sorbet de manga com maracujá e leite de coco ",
  "price": 13.99
}'

## Delete a Product

### Request

`DELETE /products/id`

curl -X 'DELETE' \
  'http://127.0.0.1:5000/api/product/1' \
  -H 'accept: application/json'



