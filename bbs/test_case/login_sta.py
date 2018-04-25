import unittest, random, sys
import time
from .models import myuni, function
from .page_obj.loginPage import Login


class LoginTest(myuni.MyTest_unittest):
    '''社区用户登陆'''

    # 测试用户登陆
    def user_login_verify(self, username='', passwd=''):
        # 发送用户名和密码
        Login.user_login(username=username, passwd=passwd)

    def test_login(self):
        # 填入空白的用户名和密码
        self.user_login_verify()
        po = Login(driver=self.driver)
        self.assertEqual(po.user_error_hint(), '账号不能为空')
        self.assertEqual(po.passwd_error_hint(), '密码不能为空')
        function.insert_img(driver=self.driver, file_name='user_pawd_empy.jpg')

    def test_login2(self):
        self.user_login_verify(username='username')
        po = Login(driver=self.driver)
        self.assertEqual(po.passwd_error_hint(), '密码不能为空')
        function.insert_img(self.driver, 'passwd_empty.jpg')

    def test_login3(self):
        self.user_login_verify(passwd='passwd')
        po = Login(driver=self.driver)
        self.assertEqual(po.passwd_error_hint(), '账号不能为空')
        function.insert_img(driver=self.driver, file_name='user_empty.jpg')

    def test_login4(self):
        self.user_login_verify(username='username', passwd='passwd')
        po = Login(driver=self.driver)
        self.assertEqual(po.passwd_error_hint(), '密码与账号不匹配')
        function.insert_img(driver=self.driver, file_name='user_passwd_error')

    def test_login5(self):
        self.user_login_verify(username='username', passwd='passwd')
        time.sleep(2)
        po = Login(driver=self.driver)
        self.assertEqual(po.user_login_success(), '登陆成功')


if __name__ == '__main__':
    unittest.main()
