#coding:utf-8
'''
    模拟登陆163邮箱并下载邮件内容
    @author: 
    @blog:
'''
import urllib
import urllib2
import cookielib
import re
import time
import json
 
class Email163:
    header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    user = ''
    cookie = None
    sid = None
    mailBaseUrl='http://twebmail.mail.163.com'
 
    def __init__(self):
        self.cookie = cookielib.CookieJar()
        cookiePro = urllib2.HTTPCookieProcessor(self.cookie)
        urllib2.install_opener(urllib2.build_opener(cookiePro))
        self.passwd = ""
 
    def login(self,user,pwd):
        '''
            登录
        '''
        if pwd == "":
            pwd = self.passwd
            
        postdata = urllib.urlencode({
                'username':user,
                'password':pwd,
                'type':1
            })
        #注意版本不同，登录URL也不同
        req = urllib2.Request(
                url='https://ssl.mail.163.com/entry/coremail/fcg/ntesdoor2?funcid=loginone&language=-1&passtype=1&iframe=1&product=mail163&from=web&df=email163&race=-2_45_-2_hz&module=&uid='+user+'&style=10&net=t&skinid=null',
                data=postdata,
                headers=self.header,
            )
        res = str(urllib2.urlopen(req).read())
        #print res
        patt = re.compile('sid=([^"]+)',re.I)
        patt = patt.search(res)
         
        uname = user.split('@')[0]
        self.user = user
        if patt:
            self.sid = patt.group(1).strip()
            #print self.sid
            print '%s Login Successful.....'%(uname)
        else:
            print '%s Login failed....'%(uname)            
 
 
    def getInBox(self):
        '''
            获取邮箱列表
        '''
        print '\nGet mail lists.....\n'
        sid = self.sid
        url = self.mailBaseUrl+'/jy3/list/list.do?sid='+sid+'&fid=1&fr=folder'
        res = urllib2.urlopen(url).read()
        #获取邮件列表
        mailList = []
        patt = re.compile('<div\s+class="tdLike Ibx_Td_From"[^>]+>.*?href="([^"]+)"[^>]+>(.*?)<\/a>.*?<div\s+class="tdLike Ibx_Td_Subject"[^>]+>.*?href="[^>]+>(.*?)<\/a>',re.I|re.S)
        patt = patt.findall(res)
        if patt==None:
            return mailList
         
        for i in patt:
            line =  {
                    'from':i[1].decode('utf8'),
                     'url':self.mailBaseUrl+i[0],
                     'subject':i[2].decode('utf8')
                     }
            mailList.append(line)
 
        return mailList
         
 
    def getMailMsg(self,url):
        '''
            下载邮件内容
        '''
        content=''
        print '\n Download.....%s\n'%(url)
        res = urllib2.urlopen(url).read()
         
        patt = re.compile('contentURL:"([^"]+)"',re.I)
        patt = patt.search(res)
        if patt==None:
            return content
        url = '%s%s'%(self.mailBaseUrl,patt.group(1))
        time.sleep(1)
        res = urllib2.urlopen(url).read()
        Djson = json.JSONDecoder(encoding='utf8')
        jsonRes = Djson.decode(res)
        if 'resultVar' in jsonRes:
            content = Djson.decode(res)['resultVar']
        time.sleep(3)
        return content


        
         
             
'''
    Demon
'''
#初始化
mail163 = Email163()
#登录
mail163.login('W93126721@163.com',"")
time.sleep(2)
 
#获取收件箱
elist = mail163.getInBox()
 
#获取邮件内容
for i in elist:
    print '主题：%s   来自：%s  内容：\n%s'%(i['subject'].encode('utf8'),i['from'].encode('utf8'),mail163.getMailMsg(i['url']).encode('utf8'))
