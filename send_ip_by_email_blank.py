# -*- coding: utf-8 -*-
#!/usr/bin/python3
# @Time    : 2019/6/18
# @Author  : YJJ
# @env     : Python3.7,Win10
# 发送方只使用qq做了测试，其他邮箱暂时未测试
# 需要补充的参数有 mail_host,mail_user,mail_pass,receivers
# 需要补足的参数有 sender，receivers，message_context，message['From']，message['To']
import requests
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#通过访问ip138获取本机外网ip
def get_ip():
    response = requests.get("http://"+str(time.localtime().tm_year)+".ip138.com/ic.asp")
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",response.content.decode(errors='ignore')).group(0)
    return ip
pc_ip = get_ip()

mail_host="smtp.qq.com"#发送邮箱的服务器，与接收邮箱无关。
mail_user="********@qq.com"#qq邮箱登陆名
mail_pass="********"  #在qq邮箱开启stmp服务的时候设置的授权码,具体百度
 
sender='*******@qq.com'#发送方qq邮箱
receivers=['**************']#接收方邮箱

today = time.strftime("%Y-%m-%d", time.localtime())#本日日期
message_context = '***本日IP：' + pc_ip + '\n' + today
message=MIMEText(message_context,'plain','utf-8')#邮件里的正文
message['From']=Header("***",'utf-8') #设置显示在邮件里的发件人
message['To']=Header("*********",'utf-8') #设置显示在邮件里的收件人
 
subject ='***本日IP'
message['Subject']=Header(subject,'utf-8') #设置主题和格式
 
try:
    smtpobj=smtplib.SMTP_SSL(mail_host,465) #本地如果有本地服务器，则用localhost ,默认端口２５,腾讯的（端口465或587）
    smtpobj.set_debuglevel(1) #用以查看调试信息
    smtpobj.login(mail_user,mail_pass)#登陆QQ邮箱服务器
    smtpobj.sendmail(sender,receivers,message.as_string())#发送邮件
    print("邮件发送成功")
    smtpobj.quit()#退出
except smtplib.SMTPException as e :
    print("Error:无法发送邮件")
    print(e)
