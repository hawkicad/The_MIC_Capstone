from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://lpi.oregonstate.edu/mic/glossary" #specify source location
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# page is formatted for all dt to bewords, dds contain definitions
word = soup.find_all('dt')
definition = soup.find_all('dd')

glossary = {}

# for testing: go through and print every matching word and definition
for i in range(0, len(word)):
    # print("{}: {}".format(word[i].text.strip(), definition[i].text.strip()))
    glossary[word[i].text.strip()] = definition[i].text.strip()

print("Testing Functionality: Enter word to recieve definition. Type 'Exit' to quit.")
loop = 1
while(loop != 0):
    find = input("Enter Word\n")
    if (find == "Exit"): loop = 0
    else: print("The definition of '{}' is:\n".format(find),glossary[find])