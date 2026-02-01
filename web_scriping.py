import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for page in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        tags = ", ".join([tag.text for tag in q.find_all("a", class_="tag")])

        data.append({
            "Quote": text,
            "Author": author,
            "Tags": tags
        })

df = pd.DataFrame(data)

print("Total rows scraped:", len(df))

df.to_csv("quotes_data.csv", index=False)

print("CSV file created successfully!")
