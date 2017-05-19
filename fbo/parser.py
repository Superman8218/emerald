import inspect
import logging
import re
import sys

from models import FboMaster

import parse_helpers

from pudb import set_trace

logger = logging.getLogger(__name__)

# Set the module name

thismodule = sys.modules[__name__]

# Determine tag type

## Field tags
field_tag_regex = re.compile(r'<[A-Z]+>')

def contains_field_tag(line):
    return bool(field_tag_regex.match(line))

## Compound tags
compound_tags = ['link', 'file']

def is_compound_tag(tag):
    return tag in compound_tags

## Complex tags
complex_fields = [function[0] for function in inspect.getmembers(parse_helpers, inspect.isfunction)]


def is_complex_tag(tag):
    return tag in complex_fields + compound_tags


# ## Text tags
# text_tag_regex = re.compile(r'<[a-z/]+>')

# def contains_text_tag(line):
    # return bool(text_tag_regex.match(line))

# Field Aliases

field_aliases = {
    'zip' : 'zip_code',
    'classcod' : 'class_code',
    'offadd' : 'office_address',
    'archdate' : 'archive_date',
    'desc' : 'description',
    'popaddress' : 'pop_address',
    'popcountry' : 'pop_country',
    'popzip' : 'pop_zip',
}

# Function for setting a field

def set_field(master, line, tag):
    # Removes just the field tags so that we can keep all the html markup we are given

    cleaned_line = clean_line(line)

    target_field_name = field_aliases[tag] if tag in field_aliases else tag

    # See if there is already anything in the field.  If so, append to that data.

    existing_data = getattr(master, target_field_name)

    if not existing_data:
        existing_data = ''

    new_data = existing_data + cleaned_line

    setattr(master, target_field_name, new_data)

# Tag manipulation

def extract_tag(line):
    tag_end_index = line.find('>')
    if tag_end_index != -1:
        return line[1:tag_end_index].lower()

def get_tag_complement(tag):
    return '</{0}>'.format(tag.upper())

def clean_line(line):
    return re.sub(field_tag_regex, '', line)


# The main method

def parse_file(file_path):
    index = 0
    current_tag = ''
    complement = ''
    previous_line = ''
    last_field_tag = ''
    master = None

    with open(file_path, 'r') as f:
        lines = [line.strip('\n') for line in list(f)]
        while index < len(lines):
            line = lines[index]
            tag = extract_tag(line)
            if not line:
                index += 1
                continue

            # 4 cases:

            # 1) Current tag not set

            if not current_tag:
                current_tag = tag
                complement = get_tag_complement(current_tag)
                master = FboMaster()
                master.save() # Necessary to add contacts later

            # 2) Complement tag

            elif line == complement:
                current_tag = ''
                try:
                    master.save()
                except Exception as ex:
                    logger.error('Unable to save FboMaster record.\nFile: {0}\nSolnbr: {1}'.format(file_path, master.solnbr))

            # 3) Field tag

            elif contains_field_tag(line):
                if is_complex_tag(tag):
                    handler_function = getattr(parse_helpers, tag)

                    # Tags that eat the next 2 lines:
                    if is_compound_tag(tag):
                        input_lines = [lines[index+1], lines[index+2]]
                        cleaned_lines = [clean_line(line) for line in input_lines]
                        index += 2
                    # Normal tags, one line
                    else:
                        cleaned_lines = clean_line(line)

                    handler_function(master, cleaned_lines)

                else:
                    set_field(master, line, tag)
                last_field_tag = tag


            # 4) Text tag

            else:
                set_field(master, line, last_field_tag)
                pass

            # Increment the index

            index += 1

