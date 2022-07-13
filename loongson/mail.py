import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

def mail():
	# Mail inf
	sender = '***'  # Sender address
	password = '***'  # Key for sender
	receivers = '***'  # Receivers

	# Msg
	content = MIMEText("<html><h2>发生预警情况</h2>", _subtype="html", _charset="utf-8")
	msg = MIMEMultipart('related')
	msg.attach(content)

	# Include picture attachments
	imageFile = "new_photo.jpg"
	imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
	imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
	msg.attach(imageApart)

	# Msg subject
	msg['Subject'] = '发生预警情况'

	# Inf for sender
	msg['From'] = sender

	# Inf for receivers
	msg['To'] = receivers

	# Main
	try:
	    server = smtplib.SMTP('smtp.qq.com')  # SMTP For QQMail
	    server.login(sender, password)
	    server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
	    print('Send_Success')
	    server.quit()
	except smtplib.SMTPException as e:
	    print('Error', e)  
	    

