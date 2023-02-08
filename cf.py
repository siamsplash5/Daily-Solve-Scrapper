import datetime

import requests
from bs4 import BeautifulSoup

username = input('Enter your handle: ')
url = 'https://codeforces.com/submissions/' + username
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
submission_data = soup.find_all('tr')
submission_data.pop(0)  # deleting the table head
submission_data.pop(len(submission_data) - 1)
submit = 0
solve = 0
today = datetime.datetime.today()

for column in submission_data:
    words = column.text.split()
    if 1 <= len(words):
        date_obj = datetime.datetime.strptime(words[1] + ' ' + words[2], '%b/%d/%Y %H:%M')
        date_obj = date_obj + datetime.timedelta(hours=3)
        if today.date() == date_obj.date():
            submit += 1
            if words[-5] == 'Accepted':
                solve += 1

print('------------------Codeforces--------------------')
print('Username:', username)
print('Date:', today.date())
print('Total Submission:', submit)
print('Total Solved:', solve)
