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

#  example for uses
#
#  python3 search.py Rules.json -h
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
        print("No results were found.")

def main():
    parser = argparse.ArgumentParser(description="Search the JSON of Mitre Attacks Detection Rules.")
    parser.add_argument("archivo_json", help="Path to JSON file")
    parser.add_argument("--id_attck", help="Value to search by ATT&CK_ID ... Examples for uses: python3 search.py Rules.json --id_attck='T1203'")
    parser.add_argument("--category_attck", help="Value to search by ATT&CK_Category ... Examples for uses: python3 search.py Rules.json --category_attck='Execution'")
    parser.add_argument("--show", help="ID to view detailed information of an entry ... Examples for uses Search Rule: python3 search.py Rules.json --show='WIN_5' or python3 search.py Rules.json --show='WIN_5' > WIN_5.json")

    args = parser.parse_args()

    try:
        with open(args.archivo_json, 'r', encoding='utf-8') as file:
            datos = json.load(file)
    except FileNotFoundError:
        print(f"File {args.archivo_json} was not found.")
        return
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in {args.archivo_json}: {e}")
        
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
            print(f"No entry found with ID '{args.show}'.")
    else:
        print("It must provide at least one search function.")

if __name__ == "__main__":
    main()

