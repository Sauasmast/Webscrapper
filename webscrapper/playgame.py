import scrape
import random


class playgame():
    def __init__(self, quotation_list):
        self.quotation_list = quotation_list
        self.random_created = []
        self.score = 0
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
        print(f"{self.quotation_list[number]['Quotation']} \n")
        answer = input("Enter the name of the person ")
        self._check_answer(self.quotation_list[number]['Author'], answer)

    def _check_answer(self, right_ans, user_ans):
        if right_ans == user_ans:
            print("Right Answer.")
            self.total_question += 1
            self.score += 1
            cont = input(
                "Do you want to continue? \n Press y if you want to continue or anything to exit: ")
            self._continue(cont)

    def _continue(self, cont):
        if cont == 'y':
            self._selectrandom()
        else:
            print(f"You score was {self.score} out of {self.total_question}.")
