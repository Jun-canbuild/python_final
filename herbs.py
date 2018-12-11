from bs4 import BeautifulSoup
import requests, json, time

with open ('title.json') as formula_titles:
    #text = json.loads(formula_titles)
    loadData = json.load(formula_titles)
    # print ('-------')
    # print ('first object\'s formulas')
    # print (loadData[0]['formulas'][0]['formula_link'])
    # print ('-------')
    #
    # print ('------')
    # print (loadData[1]['formulas'][0]['formula_link'])
    # print ('------')
    # print (loadData[1]['formulas'][1]['formula_link'])
    # print ('------')
    # print (loadData[1]['formulas'][2]['formula_link'])


    for all in loadData:
        formulas = all['formulas']

        for urlextension in formulas:
            formula_link = urlextension['formula_link']
            final_url = "https://www.sacredlotus.com" + formula_link

            herb_page = requests.get(final_url)

            page_html = herb_page.text

            soup = BeautifulSoup(page_html, "html.parser")

            all_herbs = soup.find_all("div", attrs={"class":"tcm-content"})

            #all_name = soup.find_all(string = "Quantity")

            time.sleep(0.25)

            print(all_herbs)
            # for a_herb in all_herbs:
            #
            #     the_herb = a_herb.text
            #
            #     print(the_herb)










    # print (loadData[0][0])
#     for url in formula_titles:
#         print(url)
#
#         x = json.loads(url)
#         print(x)

# x = json.load(title)
# print(x)

# all_data = []
# quantity_each = []
# channel = []
# property = []
# time.sleep(2)
#
# formula = json.load(formula.json)
#
# for url in formula['formula_link']:
#     url = "https://www.sacredlotus.com + "
#     print("Scraping!",url)
#     herb_page = requests.get(url)
#
#     page_html = herb_page.text
#     soup = BeautifulSoup(page_html, "html.parser")
