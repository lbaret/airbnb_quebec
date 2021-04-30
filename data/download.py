"""
Ce fichier a pour but de télécharger et extraire les données (en cas de mise à jour)
"""
from config import AIRBNB_FILES
import requests
import os
import argparse

EXAMPLE_URL = 'http://data.insideairbnb.com/canada/qc/quebec-city/2021-04-11/data/calendar.csv.gz'
ROOT_URL = 'http://data.insideairbnb.com/canada/qc/quebec-city'
END_DIR = 'download'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date', type=str, required=True, help='Date compiled (see http://insideairbnb.com/get-the-data.html) --> FORMAT : YYYY-MM-DD')
    args = parser.parse_args()
    date = args.date

    # URL générales
    END_DATA_URL = os.path.join(ROOT_URL, date, 'data')
    END_VIS_URL = os.path.join(ROOT_URL, date, 'visualisations')

    # Téléchargement des données
    ## data
    for name in AIRBNB_FILES['data']:
        r = requests.get(os.path.join(END_DATA_URL, name), headers=headers, stream=True)
        name = name.replace('.csv.gz', '')
        name += '_data.csv'
        with open(name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)

    ## visualisations
    for name in AIRBNB_FILES['visualisations']:
        r = requests.get(os.path.join(END_DATA_URL, name), headers=headers, stream=True)
        with open(name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
