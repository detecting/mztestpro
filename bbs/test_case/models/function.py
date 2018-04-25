# 截图函数
from selenium import webdriver
import os


def insert_img(driver, file_name):
    # 'H:/Users/hzha321/PycharmProjects/mztestpro/bbs/test_case'
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')

    # 去掉test_case
    # H:/Users/hzha321/PycharmProjects/mztestpro/bbs/
    base = base_dir.split('test_case')[0]
    file_path = base + '/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver, 'baidu.jpg')
    driver.quit()
