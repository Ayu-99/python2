# Data Analysis of BollyWood and HollyWood Movies using HTML Parsing

import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup  # External Library for parsing HTML data
url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("////////////////////////////////////////////////")

tags1 = soup.find_all("td", class_="ratingColumn")
rating = []
for tag in tags1:
    data = tag.text
    rating.append(data.strip())

x = []
for i in range(0, 20, 2):
    y = float(rating[i])
    x.append(y)

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

# List Containing Ratings
print(x)
print("====================")
# List Containing Years

print(h)

d = dict()
for i in range(0, 10):
    d.update({h[i]: x[i]})
print("-------------------------------")
print(d)

# Sorted Years List
h.sort()
print(h)
finalRating = []
for i in range(0,10):
    j = h[i]
    finalRating.append(d[j])

# Final List which is sorted according to years in sorted list h
print(finalRating)


url1 = "https://www.imdb.com/chart/top-english-movies"
response1 = requests.get(url1)

soup = BeautifulSoup(response1.text, "html.parser")

print("////////////////////////////////////////////////")

tags3 = soup.find_all("td", class_="ratingColumn")
rating2 = []
for tag in tags3:
    data = tag.text
    rating2.append(data.strip())


x2 = []
for i in range(0, 20, 2):
    y = float(rating2[i])
    x2.append(y)

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

# List Containing Years
print(h2)


print(x2)
print("====================")
print(h2)

d2 = dict()
for i in range(0, 10):
    d2.update({h2[i]: x2[i]})
print("-------------------------------")
print(d2)

# Sorting List Containing Years
h2.sort()
print(h2)
finalRating2 = []
for i in range(0,10):
    j = h2[i]
    finalRating2.append(d2[j])

# Final List which is sorted according to years in sorted list h

print(finalRating2)


plt.plot(h, finalRating, label="B")
plt.plot(h2, finalRating2, label="H")
plt.legend()
plt.xlabel('Years')
plt.ylabel('Rating')
plt.show()





