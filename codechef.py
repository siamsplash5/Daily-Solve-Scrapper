from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.codechef.com/users/siamsplash5').text
soup = BeautifulSoup(html_text, 'lxml')
print(soup.prettify())
submission = soup.find_all('span', class_='tooltiptext')
for column in submission:
    print(column.text)
