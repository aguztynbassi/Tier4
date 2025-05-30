# Sigma2SIEM - Convert Sigma Rules into SIEM Queries

This script allows the conversion of detection rules written in [Sigma](https://github.com/SigmaHQ/sigma) format into query languages specific to various SIEM engines such as Splunk, ElasticSearch, Azure Sentinel, and IBM QRadar.

## Features

- Compatibility with the following backends:
  - Splunk
  - ElasticSearch
  - Azure Sentinel
  - IBM QRadar
- Input file validation
- Automatic conversion using Sigma's official backends
- User-friendly command-line interface (CLI)

## Requirements

- Python 3.7 or higher
- Project dependencies (see Installation section)

## Installation

```bash
pip install -r requirements.txt
````

## Usage

```bash
python Sigma2Siem.py /path/to/rule.yml [backend option]
```

### Backend options:

| Option | Backend        | Description                              |
| ------ | -------------- | ---------------------------------------- |
| `-s`   | SplunkBackend  | Converts the rule to Splunk query format |
| `-e`   | ElasticBackend | Converts the rule to ElasticSearch query |
| `-a`   | AzureBackend   | Converts the rule to Azure Sentinel      |
| `-q`   | QRadarBackend  | Converts the rule to IBM QRadar          |
| `-?`   | Help           | Displays the script help menu            |

### Example

```bash
python Sigma2Siem.py ./Database/"AADInternals PowerShell Cmdlet Execution".yml -s
```
