from sql_connection import get_Sql_connection


def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.quantity_id, products.price, "
             "quantity_index.uam_name "
             "from products inner join quantity_index on "
             "quantity_index.uam_id = products.quantity_id")
    cursor.execute(query)

    response = []

    for (product_id, name, quantity_id, price, uam_name) in cursor:
        response.append({
            'product_id': product_id,
            'Name Of The Product': name,
            'Quantity needed': quantity_id,
            'Price Of the Quantity': price,
            'uam_name': uam_name
        })
        pass
    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()

    query = ("insert into products (name, quantity_id, price) "
             "values (%s, %s, %s)")
    data = (product['product_name'], product['quantity_id'], product['price'])

    cursor.execute(query, data)

    connection.commit()

    return cursor.lastrowid


def delete_from_products(connection, product_id):
    cursor = connection.cursor()

    query = ("delete from products where product_id =" + str(product_id))

    cursor.execute(query)

    connection.commit()


if __name__ == '__main__':
    connection = get_Sql_connection()
    print(insert_new_product(connection, {
        'product_name': 'Milk',
        'quantity_id': '1',
        'price': '40'
    }))

    print(delete_from_products(connection, 2))
