import requests
import pytest
from business.login_business import login


@pytest.fixture(scope="session")
def session(base_url):
    """session直接登陆"""
    s = requests.session()
    login(s, base_url)
    yield s
    print("yield后面是后置操作")
    s.close()


@pytest.fixture(scope="function")
def unlogin():
    """不需要登陆"""
    s = requests.session()
    yield s
    s.close()
