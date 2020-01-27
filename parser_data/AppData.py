import json

class App:

    def __init__(self, nombre, precio, descripcion, calificacion_contenido, categoria, calificacion_aplicacion,
                 numero_reviews, url, fecha_actualizacion, tamanio, instalaciones, minima_version_android,
                 ultima_version, purchase, metadata):

        self.nombre = nombre
        self.precio = float(precio.replace("$", ""))
        self.descripcion = descripcion.replace("\n", ". ").replace(";", "  ")
        self.calificacion_contenido = calificacion_contenido
        self.categoria = categoria
        self.calificacion_aplicacion = calificacion_aplicacion
        self.numero_reviews = numero_reviews
        self.url = url
        self.fecha_actualizacion = fecha_actualizacion


        if tamanio == "Varies with device":
            self.tamanio = -1
        elif tamanio[-1] == "M":
            self.tamanio = float(tamanio.replace("M", ""))
        elif tamanio[-1] == "k":
            self.tamanio = float(tamanio.replace("k", "")) / 1024
        else:
            print("No conversión para: " + self.tamanio)
            self.tamanio = tamanio

        self.instalaciones = instalaciones

        if minima_version_android == "Varies with device":
            self.minima_version_android = -1
        else:
            self.minima_version_android = float(minima_version_android.replace("and up", "")[0:3])





        self.ultima_version = ultima_version


        if purchase == None:
            self.purchase_inicial = 0
            self.purchase_final = 0
        elif purchase.__contains__("per item"):
            # $0.99 - $104.99 per item
            texto = purchase.replace("$", "").replace("per item", "").split("-")

            if len(texto) == 2:
                self.purchase_inicial = float(texto[0])
                self.purchase_final = float(texto[1])
            elif len(texto) == 1:
                self.purchase_inicial = float(texto[0])
                self.purchase_final = float(texto[0])
            else:
                print("No se pudo convertir: " + purchase)

                self.purchase_inicial = 0
                self.purchase_final = 0
        else:
            print("No se pudo convertir: " + purchase)

            self.purchase_inicial = 0
            self.purchase_final = 0


        self.metadata = json.loads(metadata)
        del self.metadata["description"]

    @staticmethod
    def obtener_header():
        return ['nombre', 'precio', 'calificacion_contenido', 'categoria',
                'calificacion_aplicacion', 'numero_reviews', 'url', 'fecha_actualizacion', 'tamanio_(MB)',
                'instalaciones', 'minima_version_android',
                 'ultima_version', 'purchase_from', 'purchase_to', 'metadata', 'descripcion']


    def obtener_fila(self):
        return [self.nombre, self.precio, self.calificacion_contenido, self.categoria,
                self.calificacion_aplicacion,
                 self.numero_reviews, self.url, self.fecha_actualizacion, self.tamanio, self.instalaciones,
                self.minima_version_android,
                 self.ultima_version, self.purchase_inicial, self.purchase_final, self.metadata, self.descripcion]

    def obtener_fila_diccionario(self):
        return {'nombre': self.nombre, 'precio': self.precio,
                'calificacion_contenido': self.calificacion_contenido, 'categoria': self.categoria,
                'calificacion_aplicacion': self.calificacion_aplicacion, 'numero_reviews': self.numero_reviews,
                'url':  self.url, 'fecha_actualizacion': self.fecha_actualizacion, 'tamanio_(MB)': self.tamanio,
                'instalaciones': self.instalaciones, 'minima_version_android': self.minima_version_android,
                 'ultima_version': self.ultima_version, 'purchase_from': self.purchase_inicial, 'purchase_to': self.purchase_final, 'metadata': str(self.metadata), 'descripcion': self.descripcion}

    def __str__(self):
        salida = ""
        salida += "\n\nApp nombre: " + str(self.nombre)
        salida += "\nPrecio: " + str(self.precio)
        salida += "\nDescripcion: " + str(self.descripcion)
        salida += "\nCalificación contenido: " + str(self.calificacion_contenido)
        salida += "\nCategoria: " + str(self.categoria)
        salida += "\nCalificación aplicación: " + str(self.calificacion_aplicacion)
        salida += "\nNúmero de reviews: " + str(self.numero_reviews)
        salida += "\nUrl: " + str(self.url)
        salida += "\nÚltima actualización: " + str(self.fecha_actualizacion)
        salida += "\nTamaño: " + str(self.tamanio)
        salida += "\nInstalaciones: " + str(self.instalaciones)
        salida += "\nVersión mínima: " + str(self.minima_version_android)
        salida += "\nÚltima versión: " + str(self.ultima_version)
        salida += "\nCompras integradas: " + str(self.purchase)
        salida += "\nMetadata: " + str(self.metadata)

        return salida







