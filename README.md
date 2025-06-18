# TIER4

This structure is just a starting point. You can adapt it according to the specific needs of your organisation and the way you prefer to organise your threat detection resources.

There are over 900 mapped rules covering both tactics and techniques from the MITRE matrix. Each rule includes an identifier and a detailed description, and they are organized according to the necessary requirements for their implementation.

### Example Rule

``` yml
title: Social Media Account Creation  
id: b7e2c1a0-3f4e-4a2e-9d7c-8f5e2b6c9a1d  
description: >
  Detection of new social media account creations which may be used for information operations, such as influence campaigns 
  or identity impersonation.
...
logsource:  
  product: Network  
  service: social_media_activity  
detection:  
  selection:  
    action: create_account  
  condition: selection  
fields:  
  - user
  ...
tags:  
  - attack.tactic: TA0043  # Reconnaissance  
  - attack.technique: T1590.001  # Gather Victim Identity Information: Social Media  
level: medium  
platforms:  
  - Network
```

## Contributions

If you would like to contribute to the project, feel free to fork the repository and submit a pull request. Contributions are welcome.
