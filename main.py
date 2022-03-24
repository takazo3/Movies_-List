# This program will scape the top 100 movies from stacker.com
from bs4 import BeautifulSoup
import requests

URL = "https://stacker.com/stories/1587/100-best-movies-all-time"
# TODO: Grab the web page and make some soup
response = requests.get(URL)
movie_page = response.text
soup = BeautifulSoup(movie_page, "html.parser")

all_movies = soup.find_all(name="h2", class_="ct-slideshow__slide__text-container__caption")
movie_titles = [movie.getText().strip() for movie in all_movies]
# The first element needs to be removed
del movie_titles[0]
for movie in reversed(movie_titles):
    print(movie)