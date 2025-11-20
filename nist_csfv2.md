# NIST CSF 2.0 – FULL Core Notes (All Codes, No Gaps)

> Source: **NIST CSF 2.0 Core With Withdrawn CSF 1.1 Elements** – all Functions/Categories/Subcategories listed in order.   
> Legend:  
> - **Status**: `Active (CSF 2.0)` or `Withdrawn (from CSF 1.1)`  
> - For **Withdrawn**: shows where its intent moved in CSF 2.0.  
> - For **Active**: includes a plain-English explanation + example evidence you’d show an auditor.

---

## 1. GOVERN (GV) – Set Strategy & Governance

### 1.1 Organizational Context (GV.OC)

| Code      | Status             | Meaning (plain English)                                                                                 | Example evidence                                                                                         |
|-----------|--------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| GV.OC-01  | Active (2.0)       | Mission is understood and used to guide cyber risk decisions.                                          | Slide or doc showing mission (“secure digital lending”) and linked security objectives.                  |
| GV.OC-02  | Active (2.0)       | Internal/external stakeholders and their cyber expectations are known.                                 | Stakeholder register listing regulators, customers, cloud/SaaS providers and their uptime/privacy needs. |
| GV.OC-03  | Active (2.0)       | Legal, regulatory, and contractual cyber requirements are identified and managed.                      | Compliance register (PCI, GDPR, PDPA, etc.) with owner and review date.                                 |
| GV.OC-04  | Active (2.0)       | Critical objectives/capabilities/services stakeholders rely on are identified and communicated.        | List of “critical services” (login, payments, trading) referenced in BCP/DR and architecture docs.      |
| GV.OC-05  | Active (2.0)       | External services the org depends on are identified and communicated.                                  | Architecture diagram + risk register showing dependencies on AWS, DNS, IdP, payment gateway, etc.       |

---

### 1.2 Risk Management Strategy (GV.RM)

| Code      | Status        | Meaning                                                                                             | Example evidence                                                                                  |
|-----------|---------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| GV.RM-01  | Active (2.0)  | Cyber risk-management objectives are defined and agreed by stakeholders.                           | Approved risk charter stating specific objectives (e.g., max time critical vulns can remain).     |
| GV.RM-02  | Active (2.0)  | Risk appetite and tolerance statements are defined, communicated, and maintained.                  | Documented risk appetite (“no tolerance for customer data loss”) endorsed by board.               |
| GV.RM-03  | Active (2.0)  | Cyber risk mgmt outcomes are included in enterprise risk mgmt processes.                           | ERM report including cyber risk entries alongside finance/operational risks.                      |
| GV.RM-04  | Active (2.0)  | High-level direction for how to respond to risks is defined and communicated.                      | Policy/playbook describing when to mitigate, transfer (insurance), accept, or avoid risk.         |
| GV.RM-05  | Active (2.0)  | Communication lines for cyber risks (incl. supplier risks) are established.                        | Risk or steering committee ToR including supplier risk as agenda item.                            |
| GV.RM-06  | Active (2.0)  | Standardized method for calculating/prioritizing risks is established and communicated.           | Risk scoring methodology (e.g., 1–5 impact/likelihood) used in central risk register.             |
| GV.RM-07  | Active (2.0)  | Strategic opportunities (“positive risks”) are recognized and included in discussions.             | Risk/opportunity log listing “security automation” as opportunity with benefit analysis.          |

---

### 1.3 Cybersecurity Supply Chain Risk Management (GV.SC)

