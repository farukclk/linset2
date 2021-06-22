ifconfig wlan0 down
service hostapd stop
service dnsmasq stop
service apache2 stop
killall dnsmasq 
killall hostapd
echo "exiting is succesfull"
echo " " > files/data/status.txt

airmon-ng stop wlan1mon

killall aireplay-ng

echo "exiting is succesfull"
