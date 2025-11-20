# NIST CSF 2.0 – Full Cheat Sheet (GV, ID, PR, DE, RS, RC)

> This note summarizes **all CSF 2.0 Core outcomes** (Subcategories) across:
> - GOVERN (GV)
> - IDENTIFY (ID)
> - PROTECT (PR)
> - DETECT (DE)
> - RESPOND (RS)
> - RECOVER (RC)
>
> For each code (e.g., **GV.OC-04**), you get:
> - **Plain-English meaning**
> - **Concrete, practical example**

---

## 1. GOVERN (GV)
**The organization’s cybersecurity risk management strategy, expectations, and policy are established, communicated, and monitored.**

### GV.OC – Organizational Context

- **GV.OC-01 – Mission informs cyber risk decisions**  
  *Meaning:* Cybersecurity priorities are derived from the organization’s mission and business objectives, not just “best practices.”  
  *Example:* A fintech company sets its top security priority as protecting transaction integrity because its mission is to provide trusted digital payments.

- **GV.OC-02 – Stakeholders and their expectations are understood**  
  *Meaning:* The organization knows who its internal/external stakeholders are and what they expect regarding cybersecurity (e.g., uptime, privacy, compliance).  
  *Example:* Product, legal, regulators, and key customers are mapped as stakeholders with documented expectations for RTO, RPO, and data protection.

- **GV.OC-03 – Legal, regulatory, contractual obligations are known and managed**  
  *Meaning:* Cyber-related laws, privacy rules, and contract clauses are identified and tracked so the org doesn’t accidentally violate them.  
  *Example:* The legal team maintains a register of applicable regulations (e.g., GDPR, PCI DSS, PDPA) and maps them to internal policies and controls.

- **GV.OC-04 – Services critical to external stakeholders are understood and communicated**  
  *Meaning:* The org knows which services/functions outsiders depend on (customers, partners, public) and treats them as “critical” in risk management.  
  *Example:* A SaaS provider flags its login, billing, and API gateway as “externally critical” and ensures they are prioritized in BCP and DR plans.

- **GV.OC-05 – Dependencies on others’ services are understood and communicated**  
  *Meaning:* The org knows which external services it relies on (e.g., cloud providers, ISPs) and factors them into its risk posture.  
  *Example:* The company documents dependencies on AWS, a payment gateway, and a DNS provider in its risk register and continuity plans.

---

### GV.RM – Risk Management Strategy

- **GV.RM-01 – Risk management objectives agreed by stakeholders**  
  *Meaning:* The org defines what it wants to achieve with cyber risk management (e.g., limit downtime, reduce data breach likelihood) and gets buy-in.  
  *Example:* Leadership approves objectives like “no more than 4 hours downtime for critical systems per year” and “detect high-severity incidents within 15 minutes.”

- **GV.RM-02 – Risk appetite and tolerance statements defined and shared**  
  *Meaning:* The org describes how much risk it is willing to take (appetite) and maximum acceptable risk (tolerance) for different scenarios.  
  *Example:* The board states it has low tolerance for regulatory non-compliance but higher tolerance for minor internal system outages.

- **GV.RM-03 – Cyber risk integrated into enterprise risk management (ERM)**  
  *Meaning:* Cyber risk is treated as part of overall business risk (like financial and operational), not in isolation.  
  *Example:* Cyber risk scenarios (e.g., ransomware on core ERP) are included in the same ERM dashboard as FX risk and credit risk.

- **GV.RM-04 – Strategic direction for risk response options is set**  
  *Meaning:* The org clarifies when to accept, mitigate, transfer (insure), or avoid cyber risks and aligns budgets accordingly.  
  *Example:* Management decides to purchase cyber insurance for catastrophic scenarios but to mitigate routine phishing via training and controls.

- **GV.RM-05 – Communication lines for cyber risk are defined**  
  *Meaning:* There is a clear path for risk information to flow across business units, security, suppliers, and leadership.  
  *Example:* A formal risk committee meets monthly and receives risk reports from security, IT, and major vendors.

- **GV.RM-06 – Standard method for measuring & prioritizing risk is used**  
  *Meaning:* The org uses common criteria or scoring (e.g., qualitative or quantitative) to rate and prioritize risks.  
  *Example:* All risks are logged in a tool with likelihood/impact scoring (e.g., low/medium/high or FAIR-style quantitative analysis).

