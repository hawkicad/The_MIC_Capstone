from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://lpi.oregonstate.edu/mic/glossary" #specify source location
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


glossary = {}
sections = soup.find_all('dl')

for section in sections:
    words = section.find_all('dt')
    for word in words:
        check = word.find_next('dd')
        definition = check.text.strip()
        while True:
            # see if next item in section is another word or more definition
            if check.find_next(['dt', 'dd']) is not None and (check.find_next(['dt', 'dd']).text.strip() == check.find_next('dd').text.strip()):
                check = check.find_next(['dd'])
                for item in check.ul.contents:
                    definition = definition + item.text.strip()
            else: break
        glossary[word.text.strip()] = definition
        
# Testing        
print("Testing Functionality: Enter word to recieve definition. Type 'Exit' to quit.")
loop = 1
while(loop != 0):
    find = input("Enter Word\n")
    if (find == "Exit"): loop = 0
    else: print("The definition of '{}' is:\n".format(find),glossary[find]) 
