# -*- coding: utf-8 -*-
import scrape
from bs4 import BeautifulSoup
import sys
import playgame as game

# quotation_list = []


def filter(text, attbrs):
    soup = BeautifulSoup(text, "html.parser")
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

    # while scarping_check:
    #     # Scrape the website for the first time
    #     file1 = scrape.scrape("http://quotes.toscrape.com" + next_page)
    #     value = file1.initiatescrape()

    #     # Filter the data and populate the list with the values
    #     data = filter(str(value), {'class': 'quote'})
    #     create_data(data)

    #     # Check for the other pages
    #     check_page = filter(str(value), {'class': 'next'})

    #     if check_page:
    #         href = BeautifulSoup(
    #             str(check_page[0]), "html.parser").a.get('href')
    #         scarping_check = True
    #         next_page = str(href)
    #         count += 1
    #         print(count)
    #         print(quotation_list)
    #     else:
    #         scarping_check = False

    quotation_list = [{'Quotation': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'Author': 'Albert Einstein', 'href': '/author/Albert-Einstein'}, {'Quotation': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'Author': 'J.K. Rowling', 'href': '/author/J-K-Rowling'}, {'Quotation': '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'Author': 'Albert Einstein', 'href': '/author/Albert-Einstein'}, {'Quotation': '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'Author': 'Jane Austen', 'href': '/author/Jane-Austen'}, {'Quotation': "“Imperfection is beauty, madness is genius andit's better to be absolutely ridiculous than absolutely boring.”", 'Author': 'Marilyn Monroe', 'href': '/author/Marilyn-Monroe'}, {'Quotation': '“Try not to become a man of success. Rather become a man of value.”', 'Author': 'Albert Einstein', 'href': '/author/Albert-Einstein'}, {'Quotation': '“It is better to be hated for what you are than to be loved for what you are not.”', 'Author': 'André Gide', 'href': '/author/Andre-Gide'}, {'Quotation': "“I have not failed. I've just found 10,000 ways that won't work.”", 'Author': 'Thomas A. Edison', 'href': '/author/Thomas-A-Edison'}, {'Quotation': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'Author': 'Eleanor Roosevelt', 'href': '/author/Eleanor-Roosevelt'}, {'Quotation': '“A day without sunshine is like, you know, night.”', 'Author': 'Steve Martin', 'href': '/author/Steve-Martin'}, {'Quotation': "“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”", 'Author': 'Marilyn Monroe', 'href': '/author/Marilyn-Monroe'}, {'Quotation': '“It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.”', 'Author': 'J.K. Rowling', 'href': '/author/J-K-Rowling'}, {'Quotation': "“If you can't explain it to a six year old, you don't understand it yourself.”", 'Author': 'Albert Einstein', 'href': '/author/Albert-Einstein'}, {'Quotation': "“You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never beperfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's notthere.”", 'Author': 'Bob Marley', 'href': '/author/Bob-Marley'}, {'Quotation': '“I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.”', 'Author': 'Dr. Seuss', 'href': '/author/Dr-Seuss'}, {'Quotation': '“I may not have gone where I intended to go, but I think I have ended up where I needed to be.”', 'Author': 'Douglas Adams', 'href': '/author/Douglas-Adams'},
                      {'Quotation': "“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”", 'Author': 'Elie Wiesel', 'href': '/author/Elie-Wiesel'}, {'Quotation': '“It is not a lack of love, but a lack of friendship that makes unhappy marriages.”', 'Author': 'Friedrich Nietzsche', 'href': '/author/Friedrich-Nietzsche'}, {'Quotation': '“Good friends, good books, and a sleepy conscience: this is the ideal life.”', 'Author': 'Mark Twain', 'href': '/author/Mark-Twain'}, {'Quotation': '“Life is what happens to us while we are making other plans.”', 'Author': 'Allen Saunders', 'href': '/author/Allen-Saunders'}, {'Quotation': '“I love you without knowing how, or when, or from where. I love you simply, without problems or pride: I love you in this way because I do not know any other way of loving but this, in which there is no I or you, so intimate that your hand upon my chest is my hand, so intimate that whenI fall asleep your eyes close.”', 'Author': 'Pablo Neruda', 'href': '/author/Pablo-Neruda'}, {'Quotation': '“For every minute you are angry you lose sixty secondsof happiness.”', 'Author': 'Ralph Waldo Emerson', 'href': '/author/Ralph-Waldo-Emerson'}, {'Quotation': '“If you judge people, you have no time to love them.”', 'Author': 'Mother Teresa', 'href': '/author/Mother-Teresa'}, {'Quotation': '“Anyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.”', 'Author': 'Garrison Keillor', 'href': '/author/Garrison-Keillor'}, {'Quotation': '“Beauty is in the eye of the beholder and it may be necessary from time to time to give a stupid or misinformed beholder a black eye.”', 'Author': 'Jim Henson', 'href': '/author/Jim-Henson'}, {'Quotation': '“Today you are You, that is truer than true. There is no one alive who is Youer than You.”', 'Author': 'Dr. Seuss', 'href': '/author/Dr-Seuss'}, {'Quotation': '“If you want your children to be intelligent, read them fairy tales. If you want them to be more intelligent, read them more fairy tales.”', 'Author': 'Albert Einstein', 'href': '/author/Albert-Einstein'}, {'Quotation': '“It is impossible to live without failing at something, unless you live so cautiously that you might as well not have lived at all - in which case, you fail by default.”', 'Author': 'J.K. Rowling', 'href': '/author/J-K-Rowling'}, {'Quotation': '“Logic will get you from A to Z; imagination will get you everywhere.”', 'Author': 'Albert Einstein', 'href': '/author/Albert-Einstein'}, {'Quotation': '“One good thing about music, when it hits you, you feel no pain.”', 'Author': 'Bob Marley', 'href': '/author/Bob-Marley'}, {'Quotation': "“The more that you read, the more things you will know. The more that you learn, the more places you'll go.”", 'Author': 'Dr. Seuss', 'href': '/author/Dr-Seuss'}, {'Quotation': '“Of course it is happening inside your head, Harry, but why on earth should that mean that it is not real?”', 'Author': 'J.K. Rowling', 'href': '/author/J-K-Rowling'}, {'Quotation': '“The truth is, everyone is going to hurt you. You just got to find the ones worth suffering for.”', 'Author': 'Bob Marley', 'href': '/author/Bob-Marley'}, {'Quotation': '“Not all of us cando great things. But we can do small things with great love.”', 'Author': 'Mother Teresa', 'href': '/author/Mother-Teresa'}, {'Quotation': '“To the well-organizedmind, death is but the next great adventure.”', 'Author': 'J.K. Rowling', 'href': '/author/J-K-Rowling'}, {'Quotation': "“All you need is love. But a little chocolate now and then doesn't hurt.”", 'Author': 'Charles M. Schulz', 'href': '/author/Charles-M-Schulz'}, {'Quotation': "“We read to know we're not alone.”", 'Author': 'William Nicholson', 'href': '/author/William-Nicholson'}, {'Quotation': '“Any fool can know. The point is to understand.”', 'Author': 'Albert Einstein', 'href': '/author/Albert-Einstein'}, {'Quotation': '“I have always imagined that Paradise will be a kind of library.”', 'Author': 'Jorge Luis Borges', 'href': '/author/Jorge-Luis-Borges'}, {'Quotation': '“It is never too late to be what you might have been.”', 'Author': 'George Eliot', 'href': '/author/George-Eliot'}]

    # Play the game for the user one
    p1 = game.playgame(quotation_list)
    sys.exit()
