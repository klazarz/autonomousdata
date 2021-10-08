import socket
from bs4 import BeautifulSoup
import requests

url ='https://read.amazon.com/kp/notebook'

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")


print(soup.prettify())
