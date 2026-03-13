import requests
from bs4 import BeautifulSoup as bs
import certifi
from urllib.parse import urljoin

url = 'https://itproger.com/ua'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; uk-UA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

session = requests.Session()
try:
    res = session.get(url, headers=headers, verify=certifi.where())
    if res.status_code == 200:
        soup = bs(res.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'course'})

        for el in divs:
            title = el.find('span', attrs={'class': 'title_course'})
            href = el.find('a')['href']
            if title and href:
                full_url = urljoin(url, href)
                print(f"{title.get_text(strip=True)}: {full_url}")
    else:
        print('Error')
except Exception as e:
    print(e)