| Code      | Status        | Meaning                                                                                                        | Example evidence                                                                                           |
|-----------|---------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| GV.SC-01  | Active (2.0)  | C-SCRM program (strategy, objectives, policies, processes) is established and agreed.                         | Third-party risk policy + procedure, signed by leadership.                                                |
| GV.SC-02  | Active (2.0)  | Cyber roles/responsibilities for suppliers/customers/partners are defined & coordinated.                      | RACI for vendor onboarding, security reviews, and incident handling, including external parties.          |
| GV.SC-03  | Active (2.0)  | C-SCRM integrated into cyber and ERM, risk assessment, and improvement activities.                            | Vendor risk scores in same ERM tool as internal risks; reviewed in same governance meetings.             |
| GV.SC-04  | Active (2.0)  | Suppliers are identified and prioritized by criticality.                                                       | Vendor inventory with Tier 1/2/3 tags based on data sensitivity and business impact.                       |
| GV.SC-05  | Active (2.0)  | Requirements to handle supply-chain cyber risks are defined & built into contracts/agreements.               | Contract templates including security clauses: encryption, notification SLAs, pen-test obligations, etc.  |
| GV.SC-06  | Active (2.0)  | Planning and due diligence occur before entering supplier/third-party relationships.                          | Pre-contract security questionnaire, SOC 2 review, risk rating before sign-off.                           |
| GV.SC-07  | Active (2.0)  | Supplier/third-party risks (incl. their products/services) are tracked and monitored over the relationship.   | Vendor risk register with periodic review, updated scores, and follow-up actions.                         |
| GV.SC-08  | Active (2.0)  | Relevant suppliers/third parties are included in incident planning, response, and recovery.                   | IR plan with cloud provider/MSSP contacts and joint exercise records.                                     |
| GV.SC-09  | Active (2.0)  | Supply-chain security practices are integrated into cyber/ERM programs and monitored across life cycle.      | KPIs for vendor patch turnaround, issues from audits, tracked and reported.                               |
| GV.SC-10  | Active (2.0)  | C-SCRM plans include activities after partnership/service ends.                                               | Supplier offboarding checklist (data return/deletion, key rotation, account removal).                     |

---

### 1.4 Roles, Responsibilities, and Authorities (GV.RR)

| Code      | Status        | Meaning                                                                                                 | Example |
|-----------|---------------|---------------------------------------------------------------------------------------------------------|---------|
| GV.RR-01  | Active (2.0)  | Leadership is accountable for cyber risk and promotes risk-aware, ethical, improving culture.          | Board/CISO cyber reports and tone-from-the-top communications on security. |
| GV.RR-02  | Active (2.0)  | Cyber roles, responsibilities, and authorities are defined, communicated, understood, and enforced.    | Org chart, job descriptions, and RACI aligned to security responsibilities. |
| GV.RR-03  | Active (2.0)  | Adequate resources are provided to match strategy, roles, and policies.                                | Budget and staffing decisions documented with explicit cyber risk justification. |
| GV.RR-04  | Active (2.0)  | Cybersecurity integrated into HR practices (hiring, onboarding, performance, termination, etc.).       | HR procedures for background checks, onboarding training, and access revocation. |

---

### 1.5 Policy (GV.PO)

| Code      | Status        | Meaning                                                                                                       | Example |
|-----------|---------------|---------------------------------------------------------------------------------------------------------------|---------|
| GV.PO-01  | Active (2.0)  | Policy for managing cyber risks is established based on context/strategy/priorities and is enforced.         | Information Security Policy, approved by leadership, accessible to all staff. |
| GV.PO-02  | Active (2.0)  | That policy is reviewed, updated, communicated, and enforced as things change.                               | Annual policy review log with tracked changes and communications. |

---

### 1.6 Oversight (GV.OV)

| Code      | Status        | Meaning                                                                                                        | Example |
|-----------|---------------|----------------------------------------------------------------------------------------------------------------|---------|
| GV.OV-01  | Active (2.0)  | Outcomes of cyber risk-management strategy are reviewed to adjust direction.                                 | Quarterly security performance & risk review with management actions. |
| GV.OV-02  | Active (2.0)  | Strategy is reviewed/updated to cover current org requirements and risks.                                     | Decision to extend monitoring to new cloud/SaaS after reviewing new business unit. |
| GV.OV-03  | Active (2.0)  | Cyber risk-management performance is measured and reviewed for needed adjustments.                            | KPI/KRI dashboard (MTTD, MTTR, patch SLAs) feeding into improvement backlog. |

---

## 2. IDENTIFY (ID) – Understand Assets & Risk

### 2.1 Asset Management (ID.AM)

