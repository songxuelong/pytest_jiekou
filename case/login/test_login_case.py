import pytest
from business.login_business import login


class Test_Login():
    def test_login(self, session, base_url):
        login(session, base_url)
