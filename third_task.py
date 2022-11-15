import re
import time

def json_to_xml(read_file, write_file):
    amount_of_tabs = 0
    write_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
    tg_array = []
    multiple_tg = ''
    for line in read_file:
        s = line.rstrip()
        s = re.sub(" ", "", s)
        s = re.sub('\"', '', s)

        if re.match('^{', s):
            if multiple_tg != '':
                write_file.write('    ' * amount_of_tabs + '<' + multiple_tg + '>\n')
                amount_of_tabs += 1
            continue

        if re.match('^}', s):
            if multiple_tg != '':
                amount_of_tabs -= 1
                write_file.write('    ' * amount_of_tabs + '</' + multiple_tg + '>\n')
                continue
            if tg_array != []:
                amount_of_tabs -= 1
                write_file.write('    ' * amount_of_tabs + '</' + tg_array[len(tg_array) - 1] + '>\n')
                tg_array = tg_array[:len(tg_array) - 1]
            continue

        if re.match('^]', s):
            multiple_tg = ''

        if re.match('.$', s):
            s = s[:len(s) - 1]
        s = s.split(':')
        if len(s) > 2:
            s[1] = s[1] + ":" + s[2] + ":" + s[3]
            s = s[0:2]
        if len(s) < 2:
            continue
        if re.match('{', s[1]):
            write_file.write('    ' * amount_of_tabs + '<' + s[0] + '>\n')
            tg_array.append(s[0])
            amount_of_tabs += 1
            continue
        if re.match('\[', s[1]):
            multiple_tg = s[0]
            continue
        write_file.write('    ' * amount_of_tabs + '<' + s[0] + '>' + s[1] + '</' + s[0] + '>\n')


start = time.time()
for i in range(100):
    read_file = open('Vtornik_json', "r", encoding="utf8")
    write_file = open('Vtornik_xml', "w", encoding="utf8")
    json_to_xml(read_file, write_file)
    read_file.close()
    write_file.close()
print(time.time() - start)