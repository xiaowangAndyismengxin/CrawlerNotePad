from bs4 import BeautifulSoup
import re


with open('../../example_web.html') as f:
    soup = BeautifulSoup('f', 'lxml')


print('result: ', result)
