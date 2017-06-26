# python-scripts
A collection of scripts written in Python 2.7 to automate daily tasks.

## Image Search
Gets images from flickr using the flickr API and downloads them to your system.
To use this script you need to create a KEYS.py file with your own api_key and api_secret variables.
You can get these by going to https://www.flickr.com/services/api/ and clicking Create an app. 
Also download python and the following dependencies along with this script:
> pip install flickrapi

> pip install BeautifulSoup

To run :
> python image-search.py

### Screenshots

[![solarized dualmode](https://github.com/sarthak625/python-scripts/blob/master/screenshots/is-sc.png)](#features)

[![solarized dualmode](https://github.com/sarthak625/python-scripts/blob/master/screenshots/is-sc2.png)](#features)

## Password Locker

A script that stores user passwords for different accounts. On passing an argument to the script the password gets copied onto the clipboard.

To use download the following dependency

> pip install pyperclip

To run:
> python passwordLocker.py [account]

### Screenshots  

[![solarized dualmode](https://github.com/sarthak625/python-scripts/blob/master/screenshots/passwordLocker.png)](#features)
