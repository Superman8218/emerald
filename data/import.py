from bs4 import BeautifulSoup
import urllib2
from data.models import FboMaster

def main():
    downloadFboFile('12/31/1999')
    
def downloadFboFile(date):
    url = getUrlFromDate(date)
    response = urllib2.urlopen(url)
    text_file = open('fbo_file_%s', 'w') % (date)
    text_file.write(response.read())
    text_file.close()

def getUrlFromDate(date):
    return 'ftp://ftp.fbo.gov//FBOFeed%s%s%s' % (date.year, date.month, date.day)

if __name__ == '__main__':
    main()
