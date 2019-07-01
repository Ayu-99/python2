import requests

from bs4 import BeautifulSoup  # External Library for parsing HTML data
url = "https://twitter.com/dna"
response = requests.get(url)
#print(response)

# HTML Parsing : From HTML code extract the desired/ meaningful information

soup = BeautifulSoup(response.text, "html.parser")
#print(soup)
print("Type of soup is:", type(soup))
print("****************************************")

#print(soup)
#print(soup.prettify())  # code will be displayed with indentation

print("Title is:", soup.title.text)

""""
children = soup.children  # This api returns all the HTML tags
# Html works as a tree data structure
for child in children:
    print(child)
    print("-------------------")

"""

""""
pTags = soup.find_all("p")
for tag in pTags:
    print(tag)
    print("--------------")

"""
#divTags = soup.find_all("div")
divTags = soup.find_all("div",class="js-tweet-text-container")

for tag in divTags:
    #print(tag)
    print(tag.text)
    print("------------------------")
