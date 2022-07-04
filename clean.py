# coding: utf-8
from bs4 import BeautifulSoup
with open("./paul_graham_essay.txt", 'r') as scraped_file:
    html = scraped_file.read()
    
soup = BeautifulSoup(html, "html5lib")
import re
cleaned = [
  t.replace("\n", " ")
  for t in soup.stripped_strings
  if ("Thanks to" not in t) and (not re.match(r"^\W+$", t))
]
with open("./paul_graham_essay_clean.txt", 'w') as cleaned_file:
    for line in cleaned:
        cleaned_file.write(line.strip()); cleaned_file.write("\n")
        
