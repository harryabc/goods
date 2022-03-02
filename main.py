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
            "name": "Apple iPhone 13 Pro Max 256GB",
            "image": "https://img1.360buyimg.com/img/jfs/t1/206327/14/6656/37878/614182f3Ec0388cb1/9c624f9cdc0ef6b0.jpg",
            "price": "9799.00",
            "ware": "天猫"
        },
        {
            "id": 2,
            "name": "Apple iPhone 13 Pro 套装 256GB",
            "image": "https://img30.360buyimg.com/img/jfs/t1/213424/38/890/63246/616d3d24E1b79e093/ccfb3724000eb2f3.jpg",
            "price": "12899.00",
            "ware": "淘宝"
        },
        {
            "id": 3,
            "name": "Apple iPhone 13 Pro 金色",
            "image": "https://img10.360buyimg.com/img/jfs/t1/82549/18/16596/35941/6141c60bE7c2fab8a/e619bc383c1f524a.jpg",
            "price": "8799.00",
            "ware": "淘宝"
        },
        {
            "id": 4,
            "name": "Apple iPhone 13 Pro",
            "image": "https://img20.360buyimg.com/img/jfs/t1/145583/7/20347/204802/614beca5Effadf187/e1a790c81b86aecb.jpg",
            "price": "9799.00",
            "ware": "京东"
        },
        {
            "id": 5,
            "name": "Apple iPhone 13 Pro",
            "image": "https://img14.360buyimg.com/img/jfs/t1/202422/15/6977/26859/6143579bE79557c8c/b72c71338a403952.jpg",
            "price": "8999.00",
            "ware": "拼多多"
        }
    ]

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
