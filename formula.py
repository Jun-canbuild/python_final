# This script collect all data from https://www.sacredlotus.com/ that are necessary to create the visualization for the final project
# This script scraps data from sacredlotus.com webpages and output data in a .json file
# Then it turns .json to .csv, which is the proper data format that Gephi accept to create the visualization


# The next script will use json.load and use this as a variable to get herb data from each url,
# use a for loop to get all the herbs from each formula url, then use another for loop inside the last for loop to get thru each url and parse all data into one .json file



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

    #category_titles.append(the_title)
    #print(a_title)

    title_of_formula = a_title.nextSibling.nextSibling.find_all('li')
    print (a_title)
    print (a_title.nextSibling)
    print (a_title.nextSibling.nextSibling)

#     for all_li in title_of_formula:
#         #print (all_li.text)
#         print('--------------\n')
#         li_titles = all_li.text
#         link_of_formula = all_li.find('a')
#         pinyin = link_of_formula.text
#         the_link_href = link_of_formula['href']
#
#
#
#
#         print(li_titles, pinyin, the_link_href)
#
#         detail={}
#         detail['titles'] = li_titles
#         detail['pinyin'] = pinyin
#         detail['formula_link'] = the_link_href
#
#         data['formulas'].append(detail)
#
#     all_data.append(data)
#
#
#
#
# json.dump(all_data,open('title.json', 'w'),indent=2)
#



#print (category_titles)


# all_links = soup.find_all("ul", attrs={'class':'list-category std-radius'})
#
# for titlelink in all_links:
#     for_li = titlelink.find_all("li")
#     for a_li in for_li:
#         the_a_link = a_titlelink.find("a")
#
#
#         formula_links.append(the_a_link)
# print (the_a_link)

#json.dump(formula_titles,open('title.json', 'w'),indent=2)
