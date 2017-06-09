import csv
from os import listdir
import pandas as pd
import re

from django.db.models import Q

from sam.models import SamRecord

import pudb


def generate_email_csv(csv_input):
    """Takes a csv of qualified (already won a contract) companies from usaspending.gov and uses their duns numbers to get their email addresses"""
    # Get a pandas dataframe column with all of the relevant duns numbers

    df = pd.read_csv(csv_input)
    duns_numbers = df.dunsnumber.tolist()

    # Gets the file number for the current file by taking the max of all of the other numbers in the lists directory and adding one to the hightest number

    non_decimal = re.compile(r'[^\d]+')
    file_number_list = [int(non_decimal.sub('', file)) for file in listdir('mail/lists')]
    file_number = max(file_number_list)+1 if file_number_list else 1

    file_name = 'mail/lists/email_{0}.csv'.format(file_number)

    # Actually get the emails

    sam_qs = SamRecord.objects.all().filter(duns__in=duns_numbers)[:100]

    results = set([])

    pudb.set_trace()

    for sam in sam_qs:
        email = sam.email_address
        if email:
            results.add(email)

    with open(file_name, 'w') as f:
        for email in results:
            f.write(email+"\n")

# def has_good_domain(email_address):
    # ''' Returns true if the domain does not match one of the bad domains'''

    # if not '@' in email_address:
        # return False

    # bad_domains = [
        # 'aol.com',
        # 'att.net',
        # 'bellsouth.net',
        # 'charter.net',
        # 'comcast.net',
        # 'cox.net',
        # 'earthlink.net',
        # 'juno.com',
        # 'facebook.com',
        # 'gmail.com',
        # 'gmx.com',
        # 'googlemail.com',
        # 'google.com',
        # 'hotmail.com',
        # 'hotmail.co.uk',
        # 'mac.com',
        # 'me.com',
        # 'mail.com',
        # 'msn.com',
        # 'live.com',
        # 'sbcglobal.net',
        # 'verizon.net',
        # 'yahoo.com',
        # 'yahoo.co.uk',
    # ]

    # domain = email_address.split('@')[1]

    # return domain not in bad_domains

# def get_already_used_set():
    # files = listdir('mail/lists')
    # results = set()
    # for file in files:
        # with open(file) as f:
            # results.update(f.readlines())

    # return results

# def generate_email_csv(csv_input):
    # # Get a pandas dataframe column with all of the relevant duns numbers

    # df = pd.read_csv(csv_input)
    # duns_numbers = df.dunsnumber.tolist()

    # # Gets the file number for the current file by taking the max of all of the other numbers in the lists directory and adding one to the hightest number

    # non_decimal = re.compile(r'[^\d]+')
    # file_number_list = [int(non_decimal.sub('', file)) for file in listdir('mail/lists')]
    # file_number = max(file_number_list)+1 if file_number_list else 1

    # file_name = 'mail/lists/email_{0}.csv'.format(file_number)

    # # Actually get the emails

    # sam_qs = SamRecord.objects.all().filter(duns__in=duns_numbers)[:100]

    # with open(file_name, 'w') as f:
        # for sam in sam_qs:
            # f.write(sam.email_address)



# # def generate_email_csv(list_size=1000):
    # # '''Generates a csv of email addresses that is readable by MailChimp'''

    # # # Generates a list of sam records

    # # # sam_records = [sam for sam in SamRecord.objects.all().filter(~Q(state = 'CA')).order_by('?') if has_good_domain(sam.email_address)][:100]

    # # sam_qs = SamRecord.objects.all().filter(~Q(state = 'CA')).order_by('?')[:1000]
    # # sam_records = [sam for sam in sam_qs if has_good_domain(sam.email_address)]

    # # # Filter out the addresses already used
    # # already_used_set = get_already_used_set
    # # sam_records = [sam for sam in sam_records if sam.email_address not in already_used_set]

    # # if len(sam_records) > 100:
        # # sam_records = sam_records[:100]

    # # # Gets the file number for the current file by taking the max of all of the other numbers in the lists directory and adding one to the hightest number

    # # non_decimal = re.compile(r'[^\d]+')
    # # file_number_list = [int(non_decimal.sub('', file)) for file in listdir('mail/lists')]
    # # file_number = max(file_number_list)+1 if file_number_list else 1

    # # file_name = 'mail/lists/email_{0}.csv'.format(file_number)

    # # with open(file_name, 'w') as csvfile:

        # # writer = csv.writer(csvfile)

        # # # Write the header

        # # # With only 1 column, we don't need a header because MailChimp knows it's an email
        # # # writer.writerow(['Email'])

        # # # Loop through the sam records and write them all to the csv

        # # for sam in sam_records:
            # # writer.writerow([sam.email_address])

