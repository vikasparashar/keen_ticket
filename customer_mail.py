#!/usr/bin/python
import smtplib
import email
import os
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE
from email.MIMEBase import MIMEBase
from email.parser import Parser
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email import Encoders
import mimetypes


user = 'amit.saxena@fosteringlinux.com';
password = 'globalkumar';

server = smtplib.SMTP()
server.connect('smtp.gmail.com',587) # for eg. host = 'smtp.gmail.com', port = 587
server.ehlo()
server.starttls()
server.login(user, password)


#attachment = "vikas.txt"
#Send the mail
#msg = "\nDear Team,\nKindly find the attached csv file on your work progress. Kindly check it and revert if there is any update." # The /n separates the message from the headers
#msg = "\n Hello"
#server.sendmail("vikas.parashar@fosteringlinux.com", 'savikasparashar@gmail.com' ,msg)

#SUBJECT = 'test'
#TO = ('savikasparashar@gmail.com' , 'vikas.parashar@fosteringlinux.com' )
#CC = ['vikas.parashar@fosteringlinux.com','varad.gupta@fosteringlinux.com']


msg = MIMEMultipart()
msg['Subject'] = SUBJECT 
#msg['From'] = self.EMAIL_FROM
msg['To'] = ", ".join(TO)
#msg["Cc"] = "savikasparashar@gmail.com,atanu.datta@gmail.com"
#msg['Cc'] = ", ".join(CC)
#msg["To"] = 'vikas.parashar@fosteringlinux.com,atanu.datta@fosteringlinux.com'

part = MIMEBase('application', "octet-stream")
part.set_payload(open(attachment, "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename= '+ attachment)

msg.attach(part)

#==============
# Create the body of the message (a plain-text and an HTML version).
text = "\nDear Team,\n\nKindly find the attached csv file on your work progress. Kindly check it and revert if there is any update. \n\n\n As you all know that s/w is under very intial state, so you may be need to do some extra effort to keep update me regarding your activity. \n\n Kindly try to understand, what, we all are doing only for our benefits. With the help of this, people get more incentives and more increment. \n\n\n Hope, you will cooperate to make this success. \n\n\n Sending you some sample sheet as well \n\n" # The /n separates the message from the headers"
html = """\
<html>
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>html title</title>
</head>
  <body>
<table style="border:1px solid black;border-collapse:collapse;" border=1>
<tr style="border:1px solid black" bgcolor="red" >
<th>id</th>
<th>Points_Man</th>
<th>Engineer_Name</th>
<th>Customer_Name</th>
<th>Project_Name</th>
<th>Case_Type</th>
<th>Call_Pending</th>
<th>Customer_Side</th>
<th>Keen_Side</th>
<th>Problem_Start_Date</th>
<th>Estimated_end_Date</th>
<th>Task_Description</th>
<th>Status</th>
<th>Call_Close_Date</th>
<th>Remarks</th>
<th>Points</th>
</tr>
<tr>
<td>123</td>
<td>xxx@fosteringlinux.com</td>
<td>xxx@fosteringlinux.com</td>
<td>xxxxx</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
<td></td>
<td></td>
<td>0</td>
</tr>
</table>
	

  </body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
msg.attach(part1)
msg.attach(part2)

#server = smtplib.SMTP(self.EMAIL_SERVER)
#server.sendmail(self.EMAIL_FROM, self.EMAIL_TO, msg.as_string())
server.set_debuglevel(True) # show communication with the server
try:
	#server.sendmail("amit.saxena@fosteringlinux.com", msg['To'] ,msg.as_string())
	server.sendmail("amit.saxena@fosteringlinux.com", msg["To"].split(",") ,msg.as_string())
#	server.sendmail("amit.saxena@fosteringlinux.com", msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
finally:
    server.quit()
#print SUBJECT
