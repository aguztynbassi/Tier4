# Sentinel Prompt Repository: Precision Threat Detection

This repository hosts a specialized collection of over **900 structured prompts** designed for elite threat detection and incident response. Each prompt is meticulously engineered to guide security analysts through complex investigations, ensuring no critical detail is overlooked.

Every entry is encapsulated in a schema-ready **JSON format**, featuring rich metadata, execution parameters, and—crucial for modern SOC operations—a direct mapping to the **MITRE ATT&CK® Matrix**. This repository doesn't just provide questions; it provides a standardized tactical framework for mitigating adversary behavior.

## The 1-10-60 Framework: Mastering the SOC Workflow

In high-pressure environments like cybersecurity, the **1-10-60 Framework** is the ultimate defense against "alert fatigue" and reactive chaos. It shifts the focus from merely "processing data" to "solving threats."

1. **The One Minute of Intent (1):** Identify the **critical threat** or investigation that requires your absolute focus. Instead of glancing at 50 vague alerts, you pick the one "true positive" that could compromise the network.
2. **The Ten Minutes of Planning (10):** Prepare your environment. This is where you leverage this repository. You select the appropriate **JSON Prompt**, identify the required parameters (EventIDs, timestamps, etc.), and map the logic to the specific MITRE ATT&CK tactic you are investigating.
3. **The Sixty Minutes of Deep Work (60):** Execute. With the prompt as your tactical guide, you spend an hour of uninterrupted analysis, pivoting through logs and data to reach a definitive conclusion or remediation.

## Content and Structure

The core of this project is a library of JSON objects, each acting as a modular "investigation unit."

### Standardized Schema:

* **`name`**: A clear, descriptive title (e.g., *"Suspicious Svchost Activity"*).
* **`description`**: Contextual intelligence on the threat and why it matters.
* **`tags`**: Strategic labels including **MITRE ATT&CK Tactic (TAXXXX)** and **Technique (TXXXX)** IDs.
* **`prompts`**: Actionable instructions with dynamic placeholders (`{ParameterName}`) for seamless integration with AI agents or manual analysis.
* **`parameters`**: A strict definition of the data points required (e.g., `CommandLine`, `ProcessID`) to execute the investigation.

### Example Data Structure

```json
[
  {
    "name": "Suspicious Svchost Activity Detected",
    "description": "Detects anomalous svchost.exe behavior, such as execution without services.exe as a parent.",
    "tags": ["TA0005", "T1055", "windows", "detection"],
    "prompts": [
      {
        "id": "1",
        "prompt": "Analyze the following svchost.exe activity: Event ID {EventID}, Parent Process {ParentImage}. Does this align with known Defense Evasion techniques?",
        "systemCapability": "analyzeSecurityEvent"
      }
    ],
    "parameters": [
      { "name": "EventID", "required": true, "description": "Sysmon Event ID 1 (Process Creation)." }
    ]
  }
]

```

## Why this repository improves the "One Minute of Intent"

The **"One Minute of Intent"** often fails because the user knows *what* they want to achieve but lacks a clear starting point to measure success. This repository bridges that gap in the following ways:

* **Instant Clarity:** Instead of a vague intention like "investigating alerts," the repository allows you to say: *"My intent today is to investigate Technique T1055 (Process Injection)."* The repository has already done the heavy lifting of defining what is important.
* **Elimination of Decision Fatigue:** With over 900 mapped prompts, the "Minute of Intent" becomes a tactical menu choice. You know that if you select a prompt from this repo, your goal is well-defined, standardized, and actionable.
* **Strategic Alignment:** Thanks to the **MITRE ATT&CK** mapping, your intent isn't just "working"—it's closing a specific gap in your organization’s security posture. This elevates the task from "operational" to "strategic" in under 60 seconds.
* **Defined Success Metrics:** The repository provides the necessary `parameters`. By the end of your Minute of Intent, you don't just have a goal; you know exactly which data points you need from the SIEM to make that hour of work successful.

## Contributions

Your collaboration is essential to expand and enhance this collection\! If you wish to contribute:

1.  "Fork" this repository.
2.  Add new JSON prompt objects following the defined structure and ensure you include the relevant MITRE ATT\&CK tags.
3.  Submit a "pull request" with your changes.
