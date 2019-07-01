# Data Analysis of HollyWood Movies using HTML Parsing

import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup  # External Library for parsing HTML data
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

print("////////////////////////////////////////////////")

tags3 = soup.find_all("td", class_="ratingColumn")
rating2 = []
for tag in tags3:
    data = tag.text
    rating2.append(data.strip())

"""
for rate in rating:
    print(rate)
    print("*******")
"""

#print("==================", rating)

x2 = []
for i in range(0, 20, 2):
    y = float(rating2[i])
    x2.append(y)

#print(x)


tags4 = soup.find_all("span", class_="secondaryInfo")
years2 = []
for tag in tags4:
    data = tag.text
    years2.append(data.strip())


h2 = []
v2 = []
for i in range(0, len(years2)):
    y = years2[i]
    z = int(y[1:5])
    if 2000 <= z <= 2010:

        v2.append(z)
    else:
        continue

for i in range(0, 10):
    h2.append(v2[i])


print(h2)


print(x2)
print("====================")
print(h2)

"""
print(years)
for year in years:
    print(year)
    print("*******")
"""
d2 = dict()
for i in range(0, 10):
    d2.update({h2[i]: x2[i]})
print("-------------------------------")
print(d2)


h2.sort()
print(h2)
finalRating2 = []
for i in range(0 ,10):
    j = h2[i]
    finalRating2.append(d2[j])

print(finalRating2)

"""
    two list->finalRating -> Ratings
            h -> sorted years
"""

plt.plot(h2, finalRating2)
plt.xlabel('Years')
plt.ylabel('Rating')
plt.show()


