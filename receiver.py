import imaplib
import getpass # for password input
import os
import email

# For receiving email
class Receiver :
	def __init__(self, email_user, email_pass, subject_key_word) :
		self.email_user = email_user
		self.email_pass = email_pass
		self.subject_key_word = subject_key_word

		self.mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
		self.mail.login(self.email_user, self.email_pass)
		print('Receiver connected.')
		self.replied_emails = []

	def check_mailbox(self) :
		def extract_body(latest_email):
			typ, data = self.mail.fetch(latest_email,'(RFC822)')
			msg = email.message_from_bytes(data[0][1])
			self.sender = msg['From']
			found = None
			for part in msg.walk():
				if part.get_content_type() == "text/plain":
					body = part.get_payload(decode=True)
					return body.decode('utf-8')
			print('No url.')

		print('Checking mailbox.')
		self.mail.select('Inbox')
		typ, data = self.mail.search(None, '(SUBJECT "%s")'%self.subject_key_word)
		# check search results
		if data[0].split() :
			latest_email = data[0].split()[-1]
			if latest_email not in self.replied_emails :
				self.replied_emails.append(latest_email)
				body = extract_body(latest_email)
				return body
		print(' - No new email found.')
		return False

	def __exit__(self, exc_type, exc_value, traceback):
		self.mail.logout()