| Code      | Status                    | Meaning                                                                                                                 | Example |
|-----------|---------------------------|-------------------------------------------------------------------------------------------------------------------------|---------|
| ID.AM-01  | Active (2.0)              | Inventory of organization-managed hardware is maintained.                                                               | CMDB listing laptops, servers, firewalls with owner and location. |
| ID.AM-02  | Active (2.0)              | Inventory of software, services, and systems is maintained.                                                             | Application & SaaS catalog with owner, version, and data type. |
| ID.AM-03  | Active (2.0)              | Representations (e.g., diagrams) of authorized network communication and data flows are maintained.                    | Network/data-flow diagrams in architecture repo. |
| ID.AM-04  | Active (2.0)              | Inventory of services provided by suppliers is maintained.                                                              | Vendor services list (email, CRM, payment gateway, SMS, etc.). |
| ID.AM-05  | Active (2.0)              | Assets are prioritized by classification, criticality, resources, and mission impact.                                   | Critical/High/Medium tags for assets linked to business processes. |
| ID.AM-06  | **Withdrawn (1.1)**       | Previously about cybersecurity roles for assets; now mapped to **GV.RR-02**, **GV.SC-02**.                             | Align asset ownership and role definitions under GV.RR-02 in your docs. |
| ID.AM-07  | Active (2.0)              | Inventories of key data types and metadata are maintained.                                                              | Data catalog listing PII, financial data, logs, owners, retention. |
| ID.AM-08  | Active (2.0)              | Systems/hardware/software/services/data are managed throughout life cycles.                                             | Joiner-mover-leaver + change + decommission procedures with records. |

---

### 2.2 Business Environment & Governance – legacy (ID.BE, ID.GV)

> These appear in **CSF 1.1** but are **withdrawn in 2.0** and remapped under GV.   

| Code      | Status                | Meaning (older CSF 1.1 intent)                                               | Where it moved in CSF 2.0 |
|-----------|-----------------------|-------------------------------------------------------------------------------|---------------------------|
| ID.BE     | Withdrawn Category    | Business environment (mission, stakeholders, critical services).             | → GV.OC (all)             |
| ID.BE-01  | Withdrawn             | Org role in supply chain identified and communicated.                         | → GV.OC-05                |
| ID.BE-02  | Withdrawn             | Org’s place in critical infrastructure/sector understood.                     | → GV.OC-01                |
| ID.BE-03  | Withdrawn             | Mission/objective priorities defined and communicated.                         | → GV.OC-01                |
| ID.BE-04  | Withdrawn             | Dependencies & critical functions for critical services defined.              | → GV.OC-04, GV.OC-05      |
| ID.BE-05  | Withdrawn             | Resilience requirements for critical services defined.                         | → GV.OC-04                |
| ID.GV     | Withdrawn Category    | Governance of cybersecurity risk.                                             | → GV.PO, GV.OC, GV.RR, GV.RM |
| ID.GV-01  | Withdrawn             | Org cyber policy established and communicated.                                | → GV.PO-01, GV.PO-02      |
| ID.GV-02  | Withdrawn             | Roles/responsibilities aligned with internal & external stakeholders.         | → GV.OC-02, GV.RR, GV.RR-02 |
| ID.GV-03  | Withdrawn             | Legal/regulatory requirements understood and managed.                         | → GV.OC-03                |
| ID.GV-04  | Withdrawn             | Governance & risk processes address cyber risk.                               | → GV.RM-03                |

---

### 2.3 Risk Assessment (ID.RA)

| Code      | Status        | Meaning                                                                                                    | Example |
|-----------|---------------|------------------------------------------------------------------------------------------------------------|---------|
| ID.RA-01  | Active (2.0)  | Vulnerabilities in assets are identified, validated, and recorded.                                        | Regular vuln scans with tickets in a tracking system. |
| ID.RA-02  | Active (2.0)  | Cyber threat intel is received from information-sharing sources.                                          | TI feeds from ISAC, vendors, open-source integrated into SIEM. |
| ID.RA-03  | Active (2.0)  | Internal and external threats are identified and recorded.                                                | Threat register listing phishing, ransomware, fraud, insider, DDoS, etc. |
| ID.RA-04  | Active (2.0)  | Potential impacts and likelihoods of threats exploiting vulns are identified and recorded.                | Risk matrix entries with impact/likelihood scores. |
| ID.RA-05  | Active (2.0)  | Threats, vulns, likelihood, and impact are used to understand inherent risk and prioritize responses.     | Prioritized risk list used to drive mitigation backlog. |
| ID.RA-06  | Active (2.0)  | Risk responses are chosen, prioritized, planned, tracked, and communicated.                              | Risk treatment plan with owners and due dates. |
| ID.RA-07  | Active (2.0)  | Changes/exceptions are managed, risk-assessed, recorded, and tracked.                                    | Change/exception records including risk justification and expiry date. |
| ID.RA-08  | Active (2.0)  | Processes for receiving, analyzing, and responding to vuln disclosures are established.                  | Coordinated vulnerability disclosure policy, triage workflow, response SLAs. |
| ID.RA-09  | Active (2.0)  | Authenticity/integrity of hardware/software assessed before acquisition/use.                             | Supply chain checks, signed binaries, vendor verification. |
| ID.RA-10  | Active (2.0)  | Critical suppliers are assessed before acquisition.                                                       | Third-party security assessment before vendor onboarding approval. |

