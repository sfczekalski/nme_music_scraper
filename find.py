import requests
from bs4 import BeautifulSoup
import sys

def get_headings():
    url = "https://www.nme.com/news/music"

    response = requests.get(url)
    html = response.text
    page_content = BeautifulSoup(html, "html.parser")

    return page_content.find_all("div", class_="entry-content")

def get_interest():
    return sys.argv[1]

def look_for_interest(headings):
    interest = get_interest()
    articles = ""

    for i in range(len(headings)):
        heading = headings[i].find_all('span')

        text = heading[0].text
        if interest in text:
            title = heading[0].text
            for parent in headings[i].parents:
                if parent.get('href') != None:
                    link = parent.get("href")
                    articles += title + " " + link + "\n"

    return articles


def save_to_log(data):
    with open("log.txt", "w+") as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        if data not in content:
            f.write(data)
            print(content)

def operate():
    headings = get_headings()
    articles = look_for_interest(headings)
    save_to_log(articles)

operate()








