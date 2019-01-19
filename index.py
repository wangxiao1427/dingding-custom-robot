import json
import requests
from flask import Flask, request
app = Flask(__name__)


@app.route('/merge_request', methods=['POST'])
def merge_request():
    headers = {'content-type': 'application/json'}
    url = 'https://oapi.dingtalk.com/robot/send?access_token=af7ce2df70e5af368aba688e28d552fc9d60fba4761769b0ed62e5f8cc9c2fae'
    merge_request_data = {
        "msgtype": "text",
        "text": {
            "content": "又有大佬合并代码啦"
        },
        "at": {
            "isAtAll": True
        }
    }
    res = requests.post(url, data=json.dumps(merge_request_data), headers=headers)
    return res.ok, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6799)