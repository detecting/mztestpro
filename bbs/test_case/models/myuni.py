# 自定义测试框架类
import unittest as unittest
import unittest
from .driver import browser


class MyTest_unittest(unittest.TestCase):
    # 初始化浏览器
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