---

### 2.4 Risk Management Strategy & Supply Chain – legacy (ID.RM, ID.SC)

| Code      | Status             | Meaning (old CSF 1.1 intent)                                                       | Where moved |
|-----------|--------------------|------------------------------------------------------------------------------------|------------|
| ID.RM     | Withdrawn Category | Risk management strategy.                                                         | → GV.RM    |
| ID.RM-01  | Withdrawn          | Risk mgmt priorities, constraints, assumptions established, used in decisions.    | → GV.RM-01, GV.RM-06, GV.RR-03 |
| ID.RM-02  | Withdrawn          | Risk appetite, tolerance defined and communicated.                                | → GV.RM-02, GV.RM-04          |
| ID.RM-03  | Withdrawn          | Risk mgmt processes coordinated and aligned.                                      | → GV.RM-02                    |
| ID.SC     | Withdrawn Category | Supply chain risk mgmt.                                                           | → GV.SC    |
| ID.SC-01  | Withdrawn          | Supply chain risks identified and managed.                                        | → GV.RM-05, GV.SC-01, -06, -09, -10 |
| ID.SC-02  | Withdrawn          | Dependencies and supporting services identified.                                  | → GV.OC-02, GV.SC-03, -04, -07, ID.RA-10 |
| ID.SC-03  | Withdrawn          | Supplier cyber requirements defined.                                              | → GV.SC-05                     |
| ID.SC-04  | Withdrawn          | Supplier risks monitored.                                                         | → GV.SC-07, ID.RA-10           |
| ID.SC-05  | Withdrawn          | Supplier incident processes.                                                      | → GV.SC-08, ID.IM-02           |

---

### 2.5 Improvement (ID.IM)

| Code      | Status        | Meaning                                                                                                | Example |
|-----------|---------------|--------------------------------------------------------------------------------------------------------|---------|
| ID.IM-01  | Active (2.0)  | Improvements identified from evaluations (audits, assessments, reviews).                              | Audit findings tracked as improvement tasks. |
| ID.IM-02  | Active (2.0)  | Improvements identified from security tests/exercises (incl. supplier/third-party exercises).         | Tabletop and red-team lessons-learned turned into backlog items. |
| ID.IM-03  | Active (2.0)  | Improvements identified from normal operational processes and activities.                             | SOC & ops feedback leading to updated runbooks and playbooks. |
| ID.IM-04  | Active (2.0)  | IR and other cyber plans affecting operations are established, communicated, maintained, improved.    | Versioned IR/BCP docs with update history after incidents. |

---

## 3. PROTECT (PR) – Safeguards

### 3.1 Identity Management, Authentication, and Access Control (PR.AA)

| Code      | Status        | Meaning                                                                                        | Example |
|-----------|---------------|------------------------------------------------------------------------------------------------|---------|
| PR.AA-01  | Active (2.0)  | Identities & credentials for users/services/hardware are managed by org.                       | Central IdP for SSO and managed service accounts. |
| PR.AA-02  | Active (2.0)  | Identities are proofed & bound to credentials based on context.                               | HR-approved account creation with ID verification and MFA enrollment. |
| PR.AA-03  | Active (2.0)  | Users, services, and hardware are authenticated.                                              | MFA for staff; mTLS/workload identity between services. |
| PR.AA-04  | Active (2.0)  | Identity assertions (tokens, SSO claims) are protected, conveyed, and verified.               | JWT validation (signature, issuer, audience, expiry) in APIs. |
| PR.AA-05  | Active (2.0)  | Access permissions/entitlements follow policy, least privilege, and SoD; enforced & reviewed. | RBAC roles, quarterly access reviews, separation of dev/ops duties. |
| PR.AA-06  | Active (2.0)  | Physical access to assets is managed, monitored, and enforced according to risk.              | Badge-based access and logs for DC; visitor logs and periodic review. |

#### Legacy Access Control (PR.AC – Withdrawn)

