import datetime
# from models import FboMaster
from contact.models import Contact

import pdb

def date(master, line):
    month = int(line[:2])
    day = int(line[2:])
    # pdb.set_trace()
    if master.date:
        master.date.month = month
        master.date.day = day
    else:
        master.date = datetime.date(1, month, day)

def year(master, line):
    year = int(line)
    if master.date:
        master.date = master.date.replace(year=year)
    else:
        master.date = datetime.date(year, 1, 1)

def respdate(master, line):
    # MMDDYY
    month = int(line[:2])
    day = int(line[2:4])
    year = int(line[4:])
    master.response_date = datetime.date(year, month, day)

def contact(master, line):
    contact = Contact(name='Placeholder Contact')
    contact.save()
    master.contacts.add(contact)

def link(master, lines):
    pass
