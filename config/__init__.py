from os.path import join, abspath, dirname

ROOT = abspath(dirname(__name__))

DATA_DIR = join(ROOT, 'data')
ANALYSE_DIR = join(ROOT, 'analyse')
MODEL_DIR = join(ROOT, 'model')

AIRBNB_FILES = {
    'data': [
        'listings.csv.gz',
        'calendar.csv.gz',
        'reviews.csv.gz'
    ],
    'visualisations': [
        'listings.csv',
        'reviews.csv',
        'neighbourhoods.csv',
        'neighbourhoods.geojson'
    ]
}
