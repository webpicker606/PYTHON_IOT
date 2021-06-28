import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
from_address="hamsananth007@gmail.com"
app_password="muiegdmlucsqmivc"
server.login(from_address,app_password)
print('login successfull')
message="hi i am a bot of hamsananth just testing!"
to_address="hamsananth2093@gmail.com"
server.sendmail(from_address,to_address,message)
print('mail sent')
server.quit()
