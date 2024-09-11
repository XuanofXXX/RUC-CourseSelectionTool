import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import aiosmtplib

async def send_email(title, text):
# SMTP服务器设置
    smtp_server = 'smtp.163.com'
    port = 465  # 使用SSL

# 邮箱账户信息
    sender_email = "x2500997861@163.com"
    sender_password = "RBHFXCFOTZXALMBS"
    recipient_email = "2500997861@qq.com"

# 创建邮件内容
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = title

    
    msg.attach(MIMEText(text, 'plain'))
    # 使用 aiosmtplib.SMTP 替代 SMTP_SSL
    async with aiosmtplib.SMTP(hostname=smtp_server, port=port, use_tls=True) as server:
        await server.login(sender_email, sender_password)
        # 发送邮件
        await server.send_message(msg)

