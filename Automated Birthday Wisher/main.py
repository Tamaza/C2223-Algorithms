from datetime import datetime
import pandas
import random
import smtplib

email = "your_email@gmail.com"
password = "your_password"


today = (datetime.now().month, datetime.now().day)
today_tuple = (today.mothm,today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data.row.month, data.row.day): data_row for  (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
          contents = letter_file.read()
          contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
         connection.starttls()
         connection.login(email,password)
         connection.sendmail(from_addr=email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")


