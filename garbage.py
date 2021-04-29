# -*- coding: utf-8 -*-
import requests
import gzip
import shutil
import pandas as pd

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
response = requests.get('http://data.insideairbnb.com/canada/qc/quebec-city/2021-04-11/data/calendar.csv.gz', headers=headers, stream=True)

with open('test.csv', 'wb') as f:
    for chunk in response.iter_content(chunk_size=128):
        f.write(chunk)

my_file = gzip.GzipFile(filename='test.csv')

my_file.read()

# Ok, il faut utiliser un User-Agent pour pouvoir télécharger les données sur Airbnb.


