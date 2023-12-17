import json

# Nombre del archivo JSON
archivo_json = 'WIN_rules.json'

# Cargar datos desde el archivo JSON
with open(archivo_json) as json_file:
    data_list = json.load(json_file)

# Obtener listas únicas para cada categoría
id_attck_list = list(set(x for data in data_list for x in data["ATT&CK_ID"]))
tags_attck_list = list(set(x for data in data_list for x in data["ATT&CK_Tag"]))
req_min_log_source_list = list(set(x for data in data_list for x in data["Minimum_Log_Source_Requirement"]))
categoria_attck_list = list(set(x for data in data_list for x in data["ATT&CK_Category"]))

# Mostrar resultados
print("ID ATT&CK:")
print(id_attck_list)

print("\nTags ATT&CK:")
print(tags_attck_list)

print("\nRequerimiento mínimo de fuente de registro:")
print(req_min_log_source_list)

print("\nCategoría ATT&CK:")
print(categoria_attck_list)

