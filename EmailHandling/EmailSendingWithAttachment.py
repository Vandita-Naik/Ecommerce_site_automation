import smtplib
from email.message import EmailMessage
msg=EmailMessage()
msg['Subject']="Training Invitaion"
msg['From']="Email id 1"
msg['To']="Email id 2"
msg.set_content("This is for practice purpose")

with open("EmailText.txt") as myfile:
    data=myfile.read()
    msg.set_content(data)

with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:# same for all
    server.login("Email id","Password")
    server.send_message(msg)

print("Email has been sent")

