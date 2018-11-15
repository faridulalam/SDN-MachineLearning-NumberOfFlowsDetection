#!/bin/bash

######## 4switches 4hosts (2-flow) ethtool configuration ##########

"""
To enhance the performance of a TCP connection.... the operating system can offload
TCP functionality in the network interface card of packet segmentation such as

1. generic segmentation (gso)
2. generic receive (gro)
3. TCP segmentation (tso)
 
Disabling these functions with ethtool -K command will enable inspecting individual 
packets using tcpdump and simple wireshark tools. These setting are implemented on 
every interface of each host and switch in the topology.
"""

### HOST 1 ###
ethtool -K h1-eth0 gro off
ethtool -K h1-eth0 gso off
ethtool -K h1-eth0 tso off

### HOST 2 ###
ethtool -K h2-eth0 gro off
ethtool -K h2-eth0 gso off
ethtool -K h2-eth0 tso off

### HOST 3 ###
ethtool -K h3-eth0 gro off
ethtool -K h3-eth0 gso off
ethtool -K h3-eth0 tso off

### HOST 4 ###
ethtool -K h4-eth0 gro off
ethtool -K h4-eth0 gso off
ethtool -K h4-eth0 tso off

### HOST 5 ###
ethtool -K h5-eth0 gro off
ethtool -K h5-eth0 gso off
ethtool -K h5-eth0 tso off

### SWITCH 1 ###
ethtool -K s1-eth1 gro off
ethtool -K s1-eth1 gso off
ethtool -K s1-eth1 tso off
ethtool -K s1-eth2 gro off
ethtool -K s1-eth2 gso off
ethtool -K s1-eth2 tso off
ethtool -K s1-eth3 gro off
ethtool -K s1-eth3 gso off
ethtool -K s1-eth3 tso off
ethtool -K s1-eth4 gro off
ethtool -K s1-eth4 gso off
ethtool -K s1-eth4 tso off

### SWITCH 2 ###
ethtool -K s2-eth1 gro off
ethtool -K s2-eth1 gso off
ethtool -K s2-eth1 tso off
ethtool -K s2-eth2 gro off
ethtool -K s2-eth2 gso off
ethtool -K s2-eth2 tso off
ethtool -K s2-eth3 gro off
ethtool -K s2-eth3 gso off
ethtool -K s2-eth3 tso off
ethtool -K s2-eth4 gro off
ethtool -K s2-eth4 gso off
ethtool -K s2-eth4 tso off

### SWITCH 3 ###
ethtool -K s3-eth1 gro off
ethtool -K s3-eth1 gso off
ethtool -K s3-eth1 tso off
ethtool -K s3-eth2 gro off
ethtool -K s3-eth2 gso off
ethtool -K s3-eth2 tso off
ethtool -K s3-eth3 gro off
ethtool -K s3-eth3 gso off
ethtool -K s3-eth3 tso off
ethtool -K s3-eth4 gro off
ethtool -K s3-eth4 gso off
ethtool -K s3-eth4 tso off

### SWITCH 4 ###
ethtool -K s4-eth1 gro off
ethtool -K s4-eth1 gso off
ethtool -K s4-eth1 tso off
ethtool -K s4-eth2 gro off
ethtool -K s4-eth2 gso off
ethtool -K s4-eth2 tso off
ethtool -K s4-eth3 gro off
ethtool -K s4-eth3 gso off
ethtool -K s4-eth3 tso off
ethtool -K s4-eth4 gro off
ethtool -K s4-eth4 gso off
ethtool -K s4-eth4 tso off

