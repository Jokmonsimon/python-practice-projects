import os
import random
import smtplib

# Python function that will automatically send emails to a newly registered user.
def send_automatic_email():
    fullname = input("Enter Your Full Name >>: ")
    email = input("Enter Your Email Address >>: ")
    message = (f"Dear {fullname}, Welcome to Yearn AI")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Replace with Your Email Address", "Replace with Your Google App Password")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent Successfully!")

send_automatic_email()