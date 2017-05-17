import datetime
# from models import FboMaster
from contact.models import Contact

import re

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

def link(master, lines):
    pass

# Helper methods for the contact handling

class Tokenizer():
    def __init__(self, inp):
        if isinstance(inp, list):
            self.tokens = inp
        else:
            self.tokens = self.tokenize_line(inp)

        self.index = -1

    def ___len__(self):
        return len(self.tokens)

    def get_tokens(self):
        return self.tokens

    def next(self):
        self.index += 1
        token = self.tokens[self.index]
        return token

    def prev(self):
        return self.tokens[self.index-1]

    def peek(self):
        return self.tokens[self.index+1]

    def tokenize_line(self, line):
        tokens = []
        current_token = ''
        previous_char = ''

        for char in line:
            if char == ',':
                tokens.append(current_token)
                current_token = ''
                tokens += ','
            elif char == '-':
                if current_token:
                    tokens.append(current_token)
                current_token = ''
                tokens += '-'
            elif char == ':' or char == ' ':
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
            else:
                if previous_char.isalpha() and char.isdigit():
                    if current_token:
                        tokens.append(current_token)
                        current_token = ''
                current_token = current_token + char
                previous_char = char

        # Make sure that we get the last token
        if current_token:
            tokens.append(current_token)


        return tokens

# # Accepts a Tokenizer object
# def extract_contacts(tokenizer):
    # contacts = []

    # contact = Contact()
    # current_token = tokenizer.next()

    # # Discard the first one if it is 'Name', because we are assuming the first is a name
    # if (current_token == 'Name'):
        # current_token = tokens.next()

    # name = []
    # while (tokenizer.peek() != ','):
        # name.append(tokenizer.next())

    # if len(name) == 1:
        # #Special Case
        # pass

    # else:
        # while (tokenizer.peek() != ','):
            # name.append(tokenizer.next())


    # return contacts

# Utilities

def contains_alpha_and_num(s):
    alpha = False
    num = False
    for char in s:
        if isalpha(char):
            alpha = True
        elif isdigit(char):
            num = True
    return alpha and num


phone_regex = re.compile(r'(?:\+([0-9]+)[ ,.-])?\(?([0-9]{3})\)?[ ,.-]?([0-9]{3})[ .,-]?([0-9]{4})')

# Takes a regex match for a phone number and

def clean_single_phone_number(phone_match):
    return ''.join([element for element in phone_match.groups() if element is not None])

def clean_phone_numbers(line):
    return re.sub(phone_regex, clean_single_phone_number, line)

# Takes a single person and formats the names correctly
def clean_names(person):
    tokens = ','.split(person)[0].st
    name_token = tokens[0]
    if '@' in name_token: # This is just an email
        return person
    elif contains_alpha_and_num(name_token):
        break_index = 0
        for x in xrange(0, len(name_token)-1):
            if isalpha(name_token[x]) and isdigit(name_token[x+1]) or isdigit(name_token[x]) and isalpha(name_token[x+1]):
                break_index = x+1
        if break_index == 0:
            raise ValueError('Break index is 0')
        fixed_name_token = name_token[:break_index] + ',' + name_token[break_index:]
        person = person.replace(name_token, fixed_name_token)

    # No need to go further if only one token

    if len(tokens) == 1:
        return person

    # Last, First M.
    if ' ' not in name_token:
        current_name = tokens[0] + ', ' + tokens[1]
        fixed_name = tokens[1] + ' ' + tokens[0]
        person = person.replace(current_name, fixed_name)

    # Add the 'Name: ' tag
    raise Exception()
    return person

# Takes a single person and puts commas in all the right places
def add_commas(person):
    pass


# Takes a cleaned line and returns a list of all the people in it
def get_people(line):
    return '-'.split(line)

# Takes a single person and returns a list of all the component fields
def get_fields(person):
    # Conditions where we want to return empty, we don't want this contact

    return_empty = False
    if 'FEDBID' in person.upper():
        return_empty = True

    if return_empty:
        return ''

    # Clean the names on the person
    person = clean_names(person)

    # Insert commas at the right places
    person = add_commas(person)
    return ','.split(person)

# Takes a list of component fields and turns them into a contact
def process_fields(fields):
    # Give the names the correct title case
    return ''

def extract_contacts(line):
    # Clean the line to get it looking the way that we want

    # Replace all phone numbers or fax numbers with unformatted digits
    line = clean_phone_numbers(line)

    # Now we process the cleaned line

    # Split the line into a list of different people, splitting at the '-' character
    people = get_people(line)

    # Split the people into a list of different fields, based on the commas
    field_collections = [get_fields(person) for person in people if person]

    # Process each collection of fields into a contact
    for field_collection in field_collections:
        process_fields(field_collection)

def contact(master, line):
    tokenizer = Tokenizer(line)
    contacts = extract_contacts(tokenizer)
    for contact in contacts:
        contact.save()
        master.contacts.add(contact)

    return contacts