- **GV.RM-07 – Positive opportunities (upside risk) are considered**  
  *Meaning:* Cyber investments are also viewed as enablers (e.g., trust, new markets), not just as cost/defense.  
  *Example:* Strong security posture is used as a selling point in RFPs, helping the company win contracts.

---

### GV.RR – Roles, Responsibilities, and Authorities

- **GV.RR-01 – Leadership accountable for cybersecurity and culture**  
  *Meaning:* Executives own cyber risk, not just the CISO; they promote an ethical, risk-aware culture.  
  *Example:* The CEO regularly communicates the importance of reporting phishing and supports budget requests for security.

- **GV.RR-02 – Cyber roles and responsibilities are defined and enforced**  
  *Meaning:* Specific people/teams have clearly assigned duties around cyber risk management.  
  *Example:* A RACI matrix shows who owns vulnerability management, incident response, and supplier assessments.

- **GV.RR-03 – Resources allocated in line with strategy and roles**  
  *Meaning:* The org funds people, tools, time, and training consistent with its risk strategy.  
  *Example:* Headcount is added to the SOC after a risk assessment shows monitoring gaps.

- **GV.RR-04 – Cybersecurity is integrated into HR practices**  
  *Meaning:* HR supports security through hiring, background checks, onboarding/offboarding, performance goals, and disciplinary processes.  
  *Example:* Security responsibilities are included in job descriptions and performance reviews for system admins.

---

### GV.PO – Policy

- **GV.PO-01 – Cybersecurity policy based on context and strategy**  
  *Meaning:* The org has an overarching security policy aligned with mission, risk appetite, and legal requirements.  
  *Example:* A top-level “Information Security Policy” sets expectations for access control, data handling, and incident reporting.

- **GV.PO-02 – Policy is reviewed, updated, and enforced**  
  *Meaning:* Policies are periodically refreshed (e.g., annually) and are not just documents on a shelf.  
  *Example:* Policies are re-approved each year, with updates for new cloud services and MFA requirements, and enforced via audits.

---

### GV.OV – Oversight

- **GV.OV-01 – Strategy outcomes are reviewed to adjust direction**  
  *Meaning:* Leadership checks whether cyber strategy is working and adjusts course where needed.  
  *Example:* Management sees that phishing incidents remain high and prioritizes additional phishing simulations and training.

- **GV.OV-02 – Strategy updated to cover evolving requirements & risks**  
  *Meaning:* New business lines, technologies, and regulations trigger strategy updates.  
  *Example:* When the company adopts AI-based services, the cyber strategy expands to cover model and data risks.

- **GV.OV-03 – Cyber performance metrics inform adjustments**  
  *Meaning:* KPIs and KRIs (e.g., mean time to detect/respond) drive improvements.  
  *Example:* The board receives quarterly metrics like number of critical vulnerabilities and time to patch and demands faster remediation.

---

### GV.SC – Cybersecurity Supply Chain Risk Management (C-SCRM)

- **GV.SC-01 – C-SCRM program and processes are established**  
  *Meaning:* The org has a formal program to manage cyber risks from suppliers and third parties.  
  *Example:* There is a documented C-SCRM policy, vendor tiering, and standard due diligence checklist.

- **GV.SC-02 – Supplier/customer/partner roles are defined and coordinated**  
  *Meaning:* Who does what in the shared security model is clear and agreed.  
  *Example:* A cloud contract clearly states provider vs customer responsibilities (e.g., shared responsibility model).

- **GV.SC-03 – Supply chain risk management integrated into ERM & cyber**  
  *Meaning:* Supplier risks are treated as part of core cyber and enterprise risk processes.  
  *Example:* Critical vendor issues appear on the same risk register as internal system risks.

- **GV.SC-04 – Suppliers are known and prioritized by criticality**  
  *Meaning:* The org maintains a supplier inventory and tags high-impact ones.  
  *Example:* Payment processors and IDPs are flagged as “Tier 1 critical” in the vendor list.

- **GV.SC-05 – Cyber requirements baked into contracts and agreements**  
  *Meaning:* Contracts include security clauses (e.g., incident notification, minimum controls).  
  *Example:* DPAs and SLAs demand 24-hour breach notification and specific encryption requirements.

