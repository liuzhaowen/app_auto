from selenium.webdriver.common.by import By
from Base.base import Base

# 此页面定位元素信息
loc_username = (By.ID, "com.vcooline.aike:id/etxt_username")
loc_pwd = (By.ID, "com.vcooline.aike:id/etxt_pwd")
loc_login_btn = (By.ID, "com.vcooline.aike:id/btn_login")

class LoginPage(Base):
    """登录页面"""

    # 登录页面输入用户名
    def page_input_username(self, username):
        self.base_input_element(loc_username, username)

    # 登录页面输入用户密码
    def page_input_pwd(self, passwd):
        self.base_input_element(loc_pwd, passwd)

    # 登录按钮点击
    def page_login_commit(self):
        self.base_click_element(loc_login_btn)

