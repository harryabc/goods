from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/goods', methods=['GET'])
def goods():

    data = [
        {
            "id": 1,
            "name": "Apple iPhone 13",
            "image": "https://img1.360buyimg.com/img/jfs/t1/206327/14/6656/37878/614182f3Ec0388cb1/9c624f9cdc0ef6b0.jpg",
            "price": "9799.00",
            "ware": "京东自营"
        },
        {
            "id": 2,
            "name": "Apple iPhone 13",
            "image": "https://img10.360buyimg.com/img/jfs/t1/82549/18/16596/35941/6141c60bE7c2fab8a/e619bc383c1f524a.jpg",
            "price": "8799.00",
            "ware": "天猫"
        },
        {
            "id": 3,
            "name": "小米Redmi 红米note9",
            "image": "https://img10.360buyimg.com/img/jfs/t1/168666/4/23738/170302/613ca1edE34ec60b1/f3c2ba7bbf84a149.jpg",
            "price": "1099.00",
            "ware": "淘宝"
        },
        {
            "id": 4,
            "name": "ROG游戏手机5s",
            "image": "https://img11.360buyimg.com/img/jfs/t1/192403/9/21433/117581/6130856cE2b75c0c7/fa706f41b56b77c6.jpg",
            "price": "4499.00",
            "ware": "淘宝"
        },
        {
            "id": 5,
            "name": "vivo iQOO 7",
            "image": "https://img10.360buyimg.com/img/jfs/t1/170012/31/21215/75108/61554ac7E0c731e73/d73ec930b6307bd4.jpg",
            "price": "2998.00",
            "ware": "淘宝"
        }
    ]

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
