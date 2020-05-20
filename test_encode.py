
#基于加密接口测试用例的设计
import base64
import json

import requests
class TestDecode:

    def send(self,data:dict):
        res = requests.request(data['method'],data['url'],headers=data['headers'])
        if data['encoding'] == 'base64':
            #load() 是加载文件,使用base64解码，前题是知道公司使用该方式进行的加密
            return json.loads(base64.b64decode(res.content))
        # 如果是第三方加密方式，把加密后的响应值发送给第三方，让第三方去做解密工作并返回解密后的信息
        elif data['encoding'] == 'qita':
            return  requests.post("url",data=res.content)
