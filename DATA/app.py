#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  app.py
#  
#  Copyright 2022 Agustin Bassi <[AT]aguztynbassi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
from flask import Flask, render_template, request
import json
from prettytable import PrettyTable

app = Flask(__name__)

def buscar_por_id_attck(data, attck_id):
    resultados = []
    for entrada in data:
        if "ATT&CK_ID" in entrada and attck_id in entrada["ATT&CK_ID"]:
            resultados.append(entrada)
    return resultados

def buscar_por_categoria_attck(data, categoria):
    resultados = []
    for entrada in data:
        if "ATT&CK_Category" in entrada and categoria in entrada["ATT&CK_Category"]:
            resultados.append(entrada)
    return resultados

def imprimir_resultados(resultados):
    if resultados:
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Name", "Trigger Condition", "ATT&CK ID", "Minimum Log Source Requirement", "Query"]

        for resultado in resultados:
            tabla.add_row([
                resultado.get("ID", ""),
                resultado.get("Name", ""),
                resultado.get("Trigger_Condition", ""),
                ", ".join(resultado.get("ATT&CK_ID", [])),
                ", ".join(resultado.get("Minimum_Log_Source_Requirement", [])),
                resultado.get("Query", "")
            ])

        return tabla.get_html_string()
    else:
        return "No se encontraron resultados."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    archivo_json = 'Rules.json'  # Cambia esto a la ruta correcta
    attck_id = request.form.get('attck_id')
    categoria = request.form.get('categoria')

    try:
        with open(archivo_json, 'r', encoding='utf-8') as file:
            datos = json.load(file)
    except FileNotFoundError:
        return "El archivo no se encontró."
    except json.JSONDecodeError as e:
        return f"Error al decodificar el JSON: {e}"

    if attck_id:
        resultados = buscar_por_id_attck(datos, attck_id)
    elif categoria:
        resultados = buscar_por_categoria_attck(datos, categoria)
    else:
        return "Debe proporcionar al menos una función de búsqueda."

    tabla_html = imprimir_resultados(resultados)
    return render_template('resultados.html', tabla_html=tabla_html)

if __name__ == '__main__':
    app.run(debug=True)
