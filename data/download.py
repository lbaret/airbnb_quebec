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
    for url in AIRBNB_FILES['data']:
        pass

    ## visualisations
    for url in AIRBNB_FILES['visualisations']:
        pass
