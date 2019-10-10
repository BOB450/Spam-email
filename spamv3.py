import smtplib
import sys
import time

gmail_user = input("Your Email: ")  
gmail_password = input("Your Email Passwrd: ") 
res = input("Resiver: ")
cont = input("Content: ")
amount = int(input("amount of times sent: "))
i = 0

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)

while(amount > i):


    server.sendmail(gmail_user,res,cont)
    
    i = i + 1
    print(i)
    time.sleep(2)
    
server.close()
    

