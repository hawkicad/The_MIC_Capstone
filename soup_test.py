from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://lpi.oregonstate.edu/mic/glossary" #specify source location
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# page is formatted for all dt to bewords, dds contain definitions
word = soup.find_all('dt')
definition = soup.find_all('dd')

# for testing: go through and print every matching word and definition
for i in range(0, len(word)):
    print("{}: {}".format(word[i].text.strip(), definition[i].text.strip()))