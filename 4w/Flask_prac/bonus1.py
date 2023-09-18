## 필수과제 + bonus 1

from flask import Flask, jsonify, request
# 자바스크립트 데이터 저장방식으로 저장

app = Flask(__name__)

menus = [
{'id': 1, 'name':'Espresso','price':3800},
{'id': 2, 'name':'Americano','price':4100},
{'id': 3, 'name':'Latte','price':4600}
]
nid = 4

@app.route('/')
def hello_flask():
    return 'hello_flask'

# GET /menus : 자료 가져옴
@app.route('/menus') # methods = : default값 : GET
def get_menus(): # 해당 함수 return 값이 http return값으로 들어감
    return jsonify({"menus": menus})

# POST /menus : 자료를 자원에 추가
@app.route('/menus', methods = ['POST'] )
def create_menu():
    # 전달받은 자료를 menus에 추가
    # {'name' : ..., 'price' : ...}
    global nid

    request_data = request.get_json() # request : 클라이언트의 요청 내용이 담김 -> json으로 파싱
    new_menu ={
        'id' : nid,
        'name' : request_data['name'],
        'price' : request_data['price'],
    }
    nid += 1
    menus.append(new_menu) 
    return jsonify(new_menu) # 새로 추가된 자원 반환

#PUT
@app.route('/menus/<int:id>', methods = ['PUT'])
def put_menu(id):
    request_data = request.get_json()
    menus[id-1]['name'] = request_data['name']
    menus[id-1]['price'] = request_data['price']
    
    return jsonify(menus[id-1])

# DELETE
@app.route('/menus/<int:id>', methods = ['DELETE'])
def delete_menu(id):
    before = len(menus)
    menus.pop(id-1)
    return f'{before} datas become {len(menus)} datas'

if __name__ == '__main__':
    app.run()