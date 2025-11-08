#!/usr/bin/python
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel

def SecureNet():
  setLogLevel('info')
  net=Mininet()
  net.addController('c0')

  # 1.Add hosts and Router 
  h1= net.addHost('h1',ip='10.10.10.10/24') #admin
  h2= net.addHost('h2', ip='10.10.20.20/24') #employee
  h3= net.addHost('h3', ip='10.10.20.30/24') #IDS
  r1= net.addHost('r1', ip='10.10.10.1/24') #router
  s1= net.addSwitch('s1')

  # 2.Add Links
  net.addLink(h1,s1)
  net.addLink(h2,s1)
  net.addLink(h3,s1)
  net.addLink(r1,s1)
  net.start()

  # 3.Configure Router (IP Forwarding & second subnet)
  r1.cmd('sysctl net.ipv4.ip_forward=1')
  r1.cmd('ifconfig r1-eth0 10.10.10.1/24')
  r1.cmd('ifconfig r1-eth0:1 10.10.20.1/24') #add 2nd subnet IP

  # 4.Set Host Routes
  h1.cmd('route add default gw 10.10.10.1 dev h1-eth0')
  h2.cmd('route add default gw 10.10.20.1 dev h2-eth0')
  h3.cmd('route add default gw 10.10.20.1 dev h3-eth0')

  # Disable ICMP Redirects 
  r1.cmd('sysctl -w net.ipv4.conf.all.send_redirects=0')  

  # 5.IPTABLES Firewall Rule (BLOCK Employee -> Admin Ping)
  r1.cmd('iptables -F')
  h2.cmd('iptables -A OUTPUT -d 10.10.10.10 -p icmp -j DROP')
  r1.cmd('iptables -P FORWARD DROP')
  r1.cmd('iptables -A FORWARD -s 10.0.20.0/24 -d 10.10.10.0/24 -p icmp -j DROP')
  r1.cmd('iptables -A FORWARD -m state --state RELATED, ESTABLISHED -j ACCEPT')
  r1.cmd('iptables -A FORWARD -j ACCEPT')

  # 6.IDS Setup
  h3.cmd('ifconfig h3-eth0 promisc')
  
  #Trigger the final IDS test automatically
  h2.cmd('scapy -e send(IP(dst="h3")/UDP(dport=5000)/Raw(Load="MALICIOUS-SCAN"))')

  #Start Snort in the background
  h3.cmd('snort -c /home/mininet/Secure-Network-ID-Project/snort/custom_rules.rules -A full -i h3-eth0 -l /tmp/ &')
  

  CLI(net)
  net.stop()

if __name__ == '__main__':
  SecureNet()
