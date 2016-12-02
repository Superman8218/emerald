from functools import partial
import datetime
import re

from bs4 import BeautifulSoup

from models import FboMaster
import pdb
import sys
import pprint

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

srcsgt_fields = [
    'agency',
    'office'
]

# Define aliases for importing fields, includeing functions used to handle complicated inputs

def set_contact_data(master, text):
    # nameRegex = re.search(r'^([^,]+)', text)
    # phoneRegex = re.search(r'Phone ([^,]+)', text)
    # emailRegex = re.search(r'Email ([^\s]+)', text)
    # if nameRegex:
        # master.contact_name = nameRegex.group(1).title()
    # if phoneRegex:
        # master.contact_phone = phoneRegex.group(1)
    # if emailRegex:
    #     master.contact_email = emailRegex.group(1)
    pass

def set_respdate_data(master, text):
    respYear = text[4:]
    if int(respYear) > 90:
       respYear = int('19' + respYear)
    else:
        respYear = int('20' + respYear)
    respMonth = int(text[:2])
    respDay = int(text[2:4])
    master.response_date = datetime.date(respYear, respMonth, respDay)

field_aliases = {
    'zip' : 'zip_code',
    'classcod' : 'class_code',
    'offadd' : 'office_address',
    'respdate' : set_respdate_data,
    'archdate' : 'archive_date',
    'contact' : set_contact_data,
    'desc' : 'description',
}

field_aliases_keys = field_aliases.keys()

# Get a list of all the field names in the model

field_names = [field.name for field in FboMaster._meta.get_fields()]

# Combine them to get the list of all tags that we are interested in

combined_field_list = field_names + field_aliases_keys

# Filter functions

def tag_filter(tag, name):
    return tag.name == name

def nonempty_tag(tag):
    return tag.name is not None

# The actual parsing method

def parse_file(file_path):
    """So right now this is built to only extract one type of record, but we can definitely make it extract more"""
    soup = BeautifulSoup(open(file_path))
    records = filter(nonempty_tag, soup.children)
    for record in records:
        master = FboMaster()
        master.solicitation_type = record.name
        fields = filter(lambda x: x.name in combined_field_list, record(True))
        for item in fields:
            text = item.find(text=True, recursive=False).encode('utf-8').strip()
            name = item.name
            if not text:
                continue
            if name in field_names:
                setattr(master, name, text)
            elif name in field_aliases_keys:
                destination = field_aliases[name]
                if type(destination) == str:
                    try:
                        setattr(master, field_aliases[name], text)
                    except:
                        print('Failed for {0}'.format(name))
                        return
                else:
                    destination(master, text)
            else:
                print("Field name {0} not in field lists".format(name))
        try:
            master.save()
        except:
            pprint.pprint(sys.exc_info()[0])
            pprint.pprint(master.__dict__)
            return
