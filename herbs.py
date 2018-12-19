from bs4 import BeautifulSoup
import requests, json, time, re

all_data = []
each_formula_herb = []


time.sleep(0.25)

with open ('title.json') as formula_titles:
    loadData = json.load(formula_titles)



    for all in loadData:
        formulas = all['formulas']

        for urlextension in formulas:
            formula_link = urlextension['formula_link']
            final_url = 'https://www.sacredlotus.com' + formula_link
            print('scrapping url:' + final_url);

            herb_page = requests.get(final_url)

            page_html = herb_page.text

            soup = BeautifulSoup(page_html, 'html.parser')

            all_substance_links = soup.find_all('a', href = re.compile(r'/go/chinese-herbs/substance/.*'))


            for link in all_substance_links:


                substance = {}
                substance['name'] = link.text
                substance['link'] = link['href']
                substance['name_english'] = link.next_sibling
                substance['quantity'] = link.next_sibling.next_sibling.next_sibling

                if substance['quantity'] == None:
                    continue
                else:
                    substance['quantity'] = substance['quantity'].replace('Quantity = ','')
                    substance['quantity'] = substance['quantity'].replace('grams','')
                    substance['quantity'] = substance['quantity'].strip()
                    substance['quantity'] = substance['quantity'].split("-")[0]

                row_div = link.next_sibling.next_sibling.next_sibling.next_sibling

                herb_details = row_div.find_all("div", {'class':'herb-detail clearfix'})

                for detail in herb_details:


                    key = detail.find('div',{'class':"herb-detail-left"}).text

                    key = key.replace(' ','_').replace(':','').lower()

                    value = detail.find('div',{'class':"herb-detail-right"}).text

                    substance['key'] = value

                all_data.append(substance)

json.dump(all_data,open('herbs.json', 'w'),indent=2)
