# 发送request请求
import sys

import requests

corpid = "wwe4934ce99f2df160"
secret = "nqhCN81BzVACtMZpPqoIDm-iE41EKtw8MQIfjm0BM9A"
agentid = 1000002


# 获取access_token
def get_access_token():
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}')
    return res.json()["access_token"]


# 发送消息
def send_message(msg):
    token = get_access_token()
    url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}'
    data = {
        "touser": "@all",
        "msgtype": "text",
        "agentid": 1000002,
        "text": {
            "content": msg
        }
    }
    res = requests.post(url, json=data)


if __name__ == '__main__':
    msg = sys.argv[1]
    send_message(msg)
