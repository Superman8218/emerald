from bs4 import BeautifulSoup

from data.models import FboMaster

import urllib2
import datetime
import re

FBO_DIR = 'fbo_files'

def main():
    FboMaster.objects.all().delete()
    date = datetime.date(1999, 12, 31)
    fileName = downloadFboFile(date)
    processFile(fileName)
    
def downloadFboFile(date):
    url = getUrlFromDate(date)
    response = urllib2.urlopen(url)

    fileName = '%s/fbo_%s' % (FBO_DIR, date.isoformat())

    text_file = open(fileName, 'w')
    text_file.write(response.read())
    text_file.close()

    return fileName

def getUrlFromDate(date):
    return 'ftp://ftp.fbo.gov//FBOFeed%s%s%s' % (date.year, date.month, date.day)

def processFile(fileName):
    soup = BeautifulSoup(open(fileName), 'html.parser')
    for child in soup.find_all():
        processOpportunity(child) 

def processOpportunity(source):
    master = FboMaster()

    master.solicitation_type = source.name

    if source.date:
        master.date = source.date.stripped_strings.next()

    if source.year:
        master.year = source.year.stripped_strings.next()

    if source.agency:
        master.agency = source.agency.stripped_strings.next()

    if source.office:
        master.office = source.office.stripped_strings.next()

    if source.location:
        master.location = source.location.stripped_strings.next()

    if source.zip:
        master.zip_code = source.zip.stripped_strings.next()

    if source.classcod:
        master.class_code = source.classcod.stripped_strings.next()

    if source.naics:
        master.naics = source.naics.stripped_strings.next()

    if source.offadd:
        master.office_address = source.offadd.stripped_strings.next()

    if source.subject:
        master.subject = source.subject.stripped_strings.next()

    if source.solnbr:
        master.solnbr = source.solnbr.stripped_strings.next()

    if source.respdate:
        respDate = source.respdate.stripped_strings.next()
        respYear = respDate[4:]
        if int(respYear) > 90:
           respYear = int('19' + respYear)
        else:
            respYear = int('20' + respYear)
        respMonth = int(respDate[:2])
        respDay = int(respDate[2:4])
        master.response_date = datetime.date(respYear, respMonth, respDay)

    if source.contact:
        contactString = source.contact.stripped_strings.next()
        nameRegex = re.search(r'^([^,]+)', contactString)
        phoneRegex = re.search(r'Phone ([^,]+)', contactString)
        emailRegex = re.search(r'Email ([^\s]+)', contactString)
        if nameRegex:
            master.contact_name = nameRegex.group(1)
        if phoneRegex:
            master.contact_phone = phoneRegex.group(1)
        if emailRegex:
            master.contact_email = emailRegex.group(1)

    if source.desc:
        master.description = source.desc.stripped_strings.next()

    if source.url:
        master.url = source.url.stripped_strings.next()

    master.save()


if __name__ == '__main__':
    main()
