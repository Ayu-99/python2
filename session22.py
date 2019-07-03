# Multi-threading/ Concurrent Programming/ Parallel Programming
import requests
import threading

url1 = "https://newsapi.org/v2/everything?q=apple&from=2019-07-02&to=2019-07-02&sortBy=popularity&apiKey=29f3bc59341f454b865eafa4af29cd10"
url2 = "http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2"

print("App started..")

class FetchNews(threading.Thread):
    def run(self):
        print("Fetching news from url1")
        response1 = requests.get(url1)
        print(response1.text)


class FetchBook(threading.Thread):
    def run(self):
        print("Fetching news from url1")
        response2 = requests.get(url2)
        print(response2.text)


a = FetchNews()
b = FetchBook()
a.start()
b.start()


for i in range(1, 11):
    print("i is:",i)

print("App finished")
