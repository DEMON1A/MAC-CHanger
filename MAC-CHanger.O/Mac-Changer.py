import subprocess
import optparse
import time
import sys
import os

parser = optparse.OptionParser()

parser.add_option("-i","--interface",dest="Interface",help="Interface for change its MAC-Address")
parser.add_option("-m","--mac",dest="MAC_Address",help="New Mac-Address for put it in your interface")

(options,arguments) = parser.parse_args()

inter = options.Interface
mac = options.MAC_Address

if not inter:
	os.system("python Mac-Changer.py --help")
	sys.exit()
elif not mac:
	os.system("python Mac-Changer.py --help")
	sys.exit()

print("\n>> CHanging Mac-Address for {0} To {1}".format(inter,mac))
time.sleep(5)

subprocess.call("ifconfig " + inter + " down",shell=False)
subprocess.call("ifconfig " + inter + " hw ether" + mac,shell=False)
subprocess.call("ifconfig " + inter + " up",shell=False)
print("[+]Done")

time.sleep(5)
os.system("clear")

print("[+]Now Your Mac-Address Is {0}".format(mac))
subprocess.call("ifconfig",shell=True)

#  Thanks For Using My Toolz
#  Email: mdaif1332@gmail.com
