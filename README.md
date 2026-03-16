# DHCP-yersinia-lab
This repo will hold all of the materials related to my DHCP Starvation lab using yersinia

# Introduction

This is a lab I have created to demonstrate how an attacker can use DHCP Starvation in order to cause a Denial of Service to a network.

# Architecture

As I do not have access to all of the physical hardware and software licenses required to do this with real devices (Cisco Routers and switches, multiple Linux PCs, etc.) I have done the lab virtually using GNS3. GNS3 natively supports emulated PCs in its standard form, but I also needed a way to emulate a Kali Linux PC in this enviornment. I accomplished this by running Kali Linux as a docker container on my GNS3 server, and then uploading an additional template to use. 

Additionally, I also use a mac OS computer with an Apple Silicon processor, which was becoming a huge pain when trying to host a GNS3 server in a virtual machine. In order to get around this (and learn a bit of cloud computing along the way) I spun up an Ubuntu instance on google cloud, and hosted my GNS3 server on their rather than on my host machine.

The completed Architecture looked like this:
<img width="818" height="661" alt="image" src="https://github.com/user-attachments/assets/eff40173-906b-4ef4-b52c-0c971b7cfa60" />
