import pandas
import random
import json
import smtplib
import datetime as dt


today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthday.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with open("email_info.json") as data_file:
        data = json.load(data_file)
        MY_EMAIL = data["my_email"]
        MY_PASSWORD = data["password"]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
