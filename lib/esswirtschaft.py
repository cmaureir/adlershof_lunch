import requests
from lxml import html
from bs4 import BeautifulSoup

def get_esswirtschaft(url, day):
    print("Esswirtschaft")
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    today = False
    printed = False

    for section in soup.findAll('h2'):
        next_tag = section
        option = section.text
        if "wochen" in option or "salat" in option or day.lower() == option:
            print("#", option)
            while True:
                next_tag = next_tag.nextSibling
                tag_name = next_tag.name
                if tag_name == "p":
                    tmp = next_tag.stripped_strings
                    line = ""
                    for i, a in enumerate(tmp):
                        if (i == 2):
                            line += "\n"
                        line += "".join(a)
                        line += " "
                    line = line.replace("*", "")
                    print(" *", line)
                elif tag_name == "br" or tag_name == "h2":
                    break
