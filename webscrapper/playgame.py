import scrape
import random
import data_deal as data
from bs4 import BeautifulSoup


class playgame():
    def __init__(self, quotation_list):
        self.quotation_list = quotation_list
        self.random_created = []
        self.score = 0
        self.hint = 0
        self.total_question = 0
        self._selectrandom()

    def _selectrandom(self):
        randomnumber = random.randint(0, len(self.quotation_list))
        if len(self.random_created) < 50:
            if randomnumber in self.random_created:
                self._selectrandom()
            else:
                self.random_created.append(randomnumber)
                self._askquestion(randomnumber)
        else:
            self.random_created.clear()
            self.random_created.append(randomnumber)
            self._askquestion(randomnumber)

    def _askquestion(self, number):
        self.total_question += 1
        print(f"{self.quotation_list[number]['Quotation']} \n")
        answer = input("Enter the name of the person ")
        self._check_answer(number, answer)

    def _check_answer(self, num, user_ans):
        if self.quotation_list[num]['Author'] == user_ans:
            print("Well Done !!! Right Answer")
            self.score += 1
            self._continue()
        else:
            if self.hint < 2:
                self.__hint(num)
            else:
                self.hint = 0
                print(
                    f"Sorry! Wrong Annswer. The right answer was {self.quotation_list[num]['Author']}")
                self._continue()

    def __hint(self, num):
        if self.hint == 0:
            self.hint += 1
            name = self.quotation_list[num]['Author'].split(' ')
            print(f"The initials of the author is {name[0][0]} {name[1][0]}")
        else:
            self.hint += 1
            response = scrape.scrape(
                "http://quotes.toscrape.com" + self.quotation_list[num]['href'])
            value = response.initiatescrape()
            value1 = data.filter(value, {"class": "author-born-date"}, True)
            value2 = data.filter(
                value, {"class": "author-born-location"}, True)
            print(f"The author was born on {value1} in {value2}")

        answer = input("Enter the name of the person: ")
        self._check_answer(num, answer)

    def _continue(self):
        cont = input(
            "Do you want to continue? \n Press y if you want to continue or anything to exit: ")
        if cont == 'y':
            self._selectrandom()
        else:
            print(f"You score was {self.score} out of {self.total_question}.")
