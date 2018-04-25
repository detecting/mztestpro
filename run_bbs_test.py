from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time, unittest, os


# 定义发送邮件
def send_mail(file_path):
    with open(file_path, 'rb') as fp:
        mail_body = fp.read()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试', 'uft-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('username', 'passwd')
    smtp.sendmail(from_addr='', to_addrs='', msg=msg.as_string())
    smtp.quit()

    print('email has send out')


def new_report(testReport):
    lists = os.listdir(testReport)
    lists.sort(key=lambda fn: os.path.getmtime(testReport + '\\' + 'fn'))
    file_new = os.path.join(testReport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    now = time.strftime("%y-%m-%d %H_%M_%S")
    fileName = './bbs/report' + now + 'result.html'
    with open(fileName, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='自动化测试博阿高', description='')
        discover = unittest.defaultTestLoader.discover(
            start_dir='C:\\Users\hzha321\PycharmProjects\mztestpro\\bbs\\test_case', pattern='*_sta.py')
        runner.run(discover)

    #     查找新报告的路径
    file_path = new_report(testReport='./bbs/report/')
    send_mail(file_path)
