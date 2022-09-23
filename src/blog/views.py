from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import random
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import QueryDict


def index(request):
    #return HttpResponse('hi')
    return render(request, "blog/first_page.html")

def vpn(request):
    return render(request, "blog/second_page.html")

def vpn_yes(request):
    return render(request, "blog/third_page_yes.html")

def vpn_no(request):
    return render(request, "blog/third_page_no.html")

def find_movie(movie_genre):
    print('test')
    print(movie_genre)
    html=requests.get(f'https://www.justwatch.com/us/provider/netflix/movies?genres={movie_genre}&rating_imdb=8')
    print(f'https://www.justwatch.com/us/provider/netflix/movies?genres={movie_genre}&rating_imdb=8')
    soup=BeautifulSoup(html.text, 'lxml')
    movie_urls=[]
    result = soup.find(lambda tag: tag.name == 'div' and tag.get('class') == ['title-list-grid'])
    for a in result.find_all('a', href=True):
        if '/us/movie/' in a['href']:
            movie_urls.append(a['href'])
    movie_url_short=random.choice(movie_urls)
    movie_url_long='https://www.justwatch.com'+ movie_url_short
    movie_html=requests.get(movie_url_long)
    soup_2=BeautifulSoup(movie_html.text,'lxml')
    name = soup_2.find('h1').text
    date= soup_2.find('span', class_="text-muted").text
    imdb_rating=soup_2.find('div',class_='title-info')
    imdb_rating=imdb_rating.find('a', href=True).text
    return name

def genre(request):
    # action adv 
    #yo=request.GET.get('genre_button')
    if request.method == 'POST':
        data = request.POST
        action = data.get('movie_genre')
        print("action is")
        print(action)
        print(data)
        #movie_genre = request.POST.get('act')
    name = find_movie(action)
    return render(request, "blog/genre.html", {'name': name})


def genre_vpn(request):
    # action adv 
    #yo=request.GET.get('genre_button')
    if request.method == 'POST':
        data = request.POST
        action = data.get('movie_genre')
        print("action is")
        print(action)
        print(data)
        #movie_genre = request.POST.get('act')
    name, country = find_movie_vpn(action)
    return render(request, "blog/genre_vpn.html", context={'name': name,'country': country})


def find_movie_vpn(movie_genre):
    print('test')
    print(movie_genre)
    list_countries=['au','uk','us','ca']
    random_country=random.choice(list_countries)
    html=requests.get(f'https://www.justwatch.com/{random_country}/provider/netflix/movies?genres={movie_genre}&rating_imdb=8')
    print(f'https://www.justwatch.com/us/provider/netflix/movies?genres={movie_genre}&rating_imdb=8')
    soup=BeautifulSoup(html.text, 'lxml')
    movie_urls=[]
    result = soup.find(lambda tag: tag.name == 'div' and tag.get('class') == ['title-list-grid'])
    for a in result.find_all('a', href=True):
        if f'/{random_country}/movie/' in a['href']:
            movie_urls.append(a['href'])
    movie_url_short=random.choice(movie_urls)
    movie_url_long='https://www.justwatch.com'+ movie_url_short
    movie_html=requests.get(movie_url_long)
    soup_2=BeautifulSoup(movie_html.text,'lxml')
    name = soup_2.find('h1').text
    date= soup_2.find('span', class_="text-muted").text
    imdb_rating=soup_2.find('div',class_='title-info')
    imdb_rating=imdb_rating.find('a', href=True).text
    if random_country=='au':
        random_country='Australia'
    elif random_country=='uk':
        random_country='United Kingdom'
    elif random_country=='us':
        random_country='United States'
    elif random_country=='ca':
        random_country='Canada'
    print(random_country)
    return name, random_country
    










