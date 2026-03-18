# DHCP-Starvation-Lab
This repo will hold all of the materials related to my DHCP Starvation lab using GNS3

# Introduction

This is a lab I have created to demonstrate how an attacker can use DHCP Starvation in order to cause a Denial of Service to a network.

# Architecture

As I do not have access to all of the physical hardware and software licenses required to do this with real devices (Cisco Routers and switches, multiple Linux PCs, etc.) I have done this lab completely virtually. Also, since virtualization proved to be a huge pain to do on macOS with an Apple Silicon processor, I chose to use cloud resources (Google Cloud Compute Engine) instead of my own hardware resources for the project. In summary, using a e2-standard-4 machine in Google Cloud Compute, I ran an Ubuntu VM which would act as the host for my GNS3 server. Alongside the GNS3 server, I have a Docker engine running that is creating the container for Alpine Linux machine. The reason I chose Alpine Linux over Kali Linux is I was running into issues with Kali crashing my entire cloud instance, most likely due to it being hardware intensive.Finally, alongside the server and Docker engine I am running Dynamips which is hosting my emulated Cisco3750 routers.


The full Architecture looks like this:
<img width="1360" height="1400" alt="image" src="https://github.com/user-attachments/assets/d0e5c576-cfe7-41b5-be8a-2daf99c30530" />

<img width="1508" height="638" alt="image" src="https://github.com/user-attachments/assets/cac1d068-7378-48b6-b988-2bd887a21ea9" />

## How does DHCP Starvation work?
DHCP Starvation is a type of Denial of Service attack where an attacker gains access to access port in your network, and floods the DHCP server with DHCP Discover requests. Each one of the packets that are flooded contain a fake/random MAC address that is injected into the packet, so each mapping in the DHCP pool is filled with a fake entry.

Once the DHCP pool is filled, it makes it impossible for other devices who do not yet have an IP address to obtain one, and communicate over the network. It also makes it very hard to diagnose the issue, as it is very hard to stop the attack once it has started. When initiating the attack in my lab, I was unable to use any of the DHCP commands in the Cisco CLI as the router was being overwhelmed with the massive amount of packets being flooded to it.
<img width="2720" height="1840" alt="image" src="https://github.com/user-attachments/assets/9b5d7567-5e8d-437b-a297-3c09b94af3db" />

<img width="960" height="767" alt="image" src="https://github.com/user-attachments/assets/7c63b054-7c36-45e4-a541-d378b8021ce2" />

As shown in the photo above, each DHCP Discover packet has a different randomized MAC address. This is what allows the DHCP Pool to fill up, as if the packet had the same MAC address for each Discover, the DHCP server would just ignore the request (as it is already in the table)

## Protection / Prevention
In order to protect against the DHCP Starvation attack, I have implemented storm-control on my switch. This will make it so if a device exceeds 10% of the ports total bandwidth, it will shut the port down. 
Note: This is bad - In an actual switch evnironment it would be better to use DHCP snooping or port security to achieve the desired protection. Unfortunately my dynamips image of the c3750 does not support these features, so I am just working with what I have

I ran the following commands on the switch
```
enable
conf t
interface f1/4
 storm-control broadcast level 10
 storm-control action shutdown

```
This will limit a maximum of 10% total bandwidth usage on the switchport, and if the switch receives more than 10% bandwidth it will shut down the port. This will generate a syslong message, which a network administrator can use to locate where on the network this rogue device could potentially be.



## Conclusion

In this lab I was able to explore many different topics and learn various skills including:
- Google Cloud Compute Engine basics
- Docker engine / Containerization
- Dynamips / Router emulation
- Scapy library (Python)
- GNS3
- Routing and Switching fundamentals
- Basic DHCP Configuration and Security




## Sources used 
https://www.cisco.com/c/en/us/td/docs/switches/lan/csbss/CBS220/CLI-Guide/b_220CLI/ip_dhcp_snooping_commands.pdf
https://www.cisco.com/c/en/us/td/docs/routers/nfvis/switch_command/b-nfvis-switch-command-reference/m-storm-control-commands.pdf
