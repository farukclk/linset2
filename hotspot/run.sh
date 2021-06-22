ifconfig wlan0 down
iptables --flush
echo 1 > /proc/sys/net/ipv4/ip_forward
hostapd hostapd.conf -B
ifconfig wlan0 192.168.1.1 netmask 255.255.255.0
service apache2 start
dnsmasq -C dnsmasq.conf
