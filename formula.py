from bs4 import BeautifulSoup
import requests, json, time

all_data = []
category_titles = []
formula_links = []
time.sleep(2)

url="https://www.sacredlotus.com/go/chinese-formulas/category/all"
print("scraping!",url)

formula_page = requests.get(url)

page_html = formula_page.text

soup = BeautifulSoup(page_html, "html.parser")

all_titles = soup.find_all("h3")

for a_title in all_titles:

    the_title = a_title.text

    data={}
    data['title'] = the_title
    data['formulas'] = []

    title_of_formula = a_title.nextSibling.nextSibling.find_all('li')

    for all_li in title_of_formula:
        #print (all_li.text)
        print('--------------\n')
        li_titles = all_li.text
        link_of_formula = all_li.find('a')
        pinyin = link_of_formula.text
        the_link_href = link_of_formula['href']
#
        detail={}
        detail['titles'] = li_titles
        detail['pinyin'] = pinyin
        detail['formula_link'] = the_link_href

        data['formulas'].append(detail)

    all_data.append(data)

json.dump(all_data,open('title.json', 'w'),indent=2)
