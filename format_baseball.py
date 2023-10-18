import requests
import pandas as pd

fp = open('Baseball.csv', 'r')
data = fp.read()
fp.close()

positions = {'Pitcher': '1', 'Catcher': '2', 'Baseman': '3', 'Outfielder': '4', 'Relief_P': '5'}
for pos in positions:
    data = data.replace(pos, positions[pos])

fp = open('Baseball_formatted.csv', 'w')
fp.write(data)
fp.close()
