import os
import json


# os.system("cd C:/Users/AC408/PycharmProjects/AxiataScrap/mandalaydirectory")
# os.system("scrapy crawl categories -o test_mandalaydirectory.json -t json")


with open('list_of_mandalayCategories.json', 'r') as file:
    categories_extension = json.load(file)

for element in categories_extension:
    # print(element['Name'])
    element = element['Name']
    os.system("cd C:/Users/AC408/PycharmProjects/AxiataScrap/mandalaydirectory")
    category = element.split('/')
    category = category[-1]
    category = category.split('.')
    category = category[0]
    string_argument = 'http://www.mandalaydirectory.com' + element
    string_argument = "scrapy crawl categories -o " + category + '.json' + ' -t json -a start_url=' + string_argument
    print(string_argument)
    os.system(string_argument)
    # os.system("scrapy crawl categories -o test_mandalaydirectory.json -t json -a start_url=''")

print("just kidding kmn")