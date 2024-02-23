from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error

url = "https://lpi.oregonstate.edu/mic/glossary" #specify source location

def scraper(soup):
    glossary = {}
    sections = soup.find_all('dl')

    for section in sections:
        words = section.find_all('dt')
        for word in words:
            check = word.find_next('dd')
            definition = check.text.strip()
            while check.find_next(['dt', 'dd']) is not None and (check.find_next(['dt', 'dd']).text.strip() == check.find_next('dd').text.strip()):
                # see if next item in section is another word or more definition
                check = check.find_next(['dd'])
                for item in check.ul.contents:
                    definition = definition + item.text.strip()
            glossary[word.text.strip()] = definition
    return glossary

def connect(url):
    try: 
        page = urlopen(url)
        html = page.read().decode("utf-8")  
        soup = BeautifulSoup(html, "html.parser")
        return scraper(soup)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

def test(glossary):          
    # Testing        
    print("Testing Functionality: (Case-sensitive) Enter word to recieve definition. Type 'Exit' to quit.")
    loop = 1
    while(loop != 0):
        find = input("Enter Word\n")
        if (find == "Exit"): loop = 0
        elif (find in glossary): print("The definition of '{}' is:\n".format(find),glossary[find])    
        else: print("No entry found matching word '{}'.\n".format(find))

output = connect(url)
test(output)