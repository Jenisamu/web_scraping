import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Choose the URL to scrape
url = "http://books.toscrape.com/"

# Step 2: Send a request to the website
response = requests.get(url)

# Step 3: Check if website loaded successfully
if response.status_code == 200:
    print("Website accessed successfully!")
else:
    print("Failed to access website. Error code:", response.status_code)

# Step 4: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Find all the books on the page
books = soup.find_all("article", class_="product_pod")

# Step 6: Create empty lists to store data
titles = []
prices = []

# Step 7: Loop through each book and extract title and price
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    titles.append(title)
    prices.append(price)

# Step 8: Create a DataFrame (table) using pandas
data = pd.DataFrame({
    "Book Title": titles,
    "Price": prices
})

# Step 9: Save the data to a CSV file
data.to_csv("books.csv", index=False)

print("Scraping completed successfully!")
print("Data saved to 'books.csv'")
