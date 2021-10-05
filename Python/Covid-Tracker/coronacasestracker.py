import bs4
import requests
from tkinter import *
from PIL import Image, ImageTk


def get_html_data(url):
    return requests.get(url).text


def covid_data():

    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)

    soup = bs4.BeautifulSoup(html_data, "lxml")
    info_div = soup.find("div", class_="content-inner").find_all(
        "div", id="maincounter-wrap"
    )

    return "".join(div.h1.text + " " + div.span.text + "\n" for div in info_div)


def reload():
    country_name = e.get()
    if country_name:
        get_country_data()
    else:
        data_label.config(text=covid_data())


def get_country_data():

    country_name = e.get()
    if country_name:
        url = "https://www.worldometers.info/coronavirus/country/" + country_name
        html_data = get_html_data(url)

        soup = bs4.BeautifulSoup(html_data, "lxml")
        info_div = soup.find("div", class_="content-inner").find_all(
            "div", id="maincounter-wrap"
        )
        info_div = info_div[:3]
        country_data = "".join(
            div.h1.text + " " + div.span.text + "\n" for div in info_div
        )
        data_label.config(text=country_data)
    else:
        data_label.config(text="Please enter a Country Name")


root = Tk()
root.geometry("500x500")
root.title("Coronavirus Tracker")
root.iconbitmap("covidicon.ico")

covid_img = ImageTk.PhotoImage(Image.open("covid.png"))
label = Label(root, image=covid_img).pack()

e = Entry(root, width=50, relief=SOLID, bd=3)
e.pack(pady=30)

data_label = Label(root, text=covid_data(), font="normal 20 bold")
data_label.pack()

search_button = Button(root, text="Search", command=get_country_data)
search_button.pack(pady=10)

reload_button = Button(root, text="Reload", command=reload)
reload_button.pack()

root.mainloop()
