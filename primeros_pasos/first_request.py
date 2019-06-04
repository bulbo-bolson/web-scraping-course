import requests

page_link = "https://api.github.com/events"
file_dest = "github_api.txt"
response = requests.get(page_link)

with open(file_dest, "w", encoding="utf-8") as f:
    f.write(response.text)
