from bs4 import BeautifulSoup

from data.models import FboMaster

import urllib2
import datetime

FBO_DIR = 'fbo_files'

def main():
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
    for child in soup.children:
       processOpportunity(child) 
    testDir = '%s/test' % FBO_DIR
    text_file = open(testDir, 'w+')
    # text_file.write(rec)
    text_file.close()

def processOpportunity(source):
    master = FboMaster()
    master.solicitation_type = source.name
    master.date = source.date.stripped_strings.next()
    master.year = source.year.stripped_strings.next()
    master.agency = source.agency.stripped_strings.next()
    master.office = source.office.stripped_strings.next()

    import pdb; pdb.set_trace()

if __name__ == '__main__':
    main()
