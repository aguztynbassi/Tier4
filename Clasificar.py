import os
import yaml
import shutil
import re
from typing import List, Dict, Any, Union

# --- Configuración de Rutas ---
INPUT_DIR = "sigma-rules"  # Carpeta de entrada que contiene las reglas Sigma
OUTPUT_DIR = "Database"    # Carpeta raíz donde se organizarán las reglas

# --- Mapeo de Tácticas MITRE ATT&CK ---
# Este diccionario traduce los IDs de tácticas MITRE a nombres más descriptivos
# para la creación de carpetas.
TACTIC_NAMES = {
    "TA0001": "Reconocimiento",
    "TA0002": "Desarrollo_de_Recursos",
    "TA0003": "Acceso_Inicial",
    "TA0004": "Ejecucion",
    "TA0005": "Persistencia",
    "TA0006": "Escalada_de_Privilegios",
    "TA0007": "Evasion_de_Defensas",
    "TA0008": "Acceso_a_Credenciales",
    "TA0009": "Descubrimiento",
    "TA0010": "Movimiento_Lateral",
    "TA0011": "Comando_y_Control",
    "TA0012": "Exfiltracion",
    "TA0040": "Impacto",
    "TA0042": "Inhibicion_de_Funcion_de_Respuesta"
}

def load_yaml(file_path: str) -> Union[Dict[str, Any], None]:
    """
    Carga y parsea un archivo YAML de forma segura.

    Args:
        file_path (str): La ruta al archivo YAML.

    Returns:
        dict: El contenido del archivo YAML como un diccionario, o None si hay un error.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ Error de formato YAML en '{file_path}': {e}")
    except Exception as e:
        print(f"❌ Error inesperado leyendo '{file_path}': {e}")
    return None

def extract_mitre_tactics(tags: Union[List[Union[str, Dict[str, str]]], None]) -> List[str]:
    """
    Extrae los IDs de tácticas MITRE (e.g., 'TA0001') de una lista de tags.
    Los tags pueden ser cadenas o diccionarios.

    Args:
        tags (list): Una lista de tags de una regla Sigma.

    Returns:
        list: Una lista de IDs de tácticas MITRE encontradas.
    """
    if not isinstance(tags, list):
        return []

    tactics = []
    for tag in tags:
        if isinstance(tag, dict):
            # Busca 'attack.tactic' directamente en el diccionario
            value = tag.get("attack.tactic")
            if isinstance(value, str) and value.startswith("TA"):
                tactics.append(value)
        elif isinstance(tag, str):
            # Usa una expresión regular para encontrar 'attack.tactic:TAXXXX'
            match = re.match(r"attack\.tactic\s*:\s*(TA\d{4})", tag.strip(), re.IGNORECASE)
            if match:
                tactics.append(match.group(1))
    return list(set(tactics)) # Elimina duplicados si una regla tiene la misma táctica listada varias veces

def organize_sigma_rules():
    """
    Organiza las reglas Sigma desde INPUT_DIR a OUTPUT_DIR,
    creando subcarpetas basadas en las tácticas MITRE.
    """
    if not os.path.exists(INPUT_DIR):
        print(f"❌ Error: La carpeta de entrada '{INPUT_DIR}' no fue encontrada.")
        print("Asegúrate de que tus reglas Sigma estén en el directorio correcto.")
        return

    # Inicializa contadores para el resumen final
    total_processed = 0
    total_copied = 0
    total_skipped = 0

    print(f"\n📁 Iniciando la clasificación de reglas Sigma por táctica MITRE en '{INPUT_DIR}'...\n")

    # Itera sobre todos los archivos en el directorio de entrada y sus subdirectorios
    for root, _, files in os.walk(INPUT_DIR):
        for file_name in files:
            # Solo procesa archivos YAML
            if not file_name.endswith((".yml", ".yaml")):
                continue

            total_processed += 1
            source_path = os.path.join(root, file_name)
            
            print(f"🔍 Procesando '{file_name}'...")
            
            # Carga el contenido de la regla Sigma
            sigma_rule = load_yaml(source_path)
            if not sigma_rule:
                total_skipped += 1
                continue

            # Extrae las tácticas MITRE de los tags de la regla
            tags = sigma_rule.get("tags")
            mitre_tactics = extract_mitre_tactics(tags)

            if not mitre_tactics:
                print(f"    🚫 Omitido: No se encontraron tácticas MITRE válidas en '{file_name}'.")
                total_skipped += 1
                continue

            # Copia la regla a las carpetas de destino correspondientes
            copied_to_at_least_one_folder = False
            for tactic_id in mitre_tactics:
                # Obtiene el nombre de la táctica traducido, o "Desconocido" si no está mapeado
                tactic_name = TACTIC_NAMES.get(tactic_id, "Desconocido")
                
                # Crea el nombre de la subcarpeta (e.g., "TA0003_Acceso_Inicial")
                subfolder_name = f"{tactic_id}_{tactic_name}"
                destination_dir = os.path.join(OUTPUT_DIR, subfolder_name)
                
                # Asegura que la carpeta de destino exista
                os.makedirs(destination_dir, exist_ok=True)

                destination_path = os.path.join(destination_dir, file_name)
                
                try:
                    # Usa shutil.copy2 para copiar el archivo y sus metadatos
                    shutil.copy2(source_path, destination_path)
                    print(f"    ✅ Copiado a: '{subfolder_name}'")
                    copied_to_at_least_one_folder = True
                except Exception as e:
                    print(f"    ❌ Error al copiar '{file_name}' a '{subfolder_name}': {e}")
                    # No incrementamos total_skipped aquí porque podría copiarse a otra táctica
            
            if copied_to_at_least_one_folder:
                total_copied += 1
            else:
                # Si no se pudo copiar a NINGUNA de las tácticas, entonces es un skip
                total_skipped += 1


    # --- Resumen Final ---
    print("\n--- Proceso de Clasificación Finalizado ---")
    print(f"📄 Reglas Sigma procesadas: {total_processed}")
    print(f"📦 Reglas copiadas (al menos una vez): {total_copied}")
    print(f"⛔ Reglas omitidas (sin táctica o error de copia): {total_skipped}\n")

if __name__ == "__main__":
    organize_sigma_rules()