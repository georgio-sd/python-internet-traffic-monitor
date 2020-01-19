# Internet traffic monitor for linux servers
The monitor counts inbound and outbound traffic and saves numbers into MySQL DB
I used iptables counters and chains to information about internet traffic.

/etc/sysconfig/iptables
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
-N incount
-N outcount
-I INPUT 1 -i eno1 -j incount
-I OUTPUT 1 -o eno1 -j outcount
-A incount -i eno1
-A outcount -o eno1

