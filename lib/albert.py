import requests
from lxml import html
from bs4 import BeautifulSoup

def get_albert(url, day):
    print("Albert")
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    today = False
    printed = False

    for td in soup.findAll("td"):
        if not printed:
            td_class = td.attrs['class'][0]
            td_text = td.text.strip()
            if td_class == "tag":
                if day.lower() == td_text.lower():
                    print("#", td.text)
                    today = True
                else:
                    if today:
                        today = False
                        printed = True
            if today:
                if td_class == "numeric":
                    td_title = td.attrs['data-title'].strip()
                    td_text = td.text.strip()
                    if td_title == "Gericht":
                        print(" *", td_text, end="")
                    elif td_title == "Preis":
                        print(" (%s)" % (td_text))
