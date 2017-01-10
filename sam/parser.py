
from models import SamRecord

import csv
import codecs
import re

import pdb


legend = {
    0 : 'duns',
    2 : 'cage_code',
    # 6 : 'registration_date',
    # 7 : 'expiration_date',
    # 8 : 'last update_date',
    # 9 : 'activation_date',
    10 : 'legal_name',
    11 : 'name',
    14 : 'address_1',
    15 : 'address_2',
    16 : 'city',
    17 : 'state',
    18 : 'zip_code',
    20 : 'country_code',
    # 22 : 'business_start_date',
    # 23 : 'fiscal_year_end_close_date',
    24 : 'url',
    25 : 'entity_structure',
    26 : 'state_of_incorporation',
    27 : 'country_of_incorporation',
    28 : 'business_type_counter',
    29 : 'business_type_string',
    30 : 'primary_naics',
    # 33 : 'psc_code_counter',
    # 34 : 'psc_code_string',
    # 44 : 'govt_bus_poc_first_name',
    # 45 : 'govt_bus_poc_middle initial',
    # 46 : 'govt_bus_poc_last name',
    # 47 : 'govt_bus_poc_title',
    # 48 : 'govt_bus_poc_st_add_1',
    # 49 : 'govt_bus_poc_st_add_2',
    # 50 : 'govt_bus_poc_city',
    # 51 : 'govt_bus_poc_zip',
    # 52 : 'govt_bus_poc_zip',
    # 53 : 'govt_bus_poc_country_code',
    # 54 : 'govt_bus_poc_state',
    55 : 'phone',
    56 : 'phone_ext',
    59 : 'email_address',
    140 : 'naics_exception_counter',
    141 : 'naics_exception_string',
    144 : 'sba_business_types_counter',
    145 : 'sba_business_types_string',
    146 : 'no_public_display_flag',
}

# Declare a userful regex

non_numeric = re.compile(r'[^\d~]+')

def parse_naics(param_list, master):
    """Takes the naics string and converts it into a list of strings. The only parameter in the list should be the naics string"""
    source = param_list[0]
    naics = non_numeric.sub('', source)
    naics = naics.replace('~', ' ')
    master.naics = naics
    return

additional_functions = {
    parse_naics : [32],
}

def parse_file(file_path):
    with open(file_path, 'rU') as csvfile:
        samreader = csv.reader(csvfile, delimiter='|', quotechar='"')
        count = 0
        for row in samreader:
            if (len(row) > 1):
                master = SamRecord()
                for key in legend.keys():
                    setattr(master, legend[key], row[key])
                for key in additional_functions:
                    key([row[index] for index in additional_functions[key]], master)
                master.save()
    return
