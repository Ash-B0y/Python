import requests
import urllib
from bs4 import BeautifulSoup

result = requests.get("https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/")
print(result.status_code)

