service hostapd stop
service dnsmasq stop
service apache2 stop
ifconfig wlan0 down
killall dnsmasq hostapd
echo "exiting is succesfull"
echo " " > files/data/status.txt

airmon-ng stop wlan1mon

killall aireplay-ng

#./airmon check kill

echo "exiting is succesfull"
