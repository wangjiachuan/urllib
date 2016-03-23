#-*- coding: utf8 -*-
import sys
import time
import traceback
import os,time
import random
import re
import urllib
import urllib2
import cookielib
import csv

import smtplib
from email.mime.text import MIMEText 


class Crawler(object):


    def __init__(self):
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        #urllib2.install_opener(self.opener)
        self.urllogin = "http://mail.163.com/"
        #self.login = {"return":"index.php","username":"W93126721","password":""}
        self.login = {"return":"index.php","idPlaceholder":"W93126721@163.com","pwdPlaceholder":""}
        pass 
        

    def main(self):

        data = urllib.urlencode(self.login)
        request = urllib2.Request(self.urllogin,data)
        result = self.opener.open(request).read()
        print(result)
        pass



class Mailer(object):
    def __init__(self):
        # 定义发送列表
        self.mailto_list=["93126721@qq.com","93126721@qq.com"]
        # 设置服务器名称、用户名、密码以及邮件后缀
        self.mail_host = "smtp.163.com"
        self.mail_user = "W93126721"
        self.mail_pass = "198039"
        self.mail_postfix="163.com"


    
    def main(self):
        if (True == self.send_mail(self.mailto_list,"subject","context")):
            print ("测试成功")
        else:
            print ("测试失败") 
        pass

    def send_mail(self,to_list, sub, context):
        '''''
        to_list: 发送给谁
        sub: 主题
        context: 内容
        send_mail("xxx@126.com","sub","context")
        '''
        me = self.mail_user + "<"+self.mail_user+"@"+self.mail_postfix+">"
        msg = MIMEText(context)
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            send_smtp = smtplib.SMTP()
            send_smtp.connect(self.mail_host)
            send_smtp.login(self.mail_user, self.mail_pass)
            send_smtp.sendmail(me, to_list, msg.as_string())
            send_smtp.close()
            return True
        except Exception, e:
            print(str(e))
            return False




    
if __name__ == '__main__':

    #myCrawler = Crawler()
    #myCrawler.main()

    myMailer = Mailer()
    myMailer.main()
