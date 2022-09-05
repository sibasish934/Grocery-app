def getQuantity(connection):
    cursor = connection.cursor()

    query = ("select * from quantity_index")
    cursor.execute(query)

    response = []
    for (uam_id, uam_name) in cursor:
        response.append({
            'uam_id': uam_id,
            'uam_name': uam_name
        })
    return response

if __name__ == '__main__':
    from sql_connection import get_Sql_connection
    connection = get_Sql_connection()
    print(getQuantity(connection))