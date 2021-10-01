import requests
from bs4 import BeautifulSoup
import random
import wikipedia

# $********IMPORTING MODULES*********$
import tkinter
from tkinter import *

# $********CREATING WINDOW***********$
wind = tkinter.Tk()
wind.title("WIKI SCRAPER")
wind.geometry("800x600")
wind.resizable(width=False, height=False)
wind.config(bg="grey")
global linkToScrape
linkToScrape = "https://en.wikipedia.org/wiki/Programming_language"


def randomWikipediaPages(urlToScrape):
    req = requests.get(url=urlToScrape, )

    # print(req.status_code) ITS WORKING OR NOT
    # print(req.content)  TO ACCESS THE RESPONSE BODY AS BYTES, TYPE OF HTML DOC

    beautifulSoupObj = BeautifulSoup(req.content, "html.parser")# CONVERTS TO UNICODE AND THEN PARSES IT (ALSO XML
    # PARSER)
    # print(beautifulSoupObj.prettify())
    titleObj = beautifulSoupObj.find(id="firstHeading")  # FIND TAG USING ID
    # print(title)
    print(titleObj.string)  # A STRING = BIT OF TEXT WITHIN A TAG.
    a_Title.config(text=titleObj.text)
    # print("\n"+beautifulSoupObj.getText())
    print(wikipedia.summary(title=titleObj.string))
    wikiSummary.config(text=wikipedia.summary(title=titleObj.text))
    # print(beautifulSoupObj)
    links = beautifulSoupObj.find(id="bodyContent").find_all("a")

    random.shuffle(links)

    # print(type(links[4])) ITS A TAG
    maxSize = len(links)
    point = random.randint(1, maxSize)

    for link in links[point:]:
        if link["href"].find("/wiki/") == -1:
            continue

        if not link["href"].startswith("/wiki/"):
            continue

        if link["href"].find("/wiki/Category") != -1:
            continue

        if link["href"].find("/wiki/Help") != -1 or link["href"].find("/wiki/Wikipedia") != -1:
            continue

        if link["href"].find("/wiki/File") != -1:
            continue

        if link["href"].find("/wiki/Category") != -1:
            continue
        print(link)
        global linkToScrape
        linkToScrape = link
        linkToScrape = "https://en.wikipedia.org" + linkToScrape["href"]
        # print(linkToScrape)
        break


def start():
    # randomWikipediaPages("https://en.wikipedia.org" + linkToScrape["href"])
    randomWikipediaPages(linkToScrape)


wikiTitle = Label(wind, text="WIKIPEDIA SCRAPER", font=("Fixedsys", 24,), bg="grey", fg="black", relief=RIDGE, bd=5)
wikiTitle.place(x=220, y=15, width=360, height=40)

articleTitle = Label(wind, text="Title : ", font=("Fixedsys", 15,), bg="grey", fg="black", bd=5)
articleTitle.place(x=5, y=100)

a_Title = Label(wind, text=" ", font=("Fixedsys", 15,), bg="grey", fg="black", bd=5)
a_Title.place(x=90, y=100)


convert = Button(wind, text="Change", command=start, font=("Courier", 16, "bold"), bg="black", fg="green",
                 relief=RAISED, bd=6)
convert.place(x=550, y=80)


wikiSummary = Label(wind, text=" ", font=("Fixedsys", 5,), bg="grey", fg="white", relief=RIDGE, bd=5, wraplength=600)
wikiSummary.place(x=0, y=150, width=800, height=450)

wind.mainloop()
