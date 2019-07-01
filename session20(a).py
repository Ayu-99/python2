# Data Analysis of Indian Movies using HTML Parsing
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup  # External Library for parsing HTML data
url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
"""
tags = soup.find_all("td", class_="titleColumn")
movies = []
for tag in tags:
    data = tag.text
    movies.append(data.strip())

for movie in movies:
    print(movie)
    print("*******")
"""
"""
print(movies)
for i in movies:
    print(i[17:20])

"""

print("////////////////////////////////////////////////")

tags1 = soup.find_all("td", class_="ratingColumn")
rating = []
for tag in tags1:
    data = tag.text
    rating.append(data.strip())

"""
for rate in rating:
    print(rate)
    print("*******")
"""

#print("==================", rating)

x = []
for i in range(0, 20, 2):
    y = float(rating[i])
    x.append(y)

#print(x)


tags = soup.find_all("span", class_="secondaryInfo")
years = []
for tag in tags:
    data = tag.text
    years.append(data.strip())


h = []
v = []
for i in range(0, len(years)):
    y = years[i]
    z = int(y[1:5])
    if 2000 <= z <= 2010:

        v.append(z)
    else:
        continue

for i in range(0, 10):
    h.append(v[i])


print(h)


print(x)
print("====================")
print(h)

"""
print(years)
for year in years:
    print(year)
    print("*******")
"""
d = dict()
for i in range(0, 10):
    d.update({h[i]: x[i]})
print("-------------------------------")
print(d)


h.sort()
print(h)
finalRating = []
for i in range(0 ,10):
    j = h[i]
    finalRating.append(d[j])

print(finalRating)

"""
    two list->finalRating -> Ratings
            h -> sorted years
"""

url1 = "https://www.imdb.com/chart/top-english-movies"
response1 = requests.get(url1)

soup = BeautifulSoup(response1.text, "html.parser")
"""
tags = soup.find_all("td", class_="titleColumn")
movies = []
for tag in tags:
    data = tag.text
    movies.append(data.strip())

for movie in movies:
    print(movie)
    print("*******")
"""
"""
print(movies)
for i in movies:
    print(i[17:20])

"""

plt.plot(h, finalRating, label="B")
plt.xlabel('Years')
plt.ylabel('Rating')
plt.show()





