import socket
from bs4 import BeautifulSoup
import requests
import login

url ='https://www.dfb.de/3-liga/spieltagtabelle/?no_cache=1&spieledb_path=%2Fde%2Fcompetitions%2F3-liga%2Fseasons%2F2021-22%2Fmatchday%2Fcurrent'

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

print(soup.prettify())
