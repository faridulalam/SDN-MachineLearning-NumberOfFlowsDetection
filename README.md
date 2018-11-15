# SDN-MachineLearning-NumberOfFlowsDetection


..........MasterThesis on Number of Flows Detection in SDN networks using Machine Learning.........
----------------------------------------------------------------------------------------------------

ABSTRACT
---------

The evolution of modern communication systems has led to the significant development
of Information Technology (IT) and rapid expansion of its infrastructure requires present
networks to be fast, ability to carry a huge amount of traffic, deploying the number of
dynamic applications and demands more Quality of Service (QoS). However, the network
management technologies could not cope up with the rapid change in software and network
technologies. As a result, inefficient network management and the adjustment of network
performance is quite difficult due to the highly unpredictable traffic patterns. Therefore,
future network must be able to address these new challenges and must be able to adapt
policies dynamically and automatically based on emerging internet applications and ser-
vices. The information needs to extract from the traffic in order to understand and predict
its behaviour is becoming increasingly important to perform an efficient network manage-
ment. The idea of “programmable networks” has been proposed to facilitate the network
management system to deal with emerging network technologies and virtualization. Par-
ticularly, Software Defined Networking (SDN) is an emerging paradigm that promises to
dramatically simplify the network management system and enable innovation. The main
idea of SDN is to separate the network’s control logic from underlying routers and switches.
Hence, the network intelligence is logically centralized in software-based controllers (the
control plane) and network devices turns into simple packet forwarding devices (the data
plane) that can be programmed globally on each hardware unit via an open interface (e.g.
OpenFlow).

This thesis report provides a mechanism to detect the number of flows into the network,
which will be used later for taking swift actions to avoid congestion or reroute the flow in
the network. Machine Learning (ML) has been used to build a multiple flows detection
classifier by using the programmability feature of SDN. The combination of ML and SDN
results in an increased reliability and efficiency for networking operations together with
simplified network management controllability. Therefore, this work is one of the initial
steps to achieve functional programmable network. As a result, the Mininet emulator is
used to create different scenarios to run experiments with multiple Transmission Control
Protocol (TCP) connections using the OpenFlow (OF) protocol to collect the data from
Open vSwitch (OVS) switches in the network. Python and Bash scripts have been used
to prepare the data for ML tool Waikato Environment for Knowledge Analysis (WEKA)
along with the proposed features for this purpose. Supervised learning algorithms such
as Decision tree (J48), Naive Bayes, Random forest, Bagging, AdaBoostM1, LogitBoost
and Voting (combination of multiple classifiers) are used for the training and testing of the
classifier. The classifier is trained on the training dataset, while the test dataset is used
to check the accuracy of the learned classifier. Based on validation and test datasets, the
results of seven classifiers are compared and evaluated based on various parameters. The
Random Forest classifier is the best classifier among all single algorithm based classifiers.
However, Voting method or classifier (use of multiple algorithms) is chosen based on the
overall results of the classifications. The chosen classifier will be able to detect the number
of flows more efficiently and accurately using the selected features.



Used Environment
------------------------
 1. Mininet Emulator
 2. POX OpenFlow controller 
 3. Wireshark
 4. Iperf1
 5. python for data processing
 6. Bash scripting for scenarios and GNU plot
 7. WEKA machine learning tool to train and test different decision tree algorithms
 8. Customized Linux Kernel
