# Threat Detection Prompts Collection Mapped to MITRE ATT\&CK

This repository contains a vast collection of over 900 **structured prompts for threat detection and response**, each meticulously designed to guide the investigation of security events. Each prompt is encapsulated in a detailed JSON format, including metadata, descriptions, and specific parameters required for its execution and analysis. Most importantly, each entry is directly **mapped to the tactics and techniques of the MITRE ATT\&CK Matrix**, providing a comprehensive framework for understanding and mitigating adversary behavior.

-----

## Content and Structure

The essence of this project lies in a collection of JSON files (or a single large JSON file containing a list of these objects) where each object represents a detection or investigation scenario. Following the example provided, each JSON object includes the following key structure:

  * **`name`**: A descriptive name for the detection scenario (e.g., "Suspicious Svchost Activity Detected").
  * **`description`**: A detailed explanation of what the prompt aims to detect and its relevance in the security context.
  * **`tags`**: A list of relevant tags, which **include MITRE ATT\&CK tactic (`TAXXXX`) and technique (`TXXXX`) IDs**. It can also include generic tags like `security`, `detection`, `windows`, etc.
  * **`prompts`**: An array containing one or more prompt objects, each with:
      * **`id`**: A unique identifier for the prompt.
      * **`prompt`**: The text string of the prompt, which is an instruction or question designed to be used by a security analyst or an AI system to investigate an event. It contains placeholders (`{ParameterName}`) that will be replaced by actual event values.
      * **`continueOnError`**: A boolean indicating whether execution should continue if an error occurs.
      * **`systemCapability`**: The system capability required to process this prompt (e.g., `analyzeSecurityEvent`).
  * **`parameters`**: An array of objects, each describing a parameter necessary to complete the prompt:
      * **`name`**: The name of the parameter (e.g., `EventID`, `CommandLine`).
      * **`required`**: A boolean indicating whether the parameter is mandatory.
      * **`description`**: A brief description of the parameter.

### Example Data Structure

```json
[
  {
    "name": "Suspicious Svchost Activity Detected",
    "description": "Detects anomalous `svchost.exe` activity, which is unusual if launched without significant command-line arguments and may indicate code injection by malicious processes.",
    "tags": [
      "security",
      "detection",
      "windows",
      "privilege escalation",
      "defense evasion",
      "process injection",
      "TA0004",
      "TA0005",
      "T1055"
    ],
    "prompts": [
      {
        "id": "2e7f8a9b-0c1d-4e5f-6a7b-8c9d0e1f2a3b",
        "prompt": "Suspicious `svchost.exe` activity has been detected. Event Details: Event ID {EventID}, Timestamp {Timestamp}, Image {Image}, Command Line {CommandLine}, User {User}, Computer {Computer}, Parent Image {ParentImage}. Investigate whether this activity is a process injection attempt or legitimate system service/application activity. Pay special attention to the command line and parent process.",
        "continueOnError": false,
        "systemCapability": "analyzeSecurityEvent"
      }
    ],
    "parameters": [
      {
        "name": "EventID",
        "required": true,
        "description": "The Sysmon Event ID for process creation (should be 1)."
      },
      {
        "name": "Timestamp",
        "required": true,
        "description": "The timestamp of the event."
      },
      {
        "name": "Image",
        "required": true,
        "description": "The full path to the executable (should be svchost.exe)."
      },
      {
        "name": "CommandLine",
        "required": true,
        "description": "The full command line used to launch svchost.exe."
      },
      {
        "name": "User",
        "required": true,
        "description": "The user account under which the process ran."
      },
      {
        "name": "Computer",
        "required": true,
        "description": "The name of the computer where the event occurred."
      },
      {
        "name": "ParentImage",
        "required": false,
        "description": "The image of the parent process that launched svchost.exe."
      }
    ]
  }
]
```

-----

## MITRE ATT\&CK Mapping

Mapping to the MITRE ATT\&CK Matrix is achieved through the **`tags`** associated with each prompt. This allows for rigorous classification and facilitates the identification of adversary behaviors that each prompt is designed to detect or investigate.

The `tags` use official MITRE ATT\&CK identifiers:

  * **Tactics**: Prefix `TA` followed by four digits (e.g., **`TA0004`** for "Privilege Escalation", **`TA0005`** for "Defense Evasion").
  * **Techniques/Sub-Techniques**: Prefix `T` followed by four digits, and optionally a period and three digits for sub-techniques (e.g., **`T1055`** for "Process Injection").

By including these IDs in the tags, a direct and programmatic link is created with the MITRE ATT\&CK knowledge base, allowing users to quickly correlate prompts with known adversary strategies and actions.

-----

## Use Cases

This collection of structured prompts is an invaluable tool for:

  * **Automated Detection Systems**: Integrate prompts into SIEM, SOAR, or XDR platforms to automate alert generation and initial investigations.
  * **Security Operations Center (SOC) Operations**: Provide security analysts with predefined and contextually rich prompts to guide their incident investigations.
  * **Detection Engineering**: Develop and validate new detection rules based on specific adversary techniques.
  * **Simulations and Training (Red Team/Blue Team)**: Create realistic attack scenarios and response exercises using prompts that reflect adversary behavior.
  * **Threat Research**: Explore and categorize new attack techniques within the MITRE ATT\&CK context.
  * **AI/ML Development in Cybersecurity**: Train large language models (LLMs) to generate security responses or analyses based on events, using the prompts as input/output examples.

-----

## Contributions

Your collaboration is essential to expand and enhance this collection\! If you wish to contribute:

1.  "Fork" this repository.
2.  Add new JSON prompt objects following the defined structure and ensure you include the relevant MITRE ATT\&CK tags.
3.  Submit a "pull request" with your changes.
