from bs4 import BeautifulSoup
import urllib2

# Announcement Page
url = 'http://www.dituniversity.edu.in/happenings/annoucement'
page = urllib2.urlopen(url)

soup = BeautifulSoup(page,"lxml")

# Extract the headings of individual notices
landing = soup.find(id='blog-landing')
notices = landing.find_all('h3')

for notice in notices:
    print '---------------------------------------------------------------------------------------------------------'
    n = notice.string
    print n[36:]
    print '---------------------------------------------------------------------------------------------------------'
