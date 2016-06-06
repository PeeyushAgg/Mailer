import smtplib
from email.mime.text import MIMEText


recipients = ["person@xyz.com","person2@abc.com" ]

mailSubject = "Put email subject here"
mailBody = """
Write email body here
    """

for i in recipients:

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    print "Connected"

        
    msg = MIMEText(mailBody)
    
    smtpserver.ehlo()
    smtpserver.starttls()
    #smtpserver.set_debuglevel(1)

    sender = 'your email @ gmail .com'
    passwrd = "your password"
    smtpserver.login(sender,passwrd)
    print "Logged in"
    msg['Subject'] = mailSubject
    msg['From'] = sender
    msg['To'] = i
    
    try:
        smtpserver.sendmail(sender, [i], msg.as_string()) 
        print "Sent to " + i + "\n\n"
    except(e):
        print "Mail Failed for" + i    
    del msg
    smtpserver.quit()