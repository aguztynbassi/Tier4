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

from flask import Flask, render_template
import json
from prettytable import PrettyTable

app = Flask(__name__)

def load_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def generate_table(data_list):
    table = PrettyTable()
    table.field_names = ["ID", "Name", "ATT&CK Category", "ATT&CK Tag", "ATT&CK ID", "Minimum Log Source Requirement"]

    for data in data_list:
        table.add_row([
            data["ID"],
            data["Name"],
            ", ".join(data["ATT&CK_Category"]),
            ", ".join(data["ATT&CK_Tag"]),
            ", ".join(data["ATT&CK_ID"]),
            ", ".join(data["Minimum_Log_Source_Requirement"])
        ])

    return table.get_html_string()

@app.route('/')
def index():
    json_file_path = "Mitre Attacks Detection Rules.json"  # Reemplaza esto con la ruta real de tu archivo JSON
    json_data = load_json(json_file_path)

    if isinstance(json_data, list):
        table_html = generate_table(json_data)
        return render_template('index.html', table_html=table_html)
    else:
        return "El archivo JSON no contiene una lista de objetos como se esperaba."

if __name__ == '__main__':
    app.run(debug=True)


