import csv
import requests
from parser_data.AppData import App
from bs4 import BeautifulSoup as soup
from parser_data.parser import obtener_datos_aplicacion


BASE_URL = "https://play.google.com"


urls = [
    "https://play.google.com/store/apps/category/GAME?hl=en",
    "https://play.google.com/store/apps/top/category/GAME?hl=en",
    "https://play.google.com/store/apps/new/category/GAME?hl=en",
    "https://play.google.com/store/apps/category/GAME_ACTION",
    "https://play.google.com/store/apps/category/GAME_ADVENTURE",
    "https://play.google.com/store/apps/category/GAME_ARCADE",
    "https://play.google.com/store/apps/category/GAME_BOARD",
    "https://play.google.com/store/apps/category/GAME_CARD",
    "https://play.google.com/store/apps/category/GAME_CASINO",
    "https://play.google.com/store/apps/category/GAME_CASUAL",
    "https://play.google.com/store/apps/category/GAME_EDUCATIONAL",
    "https://play.google.com/store/apps/category/GAME_MUSIC",
    "https://play.google.com/store/apps/category/GAME_PUZZLE",
    "https://play.google.com/store/apps/category/GAME_RACING",
    "https://play.google.com/store/apps/category/GAME_ROLE_PLAYING",
    "https://play.google.com/store/apps/category/GAME_SIMULATION",
    "https://play.google.com/store/apps/category/GAME_SPORTS",
    "https://play.google.com/store/apps/category/GAME_STRATEGY",
    "https://play.google.com/store/apps/category/GAME_TRIVIA",
    "https://play.google.com/store/apps/category/GAME_WORD"
]

cantidad_aplicaciones = 0
aplicaciones_no_revisadas = 0
apps_enlace_problema = []

with open('listaCompletaGooglePlay.csv', 'w', newline="", encoding="utf-8") as f:
    columnas = App.obtener_header()
    writer = csv.DictWriter(f, fieldnames=columnas, delimiter="\t")
    writer.writeheader()

    for url_categoria in urls:

        # Es la pantalla de Recommended, based on your activity, etc, muchas filas de recomendaciones
        html_principal = requests.get(url_categoria)
        html_principal_soup = soup(html_principal.text, "html.parser")

        cajas_recomendaciones = html_principal_soup.findAll('div', attrs={'class': 'xwY9Zc'})

        for caja_recomendacion in cajas_recomendaciones:

            url = BASE_URL + caja_recomendacion.a['href']

            html_pagina_apps = requests.get(url)
            html_soup_apps = soup(html_pagina_apps.text, "html.parser")
            contenedores = html_soup_apps.findAll('a', attrs={'class': 'poRVub'})
            print(len(contenedores))

            for contenedor_app in contenedores:

                enlace_detalle_app = BASE_URL + contenedor_app["href"]
                data = requests.get(enlace_detalle_app)
                data_soup = soup(data.text, 'html.parser')
                app_data = obtener_datos_aplicacion(enlace_detalle_app, data_soup)

                if app_data != None:
                    cantidad_aplicaciones += 1
                    writer.writerow(app_data.obtener_fila_diccionario())
                else:
                    aplicaciones_no_revisadas += 1
                    apps_enlace_problema.append(enlace_detalle_app)

                # print(list(app_data.metadata.keys()))
                # print(app_data.metadata["name"])
                # print(app_data.__str__())

            # break

        # break

print("Aplicaciones recolectadas: ", cantidad_aplicaciones)
print("aplicaciones_no_revisadas: ", aplicaciones_no_revisadas)
print("Enlaces no revisados: ", apps_enlace_problema)
