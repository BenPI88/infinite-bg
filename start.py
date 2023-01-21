import os
import time
os.system("sudo apt-get install ImageMagick")
while True:
	os.system("import /.bg.png")
	os.system("gsettings get org.gnome.desktop.background picture-uri 'file:///.bg.png'")
