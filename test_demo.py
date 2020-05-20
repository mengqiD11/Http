import pytest
import requests
from requests.auth import HTTPBasicAuth


class TestDemo:
    # 发起get请求
    @pytest.mark.skip
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        assert r.status_code == 200

    @pytest.mark.skip
    # 带参数的get
    def test_query(self):
        payload={
            "level" : 1,
            "name" : "testing"
        }
        r = requests.get('https://httpbin.testing-studio.com/get',params=payload)
        print(r.status_code)
        # 获取对应的字节数
        print(r.raw.read(10))
        # 获取请求的内容
        print(r.request)
        assert r.status_code == 200

    @pytest.mark.skip
    # post 请求
    def test_post_form(self):
        infomes = {
            "username" : "kingmax_zcp",
            "password" : "kingmaxzcp"
        }
        r = requests.post("https://home.testing-studio.com/login",data=infomes)
        print(r.request)

    @pytest.mark.skip
        # json 请求
    def test_post_json(self):
        infomes = {
            "username": "kingmax_zcp",
            "password": "kingmaxzcp"
        }
        r = requests.post("https://home.testing-studio.com/login", json=infomes)
        print(r.text)


    @pytest.mark.skip
    def test_header(self):
        r = requests.get("https://httpbin.testing-studio.com/get",headers={"h": "header demo"})
        print(r.json())
        r.json()['headers']['H'] == 'header demo'

    @pytest.mark.skip
    def test_headerT(self):
        # 使用header传递cookie信息，Cookie首字母大写且不加s
        header = {
            'Cookie' : 'horgwars',
            # 定制header信息
            'User-Agent': 'horgwars',
        }
        r = requests.get("https://httpbin.testing-studio.com/cookies",headers=header)
        print(r.request.headers)

    @pytest.mark.skip
    def test_cookie(self):
        header = {
            'User-Agent': 'horgwars',
        }
        cookie_data= {
            "Hogwarts" : "school",
            "teacher" : 'ad'
        }
        r = requests.get("https://httpbin.testing-studio.com/cookies", headers=header,cookies=cookie_data)
        print(r.request.headers)

    #基础认证
    def test_auth(self):
        #("zcp","123")相当于用户名、密码
        r = requests.get("http://httpbin.testing-studio.com/basic-auth/zcp/123",auth=HTTPBasicAuth("zcp","123"))
        print(r.text)