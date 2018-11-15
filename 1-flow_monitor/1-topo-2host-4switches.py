	
#!/usr/bin/python

'''
2 hosts and 4 switches (1-flow) topology to work with Pox controller

'''

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

import time

from mininet.util import dumpNodeConnections

#import webbrowser


def topology():
	"Create a network."
	net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )
	print "*** Creating Hosts"
	h1 = net.addHost( 'h1', mac = '00:00:00:00:00:01')	# h1--10.0.0.1
	h2 = net.addHost( 'h2', mac = '00:00:00:00:00:02')	# h2--10.0.0.2
	h3 = net.addHost( 'h3', mac = '00:00:00:00:00:03')	# h3--10.0.0.3
	h4 = net.addHost( 'h4', mac = '00:00:00:00:00:04')	# h4--10.0.0.4

	#h5 = net.addHost( 'h5', mac = '00:00:00:00:00:05')	# h5--10.0.0.5
	#h6 = net.addHost( 'h6', mac = '00:00:00:00:00:06')	# h6--10.0.0.6
	
	print "*** Creating Switches & Controller"
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	s3 = net.addSwitch('s3')
	s4 = net.addSwitch('s4')
	
	c0 = net.addController('c0', controller = RemoteController, defaultIP ='127.0.0.1',port=6633)

	# between hosts & switches
	print "*** Creating and configuring link between Hosts & Switches"
	net.addLink(h1, s1, intfName1='h1-eth0', intfName2='s1-eth1')	# h1--s1
	net.addLink(h2, s2, intfName1='h2-eth0', intfName2='s2-eth1')	# h2--s2
	net.addLink(h3, s3, intfName1='h3-eth0', intfName2='s3-eth1')	# h3--s3
	net.addLink(h4, s4, intfName1='h4-eth0', intfName2='s4-eth1')	# h4--s4

	#net.addLink(h5, s2, intfName1='h5-eth0', intfName2='s2-eth4')	# h5--s2
	#net.addLink(h6, s3, intfName1='h6-eth0', intfName2='s3-eth4')	# h6--s3

	net.addLink(s1, s2, intfName1='s1-eth2', intfName2='s2-eth2')	# s1--s2
	net.addLink(s2, s3, intfName1='s2-eth3', intfName2='s3-eth2',bw=20, delay='30ms',max_queue_size=100)	# s2--s3
	net.addLink(s3, s4, intfName1='s3-eth3', intfName2='s4-eth2')	# s3--s4

	print "\n*** Starting controller"
	net.build()
	c0.start

	print "*** Starting 4 switches"
	s1.start([c0])
	s1.cmd('switch s1 start')
	s2.start([c0])
	s2.cmd('switch s2 start')
	s3.start([c0])
	s3.cmd('switch s3 start')
	s4.start([c0])
	s4.cmd('switch s4 start')

	s1.cmd('bash forwarding_table_normal.sh')	# setting up switches forwarding table
	
	time.sleep(5)

	
	# to set tcp segmentation tso, gro, gso offloading disabled
	print "\n*** Configuring tso, gro, gso & Flowtable"
	h1.cmd('bash eth.sh')	# host1 -- gro, gso, tso off
	h4.cmd('bash eth.sh')	# host4 -- gro, gso, tso off
	time.sleep(2)
	s1.cmd('bash eth.sh')	# switch1 -- gro, gso, tso off
	s2.cmd('bash eth.sh')	# switch2 -- gro, gso, tso off
	s3.cmd('bash eth.sh')	# switch3 -- gro, gso, tso off
	s4.cmd('bash eth.sh')	# switch4 -- gro, gso, tso off
	time.sleep(2)
	s2.cmd('bash reno.sh')		# setting tcp RENO, window_scalling on, maximum receiver buffer
	time.sleep(2)
	# StopWatch website to open
	# webbrowser.open('http://timer-tab.com/', new = 0)

	print "*** Dumping Host Connections"
	dumpNodeConnections(net.hosts)


	print "*** Ping : Checking connectivity"
	net.pingAll()
	
	time.sleep(2)
	
	print "*** Start transfering data"
	h4.cmd('./h4.sh &')
	#h3.cmd('./h3.sh &')
	h1.cmd('./h1.sh &')
	#h2.cmd('./h2.sh &')
	'''
	# h1.cmd('h1 ping h2 -c 2')

	# h2.cmd('tcpdump -i h2-eth2 -w server-tcpdump')
	# h1.cmd('tcpdump -i h1-eth2 -w client-tcpdump')
	# h2.cmd('iperf -s > server_output.txt &')
	# h1.cmd('iperf -c ', h1.IP() + ' -i 1 -t 50   >  client_output.txt &')
	'''
	print "*** Running CLI"
	CLI( net )
	print "*** Stopping network"
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	topology()



















	
