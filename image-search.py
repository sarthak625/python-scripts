import flickrapi
from bs4 import BeautifulSoup
import urllib
import urllib2
import sys
from KEYS import api_key,api_secret

def downloadImg(link):
	html = urllib.urlopen(link)
	soup = BeautifulSoup(html,"lxml")

	#mydiv= soup.findAll('div',{'class':'photo-notes-scrappy-view'})
	mydiv = soup.findAll('img',{'class':'main-photo'})
	url ="https:"+mydiv[0].attrs['src']

	#Download images
	f = urllib2.urlopen(url)
	file_name = url.split('/')[-1]
	with open(file_name,"wb") as code:
		code.write(f.read())



search_img = raw_input("Enter a search string: ")

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
all_images = flickr.photos.search(text=search_img)

print str(all_images['photos']['total'])+" results found."

if all_images['photos']['total']<5:
	sys.exit()

#for i in range (0,len(all_images['photos']['photo'])):
for i in range (0,20):
	image_id = all_images['photos']['photo'][i]['id']
	image_info = flickr.photos.getInfo(photo_id=image_id)
	print image_info['photo']['urls']['url'][0]['_content']
	downloadImg(image_info['photo']['urls']['url'][0]['_content'])