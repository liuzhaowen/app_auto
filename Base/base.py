from selenium.webdriver.support.wait import WebDriverWait

class Base(object):
    """在Base类中，封装常用的公共方法"""

    def __init__(self, driver):
        self.driver = driver

    # 基础查找元素的方法
    def base_find_element(self,loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(*loc))

    # 基础查找元素并点击
    def base_click_element(self, loc):
        self.base_find_element(loc).click()

    # 基础查找元素并输入
    def base_input_element(self, loc, text):
        self.base_find_element(loc).clear().send_keys(text)

