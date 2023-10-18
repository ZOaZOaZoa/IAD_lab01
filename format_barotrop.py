import requests
import pandas as pd

fp = open('Barotrop.csv', 'r')
data = fp.read()
fp.close()

Barotrop = {'BARO':'0', 'TROP': '1'}
for barotrop in Barotrop:
    data = data.replace(barotrop, Barotrop[barotrop])

fp = open('Barotrop_formatted.csv', 'w')
fp.write(data)
fp.close()
