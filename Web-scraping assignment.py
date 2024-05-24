#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[23]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/list/ls056092300/'

response = requests.get(url)
response


# In[24]:


soup = BeautifulSoup(response.content,'html.parser')


# In[25]:


top_rated_movies = soup.find_all('div', class_='sc-74bf520e-3 klvfeN dli-parent')

names = []
ratings = []
year_of_release = []

for movie in top_rated_movies:
    name = movie.h3.a.text
    rating = movie.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text
    year = movie.find('span', class_='sc-b189961a-8 kLaxqf dli-title-metadata-item').text.strip('()')
    
    names.append(name)
    ratings.append(rating)
    year_of_release.append(year)

data = {'Name': names, 'Rating': ratings, 'Year of Release': year_of_release}
df = pd.DataFrame(data)

print(df)


# In[26]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.patreon.com/coreyms'

response = requests.get(url)
response


# In[21]:


import requests
from bs4 import BeautifulSoup

def scrape_patreon_posts(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    posts = []

    
    for post in soup.find_all('div', class_='sc-1s2c40n-0 bPqvTx'):
        heading = post.find('h2').text if post.find('h2') else 'N/A'
        date = post.find('time').text if post.find('time') else 'N/A'
        content = post.find('div', class_='sc-1sab0l6-0 hyjBiD').text if post.find('div', class_='sc-1sab0l6-0 hyjBiD') else 'N/A'
        likes = post.find('div', class_='sc-18u9deh-2 iXKwIz').text if post.find('div', class_='sc-18u9deh-2 iXKwIz') else 'N/A'
        
        youtube_link = 'N/A'
        for a_tag in post.find_all('a', href=True):
            if 'youtube.com' in a_tag['href']:
                youtube_link = a_tag['href']
                break
        
        posts.append({
            'heading': heading,
            'date': date,
            'content': content,
            'likes': likes,
            'youtube_link': youtube_link
        })

    return posts

def main():
    url = 'https://www.patreon.com/coreyms'
    print(f"Fetching details from {url}...")
    posts = scrape_patreon_posts(url)
    
    if posts:
        for post in posts:
            print(f"Heading: {post['heading']}")
            print(f"Date: {post['date']}")
            print(f"Content: {post['content']}")
            print(f"Likes: {post['likes']}")
            print(f"YouTube Link: {post['youtube_link']}")
            print("-" * 80)
    else:
        print("No posts found or failed to scrape the page.")

if __name__ == "__main__":
    main()


# In[28]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nobroker.in/'

response = requests.get(url)
response


# In[12]:


import requests
from bs4 import BeautifulSoup

def get_house_details(url, locality):
    response = requests.get(url, params={'searchParam': locality})
    if response.status_code != 200:
        print(f"Failed to retrieve data for {locality}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    house_list = []

    for listing in soup.find_all('div', class_='card'):
        title = listing.find('h2', class_='heading-6').text.strip() if listing.find('h2', class_='heading-6') else 'N/A'
        location = listing.find('div', class_='nb__1EwQz').text.strip() if listing.find('div', class_='nb__1EwQz') else 'N/A'
        area = listing.find('div', class_='nb__3oNyC').text.strip() if listing.find('div', class_='nb__3oNyC') else 'N/A'
        emi = listing.find('div', class_='nb__K_Q1p').text.strip() if listing.find('div', class_='nb__K_Q1p') else 'N/A'
        price = listing.find('div', class_='nb__3SxoM').text.strip() if listing.find('div', class_='nb__3SxoM') else 'N/A'
        
        house_list.append({
            'title': title,
            'location': location,
            'area': area,
            'emi': emi,
            'price': price
        })
    
    return house_list

def main():
    base_url = 'https://www.nobroker.in/property/sale'
    localities = ['Indira Nagar', 'Jayanagar', 'Rajaji Nagar']

    for locality in localities:
        print(f"Fetching details for {locality}...")
        houses = get_house_details(base_url, locality)
        if houses:
            for house in houses:
                print(house)
        else:
            print(f"No houses found for {locality}")

if __name__ == "__main__":
    main()


# In[30]:


import requests
from bs4 import BeautifulSoup

url = "https://www.bewakoof.com/bestseller?sort=popular"

response = requests.get(url)

response


# In[11]:


import requests
from bs4 import BeautifulSoup

url = "https://www.bewakoof.com/bestseller?sort=popular"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', class_='productCardBox')[:10]

product_details = []

for product in products:
    name = product.find('h3').text.strip()
    price = product.find('span', class_='discountedPriceText')
    image_url = product.find('img')['src']

    product_details.append({
        'name': name,
        'price': price,
        'image_url': image_url
    })

for detail in product_details:
    print(detail)


# In[5]:


import requests
from bs4 import BeautifulSoup

url = "https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

   
articles = soup.find_all('div', class_='article-item')

for article in articles:
      
        title = article.find('h2').get_text(strip=True)
        date = article.find('span', class_='date').get_text(strip=True)
        authors = article.find('div', class_='authors').get_text(strip=True)

        print(f"Title: {title}")
        print(f"Date: {date}")
        print(f"Authors: {authors}")
        print("-" * 80)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


# In[2]:


import requests
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/world/?region=world"


response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='Card-standardBreakerCard')


for article in articles:
  
    heading = article.find('a', class_='Card-title').get_text(strip=True)

  
    date = article.find('time', class_='Card-time')
    if date:
        date = date.get_text(strip=True)
    else:
        date = "No date available"

  
    news_link = article.find('a', class_='Card-title')['href']

 
    print(f"Heading: {heading}")
    print(f"Date: {date}")
    print(f"News Link: {news_link}")
    print("-" * 40)


# In[ ]:




