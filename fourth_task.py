import pandas as pd

read_file = open('Vtornik_json', encoding='utf8')
df = pd.read_json(read_file)
df.to_csv('Vtornik.csv', encoding='cp1251', index=True)