import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import pandas as pd

class Client(QWebPage):
    def__init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loafFinished.connect(self.on_page_load)


        def on_page_load(self):
            self.app.quit()


url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHTML()

##source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
##soup = bs.BeautifulSoup(source, 'xml')


source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

js_test = soup.find('p', class_='jstest')
print(js_test.text)








































##for url in soup.find_all('loc'):
##    print(url.text)

###print(soup.find_all('p'))
##
###print(soup.get_text())
##
###for url in soup.find_all('a'):
##    #print(url.get('href'))
##
##nav = soup.nav
###print(nav)
##
###for url in nav.find_all('a'):
###    print(url.get('href'))
##
##
####body = soup.body
####for paragraph in body.find_all('p'):
####    print(paragraph.text)
##
##
##for div in soup.find_all('div', class_='body'):
##    print(div.text)

#table = soup.table
##table = soup.find('table')
##
##table_rows = table.find_all('tr')
##
##for tr in table_rows:
##    td = tr.find_all('td')
##    row = [i.text for i in td]
##    print(row)


##dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header = 0)
##for df in dfs:
##    print(df.head())
