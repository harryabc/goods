from flask import Flask, request, abort
import json
import requests

from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/goods', methods=['GET'])
def goods():
    data = [
        {
            'id': '001',
            'name': 'iphone 13',
            'icon': 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwx2.sinaimg.cn%2Fmw690%2F005JnC28gy1gv29r6vixbj60u90sugmn02.jpg&refer=http%3A%2F%2Fwx2.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1636543502&t=d76bee196a40aaaa1ccad2f1776f0c14',
            'price': 7999
        },
        {
            'id': '002',
            'name': 'iphone 12',
            'icon': 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimgservice.suning.cn%2Fuimg1%2Fb2c%2Fimage%2FgX79QCob9Xsc-m1QKulpKw.png_800w_800h_4e&refer=http%3A%2F%2Fimgservice.suning.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1636543266&t=2cd7386edcb25f99dece44a34e0a08d3',
            'price': 5999
        },
        {
            'id': '003',
            'name': 'iphone 11',
            'icon': 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimage.suning.cn%2Fuimg%2FZR%2Fshare_order%2F161601868603214243.jpg&refer=http%3A%2F%2Fimage.suning.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1636543591&t=2dd249867f03452826633dbd7f06b439',
            'price': 3999
        },
    ]

    return jsonify(data)
    # return json.dumps(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
