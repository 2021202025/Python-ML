import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')
#print(soup.find_all('p'))

print(soup.get_text())

for url in soup.find_all('a'):
    print(url.get('href'))