| Code      | Status    | Old meaning                                     | Where moved                     |
|-----------|-----------|-------------------------------------------------|---------------------------------|
| PR.AC-01  | Withdrawn | Logical access control.                         | → PR.AA-01, PR.AA-05            |
| PR.AC-02  | Withdrawn | Physical access control.                        | → PR.AA-06                      |
| PR.AC-03  | Withdrawn | Remote access / network access restrictions.    | → PR.AA-03, PR.AA-05, PR.IR-01  |
| PR.AC-04  | Withdrawn | Access approval.                                | → PR.AA-05                      |
| PR.AC-05  | Withdrawn | Network integrity protections.                  | → PR.IR-01                      |
| PR.AC-06  | Withdrawn | Identity proofing.                              | → PR.AA-02                      |
| PR.AC-07  | Withdrawn | Strong authentication.                          | → PR.AA-03                      |

---

### 3.2 Awareness and Training (PR.AT)

| Code      | Status        | Meaning                                                                                                   | Example |
|-----------|---------------|-----------------------------------------------------------------------------------------------------------|---------|
| PR.AT-01  | Active (2.0)  | All personnel receive awareness/training to do general tasks with security in mind.                      | Annual training + phishing simulations for all staff. |
| PR.AT-02  | Active (2.0)  | People in specialized roles get training to handle security risks relevant to their tasks.               | Secure coding training for devs; DFIR training for SOC analysts. |
| PR.AT-03  | Withdrawn     | Role-based training content split.                                                                       | → PR.AT-01, PR.AT-02 |
| PR.AT-04  | Withdrawn     | Senior executive & management training.                                                                   | → PR.AT-02          |
| PR.AT-05  | Withdrawn     | Third-party training requirements.                                                                       | → PR.AT-02          |

---

### 3.3 Data Security (PR.DS)

| Code      | Status        | Meaning                                                                                                   | Example |
|-----------|---------------|-----------------------------------------------------------------------------------------------------------|---------|
| PR.DS-01  | Active (2.0)  | Confidentiality/integrity/availability of data at rest are protected.                                    | Encrypted DB & storage, RBAC, integrity checks. |
| PR.DS-02  | Active (2.0)  | Confidentiality/integrity/availability of data in transit are protected.                                 | TLS for all external/internal critical traffic; VPN for admin access. |
| PR.DS-03  | Withdrawn     | Data life-cycle management specifics.                                                                    | → ID.AM-08, PR.PS-03 |
| PR.DS-04  | Withdrawn     | Data availability via redundancy.                                                                        | → PR.IR-04           |
| PR.DS-05  | Withdrawn     | Data leak & exfil controls.                                                                              | → PR.DS-01, -02, -10 |
| PR.DS-06  | Withdrawn     | Monitoring of data access/usage.                                                                         | → PR.DS-01, DE.CM-09 |
| PR.DS-07  | Withdrawn     | Network protection for data.                                                                             | → PR.IR-01           |
| PR.DS-08  | Withdrawn     | Data integrity validation for hardware/software.                                                         | → ID.RA-09, DE.CM-09 |
| PR.DS-09  | Withdrawn     | Data retention & disposal.                                                                               | → ID.AM-08           |
| PR.DS-10  | Active (2.0)  | Confidentiality/integrity/availability of data in use are protected.                                    | Field-level access control, tokenization, minimizing raw PII in memory. |
| PR.DS-11  | Active (2.0)  | Data backups are created, protected, maintained, and tested.                                             | Encrypted offsite backups + regular restore tests. |

---

### 3.4 Information Protection Processes & Procedures / Maintenance / Protective Technology – legacy

All of these are **withdrawn categories** and re-mapped:

| Code       | Status    | Old Category / Idea                          | Where moved (high level)                      |
|------------|-----------|----------------------------------------------|-----------------------------------------------|
| PR.IP-01..12 | Withdrawn | Policies, processes, config, continuity etc.| → PR.PS, ID.AM-08, ID.RA, ID.IM, GV.RR-04     |
| PR.MA-01..02 | Withdrawn | Maintenance activities.                     | → ID.AM-08, PR.PS-02/03                       |
| PR.PT-01..05 | Withdrawn | Protective technology controls.             | → PR.PS-01, -04; PR.DS-01; PR.AA-06; PR.IR-01, -03 |

(Use them only when mapping from CSF 1.1.)

---

