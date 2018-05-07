# -*- coding: UTF-8 -*-
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from run_path import test_report_path


def send_mail(to_list, sub, content, mail_user, mail_pass):
    """

    :param to_list:  收件人
    :param sub: 主题
    :param content: 文本内容
    :param mail_user: 发送的人
    :param mail_pass: 发送人的密码
    :return:
    """
    mail_postfix = "qq.com"  # 邮箱的后缀
    mail_host = "smtp.qq.com"  # 使用的邮箱的smtp服务器地址，这里是qq的smtp地址
    me = mail_user+"@"+mail_postfix
    # 赋值
    new_report = [test_report_path() + "\\测试报告.html", "测试报告.html"]
    print(new_report[0])
    msg = MIMEMultipart()
    msg['Subject'] = sub                        # 主题
    msg['From'] = _format_addr('测试报告 <%s>' % me)  # 昵称+ 邮箱地址
    msg['To'] = ";".join(to_list)                # 将收件人列表以‘；’分隔
    # 文本内容
    text_content = MIMEText(content, 'plain', 'utf-8')
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


def _format_addr(s):
    # 添加发起人的昵称
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
