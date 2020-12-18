import requests
from bs4 import BeautifulSoup
import math

response = requests.get(url="https://news.ycombinator.com/")
pages_online = response.text

soup = BeautifulSoup(pages_online, "html.parser" )

article= soup.find_all(name = "a", class_="storylink")

article_texts = []
article_links= []



for article_tags in article:
   text =article_tags.getText()
   article_texts.append(text)
   link = article_tags.get("href")
   article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_number_index = article_upvotes.index(largest_number)

# The heigtest rated news 12/18/2020
print(article_links[largest_number_index])
print(article_texts[largest_number_index])
