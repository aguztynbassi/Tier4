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
usage: search.py [-h] [--id_attck ID_ATTCK] [--category_attck CATEGORY_ATTCK]
                 [--show SHOW]
                 archivo_json

Search the JSON of Mitre Attacks Detection Rules.

positional arguments:
  archivo_json          Path to JSON file

options:
  -h, --help            show this help message and exit
  --id_attck ID_ATTCK   Value to search by ATT&CK_ID ... Examples for uses:
                        python3 search.py Rules.json --id_attck='T1203'
  --category_attck CATEGORY_ATTCK
                        Value to search by ATT&CK_Category ... Examples for
                        uses: python3 search.py Rules.json
                        --category_attck='Execution'
  --show SHOW           ID to view detailed information of an entry ...
                        Examples for uses Search Rule: python3 search.py
                        Rules.json --show='WIN_5' or python3 search.py
                        Rules.json --show='WIN_5' > WIN_5.json
```

### --id_attck

```
python3 search.py Rules.json --id_attck="T1203"
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

### --category_attck

```
python3 search.py Rules.json --category_attck="Execution"
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

### --show

```
python3 search.py Rules.json --show="WIN_5"
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

### Save Rule

```
python3 search.py Rules.json --show="WIN_5" > WIN_5.json
```
