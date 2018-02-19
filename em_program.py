#Program to send email
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("xxxxxx","password")
msg="Hi Tej,shall we go out for movie this friday.I heard blackpanther movie is good."
s.sendmail("xxxxxx","yyyyyy",msg)
print("success")
s.quit()
