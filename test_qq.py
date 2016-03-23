import smtplib


from email.mime.text import MIMEText
from smtplib import SMTPHeloError, SMTPAuthenticationError, SMTPHeloError, SMTPSenderRefused

#easy send email, only can send plain text
def sendmail(target, subject, content) :
    msg = MIMEText(content)
    from_addr ="9312671@qq.com"
    to_addr = target

    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    try:
        s = smtplib.SMTP('smtp.qq.com')
        s.login('93126721', '') 
        s.sendmail(from_addr, to_addr, msg.as_string())
    except SMTPHeloError:
        print ('Error: Can not connect server.')
        return 1
    except SMTPAuthenticationError:
        print ('Error: Username or password is not correct.')
        return 1
    except SMTPHeloError:
        print ('Error: Can not deliver to target host.')
        return 1
    except SMTPSenderRefused:
        print ('Error: The target server don accept you from_addr')
        return 1
    except:
        print("Send failed")
        return 1
        pass
    finally:
        s.quit()

        print("Send success.")
        return 0

if __name__ =="__main__":
    sendmail("93126721@qq.com","hello","welcome to use the email.")
