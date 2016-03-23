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


class Crawler(object):


    def __init__(self):
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(self.opener)
        self.urllogin = "http://mail.163.com/"
        #self.login = {"return":"index.php","username":"W93126721","password":""}
        self.login = {"return":"index.php","idPlaceholder":"W93126721@163.com","pwdPlaceholder":"198039"}
        pass 
        

    def main(self):

        data = urllib.urlencode(self.login)
        request = urllib2.Request(self.urllogin,data)
        result = self.opener.open(request).read()
        print(result)
        pass


if __name__ == '__main__':

    myCrawler = Crawler()
    myCrawler.main()
