# NIST CSF 2.0 – Cheat Sheet by Function (GV, ID, PR, DE, RS, RC)

---

## GV – Govern

**Purpose:** Set direction, expectations, and governance for cybersecurity risk management.

### Categories

| Code  | Name                                           | What it covers (short)                                                                             |
|-------|------------------------------------------------|----------------------------------------------------------------------------------------------------|
| GV.OC | Organizational Context                         | Mission, stakeholders, legal & regulatory context for cyber risk decisions.                        |
| GV.RM | Risk Management Strategy                       | How the org defines, measures, and treats cyber risk (risk appetite, tolerance, integration to ERM). |
| GV.RR | Roles, Responsibilities, and Authorities       | Who is accountable; who does what in cyber risk management.                                       |
| GV.PO | Policy                                         | Cybersecurity policies: creation, review, communication, enforcement.                             |
| GV.OV | Oversight                                      | Board/management oversight, metrics, assurance, and governance of cyber activities.               |
| GV.SC | Cybersecurity Supply Chain Risk Management     | How supplier / third-party cyber risks are identified and managed.                                |

### Key subcategories (examples)

- **GV.OC-01** – Organizational mission is understood and used to guide cybersecurity risk management.
- **GV.OC-02** – Internal and external stakeholders (e.g., customers, regulators, partners) and their cyber expectations are identified and understood.
- **GV.OC-03** – Legal, regulatory, and contractual requirements (including privacy & civil liberties) are understood and managed.
- **GV.RM-01** – Risk management objectives are defined and agreed by stakeholders.
- **GV.RM-02** – Risk appetite and tolerance statements are established, communicated, and maintained.
- **GV.RM-03** – Cyber risk management is integrated into enterprise risk management (ERM) processes.
- **GV.RR-01** – Leadership is accountable for cyber risk and promotes a risk-aware and ethical culture.
- **GV.RR-02** – Roles, responsibilities, and authorities for cyber risk management are clearly defined, communicated, and enforced.
- **GV.PO-01** – Cyber risk management policy is established based on context and strategy, and is communicated and enforced.
- **GV.PO-02** – Cyber policies are regularly reviewed and updated to reflect changes in threats, tech, and mission.
- **GV.SC-01** (example) – Supply-chain-related cyber risks are identified and managed through requirements, contracts, and oversight.

**Example:**  
For a SaaS company using many cloud vendors, **GV.OC-03** ensures you track all regulatory obligations (e.g., GDPR), **GV.RM-02** documents low tolerance for customer data breaches, and **GV.SC-01** drives vendor security clauses and periodic reviews.

---

## ID – Identify

**Purpose:** Understand your assets, risks, and opportunities to improve.

### Categories

| Code  | Name             | What it covers (short)                                                            |
|-------|------------------|-----------------------------------------------------------------------------------|
| ID.AM | Asset Management | Inventories, dependencies, data flows, and life cycle of hardware/software/data. |
| ID.RA | Risk Assessment  | Threats, vulnerabilities, likelihood, impact, and risk response planning.        |
| ID.IM | Improvement      | Continuous improvement based on evaluations, testing, and operational feedback.  |

### Key subcategories (examples)

**Asset Management (ID.AM)**  
- **ID.AM-01** – Maintain inventories of hardware assets managed by the organization.  
- **ID.AM-02** – Maintain inventories of software, services, and systems.  
- **ID.AM-03** – Maintain representations of authorized network communication and data flows.  
- **ID.AM-04** – Maintain inventories of services provided by suppliers.  
- **ID.AM-05** – Prioritize assets based on classification, criticality, resources, and mission impact.  
- **ID.AM-07** – Maintain inventories of data and associated metadata for key data types.  
- **ID.AM-08** – Manage systems, hardware, software, services, and data across their life cycles.

**Risk Assessment (ID.RA)**  
- **ID.RA-01** – Identify, validate, and record vulnerabilities in assets.  
- **ID.RA-02** – Receive and use cyber threat intelligence from information-sharing sources.  
- **ID.RA-03** – Identify and record internal and external threats.  
- **ID.RA-04** – Identify and record potential impacts and likelihoods of threats exploiting vulnerabilities.  
- **ID.RA-05** – Use threats, vulnerabilities, likelihoods, and impacts to understand inherent risk and prioritize response.  
- **ID.RA-06** – Choose, prioritize, plan, track, and communicate risk responses.  
- **ID.RA-07** – Manage changes and exceptions, assess their risk impact, record, and track them.  
- **ID.RA-08** – Establish processes to receive, analyze, and respond to vulnerability disclosures.  
- **ID.RA-09** – Assess authenticity and integrity of hardware and software before acquisition/use.  
- **ID.RA-10** – Assess critical suppliers before acquisition.

