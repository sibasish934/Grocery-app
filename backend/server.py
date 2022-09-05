import json

from flask import Flask, request, jsonify
from sql_connection import get_Sql_connection
import products_dao
import quantity_doa
import json

connection = get_Sql_connection()
app = Flask(__name__)


@app.route('/getProducts')
def getProducts():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getQuantityDetails', methods =['GET'])
def getQuantityDetails():
    product = quantity_doa.getQuantity(connection)
    response = jsonify(product)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python flask server for grocery store system")
    app.run(port=80)