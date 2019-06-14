from bs4 import BeautifulSoup
import urllib.request as hyperlink
import os

link = hyperlink.urlopen('http://plugins.svn.wordpress.org/')
wordPressSoup = BeautifulSoup(link,'lxml')
filePath = os.path.dirname(os.path.realpath(__file__))
fileNaming = (filePath + ('scrapedlist.txt'))
for item in wordPressSoup.select("body", {"ul": "li"}):
    print('The current working directory of the file is ' + filePath + ' the scraped list has been saved to this directory as scrapedlist.txt')
    with open(fileNaming, 'w') as output:
        with open('scrapedlist.txt'.format(wordPressSoup.text), mode='wt', encoding='utf-8') as file:
            file.write(str(wordPressSoup.text.encode('utf-8')))
    break
