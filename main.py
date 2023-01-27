import requests
from send_email import send_email

api_key = "be8431ec07c348f3a429925736a31fea"

topic = "tesla"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2022-12-27&sortBy" \
      "=publishedAt&apiKey=be8431ec07c348f3a429925736a31fea&language=en"
# Write a request
request = requests.get(url)
content = request.json()
print(content)

# Send email with title and descriptions
message = "Subject: Today's News"
for article in content["articles"][:10]:
    if article is not None:
        message += "\n" + article["title"] + "\n" \
                   + article["description"] + "\n" \
                   + article["url"] + 2 * "\n"

send_email(message.encode('utf-8'))