- **GV.SC-06 – Pre-contract due diligence is performed**  
  *Meaning:* Vendors are assessed before onboarding, not after a breach.  
  *Example:* Security questionnaires, SOC 2 reports, and pen test summaries must be reviewed before signing.

- **GV.SC-07 – Supplier risks tracked across the relationship lifecycle**  
  *Meaning:* Risks from suppliers are monitored, reassessed, and addressed regularly.  
  *Example:* Annual re-assessment of critical vendors, with follow-up on any new audit findings.

- **GV.SC-08 – Suppliers included in incident planning and exercises**  
  *Meaning:* Key suppliers join incident simulations and are in your IR runbooks.  
  *Example:* The DR exercise includes the cloud provider and MSSP to test joint response.

- **GV.SC-09 – Supply chain security practices integrated and monitored**  
  *Meaning:* Supply-chain security is part of the bigger risk programs and tracked over product life cycles.  
  *Example:* A secure procurement process checks SBOMs and firmware integrity for all new hardware.

- **GV.SC-10 – Offboarding/termination activities planned for suppliers**  
  *Meaning:* The org has a plan for when a supplier relationship ends (e.g., data return, access revocation).  
  *Example:* Offboarding checklist ensures VPN/SSO access is revoked and all customer data is securely deleted.

---

## 2. IDENTIFY (ID)
**The organization’s current cybersecurity risks are understood.**

### ID.AM – Asset Management

- **ID.AM-01 – Hardware inventory maintained**  
  *Meaning:* The org knows what physical devices it owns/uses and by whom.  
  *Example:* CMDB or asset tool tracks laptops, servers, switches, with owner and location.

- **ID.AM-02 – Software, services, and systems inventory maintained**  
  *Meaning:* All applications, services, and systems are cataloged.  
  *Example:* The organization maintains a system inventory including internal apps, SaaS, and core backend services.

- **ID.AM-03 – Network communications and data flows mapped**  
  *Meaning:* The org understands how systems talk to each other and where data moves.  
  *Example:* A current data flow diagram shows traffic between web front-end, API layer, and database.

- **ID.AM-04 – Supplier services inventory maintained**  
  *Meaning:* Services provided by third parties are documented.  
  *Example:* A list shows which vendors provide email, logging, customer support platforms, etc.

- **ID.AM-05 – Assets prioritized by classification and criticality**  
  *Meaning:* Not all assets are equal; crown jewels get more protection.  
  *Example:* Payment systems and identity providers marked as “critical,” dev test environments marked “low.”

- **ID.AM-07 – Data and metadata inventories maintained**  
  *Meaning:* The org knows what data types it has, where they live, and context (owner, sensitivity).  
  *Example:* A data catalog documents PII, financial data, and logs with labels like “confidential” or “public.”

- **ID.AM-08 – Assets managed across their life cycles**  
  *Meaning:* Assets go through defined stages (onboarding, use, retirement) with controls at each stage.  
  *Example:* Laptops are imaged at onboarding, regularly patched, and securely wiped/disposed at end-of-life.

---

### ID.RA – Risk Assessment

- **ID.RA-01 – Vulnerabilities in assets identified, validated, and recorded**  
  *Meaning:* The org actively discovers and tracks vulnerabilities in systems, apps, and infra.  
  *Example:* Regular scans and bug bounty findings are logged in a vulnerability management system.

- **ID.RA-02 – Threat intelligence received from sharing forums & sources**  
  *Meaning:* The org consumes relevant intel feeds (industry groups, ISACs, vendors).  
  *Example:* Subscriptions to threat intel feeds and ISAC emails inform SOC detection rules.

- **ID.RA-03 – Internal and external threats identified and recorded**  
  *Meaning:* The org tracks potential threats from insiders, criminals, nation states, etc.  
  *Example:* A threat model lists scenarios like insider data theft and credential stuffing attacks.

- **ID.RA-04 – Impact and likelihood of threats exploiting vulnerabilities assessed**  
  *Meaning:* Risks are evaluated based on how likely and how damaging they are.  
  *Example:* A critical RCE on internet-facing apps is rated as high likelihood/high impact.

