import scrape
import random


class playgame():
    def __init__(self, quotation_list):
        self.quotation_list = quotation_list
        self.random_created = []
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
        print(f"{self.quotation_list[number]} \n")
