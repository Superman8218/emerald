from collections import namedtuple
import datetime
from functools import partial
import re

from bs4 import BeautifulSoup

from contact.models import Contact
from models import FboMaster
import sys
import pprint

import pdb

"""So the idea here is going to be to just use the list of all the fields in the fbo_master model.  If a field isn't in the fbo_master model then we can just log it and deal with it.  But all of the fields should be present"""

record_types = [
    'presol',
    'srcsgt',
    'snote',
    'combine',
    'amdcss',
    'mod',
    'award',
    'archive'
]

# Helper methods for setting fields that are more complex

MasterDateTuple = namedtuple('MasterDateTuple', ['master_id', 'date_field', 'year_field'])
master_date_tuple = MasterDateTuple(None, None, None) # Used to store a partial function

def process_date_tuple(master):
    master.date = datetime.date(int(master_date_tuple.year_field), int(master_date_tuple.date_field[:2]), int(master_date_tuple.date_field[2:]))

def handle_date(master, date):
    """Creates the master/date tuple for this record"""
    global master_date_tuple
    master_date_tuple = master_date_tuple._replace(date_field=date)
    if master_date_tuple.master_id == master.id and master_date_tuple.year_field is not None:
        process_date_tuple(master)
    else:
        master_date_tuple = master_date_tuple._replace(master_id=master.id)

def handle_year(master, year):
    """If we already have a date for this record, then create the combined date"""
    #Get the right prefix for the year

    if int(year) > 90:
       year = '19' + year
    else:
        year = '20' + year

    # Do our normal thing

    global master_date_tuple
    master_date_tuple = master_date_tuple._replace(year_field=year)
    if master.id == master_date_tuple.master_id and master_date_tuple.date_field is not None:
        process_date_tuple(master)
    else:
        master_date_tuple = master_date_tuple._replace(master_id=master.id)

def handle_respdate(master, text):
    respYear = text[4:]
    if int(respYear) > 90:
       respYear = int('19' + respYear)
    else:
        respYear = int('20' + respYear)
    respMonth = int(text[:2])
    respDay = int(text[2:4])
    master.response_date = datetime.date(respYear, respMonth, respDay)

def handle_contact(master, text):
    # nameRegex = re.search(r'^([^,]+)', text)
    # phoneRegex = re.search(r'Phone ([^,]+)', text)
    # emailRegex = re.search(r'Email ([^\s]+)', text)
    # if nameRegex:
        # master.contact_name = nameRegex.group(1).title()
    # if phoneRegex:
        # master.contact_phone = phoneRegex.group(1)
    # if emailRegex:
    #     master.contact_email = emailRegex.group(1)

    contact_regex = re.compile(r'(?P<name>[a-zA-Z]+ [a-zA-Z]+)(?:, (?P<title>[a-zA-Z]+ [a-zA-Z]+)?)?(?:, Phone (?P<phone>[0-9\-]+)?)?, (?:Fax (?P<fax>[0-9\-]+)?)?(?:, Email (?P<email>[a-zA-Z0-9@\.]+)?)?')
    contact = contact_regex.search(text)
    new_contact = Contact()
    if contact:
        new_contact.name = contact.group('name')
        new_contact.job_title = contact.group('title')
        new_contact.email = contact.group('email')
        new_contact.phone = contact.group('phone')
        try:
            new_contact.save()
        except:
            pdb.set_trace()
        master.contacts.add(new_contact)


# Define aliases for importing fields, includeing functions used to handle complicated inputs

field_aliases = {
    'date': handle_date,
    'year': handle_year,
    'zip' : 'zip_code',
    'classcod' : 'class_code',
    'offadd' : 'office_address',
    'respdate' : handle_respdate,
    'archdate' : 'archive_date',
    'contact' : handle_contact,
    'desc' : 'description',
}

field_aliases_keys = field_aliases.keys()

# Get a list of all the field names in the model

field_names = [field.name for field in FboMaster._meta.get_fields()]

# Combine them to get the list of all tags that we are interested in

combined_field_list = field_names + field_aliases_keys

# Methods to get the list of all the relevant tags

def flatten(l):
    """Takes a list of lists and flattens it into a single list"""
    return [item for sublist in l for item in sublist]

def get_records(soup):
    """Takes the soup and gets all of the nodes whose type is in the list of record types"""
    return flatten([soup.find_all(record_type) for record_type in record_types])

# The actual parsing method

def parse_file(file_path):
    """So right now this is built to only extract one type of record, but we can definitely make it extract more"""
    soup = BeautifulSoup(open(file_path))
    records = get_records(soup)
    for record in records:
        master = FboMaster()
        master.save()
        master.solicitation_type = record.name
        fields = filter(lambda x: x.name in combined_field_list, record(True))
        for item in fields:
            text = item.find(text=True, recursive=False).encode('utf-8').strip()
            name = item.name
            if not text:
                continue
            if name in field_aliases_keys:
                destination = field_aliases[name]
                if type(destination) == str:
                    try:
                        setattr(master, field_aliases[name], text)
                    except:
                        print('Failed for {0}'.format(name))
                        return
                else:
                    destination(master, text)
            elif name in field_names:
                setattr(master, name, text)
            else:
                print("Field name {0} not in field lists".format(name))
        try:
            master.save()
        except:
            pprint.pprint(sys.exc_info()[0])
            pprint.pprint(master.__dict__)
            return
