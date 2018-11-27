import sys, os
sys.path.append(os.getcwd())

from Base.get_driver import get_driver
from Page.login_page import LoginPage

class TestLogin(object):
    """登录测试类"""

    def setup_class(self):
        self.login_page = LoginPage(get_driver())

    def tear_down(self):
        self.login_page.driver.quit()

    def test_login(self):
        self.login_page.page_input_username("18210783786")
        self.login_page.page_input_pwd("shshiailin")
        self.login_page.page_login_commit()
        assert 1



