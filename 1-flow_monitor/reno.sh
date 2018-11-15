#!/bin/bash



### set tcp reno as congestion control
sysctl -w net.ipv4.tcp_congestion_control=reno

"""
TCP receive buffer size can be automatically set to achieve the match required 
by the path for full throughput The command sysctl -w net.ipv4.tcp_moderate_rcvbuf=0 
disables automatic sizing of the receiver buffer. This option is disabled as the 
receiver buffer size is manually set to a large values
"""
### set tcp auto-tunning off		 	# this option set link BW maximum 5Mbps,	
#sysctl -w net.ipv4.tcp_moderate_rcvbuf=1	# reboot can solve this problem or set it to 1

"""
The command sysctl -w net.ipv4.tcp_window_scaling=1 allows the larger window size,
greater than 64K, to be enabled to achieve higher throughput 
"""
### tcp window scaling off
sysctl -w net.ipv4.tcp_window_scaling=1

"""
The command sysctl -w net.ipv4.tcp_rmem sets the minimum, default and maximum 
values for the TCP receive buffer. The values, 10240, 3145728, 16777216, are 
the advertised window size of the receiver and chosen such that to not to limit 
the throughput on the link. 
"""
### tcp rmem should not be a limit
sysctl -w net.ipv4.tcp_rmem="10240 3145728 16777216"


### disable MPTCP, by default its disable
#sysctl -w net.mptcp.mptcp_enabled=0



