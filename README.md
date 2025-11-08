💻 Secure Network Architecture & IDS Deployment
This project simulates a secure, segmented enterprise network environment to fulfill the practical requirements of the internship application for Megaminds IT Services, demonstrating hands-on skills in network design, security implementation, and intrusion detection.

🎯 Project Goals and Responsibilities Addressed
This simulation demonstrates proficiency in the following key responsibilities outlined in the internship description:

1. Network Design and Security Implementation: Implementing network segmentation using iptables rules (representing ACLs/Firewalls) to enforce policy-based access control.

2. Simulation and Performance Analysis: Utilizing Mininet for simulating the network topology and analyzing network health (via basic connectivity tests).

4. Cybersecurity Practices and Solutions: Deploying and configuring a powerful open-source Intrusion Detection System (Snort) to monitor network traffic.

5. Evaluation of Emerging Threats: Developing custom rules to detect policy violations (network probing) and application-layer keywords.

🗺️ Network Topology and Security Policy
Topology Overview
The network consists of three hosts and one router/firewall (r1) connected via a core switch (s1). Hosts are logically segregated by IP subnet:

Host h1 (Admin): 10.10.10.10/24

Host h2 (Employee): 10.10.20.20/24

Host h3 (IDS/Monitor): 10.10.20.30/24

Enforced Security Policy
The primary security measure is enforced on the router (r1) using iptables:
Policy,Status,Rule
Admin → Employee,✅ Allowed,Default traffic flow accepted.
Employee → Admin,🚫 Blocked,All ICMP traffic from the Employee subnet to the Admin subnet is dropped.

🛠️ Implementation and Proof of Concept
I. Core Technology
Component,Tool / Concept,Role
Network Simulation,Mininet,"Creates the virtual hosts, switch, and links."
Firewall,iptables (via router commands),Enforces the access control policy (segmentation).
IDS,Snort (Manual Launch),Monitors the network for custom-defined policy violations.
Here is the full text code for your README.md file. You can copy and paste this directly into your GitHub repository's README.md editor.💻 Secure Network Architecture & IDS DeploymentThis project simulates a secure, segmented enterprise network environment to fulfill the practical requirements of the internship application for Megaminds IT Services, demonstrating hands-on skills in network design, security implementation, and intrusion detection.🎯 Project Goals and Responsibilities AddressedThis simulation demonstrates proficiency in the following key responsibilities outlined in the internship description:1. Network Design and Security Implementation: Implementing network segmentation using iptables rules (representing ACLs/Firewalls) to enforce policy-based access control.2. Simulation and Performance Analysis: Utilizing Mininet for simulating the network topology and analyzing network health (via basic connectivity tests).4. Cybersecurity Practices and Solutions: Deploying and configuring a powerful open-source Intrusion Detection System (Snort) to monitor network traffic.5. Evaluation of Emerging Threats: Developing custom rules to detect policy violations (network probing) and application-layer keywords.🗺️ Network Topology and Security PolicyTopology OverviewThe network consists of three hosts and one router/firewall (r1) connected via a core switch (s1). Hosts are logically segregated by IP subnet:Host h1 (Admin): 10.10.10.10/24Host h2 (Employee): 10.10.20.20/24Host h3 (IDS/Monitor): 10.10.20.30/24Enforced Security PolicyThe primary security measure is enforced on the router (r1) using iptables:PolicyStatusRuleAdmin → Employee✅ AllowedDefault traffic flow accepted.Employee → Admin🚫 BlockedAll ICMP traffic from the Employee subnet to the Admin subnet is dropped.🛠️ Implementation and Proof of ConceptI. Core TechnologyComponentTool / ConceptRoleNetwork SimulationMininetCreates the virtual hosts, switch, and links.Firewalliptables (via router commands)Enforces the access control policy (segmentation).IDSSnort (Manual Launch)Monitors the network for custom-defined policy violations.II. Proof of Policy Enforcement (Firewall)The Mininet script confirms that the iptables rule successfully drops traffic intended to violate the policy:
mininet> h2 ping -c 1 h1
# Output: 0 received, 100% packet loss (PROOF OF FIREWALL SUCCESS)
Here is the full text code for your README.md file. You can copy and paste this directly into your GitHub repository's README.md editor.💻 Secure Network Architecture & IDS DeploymentThis project simulates a secure, segmented enterprise network environment to fulfill the practical requirements of the internship application for Megaminds IT Services, demonstrating hands-on skills in network design, security implementation, and intrusion detection.🎯 Project Goals and Responsibilities AddressedThis simulation demonstrates proficiency in the following key responsibilities outlined in the internship description:1. Network Design and Security Implementation: Implementing network segmentation using iptables rules (representing ACLs/Firewalls) to enforce policy-based access control.2. Simulation and Performance Analysis: Utilizing Mininet for simulating the network topology and analyzing network health (via basic connectivity tests).4. Cybersecurity Practices and Solutions: Deploying and configuring a powerful open-source Intrusion Detection System (Snort) to monitor network traffic.5. Evaluation of Emerging Threats: Developing custom rules to detect policy violations (network probing) and application-layer keywords.🗺️ Network Topology and Security PolicyTopology OverviewThe network consists of three hosts and one router/firewall (r1) connected via a core switch (s1). Hosts are logically segregated by IP subnet:Host h1 (Admin): 10.10.10.10/24Host h2 (Employee): 10.10.20.20/24Host h3 (IDS/Monitor): 10.10.20.30/24Enforced Security PolicyThe primary security measure is enforced on the router (r1) using iptables:PolicyStatusRuleAdmin → Employee✅ AllowedDefault traffic flow accepted.Employee → Admin🚫 BlockedAll ICMP traffic from the Employee subnet to the Admin subnet is dropped.🛠️ Implementation and Proof of ConceptI. Core TechnologyComponentTool / ConceptRoleNetwork SimulationMininetCreates the virtual hosts, switch, and links.Firewalliptables (via router commands)Enforces the access control policy (segmentation).IDSSnort (Manual Launch)Monitors the network for custom-defined policy violations.II. Proof of Policy Enforcement (Firewall)The Mininet script confirms that the iptables rule successfully drops traffic intended to violate the policy:Bashmininet> h2 ping -c 1 h1
# Output: 0 received, 100% packet loss (PROOF OF FIREWALL SUCCESS)
III. Intrusion Detection RulesThe IDS successfully generated alerts for both required scenarios (Proof is included in the artifacts/alert.log file):
Alert ID,Test Performed,Snort Rule Type
1000001,h2 attempts forbidden ping to h1.,Policy Violation (ICMP)
1000002,"h2 sends payload containing ""MALICIOUS-SCAN"".",Content Inspection (UDP)

⚙️ Setup and Execution
Prerequisites
A Linux environment (Mininet VM or Ubuntu)

Mininet and Snort installed.

Custom rule file located at snort/custom_rules.rules.

How to Run and Generate Logs
1.Clone this repository:
git clone [YOUR REPO LINK]
cd Secure-Network-IDS-Project
2.Launch the Mininet network (this also sets up the firewall):
sudo python3 topology.py
3.Inside the mininet> prompt, manually run the Snort command (adapted to bypass VM configuration errors):
mininet> h3 "/usr/sbin/snort -c /home/mininet/Secure-Network-IDS-Project/snort/custom_rules.rules -A full -i h3-eth0 -l /home/mininet/Secure-Network-IDS-Project/artifacts -F"
