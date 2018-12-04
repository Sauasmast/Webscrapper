# -*- coding: utf-8 -*-
import scrape
from bs4 import BeautifulSoup
import sys
import playgame as game

quotation_list = []


def filter(text, attbrs, gettext=False):
    soup = BeautifulSoup(text, "html.parser")
    if gettext:
        divs = soup.find(attrs=attbrs).get_text()
    else:
        divs = soup.find_all(attrs=attbrs)
    return divs


def create_data(data):
    for div in data:
        soup = BeautifulSoup(str(div), "html.parser")
        quotation = soup.find(itemprop="text").get_text()
        authortag = soup.find(itemprop="author").get_text()
        href = soup.find(
            itemprop="author").next_sibling.next_sibling.get('href')
        quotation_list.append(
            {'Quotation': quotation, 'Author': authortag, 'href': href})


if __name__ == "__main__":

    scarping_check = True
    next_page = ''
    count = 0

    print("Loading ......")
    while scarping_check:
        # Scrape the website for the first time
        file1 = scrape.scrape("http://quotes.toscrape.com" + next_page)
        value = file1.initiatescrape()

        # Filter the data and populate the list with the values
        data = filter(str(value), {'class': 'quote'})
        create_data(data)

        # Check for the other pages
        check_page = filter(str(value), {'class': 'next'})

        if check_page:
            href = BeautifulSoup(
                str(check_page[0]), "html.parser").a.get('href')
            scarping_check = True
            next_page = str(href)
        else:
            scarping_check = False

    # Play the game for the user one
    p1 = game.playgame(quotation_list)
    sys.exit()
