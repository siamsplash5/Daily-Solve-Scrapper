from bs4 import BeautifulSoup

# turn the html file into object
with open('home.html', 'r') as html_file:
    # from object file, read the content of the file
    content = html_file.read()
    # create an instance soup
    # lxml is a parser method
    soup = BeautifulSoup(content, 'lxml')
    # prettify() used to format the html file code
    tags = soup.find_all('h3')
    for x in tags:
        print(x.text)
