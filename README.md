# MITRE Enterprise ATT&CK v14 Detection Rules for Windows

## The MITRE ATT&amp;CK Alerts For log point

![MITRE ATT&amp;CK Windows V14](IMG/Mitre_ATTCK_Windows.svg)

## Usage

### help

```
python3 search.py -h
```

### Ouput

```
usage: search.py [-h] [--buscar_por_id_attck BUSCAR_POR_ID_ATTCK]
                 [--buscar_por_categoria_attck BUSCAR_POR_CATEGORIA_ATTCK]
                 [--ver_data VER_DATA]
                 archivo_json

Buscar en el JSON de Mitre Attacks Detection Rules.

positional arguments:
  archivo_json          Ruta al archivo JSON

options:
  -h, --help            show this help message and exit
  --buscar_por_id_attck BUSCAR_POR_ID_ATTCK
                        Valor para buscar por ATT&CK_ID
  --buscar_por_categoria_attck BUSCAR_POR_CATEGORIA_ATTCK
                        Valor para buscar por ATT&CK_Category
  --ver_data VER_DATA   ID para ver información detallada de una entrada
```

### --buscar_por_id_attck

```
python3 search.py Rules.json --buscar_por_id_attck="T1203"
```

### Ouput

```
+--------+----------------------------------------------------+--------------+--------------------------------+
|   ID   |                        Name                        |  ATT&CK ID   |        ATT&CK_Category         |
+--------+----------------------------------------------------+--------------+--------------------------------+
| WIN_5  | Suspicious Microsoft Equation Editor Child Process |    T1203     |           Execution            |
| WIN_69 |     Antivirus Exploitation Framework Detection     | T1203, T1219 | Execution, Command and Control |
+--------+----------------------------------------------------+--------------+--------------------------------+
```

### --buscar_por_categoria_attck

```
python3 search.py Rules.json --buscar_por_categoria_attck="Execution"
```

### Ouput

```
+--------+----------------------------------------------------+---------------------------------------------------+--------------------------------+
|   ID   |                        Name                        |                     ATT&CK ID                     |        ATT&CK_Category         |
+--------+----------------------------------------------------+---------------------------------------------------+--------------------------------+
| WIN_3  |      AADInternals PowerShell Cmdlet Execution      |                  T1059, T1059.001                 |           Execution            |
| WIN_5  | Suspicious Microsoft Equation Editor Child Process |                       T1203                       |           Execution            |
| WIN_10 |        Suspicious File Execution via MSHTA         |            T1059.007, T1140, T1218.005            |   Execution, Defense Evasion   |
| WIN_49 |         MSHTA Spwaned by SVCHOST Detected          |                  T1218, T1218.005                 |   Defense Evasion, Execution   |
| WIN_50 |       MSHTA Spawning Windows Shell Detected        |                  T1218, T1218.005                 |   Defense Evasion, Execution   |
| WIN_67 | Adobe Flash Use-After-Free Vulnerability Detected  |                       T1204                       |           Execution            |
| WIN_68 |              Adwind RAT JRAT Detected              | T1059, T1059.001, T1059.003, T1059.005, T1059.007 |           Execution            |
| WIN_69 |     Antivirus Exploitation Framework Detection     |                    T1203, T1219                   | Execution, Command and Control |
+--------+----------------------------------------------------+---------------------------------------------------+--------------------------------+
```

### --ver_data

```
python3 search.py Rules.json --ver_data="WIN_5"
```

### Ouput

```
{
  "ID": "WIN_5",
  "Name": "Suspicious Microsoft Equation Editor Child Process",
  "Trigger_Condition": "A suspicious child process of Microsoft\u2019s equation editor is detected as a sign of possible exploitation of CVE-2017-11882. CVE-2017-11882 is a vulnerability in Microsoft Office\u2019s Equation Editor component.",
  "ATT&CK_Category": [
    "Execution"
  ],
  "ATT&CK_Tag": [
    "Exploitation for Client Execution"
  ],
  "ATT&CK_ID": [
    "T1203"
  ],
  "Minimum_Log_Source_Requirement": [
    "Windows Sysmon",
    "Windows"
  ],
  "Query": "label=\"Process\" label=Create parent_process=\"*\\EQNEDT32.exe\" -\"process\" IN [\"C:\\Windows\\System32\\WerFault.exe\", \"C:\\Windows\\SysWOW64\\WerFault.exe\"]"
}
```