- **ID.RA-05 – Inherent risk understood and used to prioritize response**  
  *Meaning:* Risk is evaluated before considering controls to show where the biggest dangers are.  
  *Example:* A risk heatmap highlights that a legacy core banking app has very high inherent risk.

- **ID.RA-06 – Risk responses selected, prioritized, planned, tracked, communicated**  
  *Meaning:* The org chooses what to do with each risk (accept/mitigate/transfer/avoid) and tracks action plans.  
  *Example:* A POA&M lists each risk, owner, due dates, and status.

- **ID.RA-07 – Changes and exceptions managed, assessed, and tracked**  
  *Meaning:* Changes to systems or policy exceptions are treated as risk events and recorded.  
  *Example:* An exception to disable MFA for a system is time-limited, risk-assessed, and logged.

- **ID.RA-08 – Vulnerability disclosure process established**  
  *Meaning:* The org has a clear process for receiving and handling vulnerability reports (e.g., via security.txt).  
  *Example:* A public “Responsible Disclosure” page describes how researchers can report issues.

- **ID.RA-09 – Authenticity and integrity of hardware/software checked before use**  
  *Meaning:* The org verifies that what it buys/installs is genuine and untampered.  
  *Example:* Firmware and software images are validated using checksums and trusted sources.

- **ID.RA-10 – Critical suppliers assessed before acquisition**  
  *Meaning:* High-impact vendors are security-assessed before onboarding.  
  *Example:* Before choosing a new cloud-based CRM, the security team reviews SOC 2 reports and security posture.

---

### ID.IM – Improvement

- **ID.IM-01 – Improvements identified from evaluations (audits, reviews)**  
  *Meaning:* The org learns from internal/external audits and assessments.  
  *Example:* ISO 27001 audit findings are fed into the security improvement roadmap.

- **ID.IM-02 – Improvements identified from tests and exercises**  
  *Meaning:* Pen tests, red-teaming, DR exercises, and IR simulations drive changes.  
  *Example:* A tabletop exercise reveals unclear escalation paths, leading to IR plan updates.

- **ID.IM-03 – Improvements identified from daily operations**  
  *Meaning:* Lessons learned from real incidents or operational issues are captured.  
  *Example:* A recurring misconfiguration leads to standardizing IaC templates.

- **ID.IM-04 – IR and other cyber plans created, updated, and improved**  
  *Meaning:* Incident response and related plans are living documents.  
  *Example:* After a ransomware incident, the IR playbook and backup strategy are revised.

---

## 3. PROTECT (PR)
**Safeguards to manage the organization’s cybersecurity risks are used.**

### PR.AA – Identity Management, Authentication, and Access Control

- **PR.AA-01 – Identities and credentials are managed**  
  *Meaning:* The org lifecycle-manages user/service accounts and credentials (create, modify, revoke).  
  *Example:* HR onboarding triggers automatic account provisioning; offboarding disables access on last day.

- **PR.AA-02 – Identities are proofed and bound to credentials**  
  *Meaning:* The org verifies identities appropriately before issuing credentials (KYC, HR checks, strong verification).  
  *Example:* Admin access requires in-person identity verification plus strong ID documents.

- **PR.AA-03 – Users, services, and hardware are authenticated**  
  *Meaning:* All access is properly authenticated (MFA, keys, certificates, etc.).  
  *Example:* Admin logins require MFA and SSH keys; services authenticate using mutual TLS.

- **PR.AA-04 – Identity assertions protected and verified**  
  *Meaning:* Tokens, SAML assertions, JWTs, etc., are securely handled, validated, and not easily forged.  
  *Example:* APIs validate JWT signature, issuer, audience, and expiration before granting access.

- **PR.AA-05 – Access permissions defined, enforced, and reviewed**  
  *Meaning:* Least privilege, SoD, and periodic access reviews are in place.  
  *Example:* Quarterly access reviews ensure that only finance staff can approve payments above a threshold.

- **PR.AA-06 – Physical access is controlled and monitored**  
  *Meaning:* Doors, server rooms, and other areas are access-controlled and logged.  
  *Example:* Badge access is required to enter the data center; entry/exit logs are reviewed.

---

### PR.AT – Awareness and Training

