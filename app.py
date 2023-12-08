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
    table.field_names = ["ID", "Name", "Trigger Condition", "ATT&CK Category", "ATT&CK Tag", "ATT&CK ID", "Minimum Log Source Requirement", "Query"]

    for data in data_list:
        table.add_row([
            data["ID"],
            data["Name"],
            data["Trigger_Condition"],
            ", ".join(data["ATT&CK_Category"]),
            ", ".join(data["ATT&CK_Tag"]),
            ", ".join(data["ATT&CK_ID"]),
            ", ".join(data["Minimum_Log_Source_Requirement"]),
            data["Query"]
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


