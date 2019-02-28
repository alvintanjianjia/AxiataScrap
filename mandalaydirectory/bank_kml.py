import csv
import xml.etree.ElementTree as et

doc = et.parse('AYA_Location.kml')
nmsp = '{http://www.opengis.net/kml/2.2}'
mainArray = []
finalArray = []
for pm in doc.iterfind('.//{0}Placemark'.format(nmsp)):
    print(pm.find('{0}name'.format(nmsp)).text)
    mainArray.append(pm.find('{0}name'.format(nmsp)).text)
    for ls in pm.iterfind('{0}ExtendedData/{0}Data/{0}value'.format(nmsp)):
        item = ls.text.strip().replace('\n', '')
        mainArray.append(item)


print(len(mainArray)//7)

counter = 7
for i in range(len(mainArray)//7):
    name = mainArray[counter*i]
    no = mainArray[counter*i + 1]
    address = mainArray[counter * i + 2]
    country = mainArray[counter * i + 3]
    latitude = mainArray[counter * i + 4]
    longitude = mainArray[counter * i + 5]
    primaryPhone = (mainArray[counter * i + 6]).split('/')[0]
    finalArray.append([name, 'Bank', address, '', '', primaryPhone, latitude, longitude])

    print(i, counter , 'i and counter')

with open('yangon&mandalayraw.csv', 'a', encoding='utf8', newline='') as csvFile:
    writer = csv.writer(csvFile)

    for element in finalArray:
        print(element)
        writer.writerow(element)
print(len(mainArray))



# root = doc.getroot()
# print(root, 'root')
# elements = doc.findall('{http://www.opengis.net/kml/2.2}kmlPlacement')
# print(elements, 'elements')
#
# for item in elements:
#     print(item, 'elements')
# for pm in doc.iterfind('{0}Placemark'):
#     print(pm.find('{0}name'.text))