- **PR.AT-01 – General staff trained for secure behavior**  
  *Meaning:* All staff receive baseline awareness on phishing, passwords, reporting incidents, etc.  
  *Example:* Mandatory annual e-learning plus phishing simulations.

- **PR.AT-02 – Specialized roles receive deeper training**  
  *Meaning:* Admins, devs, SOC analysts, etc., get role-specific security training.  
  *Example:* Developers attend secure coding workshops and get OWASP-based guidance.

---

### PR.DS – Data Security

- **PR.DS-01 – Data-at-rest protected (CIA)**  
  *Meaning:* Data stored on disks, DBs, backups, etc., is protected for confidentiality, integrity, and availability.  
  *Example:* Full-disk encryption on laptops and encryption at rest for cloud storage.

- **PR.DS-02 – Data-in-transit protected (CIA)**  
  *Meaning:* Data moving over networks is protected (e.g., TLS, VPNs, integrity checks).  
  *Example:* All external web apps enforce HTTPS using modern TLS configurations.

- **PR.DS-10 – Data-in-use protected (CIA)**  
  *Meaning:* Sensitive data is protected while being processed (e.g., memory, application layer).  
  *Example:* Tokens instead of raw card numbers used in payment processing pipelines.

- **PR.DS-11 – Backups created, protected, maintained, and tested**  
  *Meaning:* Backups exist, are secure, and are regularly tested for successful restore.  
  *Example:* Secure, offline backups are tested quarterly with full restoration drills.

---

### PR.PS – Platform Security

- **PR.PS-01 – Configuration management practices in place**  
  *Meaning:* Secure baselines, configuration standards, and change control are used.  
  *Example:* Hardened OS baseline applied via configuration management tools (e.g., Ansible, DSC).

- **PR.PS-02 – Software maintained, replaced, removed by risk**  
  *Meaning:* Patch management and retirement strategies are in place.  
  *Example:* Monthly patch cycles for servers; EOL software is prioritized for migration.

- **PR.PS-03 – Hardware maintained, replaced, removed by risk**  
  *Meaning:* Old or unsupported hardware is phased out systematically.  
  *Example:* End-of-support firewalls replaced per a scheduled lifecycle plan.

- **PR.PS-04 – Logs generated and available for monitoring**  
  *Meaning:* Systems and apps produce relevant logs, sent to central monitoring.  
  *Example:* Syslog and application logs are shipped to SIEM with retention and search.

- **PR.PS-05 – Unauthorized software prevented from execution**  
  *Meaning:* Application allow-lists, EDR, or similar mechanisms control software execution.  
  *Example:* Only signed, approved binaries can run on production servers.

- **PR.PS-06 – Secure SDLC practices integrated and monitored**  
  *Meaning:* Security is part of the software lifecycle (requirements, design, code, test, deploy).  
  *Example:* SAST, DAST, and dependency scanning integrated into CI/CD with gates.

---

### PR.IR – Technology Infrastructure Resilience

- **PR.IR-01 – Networks/environments protected from unauthorized logical access**  
  *Meaning:* Segmentation, firewalls, NAC, and zero-trust principles reduce unauthorized access.  
  *Example:* Production network segmented from office network; access via VPN + zero trust.

- **PR.IR-02 – Technology assets protected from environmental threats**  
  *Meaning:* Physical and environmental controls (power, cooling, fire, flood) protect equipment.  
  *Example:* Data centers with redundant power, fire suppression, and environmental monitoring.

- **PR.IR-03 – Mechanisms support resilience in normal and adverse situations**  
  *Meaning:* Redundancy and failover capabilities keep services running amid faults.  
  *Example:* Active-passive database clusters and geo-redundant deployments.

- **PR.IR-04 – Capacity maintained to ensure availability**  
  *Meaning:* Resources (compute, storage, bandwidth) are sufficient under normal and peak load.  
  *Example:* Capacity planning exercises ensure systems can handle peak shopping seasons.

---

## 4. DETECT (DE)
**Possible cybersecurity attacks and compromises are found and analyzed.**

### DE.CM – Continuous Monitoring

- **DE.CM-01 – Networks and network services monitored for adverse events**  
  *Meaning:* Network traffic and services are continuously watched for suspicious activity.  
  *Example:* IDS/IPS, NDR, and firewall logs monitored 24/7 by a SOC.

