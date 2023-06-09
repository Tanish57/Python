import requests
from bs4 import BeautifulSoup

url = 'https://www.justdial.com/Mumbai/Uv-Flatbed-Printing-Services/nct-10943884'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
printer_titles = []
h2_tags = soup.find_all('h2')
for h2 in h2_tags:
    printer_titles.append(h2.text)
