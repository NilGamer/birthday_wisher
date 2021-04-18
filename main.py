import smtplib
import datetime as dt
import pandas
import random

my_email = "email"
password = "password"

# read the csv file
data = pandas.read_csv('birthdays.csv')

now = dt.datetime.now()
# create a tuple
today = (now.month, now.day)

# dictionary with key as monday,day tuple and value as row
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    # get the current data
    birthday_person = birthdays_dict[today]
    letter_number = random.randint(1, 3)
    file_path = f"letter_templates/letter_{letter_number}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
