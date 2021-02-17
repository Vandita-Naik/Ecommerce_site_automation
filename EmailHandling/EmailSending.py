# import smtplib
# from email.message import EmailMessage
# msg=EmailMessage()
# msg['Subject']="Training Invitaion"
# msg['From']="Email Id 1"
# msg['To']="EmailId 2"
# msg.set_content("This is for practice purpose")
# server=smtplib.SMTP_SSL("smtp.gmail.com",465) # same for all
# server.login("Email Id","password")
# server.send_message(msg)
# # server.sendmail("Email Id 1", "Email Id 2", "Message")
# server.quit()

import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465) # same for all
server.login("Email Id ","Password")
server.sendmail("Email Id 1", "Email Id 2", "Message")
server.quit()
