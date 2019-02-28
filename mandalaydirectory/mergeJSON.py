import json
import glob, os

print('start merging json')
print(os.curdir)
os.chdir('C:/Users/AC408/PycharmProjects/AxiataScrap/mandalaydirectory/POI_data')
result = []
for f in glob.glob('*.json'):
    print(f)
    try:
        with open(f, 'r') as infile:
            result.append(json.load(infile))
    except:
        print(f + 'is an empty file')

os.chdir('C:/Users/AC408/PycharmProjects/AxiataScrap/mandalaydirectory')
with open('mandalaydir_dd.json', 'w') as outfile:
    json.dump(result, outfile)














print('mergin json end')