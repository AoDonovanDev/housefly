from flask import Flask, render_template, request, flash, redirect, session, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
from forms import CakeForm
from pw import empw

import os
import smtplib
from email.message import EmailMessage


CURR_USER_KEY = "curr_user"

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = '1234'
toolbar = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template('fly.html')

@app.route('/order')
def order():
    form = CakeForm()
    return render_template('order.html', form=form)

@app.route('/test', methods=['post'])
def test():
   
   form = CakeForm()

   def send_email(to, subject, message):

        email_address = 'hfcakerobot@gmail.com'
        email_password = empw

        # create email
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email_address
        msg['To'] = to
        msg.set_content(message)
        print(msg)

    # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)

   if form.validate_on_submit():
    print(form.data)
    message = ''
    for key in form.data:
        if key != 'csrf_token':
            message += f'{key}: {form.data[key]} \n'
    send_email('aodonovancodes@gmail.com', 'hello', message)

    return redirect('/')
   return redirect('/')
