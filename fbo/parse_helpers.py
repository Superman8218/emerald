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

# Accepts a Tokenizer object
def extract_contacts(tokenizer):
    contacts = []

    contact = Contact()
    current_token = tokenizer.next()

    # Discard the first one if it is 'Name', because we are assuming the first is a name
    if (current_token == 'Name'):
        current_token = tokens.next()

    name = []
    while (tokenizer.peek() != ','):
        name.append(tokenizer.next())

    if len(name) == 1:
        #Special Case
        pass

    else:
        while (tokenizer.peek() != ','):
            name.append(tokenizer.next())


    return contacts

def contact(master, line):
    tokenizer = Tokenizer(line)
    contacts = extract_contacts(tokenizer)
    for contact in contacts:
        contact.save()
        master.contacts.add(contact)

    return contacts


