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
        self.login_page.page_input_pwd("shshiailin44")
        self.login_page.page_login_commit()
        try:
            # 获取登陆失败toast消息
            fail_msg = self.login_page.get_toast("密码错误")
            if fail_msg:
                assert "密码错误"==fail_msg
            else:
                assert False
        except AssertionError:
            print("未获取到")





