import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')

netflix_data = {}
netflix_data["Date"] = None
netflix_data["Open"] = None
netflix_data["High"] = None
netflix_data["Low"] = None
netflix_data["Close"] = None
netflix_data["Volume"] = None
for row in soup.find('tbody').find_all('tr'):
    col= row.find_all('td')
    date = col[0].text
    open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
netflix_data["Date"]= date
netflix_data["Open"]= open
netflix_data["High"]= high
netflix_data["Low"]= low
netflix_data["Close:"]=close
netflix_data["Volume"]= volume
df_netflix = pd.DataFrame(netflix_data, index= range(len(netflix_data["Date"])))
print(df_netflix.head())