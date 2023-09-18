from flask import Flask, jsonify, request
# 자바스크립트 데이터 저장방식으로 저장
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

@app.route('/')
def hello_flask():
    return 'hello_flask'

# GET /menus : 자료 가져옴
@app.route('/menus') # methods = : default값 : GET
def get_menus(): # 해당 함수 return 값이 http return값으로 들어감
    # connect with db
    db_connection = connection() 
    cursor = db_connection.cursor()
    # GET
    query = 'SELECT * FROM menu'
    cursor.execute(query)
    # return
    data = cursor.fetchall()
    #close
    close(cursor,db_connection)

    return jsonify(data)

# POST /menus : 자료를 자원에 추가
@app.route('/menus', methods = ['POST'] )
def create_menu():
    # 전달받은 자료를 menus에 추가 : {'name' : ..., 'price' : ...}
    # connect with db
    db_connection = connection()
    cursor = db_connection.cursor()
    request_data = request.get_json() # request : 클라이언트의 요청 내용이 담김 -> json으로 파싱
    # POST
    insert_query = "INSERT INTO menu(name,price) VALUES(%s,%s)"                                    
    data = (request_data['name'],request_data['price'])
    cursor.execute(insert_query,data)
    db_connection.commit()
    # return
    output_query = 'SELECT * FROM menu ORDER BY id DESC LIMIT 1'
    cursor.execute(output_query)
    output = cursor.fetchall()
    # close
    close(cursor, db_connection)

    return jsonify(output)
        # 새로 추가된 자원 반환

# PUT : 수정
@app.route('/menus/<int:id>', methods = ['PUT'])
def put_menu(id):
    db_connection = connection()
    request_data = request.get_json()
    cursor = db_connection.cursor()
    # PUT
    put_query = 'UPDATE menu SET name=%s,price=%s WHERE id=%s'
    data = (request_data['name'], request_data['price'], str(id))
    cursor.execute(put_query, data)
    db_connection.commit() # 이걸 해야 적용됨.
    # return
    output_query = 'SELECT * FROM menu WHERE id=%s'
    cursor.execute(output_query, (id,)) # 전달할 인자가 하나더라도 tuple 또는 list 형태를 유지할 것.
    output = cursor.fetchall()
    # close
    close(cursor, db_connection)
    return jsonify(output)

# DELETE
@app.route('/menus/<int:id>', methods = ['DELETE'])
def delete_menu(id):
    # connet with db
    db_connection = connection()
    cursor = db_connection.cursor()
    # # return 
    output_query = 'SELECT * FROM menu WHERE id=%s'
    cursor.execute(output_query, (id,))
    output = cursor.fetchall()
    # DELETE 
    delete_query = 'DELETE FROM menu WHERE id = %s'
    cursor.execute(delete_query, (id,))
    db_connection.commit()
    # close
    close(cursor, db_connection)
    return jsonify(output)

if __name__ == '__main__':
    app.run()


'''
mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="pw",
    database="FLASK_BASIC",
    auth_plugin='mysql_native_password'
)
'''