import pytest
from business.dk_business import dk


class Test_Dk():
    def test_login(self, session, base_url):
        dk(session, base_url)
