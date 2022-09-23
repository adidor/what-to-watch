from bs4 import BeautifulSoup
import requests
import random

#program to choose netflix movie for you


user_input = input("Choose action (a) or comedy (c): ")
if user_input=='c':
    html=requests.get('https://www.justwatch.com/us/provider/netflix/movies?genres=cmy&rating_imdb=8')
if user_input=='a':
    html=requests.get('https://www.justwatch.com/us/provider/netflix/movies?genres=act&rating_imdb=8')


soup=BeautifulSoup(html.text, 'lxml')
#soup=soup.find_all('div',class_='title-list-grid__item')
#movie= movie.find('a').href
#print(movie)
movie_urls=[]
for a in soup.find_all('a', href=True):
    if '/us/movie/' in a['href']:
        movie_urls.append(a['href'])
        #print("URL:", a['href'])

movie_url_short=random.choice(movie_urls)
movie_url_long='https://www.justwatch.com'+ movie_url_short
movie_html=requests.get(movie_url_long)
soup_2=BeautifulSoup(movie_html.text,'lxml')

class info:
  def __init__(self, name, date, imdb_rating):
    self.name = name
    self.date = date
    self.imdb_rating = imdb_rating

movie_info=info('','','')

name = soup_2.find('h1').text
date= soup_2.find('span', class_="text-muted").text
imdb_rating=soup_2.find('div',class_='title-info')
#print(imdb_rating)
imdb_rating=imdb_rating.find('a', href=True).text
#imdb_rating=imdb_rating[-1]
movie_info.name, movie_info.date, movie_info_imdb_rating=name,date, imdb_rating

print("WATCH THIS!!!:" + movie_info.name + movie_info.date)
print("IMDB rating:" + movie_info_imdb_rating)