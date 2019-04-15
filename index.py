import json
import requests
from flask import Flask, request
app = Flask(__name__)

# https://oapi.dingtalk.com/robot/send?access_token=8d6b1dcc3a69d80eca2823780ac98cf4e2dcd1fc5f1cee22ddb16e9936f1664c
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

@app.route('/merge_request_to/<svc>', methods=['POST'])
def merge_request_to(svc):

    if not request.json or request.json.get('event_type') not in ('merge_request'):
        return 'miss', 200

    tels = request.args.get('tels', '')
    headers = {'content-type': 'application/json'}
    url = 'https://oapi.dingtalk.com/robot/send?access_token=0100b90e11fb19345116ca4580c9b168995c1f3ef95f67bb941ff11a80ca137c'
    at_any_person = ''
    for tel in tels.split(','):
        at_any_person = at_any_person + '@' + tel + ' '
    merge_request_data = {
        "msgtype": "markdown",
        "markdown": {
            "title":"又有大佬合并代码啦",
            "text": "#### 又有大佬合并代码啦,{} 快去合并 \n".format(at_any_person) +
                    "microservice.{}".format(svc) +
                    "> ![screenshot](http://shawn-resource-test.oss-cn-hongkong.aliyuncs.com/heihei%20-%20%E5%89%AF%E6%9C%AC.jpg)\n"  +
                    "> ###### [Open Repostory](http://{}/ifaios/microservice.{}/merge_requests) \n".format(request.remote_addr, svc)
        },
        "at": {
            "isAtAll": not bool(tels),
            'atMobiles': tels.split(',')
        }
    }
    
    res = requests.post(url, data=json.dumps(merge_request_data), headers=headers)
    return str(res.ok), 200
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10087)