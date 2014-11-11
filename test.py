# -*- coding: utf-8 -*-
import smtplib, time, os, mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def get_report():
    result_dir='D:\\vic_test_data\\KWS_test\\'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda x:os.path.getmtime(result_dir+x), reverse=True)
    i=0
    reports=[]
    for file in lists:
        reports.append((result_dir+file,file))
        if file[file.rfind('.')+1:] == 'html':
            break
        i+=1
    return reports

def send_report():
    # 发送邮箱
    sender = 'vicwangtest@163.com'
    # 接收邮箱
    receiver = 'vicwangtest@126.com'
    # 发送邮件主题
    subject = get_report()[-1][1]
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户/密码
    username = sender
    password = 'abcd123!'
    
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'TKtester'
    msg['To'] = receiver
    msg['date'] = time.strftime('%Y-%m-%d %H:%M:%S:%z')
    msg.attach(MIMEText('KWS report',_charset='utf-8'))
    
    reports = get_report()[::-1]

    for file in reports:
         
        fileName = file[0]
        ctype, encoding = mimetypes.guess_type(fileName)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        att = MIMEImage((lambda f: (f.read(), f.close()))(open(fileName, 'rb'))[0], _subtype = subtype)
        att.add_header('Content-Disposition', 'attachment', filename = fileName)
        msg.attach(att)
     
     
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('email has sent to %s' %receiver)
    
send_report()