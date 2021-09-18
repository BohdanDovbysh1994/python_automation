from requests import get
from bs4 import BeautifulSoup, ResultSet

response = get("https://online.ithillel.ua/courses/qa-automation-python?gclid=Cj0KCQjwnJaKBhDgARIsAHmvz6dytRx420Wgp5r4o7dNi_xXT2bfE1Kw4PDA7P5dyvnsnKRIKsy_FVkaAtPtEALw_wcB")

soup = BeautifulSoup(response.content, "html.parser")
block_elements: ResultSet = soup.find_all("div", class_="programme-collapsible_header")
theme_elements: ResultSet = soup.find_all("div", class_="programme-collapsible_container")

themes = dict()

for block in block_elements:
    themes[block.contents[0].strip()] = []

block_names = list(themes.keys())

counter = 0
for theme in theme_elements:

    for block_themes in theme.contents[1].contents[1]:
        themes[block_names[counter]].append(block_themes.contents[0])

    counter += 1

print(themes)