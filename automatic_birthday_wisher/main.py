import os
import smtplib
import pandas as pd
import datetime as dt
import random

my_email = 'udemypythoncourse01@gmail.com'
my_password = 'uplx bsnu fpms rkbd'

# ------------------------------------------ import csv and details

df = pd.read_csv('birthdays.csv')

# ------------------------------------------ check if current date matches with any birthdays
# ------------------------------------------ runs all code below if date matches with a birthday in birthdays csv

now = dt.datetime.now()
birthmonths = df['month'].to_list()
birthdays = df['day'].to_list()

if now.month in birthmonths:
    if now.day in birthdays:
        birthday_person = df[(df['month'] == now.month) &
                             (df['day'] == now.day)]['name'].to_string(index=False)
        birthday_email = df[(df['month'] == now.month) &
                            (df['day'] == now.day)]['email'].to_string(index=False)

# ------------------------- check directory and create a list of well wishes from txt files

        list_of_well_wishes = os.listdir('well_wishes')

# ------------------------- choose random letter and replace placeholders with name

        with open('well_wishes/' + random.choice(list_of_well_wishes)) as data:
            temp = data.read()
            well_wishes = temp.replace('[NAME]', birthday_person)

# ------------------------- send email to birthday person

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_email,
                                msg=f'Subject: Happy Birthday {birthday_person}\n\n'
                                    f'{well_wishes}')


print(birthday_person)
print(birthday_email)
print('\n')
print(well_wishes)




