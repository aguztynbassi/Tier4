#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  search.py
#  
#  Copyright 2024 Agustin Bassi <[AT]aguztynbassi>
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

# FORMAS DE BUSCAR
#
# python3 search.py Rules.json --id_attck="T1203"
# 
# python3 search.py Rules.json --category_attck="Execution"
#

import json
import argparse
from prettytable import PrettyTable

def id_attck(data, attck_id):
    resultados = []
    for entrada in data:
        if "ATT&CK_ID" in entrada and attck_id in entrada["ATT&CK_ID"]:
            resultados.append(entrada)
    return resultados

def category_attck(data, categoria):
    resultados = []
    for entrada in data:
        if "ATT&CK_Category" in entrada and categoria in entrada["ATT&CK_Category"]:
            resultados.append(entrada)
    return resultados

def show(data, id_buscar):
    for entrada in data:
        if entrada.get("ID") == id_buscar:
            return entrada
    return None

def imprimir_resultados(resultados):
    if resultados:
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Name", "ATT&CK ID", "ATT&CK_Category"]

        for resultado in resultados:
            tabla.add_row([
                resultado.get("ID", ""),
                resultado.get("Name", ""),
                ", ".join(resultado.get("ATT&CK_ID", [])),
                ", ".join(resultado.get("ATT&CK_Category", []))
            ])

        print(tabla)
    else:
        print("No se encontraron resultados.")

def main():
    parser = argparse.ArgumentParser(description="Buscar en el JSON de Mitre Attacks Detection Rules.")
    parser.add_argument("archivo_json", help="Ruta al archivo JSON")
    parser.add_argument("--id_attck", help="Valor para buscar por ATT&CK_ID")
    parser.add_argument("--category_attck", help="Valor para buscar por ATT&CK_Category")
    parser.add_argument("--show", help="ID para ver información detallada de una entrada")
    args = parser.parse_args()

    try:
        with open(args.archivo_json, 'r', encoding='utf-8') as file:
            datos = json.load(file)
    except FileNotFoundError:
        print(f"El archivo {args.archivo_json} no se encontró.")
        return
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el JSON en {args.archivo_json}: {e}")
        
        with open(args.archivo_json, 'r', encoding='utf-8') as file:
            # Leer el archivo línea por línea para identificar la línea problemática
            lines = file.readlines()
            for i, line in enumerate(lines):
                if e.lineno - 1 == i:
                    print(f"Línea {i + 1}: {line.strip()}")
                    break

        return

    if args.id_attck:
        # Buscar e imprimir entradas con ATT&CK_ID igual al valor proporcionado
        resultados = id_attck(datos, args.id_attck)
        imprimir_resultados(resultados)
    elif args.category_attck:
        # Buscar e imprimir entradas por ATT&CK_Category igual al valor proporcionado
        resultados = category_attck(datos, args.category_attck)
        imprimir_resultados(resultados)
    elif args.show:
        # Ver información detallada de una entrada por ID
        resultado = show(datos, args.show)
        if resultado:
            print(json.dumps(resultado, indent=2))
        else:
            print(f"No se encontró ninguna entrada con ID '{args.show}'.")
    else:
        print("Debe proporcionar al menos una función de búsqueda.")

if __name__ == "__main__":
    main()

