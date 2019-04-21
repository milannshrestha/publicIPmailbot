import smtplib
import requests

my_exIP = requests.get('https://api.ipify.org').text
print (my_exIP)
sender_email = 'sender_email@gmail.com'
reciever_email = 'reciever_email@gmail.com'
msg = ('Your External IP is: {}'.format(my_exIP))
print (msg)

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(sender_email,'sender_email_password_here')
mail.sendmail(sender_email,reciever_email, my_exIP)
mail.quit()
