import re
import string
import json

file = open("content.txt", "r", encoding="utf-8")

content = {}
b = 0

for line in file.readlines():

    if 'Tick' in line:
        title = line.split(' (')[0]
        content[title] = []
        n = 1
        b += 1
    else:
        x = re.findall('\(\d\)', line)
        if x:
            point = re.sub('\(\d\)', '', line)
            
            point = point.split('-')[-1] if '-' in point else point.split('–')[-1]
            point=point.encode('utf-8','ignore').decode("utf-8")
            printable = set(string.printable)
            point = ''.join(filter(lambda x: x in printable, point))

            content[title].append(f"{b}.{n} {point.strip()}")
            n += 1  

for i in content['Evaluation']:
    print(i)
# f = open("content.json", "w", encoding="utf-8")
# json.dump(content, f, ensure_ascii=False, indent=4)

