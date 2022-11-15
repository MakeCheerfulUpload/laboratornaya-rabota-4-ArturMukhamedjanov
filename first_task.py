import time


def json_to_xml(read_file, write_file):
    amount_of_tabs = 0
    write_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
    tg_array = []
    multiple_tg = ''
    for line in read_file:
        s = line.rstrip()
        s = s.lstrip()
        s = s.rstrip()
        if s[len(s) - 1] == ',':
            s = s[:len(s) - 1]
        #Проверка на исправность файла
        if len(s) == 1 and (s != "{" and s != "]" and s != "}" and s != ']'):
            print("JSON файл ошибочен")
            exit(-1)
        if len(s) == '':
            continue
        if len(s) > 1 and s.count(":") == 0:
            print("JSON файл ошибочен")
            exit(0)

        if s == "{":
            if multiple_tg != '':
                write_file.write('    ' * amount_of_tabs + '<' + multiple_tg + '>\n')
                amount_of_tabs += 1
            continue

        if s.count('}'):
            if multiple_tg != '':
                amount_of_tabs -= 1
                write_file.write('    ' * amount_of_tabs + '</' + multiple_tg + '>\n')
                continue
            if tg_array != []:
                amount_of_tabs -= 1
                write_file.write('    ' * amount_of_tabs + '</' + tg_array[len(tg_array) - 1] + '>\n')
                tg_array = tg_array[:len(tg_array) - 1]
            continue

        if s == "]":
            multiple_tg = ''

        if s[len(s) - 1] == ',':
            s = s[:len(s) - 1]
        if len(s) < 2:
            continue
        s = s.split(':')
        if s[0] == "\"time\"":
            s[1] = s[1] + ":" + s[2] + ":" + s[3]
            s = s[0:2]
        s[0] = s[0].lstrip()
        s[0] = s[0].rstrip()
        s[1] = s[1].lstrip()
        s[1] = s[1].rstrip()

        if s[0][0] != '\"' or s[0][len(s[0]) - 1] != '\"':
            print("JSON файл ошибочен")
            exit(0)

        if s[1] == '{':
            write_file.write('    ' * amount_of_tabs + '<' + s[0] + '>\n')
            tg_array.append(s[0].replace('\"', ''))
            amount_of_tabs += 1
            continue
        if s[1] == '[':
            multiple_tg = s[0].replace('\"', '')
            continue
        if s[1][0] != '\"' or s[1][len(s[1]) - 1] != '\"':
            print("JSON файл ошибочен")
            exit(0)
        write_file.write('    ' * amount_of_tabs + '<' + s[0] + '>' + s[1] + '</' + s[0] + '>\n')


start = time.time()
for i in range(100):
    read_file = open('Vtornik_json', "r", encoding="utf8")
    write_file = open('Vtornik_xml', "w", encoding="utf8")
    json_to_xml(read_file, write_file)
    read_file.close()
    write_file.close()
print(time.time() - start)