import requests

api_key = "be8431ec07c348f3a429925736a31fea"
youtube_api_key = "AIzaSyDdEzmAYt3PfCYYqPN3y0GbuBQCQShfo8g"
url = f"https://www.youtube.com/playlist?list=PLm1rwsFzd6CBtmBuuLRSBuroTw7" \
      f"q93vhe{youtube_api_key}"
url2 = "https://newsapi.org/v2/everything?q=tesla&from=2022-12-25&sortBy=" \
       "publishedAt&apiKey=be8431ec07c348f3a429925736a31fea"
# Write a request
request = requests.get(url2)
content = request.json()

# Print out content of API
print(content["articles"][1]["source"]["name"])
print(content)

# Access authors and description of each article
for cont in content["articles"]:
    print(f"AUTHOR --- {cont['author']}")
    print(f"ARTICLE --- {cont['title']}")