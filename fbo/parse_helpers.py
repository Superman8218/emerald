import datetime
# from models import FboMaster
from contact.models import Contact

import re

def date(master, line):
    month = int(line[:2])
    day = int(line[2:])
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

def link(master, lines):
    pass

phone_cleaning_regex = re.compile(r'(?:\+([0-9]+)[ ,.-])?\(?([0-9]{3})\)?[ ,.-]?([0-9]{3})[ .,-]?([0-9]{4})')
alphanumeric_regex = re.compile(r'^([A-Z][a-z]+(?: [A-Za-z]\.?)? [A-Z][a-z]+) ?([0-9]+)$')
last_first_regex = re.compile(r'^([A-Za-z]+), ?([A-Za-z. ]+)$')
title_regex = re.compile(r'^(?:Title:? ?)?([A-Za-z .]+)?$')
fax_regex = re.compile(r'^(?:Fax:? ?)([0-9]+)$')
phone_regex = re.compile(r'^(?:Phone:? ?)?([0-9]+)$')
email_regex = re.compile(r'^(?:Email:? ?)?(.+\@.+\..+)$')


# Takes a regex match for a phone number and

def clean_single_phone_number(phone_match):
    return ''.join([element for element in phone_match.groups() if element is not None])

def clean_phone_numbers(line):
    return re.sub(phone_cleaning_regex, clean_single_phone_number, line)


# Takes a single person and formats the names correctly
def format_name(person):

    # email@address.com
    if ' ' not in person.strip() and '@' in person:
        return person

    # # First Last1234567890
    # # First Last 1234567890

    match = alphanumeric_regex.match(person)

    if match:
        person = 'Name: {0}, Phone: {1}'.format(match.group(1), match.group(2))
        return person

    # # Last, First M.
    match = last_first_regex.match(person) 
    if match:
        person = 'Name: {0} {1}'.format(match.group(2), match.group(1))
        return person

    # Strip the name tag, and then add in our own

    person = re.sub(r'^Name:? ??', '', person)
    person = 'Name: ' + person

    return person

# Formats the job title field

def format_title(person):
    parts = person.split(',')
    if len(parts) == 1:
        return person
    title_part = parts[1]
    match = title_regex.match(title_part)

    if match:
        parts[1] = 'Title: {0}'.format(match.group(1))
        return ','.join(parts)

    return person

def format_fax_worker(part):
    match = fax_regex.match(part)
    if match:
        return 'Fax: {0}'.format(match.group(1))
    return part

def format_phone_worker(part):
    match = phone_regex.match(part)
    if match:
        return 'Phone: {0}'.format(match.group(1))
    return part

def format_email_worker(part):
    match = email_regex.match(part)
    if match:
        return 'Email: {0}'.format(match.group(1))
    return part

def format_other(person):
    parts = person.split(',')
    parts = [format_fax_worker(part) for part in parts]
    parts = [format_phone_worker(part) for part in parts]
    parts = [format_email_worker(part) for part in parts]
    return ','.join(parts)

def format_data(person):
    person = format_name(person)
    person = format_title(person)
    person = format_other(person)
    return person

# Takes a cleaned line and returns a list of all the people in it
def get_people(line):
    return line.split('-')

# Takes a single person and returns a list of all the component fields
def get_fields(person):
    # Conditions where we want to return empty, we don't want this contact

    return_empty = False
    if 'FEDBID' in person.upper():
        return_empty = True

    if return_empty:
        return ''

    # Remove unnecessary spaces
    person = ','.join([x.strip() for x in person.split(',')])

    # Format the data on the person
    person = format_data(person)

    return person.split(',')

field_names = {
    'Name': 'name',
    'Title': 'title',
    'Phone': 'phone',
    'Email': 'email',
    'Fax': 'fax',
}

# Takes a list of component fields and turns them into a contact
def process_fields(fields):
    # Give the names the correct title case
    contact = Contact()
    for field in fields:
        key, value = [x.strip() for x in field.split(':')]
        if key in ['Name', 'Title']:
            value = value.title()
        setattr(contact, field_names[key], value)

    return contact

# Return a list of contact objects
def extract_contacts(line):
    # Clean the line to get it looking the way that we want


    # Replace all phone numbers or fax numbers with unformatted digits
    line = clean_phone_numbers(line)

    # Replace ';' with '-' to facillitate splitting
    line = line.replace(';', '-')


    # Now we process the cleaned line


    # Split the line into a list of different people, splitting at the '-' character
    people = get_people(line)

    # Split the people into a list of different fields, based on the commas
    field_collections = [get_fields(person) for person in people if person]

    # Process each collection of fields into a contact
    return [process_fields(collection) for collection in field_collections]

def contact(master, line):
    contacts = extract_contacts(line)
    for contact in contacts:
        contact.save()
        master.contacts.add(contact)



