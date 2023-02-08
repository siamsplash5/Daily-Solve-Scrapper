import datetime

import requests
from bs4 import BeautifulSoup

username = input('Enter your handle: ')
url = 'https://lightoj.com/user/' + username
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
submission_data = soup.find_all('h4')
today = datetime.datetime.today()
solve = 0

for column in submission_data:
    words = column.text.split()
    if len(words) == 3:
        if words[1] == 'seconds' or words[1] == 'minutes' or words[1] == 'hours':
            solve += 1

print('Username:', username)
print('LightOJ Solve', solve)
