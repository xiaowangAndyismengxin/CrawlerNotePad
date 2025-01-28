from bs4 import BeautifulSoup


with open('../example_web.html') as f:
    soup = BeautifulSoup(f, 'lxml')
print(type(soup), str(soup)[:50], '......\n')
print(type(soup.prettify()), soup.prettify()[:50], '......\n')
print(type(soup.title), soup.title)
print(type(soup.title.string), soup.title.string)
