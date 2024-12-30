import sqlite3
import json

# Conexión a la base de datos SQLite
connection = sqlite3.connect('rvr1960.sqlite')
cursor = connection.cursor()

# Consulta SQL para unir las tablas y obtener los datos necesarios
query = """
SELECT
    verse.id AS verse_id,
    verse.book_id,
    book.testament_id,
    testament.name AS testament_name,
    book.name AS book_name,
    book.abbreviation,
    verse.chapter,
    verse.verse,
    verse.text
FROM
    verse
JOIN
    book ON verse.book_id = book.id
JOIN
    testament ON book.testament_id = testament.id
"""

cursor.execute(query)
data = cursor.fetchall()

# Nombres de las columnas
columns = [
    "verse_id",
    "book_id",
    "testament_id",
    "testament_name",
    "book_name",
    "abbreviation",
    "chapter",
    "verse",
    "text"
]

# Convertir los datos a una lista de diccionarios
result = [dict(zip(columns, row)) for row in data]

# Guardar el resultado en un archivo JSON
with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, ensure_ascii=False, separators=(',', ':'))

# Cerrar la conexión a la base de datos
connection.close()

print("Datos convertidos y guardados en 'output.json'.")
