import requests
import pprint
import csv
from bs4 import BeautifulSoup

domain = 'https://chelyabinsk.n1.ru'
URL = f'{domain}/kupit/kvartiry/vtorichka/district-Kalininskiy-rayon/'

response = requests.get( URL )
print( response.status_code )

soup = BeautifulSoup( response.text, 'html.parser')

div_tags = soup.find_all( 'div', class_='living-list-card__main-container' )
#print( len( div_tags ), type( div_tags ))

lst = []
for v1 in div_tags:
    #print( v1 )

    dic = {}
    dic['region'] = ''
    dic['city'] = ''
    dic['address'] = ''
    dic['characteristic'] = ''
    dic['price'] = ''

#    try:
    tags = v1.find('a', class_='link')
    #print(tags.text)
    dic['address'] = tags.text
#    except  AttributeError:
#        pass

    #try:
    #tags = v1.find('div', class_='search-item-district living-list-card__inner-block')
    tags = v1.find('div', class_='search-item-district')
    #print(  tags.text )
    dic['region'] = tags.text
    #except  AttributeError:
    #    pass

#    try:
    #tags = v1.find('div', class_='living-list-card__city-with-estate living-list-card-city-with-estate living-list-card__inner-block')
    tags = v1.find('div', class_='living-list-card__city-with-estate')
    #print(tags.text)
    dic['city'] = tags.text
#    except  AttributeError:
#        pass

#    try:
    #tags = v1.find('div', class_='living-list-card__area living-list-card-area living-list-card__inner-block')
    tags = v1.find('div', class_='living-list-card__area')
    #print(tags.text)
    dic['characteristic'] += tags.text
#    except  AttributeError:
#        pass

    #try:
    #tags = v1.find('div', class_='living-list-card__floor living-list-card-floor living-list-card__inner-block')
    tags = v1.find('div', class_='living-list-card__floor')
    #print(tags.text)
    dic['characteristic'] += " "+tags.text
    #except  AttributeError:
    #    pass

#   try:
    #tags = v1.find('div', class_='living-list-card__material living-list-card-material living-list-card__inner-block')
    tags = v1.find('div', class_='living-list-card__material')
    #print(tags.text)
    dic['characteristic'] += " " + tags.text
#    except  AttributeError:
#        pass

#    try:
    tags = v1.find('div', class_='living-list-card-price__item _object')
    #print(tags.text)
    dic['price'] = (tags.text).replace(chr(160),' ') +'руб'
#    except  AttributeError:
#        print("!!!!!!!! нету !!!!!!!!!")

    lst.append( dic )
    #print('-----------', )

print("\n=================================")
pprint.pprint( lst )
print("=================================\n")

title =  ['region', 'city','address','characteristic','price']

with open( "chel_hausing.csv", mode="w", encoding='utf-8', newline='') as w_file:
    f = csv.writer(w_file, delimiter = "!" )
    f.writerow( title )
    for d in lst:
        #print( d['region'], d['city'], d['address'], d['characteristic'] )
        f.writerow(  [ d['region'], d['city'], d['address'], d['characteristic'], d['price'] ]    )