- **DE.CM-02 – Physical environment monitored for adverse events**  
  *Meaning:* Physical security systems detect intrusion, tampering, environmental anomalies.  
  *Example:* Access control logs, CCTV, and environmental sensors integrated into monitoring.

- **DE.CM-03 – Personnel activity and technology usage monitored**  
  *Meaning:* User and endpoint activities are monitored for anomalies and risky behavior.  
  *Example:* UEBA tools detect unusual login times, impossible travel, and abnormal data access.

- **DE.CM-06 – External service providers monitored**  
  *Meaning:* Vendor activity and outsourced services are monitored for anomalies and incidents.  
  *Example:* Logs from MSSP and cloud platforms are ingested into your SIEM and reviewed.

- **DE.CM-09 – Computing hardware/software and data monitored**  
  *Meaning:* Host and application-level monitoring identifies suspicious or anomalous behavior.  
  *Example:* EDR agents and application logs detect unexpected process executions and config changes.

---

### DE.AE – Adverse Event Analysis

- **DE.AE-02 – Potentially adverse events analyzed to understand activity**  
  *Meaning:* Alerts are investigated to understand what actually happened.  
  *Example:* An analyst reviews an alert about unusual outbound traffic and traces it to a malware infection.

- **DE.AE-03 – Information correlated from multiple sources**  
  *Meaning:* Logs, alerts, intel, and context are combined for better analysis.  
  *Example:* SIEM correlates AV alerts, firewall logs, and identity logs to form a single incident.

- **DE.AE-04 – Impact and scope of adverse events understood**  
  *Meaning:* The org determines what systems/data were affected and how badly.  
  *Example:* An incident report shows which servers were encrypted and what data was exposed.

- **DE.AE-06 – Information on adverse events provided to authorized staff/tools**  
  *Meaning:* Relevant people and tools have access to event data for investigation and follow-up.  
  *Example:* Forensic team is granted access to logs and disk images via a secure case system.

- **DE.AE-07 – Threat intel and context integrated into analysis**  
  *Meaning:* Analysts use threat intelligence and contextual info during triage and investigation.  
  *Example:* Hashes found on an endpoint are checked against threat intel feeds to identify known malware.

- **DE.AE-08 – Incidents declared based on defined criteria**  
  *Meaning:* Clear thresholds/mechanisms exist for when an event becomes a formal “incident.”  
  *Example:* A playbook states that any confirmed exfiltration of PII triggers an incident declaration and escalation.

---

## 5. RESPOND (RS)
**Actions regarding a detected cybersecurity incident are taken.**

### RS.MA – Incident Management

- **RS.MA-01 – IR plan executed with relevant third parties when incident declared**  
  *Meaning:* When an incident is confirmed, the organization follows a documented plan involving necessary external parties.  
  *Example:* A ransomware incident triggers activation of the IR plan including legal counsel and the incident response retainer vendor.

- **RS.MA-02 – Incident reports triaged and validated**  
  *Meaning:* Reports/alerts are reviewed to confirm if they are real incidents or false positives.  
  *Example:* SOC screens phishing reports from employees and validates which ones are malicious.

- **RS.MA-03 – Incidents categorized and prioritized**  
  *Meaning:* Incidents are classified (e.g., P0–P3) based on impact and urgency.  
  *Example:* A compromised domain controller is treated as P0; a single malware-infected workstation as P2.

- **RS.MA-04 – Incidents escalated as needed**  
  *Meaning:* Serious incidents are escalated to higher levels (CISO, execs, board) per defined criteria.  
  *Example:* Breaches with regulatory impact are escalated to legal and executive leadership.

- **RS.MA-05 – Criteria for initiating recovery are applied**  
  *Meaning:* Clear conditions define when the org can move from response to recovery.  
  *Example:* Recovery begins only after containment is confirmed (no new malicious traffic for 24 hours).

---

### RS.AN – Incident Analysis

- **RS.AN-03 – Analysis performed to reconstruct events and root cause**  
  *Meaning:* The org investigates what happened, how, and why.  
  *Example:* Forensics traces initial compromise to a spear-phishing email and identifies the exploited vulnerability.

