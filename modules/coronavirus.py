"""
Ten moduł służy do wysyłania informacji o koronawirusie
"""

import requests
from bs4 import BeautifulSoup


def coronavirus():
    url = "https://www.worldometers.info/coronavirus/"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    table = soup.find("tbody")
    rows = table.findAll("tr", attrs={"style":""})
    countries = {}
    for row in rows:
        cols = row.findAll("td")[1:]
        numbers = []
        for col in cols:
            if len(col.contents) > 0:
                number = str(col.contents[0])
                if "+" in  number:
                    number = number.replace("+","")
                if "," in number:
                    number = number.replace(",","")
                try:
                    numbers.append(float(number))
                except:
                    numbers.append(0.0)
            else:
                numbers.append(0.0)

        country = row.findAll("td")
        country = country[1].contents[0]
        if len(country) == 1:
            try:
                country = country.contents[0]
            except:
                country = "Diamond Princess"

        countries[country.strip()]=numbers

    message = "BIEŻĄCE INFORMACJE O KORONAWIRUSIE\n\n"
    message += "POLSKA, zarażeni: " + str(countries["Poland"][0]).replace(".0","") + "\n"
    message += "POLSKA, wyleczeni: " + str(countries["Poland"][4]).replace(".0","") + "\n"
    message += "POLSKA, śmierci: " + str(countries["Poland"][2]).replace(".0","") + "\n\n"
    message += "ŚWIAT, zarażeni: " + str(countries["World"][0]).replace(".0","") + "\n"
    message += "ŚWIAT, wyleczeni: " + str(countries["World"][4]).replace(".0","") + "\n"
    message += "ŚWIAT, śmierci: " + str(countries["World"][2]).replace(".0","") + "\n\n"
    return message
