import requests
from bs4 import BeautifulSoup

r = requests.get('https://open.kattis.com/problem-sources/2022%20ICPC%20North%20America%20Regional%20Programming%20Contests%20%28February%2025%2C%202023%29')
soup = BeautifulSoup(r.text, 'html.parser')
problems = soup.find_all('tr')
print(len(problems))