- **RS.AN-06 – Actions during investigation recorded and protected**  
  *Meaning:* Investigation steps are logged; evidence chain of custody is preserved.  
  *Example:* IR handlers document each action in an incident management system with timestamps.

- **RS.AN-07 – Incident data and metadata collected with integrity preserved**  
  *Meaning:* Logs, images, and artifacts are collected in ways that support future analysis or legal needs.  
  *Example:* Disk images taken using forensically sound tools and stored in a secure repository.

- **RS.AN-08 – Incident magnitude estimated and validated**  
  *Meaning:* The organization estimates the scale of damage and validates it with evidence.  
  *Example:* The team determines how many records were accessed and which regions/customers are impacted.

---

### RS.CO – Incident Response Reporting and Communication

- **RS.CO-02 – Internal and external stakeholders notified**  
  *Meaning:* Appropriate parties (regulators, customers, partners) are informed within required timelines.  
  *Example:* For a breach with PII exposure, the organization notifies regulators and affected customers within legal deadlines.

- **RS.CO-03 – Information shared with designated stakeholders**  
  *Meaning:* Incident-related information is shared with the right people, at the right detail level.  
  *Example:* Executives receive summarized impact and business risk; technical teams receive detailed IOCs and remediation steps.

---

### RS.MI – Incident Mitigation

- **RS.MI-01 – Incidents contained**  
  *Meaning:* Actions are taken to stop attacker activity and prevent further spread.  
  *Example:* Compromised hosts are isolated from the network and malicious accounts disabled.

- **RS.MI-02 – Incidents eradicated**  
  *Meaning:* Malicious artifacts and persistence mechanisms are fully removed.  
  *Example:* Malware is removed, persistence keys deleted, and vulnerable services patched or reconfigured.

---

## 6. RECOVER (RC)
**Assets and operations affected by a cybersecurity incident are restored.**

### RC.RP – Incident Recovery Plan Execution

- **RC.RP-01 – Recovery portion of IR plan executed when initiated**  
  *Meaning:* Once response criteria are met, recovery activities follow a documented plan.  
  *Example:* After containment, DR playbooks are executed to restore critical workloads from backups.

- **RC.RP-02 – Recovery actions selected, scoped, prioritized, and performed**  
  *Meaning:* The org decides what to restore first, based on business priorities.  
  *Example:* Customer-facing services are restored before internal reporting systems.

- **RC.RP-03 – Integrity of backups and restoration assets verified before use**  
  *Meaning:* Recovery data and images are checked to ensure they are complete and clean.  
  *Example:* Backups are scanned for malware before being restored into production.

- **RC.RP-04 – Critical mission functions and cyber risk considered in post-incident norms**  
  *Meaning:* Recovery planning considers both business mission and updated security posture.  
  *Example:* After a serious outage, RTO and RPO are redefined for critical applications.

- **RC.RP-05 – Integrity of restored assets verified and normal status confirmed**  
  *Meaning:* Restored systems are validated before declaring them back in service.  
  *Example:* Post-restore testing confirms apps function correctly and logs show no ongoing malicious activity.

- **RC.RP-06 – End of recovery declared and documentation completed**  
  *Meaning:* There is a formal endpoint to recovery, with documentation finalized.  
  *Example:* The incident commander declares “recovery complete” after all systems are stable and the post-incident report is finished.

---

### RC.CO – Incident Recovery Communication

- **RC.CO-03 – Recovery progress communicated to stakeholders**  
  *Meaning:* Internal and key external parties get updates during the recovery phase.  
  *Example:* Business units receive daily updates on service restoration timelines.

- **RC.CO-04 – Public updates on recovery provided with approved messaging**  
  *Meaning:* Public communication (press, social media, website) is coordinated and controlled.  
  *Example:* The company posts a breach and recovery update on its website and sends emails with consistent, approved wording.

---

## Quick Usage Tips

- Use the codes (**GV.OC-04**, **ID.RA-05**, **PR.AA-05**, etc.) in:
  - Risk registers
  - Gap assessments
  - Control matrices and mapping (e.g., to ISO 27001, SOC 2, 800-53)
- For each Subcategory:
  - Take the **“Meaning”** line as a requirement/outcome.
  - Use the **“Example”** as inspiration for practical implementation in your environment.

