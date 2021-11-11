import requests
from bs4 import BeautifulSoup
import re

print("入力してちょ")
html_doc = input()
soup = BeautifulSoup(html_doc, 'html.parser')  # BeautifulSoupの初期化

real_page_tags = soup.find("a")

print("")
print("============================================")
print("")
print(real_page_tags.get("href"))

print("終了したい場合はクリックしてください")
input()
