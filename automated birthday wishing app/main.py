
from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "soham.belokar794@gmail.com"
MY_PASSWORD = ""# not added for security reasons

today = datetime.now()
today_tuple = (today.month, today.day)

#have to add actual path
data = pandas.read_csv("birthdays.csv") #not added the actual path due to security reasons
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
                        # not added for security reasons
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday 1F300–1F5FF!!!	\n\n{contents}" # cake emoji added
        )
