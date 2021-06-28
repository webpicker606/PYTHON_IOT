import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("hamsananth007@gmail.com","muiegdmlucsqmivc")
print('login successfull')
server.sendmail("hamsananth007@gmail.com","hamsananth2093@gmail.com","hi i am a bot of hamsananth just testing whether i am working or not")
print('mail sent')
server.quit()