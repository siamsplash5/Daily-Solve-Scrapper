from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://leetcode.com/acmashraf/').text
soup = BeautifulSoup(html_text, 'lxml')
print(soup.prettify())
value = soup.text
words = value.split()
for word in words:
    print(word)