**Improvement (ID.IM)**  
- **ID.IM-01** – Identify improvements from evaluations (e.g., audits, risk assessments).  
- **ID.IM-02** – Identify improvements from security tests/exercises (including those with suppliers).  
- **ID.IM-03** – Identify improvements from day-to-day operational processes and activities.  
- **ID.IM-04** – Establish, communicate, maintain, and improve incident response and other cybersecurity plans.

**Example:**  
For a payment system risk assessment, you use **ID.AM** to map servers, APIs, and data flows; **ID.RA-01..05** to document vulns, threats, likelihood, and impact; then **ID.IM-01/04** to feed lessons learned into updated IR plans and hardening roadmaps.

---

## PR – Protect

**Purpose:** Implement safeguards to limit the impact and likelihood of cyber events.

### Categories

| Code  | Name                                           | What it covers (short)                                              |
|-------|------------------------------------------------|---------------------------------------------------------------------|
| PR.AA | Identity Management, Authentication & Access   | Identities, authentication, authorization, and physical access.     |
| PR.AT | Awareness and Training                         | Security awareness and role-based training.                         |
| PR.DS | Data Security                                  | Protecting data at rest, in transit, and in use; backup and DLP.    |
| PR.PS | Platform Security                              | Secure configuration & life cycle of software/hardware/platforms.   |
| PR.IR | Technology Infrastructure Resilience           | Network and infrastructure protections and resilience measures.     |

### Key subcategories (examples)

**Identity & Access (PR.AA)**  
- **PR.AA-01** – Manage identities and credentials for authorized users, services, and hardware.  
- **PR.AA-02** – Proof identities and bind them to credentials based on interaction risk.  
- **PR.AA-03** – Authenticate users, services, and hardware before granting access.  
- **PR.AA-04** – Protect, convey, and verify identity assertions (tokens, certificates, SSO).  
- **PR.AA-05** – Define, enforce, and review access permissions and entitlements using least privilege and separation of duties.  
- **PR.AA-06** – Manage and monitor physical access to assets according to risk.

**Awareness & Training (PR.AT)**  
- **PR.AT-01** – Provide general staff with cyber awareness and training for day-to-day tasks.  
- **PR.AT-02** – Provide specialized training to staff in high-impact roles (admins, devs, SOC, etc.).

**Data Security (PR.DS)**  
- **PR.DS-01** – Protect confidentiality, integrity, and availability of data-at-rest (e.g., disk encryption, access controls).  
- **PR.DS-02** – Protect data-in-transit (e.g., TLS, VPNs, integrity checks).  
- **PR.DS-10** – Protect data-in-use (e.g., memory protections, TEEs, process isolation).  
- **PR.DS-11** – Create, protect, maintain, and regularly test data backups.

**Platform Security (PR.PS)**  
- **PR.PS-01** – Establish and apply configuration management practices (baselines, hardening, change control).  
- **PR.PS-02** – Maintain, replace, and remove software based on risk (patching, decommissioning).  
- **PR.PS-03** – Maintain, replace, and remove hardware based on risk (secure disposal, refresh).  
- **PR.PS-04** – Generate and retain log records to support continuous monitoring.  
- **PR.PS-05** – Prevent installation and execution of unauthorized software (allow-listing, EDR).  
- **PR.PS-06** – Integrate and monitor secure SDLC practices across the software life cycle.

**Technology Infrastructure Resilience (PR.IR)**  
- **PR.IR-01** – Protect networks and environments from unauthorized logical access and use.  
- **PR.IR-02** – Protect technology assets from environmental threats (power, fire, flooding, etc.).  

**Example:**  
For an internal HR web app: **PR.AA-01..05** ensure SSO + RBAC; **PR.DS-01/02/11** ensure encrypted DB, TLS, and tested backups; **PR.PS-01/04/05** enforce hardened builds, logging, and app allow-listing on servers.

---

## DE – Detect

**Purpose:** Quickly detect cyber events through monitoring and analysis.

### Categories

| Code  | Name                   | What it covers (short)                                       |
|-------|------------------------|--------------------------------------------------------------|
| DE.CM | Continuous Monitoring  | Monitoring networks, endpoints, users, and systems for events. |
| DE.AE | Adverse Event Analysis | Analyzing and triaging events to determine incidents and impact. |

### Key subcategories (examples)

