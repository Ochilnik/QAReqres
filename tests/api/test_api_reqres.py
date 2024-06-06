import pytest


@pytest.mark.api
def test_list_users(reqres_api):
    r = reqres_api.list_users()
    assert r['data'] != 0

@pytest.mark.api
def test_list_user(reqres_api):
    num = reqres_api.list_users()
    for user_num in range(1, num['total']+1):
        r = reqres_api.list_user(user_num)
        assert r['data']['id'] == user_num

@pytest.mark.api
def test_no_user(reqres_api):
    user_num = 23
    r = reqres_api.list_user(user_num)
    assert r == {}

@pytest.mark.api
def test_list_resources(reqres_api):
    r = reqres_api.list_resources()
    assert r['data'] != 0

@pytest.mark.api
def test_list_resource(reqres_api):
    num = reqres_api.list_resources()
    for res_num in range(1, num['per_page']+1):
        r = reqres_api.list_resource(res_num)
        #print(r['data']['id'])
        assert r['data']['id'] == res_num

@pytest.mark.api
def test_no_resource(reqres_api):
    res_num = 23
    r = reqres_api.list_resource(res_num)
    assert r == {}
