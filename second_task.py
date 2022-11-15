import json
import time
from dict2xml import dict2xml

start = time.time()
for i in range(100):
    read_file = open('Vtornik_json', "r", encoding="utf8")
    write_file = open('Vtornik_xml', "w", encoding="utf8")
    text = json.load(read_file)
    xml = dict2xml(text)
    write_file.write(xml)
    read_file.close()
    write_file.close()
print(time.time() - start)