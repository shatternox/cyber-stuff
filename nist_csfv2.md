# NIST CSF 2.0 – Overview & Examples (GV, ID, PR, DE, RS, RC)

NIST CSF 2.0 defines **6 Functions**:

1. **Govern (GV)**
2. **Identify (ID)**
3. **Protect (PR)**
4. **Detect (DE)**
5. **Respond (RS)**
6. **Recover (RC)**

They form a lifecycle:

> Govern → Identify → Protect → Detect → Respond → Recover

---

## 1. Govern (GV)

**Purpose:**  
Set the overall **direction, risk appetite, responsibilities, and policies** for cybersecurity and privacy. This is about how leadership manages cyber risk as part of business risk.

**Examples:**

- The board approves a **Cybersecurity Risk Management Policy** and reviews KPIs every quarter.
- The company defines a **risk appetite** (e.g., “no tolerance for data loss of customer PII”).
- Roles & responsibilities are documented: CISO, incident responder, system owner, data owner, etc.
- Third-party risk management process is established (due diligence, security clauses in contracts).

**Sample practical actions:**

- Create and maintain:
  - Cybersecurity policy
  - Acceptable Use Policy (AUP)
  - Third-Party Risk Management Policy
- Define:
  - Who approves exceptions (e.g., firewall rule bypass)
  - Who is accountable for each critical system

---

## 2. Identify (ID)

**Purpose:**  
Understand **what you have, what is important, and what risks you face.**

**Examples:**

- Maintain an **asset inventory** (servers, laptops, cloud accounts, SaaS apps).
- Classify data (e.g., Public, Internal, Confidential, Restricted).
- Perform risk assessments on critical systems (e.g., core banking app, payment gateway).
- Map **business processes** to the IT systems that support them.

**Sample practical actions:**

- Build/maintain a CMDB or asset list that includes:
  - Owner
  - Location
  - Data sensitivity
  - Internet-exposed or not
- Conduct annual/regular risk assessments:
  - Identify threats (ransomware, insider, misconfig)
  - Identify vulnerabilities (unpatched OS, weak auth)
  - Rate likelihood & impact (e.g., using a simple heatmap)

---

## 3. Protect (PR)

**Purpose:**  
Implement safeguards to **limit or contain the impact** of cyber events.

**Examples:**

- Enforce **MFA** for VPN, email, and admin accounts.
- Apply **least privilege** and role-based access control (RBAC).
- Patch management program for OS, applications, and network devices.
- Implement endpoint protection (EDR/antivirus), disk encryption, and secure configurations.
- Security awareness training and phishing simulations for employees.

**Sample practical actions:**

- Access Control:
  - Use centralized identity (IdP) and SSO.
  - Review privileged accounts regularly.
- Data Protection:
  - Encrypt laptops and databases with sensitive data.
  - Implement DLP for emails and cloud storage.
- Secure Configuration:
  - Baseline hardening based on CIS Benchmarks.
  - Disable unnecessary services and default accounts.
- Training:
  - Run annual security awareness training.
  - Simulated phishing campaigns with follow-up training.

---

## 4. Detect (DE)

**Purpose:**  
**Discover** cybersecurity events quickly and accurately.

**Examples:**

- Centralize logs into a **SIEM** (e.g., firewall, AD, EDR, application logs).
- Set up alerts for suspicious activity:
  - Multiple failed logins
  - Impossible travel logins
  - Large data download from sensitive folders
- Run regular **vulnerability scans** and monitor for new critical findings.
- Use IDS/IPS or cloud-native detection tools.

**Sample practical actions:**

- Logging & Monitoring:
  - Ensure critical systems send logs to SIEM.
  - Define and tune detection rules/use-cases.
- Detection Processes:
  - Daily SOC monitoring of alerts.
  - Weekly review of high-priority vulnerabilities.
- Testing:
  - Perform tabletop exercises for detection scenarios.
  - Red team / purple team exercises to validate detection coverage.

---

## 5. Respond (RS)

**Purpose:**  
Take action **during or right after** a detected incident to contain impact and coordinate communication.

**Examples:**

- Use a formal **Incident Response Plan (IRP)** with defined severity levels (SEV1–SEV4).
- When ransomware is detected:
  - Isolate affected machines
  - Block malicious IPs/domains
  - Disable compromised accounts
- Communication:
  - Notify management
  - Notify legal/privacy officers and, if needed, regulators and affected customers.
- Forensic investigation:
  - Collect logs, memory images, and relevant artifacts.

**Sample practical actions:**

- Prepare:
  - Incident Response playbooks (e.g., phishing, malware, data leakage, account compromise).
  - Incident communication templates (internal and external).
- During incident:
  - Assign Incident Commander and roles (tech, comms, legal).
  - Document actions, timelines, and decisions.
- After incident:
  - Root Cause Analysis (RCA).
  - Lessons learned meeting.
  - Update IRP and controls to prevent recurrence.

---

## 6. Recover (RC)

**Purpose:**  
Restore **systems, data, and business operations** after an incident and improve resilience.

**Examples:**

- Restore servers and data from backups after ransomware (with integrity verification).
- Execute **Disaster Recovery (DR)** plan for a data center outage:
  - Failover to secondary site or cloud region.
- Communicate service restoration status to customers and stakeholders.
- Update business continuity plans (BCP) based on lessons learned.

**Sample practical actions:**

- Backup & Restore:
  - Regular backups of critical systems; test restores (not just backup success logs).
  - Keep offline/immutable backups to protect from ransomware.
- Business Continuity:
  - Document RTO/RPO for critical services.
  - Run periodic DR drills (e.g., simulate data center failure).
- Post-incident improvements:
  - Review what worked and what didn’t in recovery.
  - Adjust capacity, architecture, or processes (e.g., add redundancy, improve RTO).

---

## Simple Mapping Example (End-to-End Scenario)

**Scenario:** Ransomware attack on a file server.

- **Govern (GV):**  
  Org has an approved risk appetite, IR policy, and defined roles (CISO, incident commander, system owners).

- **Identify (ID):**  
  File server is listed as a **critical asset** storing confidential documents.

- **Protect (PR):**  
  Server is hardened, patched regularly, has EDR, and backups are configured.

- **Detect (DE):**  
  SIEM/EDR detects suspicious file encryption activity and generates a high-severity alert.

- **Respond (RS):**  
  Incident team isolates the server, disables compromised accounts, engages forensics, and notifies management.

- **Recover (RC):**  
  Server is rebuilt from clean images, data restored from secure backups, and lessons learned are added to improve defenses.

---
