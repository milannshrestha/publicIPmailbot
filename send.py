import smtplib
import requests

my_exIP = requests.get('https://api.ipify.org').text
print (my_exIP)


msg = my_exIP

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('bugeshunt@gmail.com','--password---')
mail.sendmail('bugeshunt@gmail.com','bugeshunt@gmail.com',em)
mail.quit()
''