**Continuous Monitoring (DE.CM)**  
- **DE.CM-01** – Monitor networks and network services (traffic, connections, anomalies).  
- **DE.CM-02** – Monitor user activity and access to detect unusual behavior.  
- **DE.CM-03** – Monitor physical access and environmental conditions where appropriate.  
- **DE.CM-04** – Monitor endpoints, servers, and applications for security-relevant events.  
- **DE.CM-07/08** (examples) – Perform security monitoring such as IDS/IPS alerts and vulnerability scans; integrate them into centralized monitoring/SIEM.

**Adverse Event Analysis (DE.AE)**  
- **DE.AE-01** (example) – Establish criteria and processes to analyze detection alerts and determine if they represent a cybersecurity incident.  
- **DE.AE-02** (example) – Correlate events from multiple sources to identify attack patterns.  
- **DE.AE-03** (example) – Document analysis results to support response and lessons learned.

**Example:**  
A SOC uses **DE.CM-01/02/04** for network, user, and host logging into a SIEM. Use-cases and correlation rules implement **DE.AE** to flag potential credential stuffing or lateral movement for investigation.

---

## RS – Respond

**Purpose:** Take action once an incident is detected to contain and manage it.

### Categories

| Code  | Name                                      | What it covers (short)                                           |
|-------|-------------------------------------------|------------------------------------------------------------------|
| RS.MA | Incident Management                       | Executing IR plan, triage, categorization, escalation, recovery triggers. |
| RS.AN | Incident Analysis                         | Analyzing incidents to support response, forensics, and recovery. |
| RS.CO | Incident Response Reporting & Communication| Internal & external communications during incidents.             |
| RS.MI | Incident Mitigation                       | Containment, eradication, and limiting incident impact.          |

### Key subcategories (examples)

**Incident Management (RS.MA)**  
- **RS.MA-01** – Execute the incident response plan in coordination with relevant third parties once an incident is declared.  
- **RS.MA-02** – Triage and validate incident reports.  
- **RS.MA-03** – Categorize and prioritize incidents.  
- **RS.MA-04** – Escalate or elevate incidents as needed (e.g., to management, regulators).  
- **RS.MA-05** – Apply criteria to initiate incident recovery activities.

**Incident Analysis (RS.AN)**  
- **RS.AN-03** (key remaining subcategory) – Perform analysis to understand root cause, scope, and impact, and to support forensics and recovery.

**Incident Response Reporting & Communication (RS.CO)**  
- **RS.CO-01** (example) – Define who communicates what, when, and to whom during an incident.  
- **RS.CO-02** (example) – Ensure incidents are reported according to internal and external requirements (e.g., regulators, customers).  
- **RS.CO-03** (example) – Coordinate information sharing with stakeholders and partners based on response plans.

**Incident Mitigation (RS.MI)**  
- **RS.MI-01** (example) – Contain incidents (e.g., isolate hosts, block IPs, revoke tokens).  
- **RS.MI-02** (example) – Eradicate malicious artifacts and implement short-term fixes.  
- **RS.MI-03** (example) – Apply longer-term remediations to prevent recurrence.

**Example:**  
A ransomware event: **RS.MA-01..03** drive IR playbook execution and triage; **RS.MI-01** isolates affected servers; **RS.CO** handles comms to executives and customers; **RS.MA-05** and **RC.RP-01** trigger formal recovery activities.

---

## RC – Recover

**Purpose:** Restore services and capabilities after an incident and improve resilience.

### Categories

| Code  | Name                               | What it covers (short)                                      |
|-------|------------------------------------|-------------------------------------------------------------|
| RC.RP | Incident Recovery Plan Execution   | Executing recovery plans to restore systems & services.     |
| RC.CO | Incident Recovery Communication    | Communicating recovery status and outcomes to stakeholders. |

### Key subcategories (examples)

**Incident Recovery Plan Execution (RC.RP)**  
- **RC.RP-01** – Execute the recovery portion of the incident response plan once triggered by the response process.  
- **RC.RP-02** – Select, scope, prioritize, and perform recovery actions (e.g., restore from backup, rebuild systems).  
- **RC.RP-03** (example) – Validate that recovered services meet security and business requirements before returning to normal use.

**Incident Recovery Communication (RC.CO)**  
- **RC.CO-01** (example) – Communicate recovery progress, status, and residual risk to internal stakeholders (leadership, ops teams).  
- **RC.CO-02** (example) – Communicate recovery status and relevant information to external stakeholders (customers, partners, regulators) as required.  
- **RC.CO-03** (example) – Capture feedback and lessons learned to improve recovery planning and resilience.

**Example:**  
After a major outage, **RC.RP-01/02** govern restoring services from clean backups and rebuilding affected components. **RC.CO-01/02** guide status updates to executives, customers, and regulators, while outputs feed back into **ID.IM** and **GV.RM** for future improvements.

---