### 3.5 Platform Security (PR.PS)

| Code      | Status        | Meaning                                                                                               | Example |
|-----------|---------------|-------------------------------------------------------------------------------------------------------|---------|
| PR.PS-01  | Active (2.0)  | Configuration management practices are established and applied.                                      | Hardened baselines, IaC templates, config drift monitoring. |
| PR.PS-02  | Active (2.0)  | Software is maintained, replaced, and removed according to risk.                                    | Patch policy with deadlines; decommission unsupported OS. |
| PR.PS-03  | Active (2.0)  | Hardware is maintained, replaced, and removed according to risk.                                    | Lifecycle plan for firewalls/servers with secure disposal. |
| PR.PS-04  | Active (2.0)  | Log records are generated and made available for continuous monitoring.                             | OS/app/network device logs shipped to SIEM. |
| PR.PS-05  | Active (2.0)  | Installation/execution of unauthorized software is prevented.                                       | Application allow-listing / EDR policies. |
| PR.PS-06  | Active (2.0)  | Secure software development practices are integrated and monitored across SDLC.                     | CI/CD with SAST/SCA, code review, security gates before prod. |

---

### 3.6 Technology Infrastructure Resilience (PR.IR)

| Code      | Status        | Meaning                                                                                           | Example |
|-----------|---------------|---------------------------------------------------------------------------------------------------|---------|
| PR.IR-01  | Active (2.0)  | Networks/environments protected from unauthorized logical access/usage.                          | Segmentation, firewalls, zero-trust network access. |
| PR.IR-02  | Active (2.0)  | Technology assets are protected from environmental threats.                                      | DR datacenter, multi-region cloud, redundant power & cooling. |
| PR.IR-03  | Active (2.0)  | Mechanisms are implemented to meet resilience requirements in normal and adverse situations.     | Multi-AZ deployments, failover tests, DDoS protection. |
| PR.IR-04  | Active (2.0)  | Adequate resource capacity is maintained to ensure availability.                                 | Capacity planning, load testing, autoscaling rules. |

---

## 4. DETECT (DE) – Monitoring & Analysis

### 4.1 Continuous Monitoring (DE.CM)

| Code      | Status        | Meaning                                                                                                   | Example |
|-----------|---------------|-----------------------------------------------------------------------------------------------------------|---------|
| DE.CM-01  | Active (2.0)  | Networks and network services are monitored for potentially adverse events.                              | IDS/IPS, flow logs, firewall logs into SIEM with alerts. |
| DE.CM-02  | Active (2.0)  | Physical environment is monitored for potentially adverse events.                                        | Badge logs, door alarms, CCTV monitoring DC access. |
| DE.CM-03  | Active (2.0)  | Personnel activity and technology usage are monitored for potentially adverse events.                    | UEBA/CASB monitoring unusual logins, data movements. |
| DE.CM-04  | Withdrawn     | Legacy log/monitoring coverage.                                                                          | → DE.CM-01, DE.CM-09 |
| DE.CM-05  | Withdrawn     | Legacy monitoring for indicators-of-attack.                                                              | → DE.CM-01, DE.CM-09 |
| DE.CM-06  | Active (2.0)  | External service-provider activities/services are monitored for potentially adverse events.              | Cloud/SaaS logs (CloudTrail, Okta, M365) in SIEM with alerts. |
| DE.CM-07  | Withdrawn     | Extended monitoring of users, networks, external services combined.                                      | → DE.CM-01, -03, -06, -09 |
| DE.CM-08  | Withdrawn     | Monitoring of security tools effectiveness.                                                              | → ID.RA-01            |
| DE.CM-09  | Active (2.0)  | Computing hardware/software, runtime env, and their data are monitored for potentially adverse events.   | EDR/agent telemetry, container runtime security, FIM. |

---

### 4.2 Adverse Event Analysis (DE.AE)

