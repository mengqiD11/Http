import requests


class TestWeworkRequests:
    corpid = "ww6b880a6a2a8988f6"
    corpsecret = "Du2nvVZHl_gbjePd6NgbfQgBbP4GxXEBMJXr6F0CiUg"

    depart_data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 2
    }
    depart_data_update = {
        "id": 2,
        "name": "广州中心",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1
    }
  # 在setup中先获取token
    def setup(self):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}")
        self.token = r.json()['access_token']

    def test_wework(self):
        # 获取部门列表
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id=2")
        if r.json()['errcode'] == 0:
              # 删除部门
              r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=2")
              print(r.json())

        # 创建部门
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}",json=self.depart_data)
        print(r.json())

        # 更新部门
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}",json=self.depart_data_update)
        print(r.json())




