from selenium import webdriver
from time import *


# 初始化类
class Page(object):
    login_url = 'http://www.126.com'

    def __init__(self, driver, url):
        self.base_url = url
        self.driver = driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_utl == (self.base_url) + self.url

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'did not land on {}'.format(url)

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):
    '''page login model'''
    username_loc = (BY.ID, 'idInput')
    passwd_loc = (BY.ID, 'pwdInput')
    submit_loc = (BY.ID, 'loginBtn')
    '''input username'''

    def type_username(self, username):
        self.find_element(self.username_loc).send_keys(username)

    def type_passwd(self, passwd):
        self.find_element(self.passwd_loc).send_ksys(passwd)

    def submit(self):
        self.find_element(self.submit_loc).click()


def test_user_login(driver, username, passwd):
    '''获取用户名和密码是否可用'''
    '''get the page '''
    login_page = LoginPage(driver)

    '''imput username'''
    login_page.type_username(username)
    '''input passwd'''
    login_page.type_passwd(passwd)
    '''submit'''
    login_page.submit()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    username = 'username'
    passwd = 'passwd'
    test_user_login(driver, username, passwd)
