import os
import time
os.system("sudo apt-get install import")
while True:
	os.system("import /.bg.png")
	os.system("gsettings get org.gnome.desktop.background picture-uri 'file:///.bg.png'")
