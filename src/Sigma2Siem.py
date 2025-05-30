#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright Agustin Bassi <[AT]aguztynbassi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License.
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

import os
import argparse
from sigma.parser import SigmaParser
from sigma.backends.splunk import SplunkBackend
from sigma.backends.elastic import ElasticBackend
from sigma.backends.qradar import QRadarBackend
from sigma.backends.azure import AzureBackend

def sigma_to_siem(sigma_rule_path, backend_type):
    # Leer la regla Sigma
    if not os.path.isfile(sigma_rule_path):
        raise FileNotFoundError(f"La ruta {sigma_rule_path} no existe o no es un archivo válido.")
    
    with open(sigma_rule_path, 'r') as file:
        sigma_rule = file.read()

    # Parsear la regla Sigma
    parser = SigmaParser()
    rule = parser.parse(sigma_rule)

    # Seleccionar el backend adecuado
    if backend_type == 'splunk':
        backend = SplunkBackend()
    elif backend_type == 'elastic':
        backend = ElasticBackend()
    elif backend_type == 'azure':
        backend = AzureBackend()
    elif backend_type == 'qradar':
        backend = QRadarBackend()
    else:
        raise ValueError(f"Backend tipo {backend_type} no soportado.")
    
    # Convertir la regla Sigma
    siem_query = backend.convert(rule)

    return siem_query

if __name__ == "__main__":
    # Configuración de los argumentos de línea de comandos
    parser = argparse.ArgumentParser(
        description="Convertir reglas Sigma a consultas SIEM",
        usage="python script.py /ruta/a/la/regla.yml [-s | -e | -a | -q | -?]",
        add_help=False
    )
    parser.add_argument("sigma_rule_path", help="Ruta del archivo de la regla Sigma (por ejemplo, /path/to/your/sigma_rule.yml)")
    parser.add_argument("-s", "--splunk", action="store_true", help="Convertir a consulta Splunk")
    parser.add_argument("-e", "--elastic", action="store_true", help="Convertir a consulta ElasticSearch")
    parser.add_argument("-a", "--azure", action="store_true", help="Convertir a consulta Azure Sentinel")
    parser.add_argument("-q", "--qradar", action="store_true", help="Convertir a consulta QRadar")
    parser.add_argument("-?", "--help", action="help", help="Mostrar este mensaje de ayuda y salir")

    args = parser.parse_args()

    # Determinar el backend basado en la opción seleccionada
    if args.splunk:
        backend_type = "splunk"
    elif args.elastic:
        backend_type = "elastic"
    elif args.azure:
        backend_type = "azure"
    elif args.qradar:
        backend_type = "qradar"
    else:
        parser.error("Debe especificar un backend con una de las opciones: -s, -e, -a, -q, -?")

    try:
        siem_query = sigma_to_siem(args.sigma_rule_path, backend_type)
        print(f"\nConsulta generada para {backend_type}:")
        print(siem_query)
    except Exception as e:
        print(f"Error: {e}")
