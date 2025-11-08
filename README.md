## 💻 Secure Network Architecture & IDS Deployment

This project simulates a secure, segmented enterprise network environment to fulfill the practical requirements of the internship application for Megaminds IT Services, demonstrating hands-on skills in network design, security implementation, and intrusion detection.

---
## 🎯 Project Goals and Responsibilities Addressed

This simulation demonstrates proficiency in the following key responsibilities outlined in the internship description:

* **1. Network Design and Security Implementation:** Implementing network segmentation using **`iptables`** rules (representing ACLs/Firewalls) to enforce policy-based access control.
* **2. Simulation and Performance Analysis:** Utilizing **Mininet** for simulating the network topology and analyzing network health (via basic connectivity tests).
* **4. Cybersecurity Practices and Solutions:** Deploying and configuring a powerful open-source Intrusion Detection System (**Snort**) to monitor network traffic.
* **5. Evaluation of Emerging Threats:** Developing custom rules to detect policy violations (network probing) and application-layer keywords.

---
## 🗺️ Network Topology and Security Policy

### Topology Overview

The network consists of three hosts and one router/firewall (`r1`) connected via a core switch (`s1`). Hosts are logically segregated by IP subnet:

* Host `h1` (Admin): `10.10.10.10/24`
* Host `h2` (Employee): `10.10.20.20/24`
* Host `h3` (IDS/Monitor): `10.10.20.30/24`

### Enforced Security Policy

The primary security measure is enforced on the router (`r1`) using `iptables`: Traffic from the Employee subnet (`h2`, `h3`) to the Admin subnet (`h1`) is **blocked** via ICMP protocol (`ping`).

---
## 🛠️ Implementation and Proof of Concept

### I. Core Technology

| Component | Tool / Concept |
| :--- | :--- |
| Network Simulation | **Mininet** |
| Firewall | **`iptables`** |
| IDS | **Snort** (Manual Launch) |

### II. Proof of Policy Enforcement (Firewall)

The script confirms the policy is enforced:

```bash
mininet> h2 ping -c 1 h1
# Output: 0 received, 100% packet loss (PROOF OF FIREWALL SUCCESS)
