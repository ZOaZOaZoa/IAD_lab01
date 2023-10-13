import requests
import pandas as pd

url = 'http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights'
html = requests.get(url).content
df_list = pd.read_html(html)
print(df_list)
print(len(df_list))
df = df_list[1]
df.to_csv('dataset.csv')