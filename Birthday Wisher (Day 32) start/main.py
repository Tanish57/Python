import smtplib
#
# my_email = "anyemail@gmail.com"
# password = "qhcypsnshgocoxae"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()   #making connection secure, so if someone tries to intercept our email, it'll get encrypted
#     connection.login(user=my_email, password=password)
#
#     connection.sendmail(
#         from_addr=my_email, to_addrs="receiver@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()
print(weekday)

date_of_birth = dt.datetime(year=2001, month=5, day=7, hour=8, minute=30)
print(date_of_birth)

import random

if weekday == 0:
    with open("quotes.txt") as quote_file:
        list_of_quotes = quote_file.readlines()
        quote = random.choice(list_of_quotes)

    print(quote)

    my_email = "anyemail@gmail.com"
    password = "qhcypsnshgocoxae"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()   #making connection secure, so if someone tries to intercept our email, it'll get encrypted
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email, to_addrs="receiver@gmail.com",
            msg=f"Subject:Quote Of The Day\n\n{quote}"
        )
    print("Monday Motivation done")
