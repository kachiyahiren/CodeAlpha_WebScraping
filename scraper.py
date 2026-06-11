import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for page in range(1, 51):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping Page {page}")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article")

    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).text

        rating = book.p["class"][1]

        data.append(
            [title, price, rating]
        )

df = pd.DataFrame(
    data,
    columns=[
        "Title",
        "Price",
        "Rating"
    ]
)

df.to_csv(
    "data/books.csv",
    index=False
)

print("Dataset Saved")
print(df.shape)