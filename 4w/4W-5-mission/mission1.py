from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def connection(): # SQL과 연결할 때 사용
    return mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Wjddusjy12!",
    database="FLASK_BASIC"
    )

def close(cursor, db_connection): # 사용 후 반드시 닫아주기!
    return cursor.close() ; db_connection.close()


@app.route('/whoami')
def get_gitid():
    id = 'JY-maru'
    return jsonify({"name":id})

@app.route('/echo')
def get_str():
    query = request.args.get('string', default=None)

    if query is not None:
        output = { "value" : query }
    else :
        output = { "error" : "No 'String' parameter provided in Query"}
    return jsonify(output)


### SQL과 연동된 API
def connection(): # SQL과 연결할 때 사용
    return mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Wjddusjy12!",
    database="FLASK_BASIC"
    )

def close(cursor, db_connection): # 사용 후 반드시 닫아주기!
    return cursor.close() ; db_connection.close()

# READ
@app.route('/weapon')
def get_weapon(): 
    db_conn = connection()
    cursor = db_conn.cursor()
    # get
    get_q = 'SELECT * FROM weapon'
    cursor.execute(get_q)
    # output
    output = cursor.fetchall()
    
    #close
    close(cursor,db_conn)
    return jsonify(output)

# Create
@app.route('/weapon', methods=['POST'])
def put_weapon():
    db_conn = connection()
    cursor = db_conn.cursor()
    request_data = request.get_json()

    post_q = 'SELECT * FROM weapon WHERE name=%s'
    name, stock = request_data['name'],request_data['stock']
    cursor.execute(post_q,(name,))

    result = cursor.fetchall()

    if result : #exception
        output = f"Existent weapon \'{name}\', Use Update "
    else : 
        cursor.execute('INSERT INTO weapon (name,stock) VALUES(%s, %s)',(name,stock))
        db_conn.commit()
        cursor.execute('SELECT * FROM weapon WHERE name=%s',(name,))
        output = cursor.fetchall()
    
    return jsonify(output)

# UPDATE
@app.route('/weapon/<string:name>', methods=['PUT'])
def post_weapon(name): 
    db_conn = connection()
    cursor = db_conn.cursor()
    request_data = request.get_json()
    # PUT
    post_q = 'SELECT * FROM weapon WHERE name=%s'
    r_stock = request_data['stock']
    cursor.execute(post_q,(name,))

    result = cursor.fetchall() # 2차원 list형태

    if not result : #exception
        output = f"Key Error : Non-Existent weapon \'{name}\' "
    else : 
        cursor.execute('UPDATE weapon SET stock=%s WHERE name=%s',(r_stock+result[0][1],name))
        db_conn.commit()
        cursor.execute('SELECT * FROM weapon WHERE name=%s',(name,))
        output = cursor.fetchall()

    close(cursor,db_conn)
    return jsonify(output)

#Delete
@app.route('/weapon/<string:name>', methods=['DELETE'])
def delete_weapon(name):
    db_conn = connection()
    cursor = db_conn.cursor()
    request_data = request.get_json()
    # DELETE
    post_q = 'SELECT * FROM weapon WHERE name=%s'
    cursor.execute(post_q,(name,))

    result = cursor.fetchall() # 2차원 list형태

    if not result : #exception
        output = f"Key Error : Non-Existent weapon \'{name}\' "
    else : 
        cursor.execute('DELETE FROM weapon WHERE name=%s',(name, ))
        db_conn.commit()
        output = result

    close(cursor,db_conn)
    return jsonify(output)
