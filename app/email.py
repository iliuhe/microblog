from flask_mail import Message
from app import mail, app
from flask import render_template
from threading import Thread


def send_email(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender = sender, recipients = recipients)
	msg.body = text_body
	msg.html = html_body
	mail.send(msg)

def send_password_reset_email(user):
	token = user.get_reset_password_token()
	send_email('[Microblog] Reset Your Password', 
		sender = app.config['ADMINS'][0], 
		recipients = [user.email],
		text_body = render_template('email/reset_password.txt', user = user, token = token),
		html_body = render_template('email/reset_password.html', user = user, token = token)
		)

'''# sending async emails 
def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender = sender, recipients = recipients)
	msg.body = text_body
	msg.html = html_body
	Thread(target = send_async_email, args = (app, msg)).start()'''


'''
# setting environment parameters
export MAIL_PORT=8025
export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=465
export MAIL_USE_TLS=1
export MAIL_USERNAME=heliu1433@gmail.com
export MAIL_PASSWORD=Lovef12266282!

# testing script
# using flask shell

from flask_mail import Message
from app import mail
msg = Message('test subject', sender = app.config['ADMINS'][0], recipients = ['he.liu10@hotmail.com'])
msg.body = 'test body'
msg.html = '<h1>HTML body</h1>'
mail.send(msg)

'''