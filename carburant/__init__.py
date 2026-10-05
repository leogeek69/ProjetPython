import requests
import pandas as pd
from rich.console import Console
from pathlib import Path
import json

response = requests.get('https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/exports/json')
if response.status_code == 200:
    data = response.json()
    json.dump(data,Path("fichier_complet.json").open('w'))
else:
    print("Erreur :", response.status_code)  

response = requests.get('https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/exports/json')
if response.status_code == 200:
    data = response.json()
    
    # Filtrer : garder seulement les clés voulues dans chaque ligne
    cols_voulues = ["id", "cp","id","adresse","ville","cp", "gazole_prix" ,"sp95_prix" ,"e85_prix", "gplc_prix", "e10_prix", " sp98_prix", "carburants_disponibles", "carburants_indisponibles"]
    data_filtree = [{k: row[k] for k in cols_voulues if k in row} for row in data]
    
    json.dump(data_filtree, Path("fichier.json").open('w'))
else:
    print("Erreur :", response.status_code)