from .AppData import App


def obtener_datos_aplicacion(url, data_soup):

    try:

        nombre = data_soup.find('h1', attrs={'itemprop': 'name'}).span.text
        precio = data_soup.find('meta', attrs={'itemprop': 'price'})['content']
        descripcion = data_soup.find('meta', attrs={'itemprop': 'description'})
        calificacion_contenido = data_soup.find('div', attrs={'class': 'KmO8jd'}).text
        categoria = data_soup.find('a', attrs={'itemprop': 'genre'}).text
        calificacion_aplicacion = data_soup.find('div', attrs={'class': 'BHMmbe'}).text
        reviews = data_soup.find('span', attrs={'class': 'EymY4b'}).find('span', attrs={'class': ''}).text
        json_extra = data_soup.find('script', attrs={'type': 'application/ld+json'}).text

        actualizacion = None
        tamanio = None
        numero_instalaciones = None
        version_minima = None
        version_actual = None
        compras = None

        info_box = [info_box.text.strip() for info_box in data_soup.find_all('div', 'hAyfc')]
        for item in info_box:

            if item.startswith("Updated"):
                actualizacion = str(item[7:])
            if item.startswith("Size"):
                tamanio = str(item[4:])
            if item.startswith("Installs"):
                numero_instalaciones = str(item[8:])
            if item.startswith("Requires Android"):
                version_minima = str(item[16:])
            if item.startswith("Current Version"):
                version_actual = str(item[15:])
            if item.startswith("In-app Products"):
                compras = str(item[15:])

        return App(nombre, precio, descripcion['content'], calificacion_contenido, categoria, float(calificacion_aplicacion),
                   int(reviews.replace(",", "")), url, actualizacion, tamanio, int(numero_instalaciones.replace("+", "").replace(",", "")),
                   version_minima, version_actual, compras, json_extra)

    except:
        print("Error con: " + url)
        return None
