import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oxfam_bs_db_project.settings')

from datetime import datetime, timedelta
import smtplib
from volunteers.models import Volunteer

import django
django.setup()


def send_email():

    birthday_volunteers = Volunteer.objects.filter(birthday__in=[datetime.today() + timedelta(days=i) for i in range(1,8)])
    names = ""

    if birthday_volunteers:
        for vol in birthday_volunteers:
            names += '          ' + vol.forename + ' ' + vol.surname + ' -- ' + vol.birthday.strftime("%A") +'\n\n'
    else:
        names = "No birthdays this week."



    content = """SUBJECT:Weekly Birthday List Test
    \n\nHello from your website,\n\nThis weeks birthdays:\n\n\n%s
    \nRegards,\n\n\nYour Website\n\nNote: This email does not include birthdays on the day it was send.\n\n





    """ % (names)

    username = 'oxfamvolunteerswebsite'
    password = 'PearsurgeoN11'
    from_address = 'oxfamvolunteerswebsite@gmail.com'
    to_address = 'oxfamshopf6029@oxfam.org.uk'

    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(username, password)
        mail.sendmail(from_address, to_address, content)
        mail.close()
    except:
        print "**********Exception while trying to send birthday list email on " + datetime.today().isoformat() + "**********"


if __name__ == '__main__':
    print "Starting Oxfam Volunteers email script..."
    if datetime.today().weekday() == 0:
        print "Sending email"
        send_email()