| Code      | Status        | Meaning                                                                                                   | Example |
|-----------|---------------|-----------------------------------------------------------------------------------------------------------|---------|
| DE.AE-01  | Withdrawn     | Older “event detection baselines”; folded elsewhere.                                                     | → ID.AM-03 |
| DE.AE-02  | Active (2.0)  | Potentially adverse events are analyzed to better understand what is happening.                          | Analyst reviewing alert timeline and host/process data. |
| DE.AE-03  | Active (2.0)  | Information is correlated from multiple sources.                                                         | SIEM rules combining VPN, EDR, IAM, and app logs. |
| DE.AE-04  | Active (2.0)  | Estimated impact and scope of adverse events are determined.                                             | Documenting impacted users, systems, and data sets. |
| DE.AE-05  | Withdrawn     | Old “incident declaration” text, moved.                                                                 | → DE.AE-08 |
| DE.AE-06  | Active (2.0)  | Information on adverse events is provided to authorized staff and tools.                                | Tickets and pager alerts automatically sent with full context. |
| DE.AE-07  | Active (2.0)  | Threat intel and contextual info are integrated into analysis.                                          | Enrich alerts with TI (malicious IP lists, malware families). |
| DE.AE-08  | Active (2.0)  | Incidents are declared when adverse events meet defined criteria.                                       | Incident classification runbook with thresholds for SEV1–4. |

---

### 4.3 Detection Processes (DE.DP – legacy)

| Code      | Status    | Summary (old intent)                                        | Where moved                                 |
|-----------|-----------|-------------------------------------------------------------|---------------------------------------------|
| DE.DP-01  | Withdrawn | Defined detection roles/processes.                          | → GV.RR-02                                  |
| DE.DP-02  | Withdrawn | Formal detection policies/procedures.                       | → DE.AE                                     |
| DE.DP-03  | Withdrawn | Testing and improving detection processes.                  | → ID.IM-02                                  |
| DE.DP-04  | Withdrawn | Communication of detection activities/results.              | → DE.AE-06                                  |
| DE.DP-05  | Withdrawn | Lessons learned from detection activities.                  | → ID.IM, ID.IM-03                            |

---

## 5. RESPOND (RS) – Incident Handling

### 5.1 Response Planning (RS.RP – legacy)

| Code      | Status    | Meaning (old)                   | Where moved   |
|-----------|-----------|----------------------------------|---------------|
| RS.RP-01  | Withdrawn | Response plan established.      | → RS.MA-01    |

---

### 5.2 Incident Management (RS.MA)

| Code      | Status        | Meaning                                                                                                  | Example |
|-----------|---------------|----------------------------------------------------------------------------------------------------------|---------|
| RS.MA-01  | Active (2.0)  | Incident response plan is executed with relevant third parties once incident is declared.               | IR playbook listing internal/external roles and steps. |
| RS.MA-02  | Active (2.0)  | Incident reports/alerts are triaged and validated.                                                      | SOC triage workflow with runbooks for common alerts. |
| RS.MA-03  | Active (2.0)  | Incidents are categorized and prioritized.                                                              | Severity model (SEV1–4) and service-impact definitions. |
| RS.MA-04  | Active (2.0)  | Incidents are escalated/elevated as needed.                                                             | On-call escalation matrix and management notification policy. |
| RS.MA-05  | Active (2.0)  | Criteria for initiating incident recovery are applied.                                                  | Defined handover point from “response” to “recovery” phases. |

---

### 5.3 Incident Analysis (RS.AN)

| Code      | Status        | Meaning                                                                                                   | Example |
|-----------|---------------|-----------------------------------------------------------------------------------------------------------|---------|
| RS.AN-01  | Withdrawn     | Initial analysis of incident info.                                                                      | → RS.MA-02 |
| RS.AN-02  | Withdrawn     | Triaging and categorizing events.                                                                      | → RS.MA-02, RS.MA-03, RS.MA-04 |
| RS.AN-03  | Active (2.0)  | Analysis determines what happened and finds root cause.                                                 | Root cause analysis doc with timeline and cause. |
| RS.AN-04  | Withdrawn     | Mapping incidents to categories.                                                                        | → RS.MA-03 |
| RS.AN-05  | Withdrawn     | Use of vuln disclosure/information to improve response.                                                 | → ID.RA-08 |
| RS.AN-06  | Active (2.0)  | Actions during investigation are recorded; integrity/provenance of records is preserved.               | Case management tool logging every IR step and evidence hash. |
| RS.AN-07  | Active (2.0)  | Incident data and metadata are collected with integrity and provenance preserved.                       | Forensic images/logs stored in secure evidence repository. |
| RS.AN-08  | Active (2.0)  | Incident magnitude is estimated and validated.                                                           | Impact assessment summarizing affected systems/users/data. |

---

### 5.4 Incident Response Reporting and Communication (RS.CO)

