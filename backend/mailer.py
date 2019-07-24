#!/usr/bin/env python

import smtplib, os, sys
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from html.parser import HTMLParser

# EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
# FROM_ADDRESS = os.environ.get('FROM_ADDRESS')
# SMTP_ADDRESS = os.environ.get('SMTP_ADDRESS')
# SUBJECT = os.environ.get('SUBJECT')
# TO_ADDRESS = os.environ.get('TO_ADDRESS')
# SAVE_LOCATION = os.environ.get('SAVE_LOCATION')

attachments = [SAVE_LOCATION] # filepath to the screenshot you want to send
msgsubject = 'Here is your weekly overview from Datadog'
htmlmsgtext = """<h2>Header</h2>
                <p>\
                 Body of message. Here is a link to your datadog screenboard, and below you will have an attached screenshot as well.
                 </p>
                
                <p><strong>Here are your attachments:</strong></p><br />"""
######### In normal use nothing changes below this line ###############

# A snippet - class to strip HTML tags for the text version of the email

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

########################################################################
parsed_recipients = TO_ADDRESS.split(', ')
for recipient in parsed_recipients:
    try:
        # Make text version from HTML - First convert tags that produce a line break to carriage returns
        msgtext = htmlmsgtext.replace('</br>',"\r").replace('<br />',"\r").replace('</p>',"\r")
        # Then strip all the other tags out
        msgtext = strip_tags(msgtext)

        # necessary mimey stuff
        msg = MIMEMultipart()
        msg.preamble = 'This is a multi-part message in MIME format.\n'
        msg.epilogue = ''

        body = MIMEMultipart('alternative')
        body.attach(MIMEText(msgtext))
        body.attach(MIMEText(htmlmsgtext, 'html'))
        msg.attach(body)

        if 'attachments' in globals() and len('attachments') > 0: # are there attachments?
            for filename in attachments:
                f = filename
                part = MIMEBase('application', "octet-stream")
                part.set_payload( open(f,"rb").read() )
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
                msg.attach(part)

        msg.add_header('From', FROM_ADDRESS)
        msg.add_header('To', recipient)
        msg.add_header('Subject', SUBJECT)
        msg.add_header('Reply-To', FROM_ADDRESS)

        # The actual email delivery
        server = smtplib.SMTP(SMTP_ADDRESS)
        server.set_debuglevel(False) # set to True for verbose output
        try:
            # gmail expect tls
            server.starttls()
            server.login(FROM_ADDRESS,EMAIL_PASSWORD)
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
            server.quit() # bye
        except:
            # if tls is set for non-tls servers you would have raised an exception, so....
            server.login(FROM_ADDRESS,EMAIL_PASSWORD)
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
            server.quit() # sbye bye        
    except:
        print ('Email NOT sent to %s successfully. %s ERR: %s %s %s ', str(toaddr), 'tete', str(sys.exc_info()[0]), str(sys.exc_info()[1]), str(sys.exc_info()[2]) )