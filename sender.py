import smtplib

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

import re

# For sending email
class Sender :
	def __init__(self, user, password, send_to, subject_prefix):
		self.user = user
		self.password = password
		self.send_to = send_to
		self.subject_prefix = subject_prefix

		self.smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
		self.smtpObj.ehlo() # should return 250
		self.smtpObj.starttls() # should return 220
		self.smtpObj.login(self.user, self.password)
		print('Sender connected.')

	def send(self, url):
		msg = MIMEMultipart()
		msg['From'] = self.user
		msg['To'] = self.send_to
		msg['Date'] = formatdate(localtime=True)
		msg['Subject'] = self.subject_prefix + ' _ ' + formatdate(localtime=True)
		# add text
		msg.attach(MIMEText(url))
		# send email
		self.smtpObj.sendmail(self.user, self.send_to, msg.as_string())
		print(' - Sent attachments successfully.')
						
	def __del__(self) :
		self.smtpObj.quit()
