

texto = "$0.99 - $104.99 per item".replace("$", "").replace("per item", "").split("-")
inicio = float(texto[0])
fin = float(texto[1])

print(inicio, fin)
