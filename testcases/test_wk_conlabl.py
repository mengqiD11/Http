import json
from pprint import pprint

import pytest

from api.base_api import BaseApi
from api.department import Department


class TestContestLbl():
    test_data = BaseApi.loadyaml('test_department_data.yaml')

    # 将setup提升为setupclass，这样所有用例执行前只需要执行一次，不需要每次都执行
    @classmethod
    def setup_class(cls):
        cls.depart = Department()

    def setup(self):
        pass

    # 添加部门用例
    @pytest.mark.parametrize("old_name,new_name", test_data)
    def test_all(self, old_name, new_name):
        # 将删除功能提升到setup_class 中
        for name in [old_name, new_name]:
            depart_id = self.depart.jsonPath(self.depart.get_demprt_list(), f'$..department[?(@.name=="{name}")].id')
            if depart_id:
                self.depart.del_demprt(id=depart_id[0])
        assert self.depart.add_demprt(name=old_name, id=3)['errcode'] == 0
        # 需要加[0]
        depart_id = self.depart.jsonPath(self.depart.get_demprt_list(), f'$..department[?(@.name=="{old_name}")].id')[0]
        print(depart_id)
        assert self.depart.edit_demprt(name=new_name, id=depart_id)['errcode'] == 0



    @pytest.mark.skip
    # 获取部门用例
    def test_get_deprtList(self):
        # json.dumps对返回的json数据进行格式化，这里indent是缩进的意思一般写为4 或者2
        print(json.dumps(self.depart.get_demprt_list(), indent=2))

    @pytest.mark.skip
    # 编辑部门用例
    def test_edit_deprt(self):
        print(self.depart.edit_demprt(3, "上海中心"))

    @pytest.mark.skip
    # 删除部门用例
    def test_del_deprt(self):
        print(self.depart.del_demprt(3))
