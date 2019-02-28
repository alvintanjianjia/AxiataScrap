import json
import glob, os
from itemClass import mandalayItem
import csv


# ----------merging both csv---------------
poi_dict = {}
with open('mandalay_dir.csv', 'r', encoding='utf8', newline='') as csvFile1:
    reader = csv.reader(csvFile1)
    next(reader, None)
    counter = 0
    for row in reader:
        name = row[0]
        category = row[1]
        address = row[2]
        township = row[3]
        state = row[4]
        phone = row[5]
        latitude = row[6]
        longitude = row[7]
        if len(latitude) == 0 or latitude is None:
            pass
        elif len(longitude) == 0 or longitude is None:
            pass
        elif len(name) == 0 or name is None:
            pass
        key = category + latitude + longitude
        if key in poi_dict:
            pass
        else:
            # print([name, category, address, township, state, phone, latitude, longitude])
            # print(key)
            poi_dict[key] = [name, category, address, township, state, phone, latitude, longitude]

csv_result = []
poi_dict2 = {}
with open('yangondir_dd.csv', encoding='utf8', newline='') as infile2:
    reader = csv.reader(infile2)
    next(reader, None)
    counter = 0
    for row in reader:
        address = row[0]
        category = row[1]
        latitude = row[2]
        longitude = row[3]
        name = row[4]
        state = row[5]
        township = row[6]
        key = category + latitude + longitude
        if key in poi_dict2:
            pass
        else:
            # print([name, category, address, township, state, phone, latitude, longitude])
            # print(key)
            poi_dict2[key] = [name, category, address, township, state, phone, latitude, longitude]
            csv_result.append([name, category, address, township, state, phone, latitude, longitude])




with open('yangon&mandalayraw(uniquelatlong).csv', 'w', encoding='utf8', newline='') as csvFile3:
    writer3 = csv.writer(csvFile3)
    writer3.writerow(['Name', 'Category', 'Address', 'Township', 'State', 'Phone', 'Latitude', 'Longitude'])
    for element in csv_result:
        writer3.writerow(element)
    for item in poi_dict:
        writer3.writerow(poi_dict[item])



print(len(csv_result))
print(len(poi_dict))
print(len(poi_dict2))