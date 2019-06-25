#openwhethermap
#news Api
#news aggregator
# import requests
import requests as rq
import json as js


url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=29f3bc59341f454b865eafa4af29cd10"
response = rq.get(url)  # get data from server
newsData = js.loads(response.text)
print(newsData)

# JSON parsing
print(newsData['status'])

