# https yazmadigin surece tum http siteleri yonlendiriyor
#google u da yonlendiriyor
service apache2 start
ifconfig wlan0 192.168.1.1 netmask 255.255.255.0
dnsmasq -C dnsmasq.conf
hostapd hostapd.conf -B

