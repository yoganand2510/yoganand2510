#Program to send email
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("yoganandyamcha@gmail.com","yoganand25")
msg="Hi Tej,shall we go out for movie this friday.I heard blackpanther movie is good."
s.sendmail("yoganandyamcha@gmail.com","yoganandyamcha@gmail.com",msg)
print("success")
s.quit()
