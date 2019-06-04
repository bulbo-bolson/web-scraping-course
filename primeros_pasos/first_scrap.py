import requests

response = requests.get("https://stallman.org/")
with open("stallman.txt", "w", encoding="utf-8") as f:
    f.write(response.text)


