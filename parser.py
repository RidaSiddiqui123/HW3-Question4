from pymongo import MongoClient
from db_connection_mongo_CS import *
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://www.cpp.edu/sci/computer-science/'
frontier = [url]
visited = []

if __name__ == '__main__':
    # Connecting to the database
    db = connectDataBase()
    # Creating a collection
    pages = db.pages
    professors = db.professors

def crawlerThread(frontier):
    while len(frontier) != 0:
        url = frontier[0]
        visited.append(url)
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html.parser')
        frontier.pop(0)
        information = str(bs.find("body"))
        insertPage(pages, url, information)
        if bs.find('h1').get_text() == "Permanent Faculty":
            page = visited[len(visited)-1]
            print(page)
            frontier.clear()
            break
        else:
            links = bs.find_all("a")  # Find all elements with the tag <a>
            for link in links:
                href = link.get("href")
                absolute_url = urljoin(url, href)
                frontier.append(absolute_url)

try:
    crawlerThread(frontier)
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')






























