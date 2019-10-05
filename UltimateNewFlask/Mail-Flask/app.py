from flask import Flask 
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'abdumaliksharipov@gmail.com'
app.config['MAIL_PASSWORD'] = 'Masdf@45632456fasdl;kfa2'
app.config['MAIL_DEFAULT_SENDER'] = ('AbdulMalik from Boeing','abdumaliksharipov@gmail.com')
app.config['MAIL_MAX_EMAILS'] = None
#app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

#mail = Mail()
#mail.init_app(app)

@app.route('/')
def index():
    msg = Message('Peace be upon you,', recipients=['abdumalikshareef@gmail.com'])
    msg.add_recipient('abdsh8@yahoo.com')
    # msg.body='This one is just example mail to remind you about upcoming session. If you know just ignore'
    msg.html='<b>SOme more blah blah text that is supposedly formated to be bold</b>'
    

    with app.open_resource('cat.jpg')as cat:
    	msg.attach('cat.jpg','image/jpeg',cat.read())


    mail.send(msg)

    msg = Message(
            subject = '',
            recipients = [],
            body = '',
            html = '',
            sender = '',
            cc = [],
            bcc = [],
            attachments = [],
            reply_to = [],
            date = 'date',
            charset = '',
            extra_headers = {'': ''},
            mail_options = [],
            rcpt_options = []
        )

    return 'Message has been sent!'


@app.route('/bulk')
def bulk():
	users=[{"email":'blah@gmail.com', 'name':'ABdul'}]

	with mail.connect() as conn:
		for user in users:
			msg=Message("Bulk",recipients=[user['email']])
			msg.body='Message body goes here'
			conn.send(msg)




if __name__ == '__main__':
    app.run()