| Code      | Status        | Meaning                                                                                                 | Example |
|-----------|---------------|---------------------------------------------------------------------------------------------------------|---------|
| RS.CO-01  | Withdrawn     | Training about communication / awareness.                                                              | → PR.AT-01 |
| RS.CO-02  | Active (2.0)  | Internal and external stakeholders are notified of incidents.                                          | Incident notification emails/letters to regulators, partners, management. |
| RS.CO-03  | Active (2.0)  | Information is shared with designated internal and external stakeholders.                             | Secure portal/encrypted email sharing IOCs and status updates. |
| RS.CO-04  | Withdrawn     | Specific communications procedures.                                                                    | → RS.MA-01, RS.MA-04 |
| RS.CO-05  | Withdrawn     | Lessons learned from comms.                                                                            | → RS.CO-03 |

---

### 5.5 Incident Mitigation (RS.MI) & Improvements (RS.IM – legacy)

| Code      | Status        | Meaning                                                                                                 | Example |
|-----------|---------------|---------------------------------------------------------------------------------------------------------|---------|
| RS.MI-01  | Active (2.0)  | Incidents are contained.                                                                               | Isolating hosts, blocking malicious IPs, disabling compromised accounts. |
| RS.MI-02  | Active (2.0)  | Incidents are eradicated.                                                                              | Removing malware, patching exploited vulns, cleaning persistence. |
| RS.MI-03  | Withdrawn     | Longer-term mitigation strategy.                                                                       | → ID.RA-06 |
| RS.IM-01  | Withdrawn     | Post-incident improvements.                                                                            | → ID.IM-03, ID.IM-04 |
| RS.IM-02  | Withdrawn     | Testing/checking response improvements.                                                                | → ID.IM-03 |

---

## 6. RECOVER (RC) – Restore & Communicate

### 6.1 Incident Recovery Plan Execution (RC.RP)

| Code      | Status        | Meaning                                                                                                        | Example |
|-----------|---------------|----------------------------------------------------------------------------------------------------------------|---------|
| RC.RP-01  | Active (2.0)  | Recovery portion of IR plan is executed once initiated.                                                       | Recovery playbook invoked after containment. |
| RC.RP-02  | Active (2.0)  | Recovery actions are selected, scoped, prioritized, and performed.                                           | Workplan prioritizing restoration of critical services and data. |
| RC.RP-03  | Active (2.0)  | Integrity of backups/restoration assets is verified before restore.                                         | Restore to sandbox and hash-compare before production restore. |
| RC.RP-04  | Active (2.0)  | Critical mission functions and cyber risk mgmt considered when defining post-incident norms.                 | Decision log documenting new SLAs and temporary workarounds. |
| RC.RP-05  | Active (2.0)  | Integrity of restored assets is verified; systems/services restored; normal status confirmed.               | Validated tests, monitoring, and approvals prior to declaring “back to normal”. |
| RC.RP-06  | Active (2.0)  | Criteria to end recovery are applied and incident documentation is completed.                               | Checklist ensuring RCA done, lessons learned captured, incident formally closed. |

---

### 6.2 Incident Recovery Communication (RC.CO, RC.IM)

| Code      | Status        | Meaning                                                                                           | Example |
|-----------|---------------|---------------------------------------------------------------------------------------------------|---------|
| RC.CO-01  | Withdrawn     | Internal communications guidance for recovery (legacy).                                          | → RC.CO-04 |
| RC.CO-02  | Withdrawn     | External comms guidance for recovery (legacy).                                                   | → RC.CO-04 |
| RC.CO-03  | Active (2.0)  | Recovery activities and progress are communicated to designated internal and external stakeholders.| Daily or weekly status updates for leadership/customers/regulators during recovery. |
| RC.CO-04  | Active (2.0)  | Public updates on incident recovery are shared using approved methods/messaging.                 | Status page posts and customer emails vetted by Legal/Comms. |
| RC.IM-01  | Withdrawn     | Recovery improvement items.                                                                      | → ID.IM-03, ID.IM-04 |
| RC.IM-02  | Withdrawn     | Testing/verification of recovery improvements.                                                   | → ID.IM-03 |

---

## Implementation Steps (7 Steps)

1. Prioritize and Scope
2. Orientation
3. Develop a Profile
4. Conduct a Risk Assessment
5. Createa a Target Profile
6. Analyze & Prioritize Gaps
7. Implementation

















