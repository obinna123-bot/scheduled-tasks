import pandas
import datetime as dt
import random
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")


#getting today's date in a tuple
now = dt.datetime.now()
today_tuple = (now.month, now.day)

#reading the csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg = f"subject: Happy birthday!\n\n{contents}")


