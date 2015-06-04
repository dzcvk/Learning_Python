import smtplib
import email.utils
from email.mime.text import MIMEText

senderAddress='89195333@qq.com'
senderName='LinPei'

receiverAddress='linpei1987@hotmail.com'
receiverName='Vincent'

username='89195333'
password='qq88913491lin'

msg = MIMEText('this is the body of the message')
msg['To']=email.utils.formataddr((receiverName,receiverAddress))
msg['From']=email.utils.formataddr((senderName,senderAddress))
msg['Subject']='Simple test message'
server = smtplib.SMTP('smtp.qq.com')
try:
    server.set_debuglevel(True)
    server.ehlo()
    if server.has_extn('STARTTLS'):
        server.starttls()
        server.ehlo()
        server.login(username,password)
        server.sendmail(senderAddress,[receiverAddress],msg.as_string())
finally:
    server.quit()
