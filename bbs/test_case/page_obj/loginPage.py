from selenium.webdriver.common.by import By
from .base import Page
from time import *


class Login(Page):
    '''用户登录页'''
    url = '/'
    # action
    bbs_lgin_user_loc = (BY.XPATH, '//*')
    bbs_login_button_loc = (BY.ID, 'mslogin')

    def bbs_login(self):
        self.driver.find_element(*self.bbs_lgin_user_loc).click()
        sleep(1)
        self.driver.find_element(*self.bbs_login_button_loc).click()

    login_username_loc = (BY.ID, 'account')
    login_passwd_loc = (BY.ID, 'passwd')
    bbs_login_button_loc = (BY.ID, 'login')

    '''登陆用户名'''

    def login_username(self, username):
        self.driver.find_element(*self.login_username_loc).send_key(username)

    '''登陆密码'''

    def login_passwd(self, passwd):
        self.driver.find_element(*self.login_passwd_loc).send_key(passwd)

    '''登陆按钮'''

    def login_button(self):
        self.driver.find_element(*self.bbs_login_button_loc)

    '''定义统一的登陆按钮'''
    username = 'username'
    passwd = 'passwd'

    def user_login(self, username=username, passwd=passwd):
        self.open()
        self.bbs_login()
        # 发送用户名
        self.login_username(username)
        # 发送密码
        self.login_passwd(passwd)
        self.login_button()
        sleep(1)

    '''登陆错误提示'''
    user_error_hint_loc = (BY.XPATH, '')
    passwd_error_hint_loc = (BY.XPATH, '')
    user_login_success_loc = (BY.ID, '')

    def user_error_hint(self):
        return self.driver.find_element(*self.user_error_hint_loc).text

    def passwd_error_hint(self):
        return self.driver.find_element(*self.passwd_error_hint_loc).text

    def user_login_success(self):
        return self.driver.find_element(*self.user_login_success_loc).text
