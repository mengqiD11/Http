#基于加密接口测试用例的设计

import test_encode


class TestDe:
    req_data = {
        "method": "get",
        "url": "http://localhost:9999/demo1.txt",
        "headers" : None,
        "encoding" : "base64"
    }

    def test_send(self):
        ar = test_encode.TestDecode()
        print(ar.send(self.req_data))