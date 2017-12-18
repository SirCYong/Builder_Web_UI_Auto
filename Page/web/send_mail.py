# -*- coding: UTF-8 -*-
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from run_path import test_report_path

mailto_list = ['caoyong@zlddata.cn']           # 收件人(列表)
mail_host = "smtp.qq.com"            # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user = "649803977"                           # 用户名
mail_pass = "xrycvnzvusztbcad"                             # 密码
mail_postfix = "qq.com"  # 邮箱的后缀


def send_mail(to_list, sub, content):
    me = mail_user+"@"+mail_postfix
    new_report = [test_report_path() + "\\result.html", "result.html"]
    print(new_report[0])
    msg = MIMEMultipart()
    msg['Subject'] = sub                        # 主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)                # 将收件人列表以‘；’分隔
    # 文本内容
    text_content = MIMEText(content)
    msg.attach(text_content)
    # 附件
    attachment = MIMEApplication(open(new_report[0], 'rb').read())
    attachment.add_header("Content-Disposition", "attachment", filename=new_report[1])
    msg.attach(attachment)
    try:
        server = smtplib.SMTP(mail_host, timeout=30)
        server.set_debuglevel(1)
        server.starttls()
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(str(e))
        return False
for i in range(1):                             # 发送1封，上面的列表是几个人，这个就填几
    if send_mail(mailto_list, "测试报告", 'test'):  # 邮件主题和邮件内容
        print("done!")
    else:
        print("failed!")

