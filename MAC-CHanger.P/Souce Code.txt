import subprocess
import time
import sys
import os

print("""
		>> Auto Mac-CHanger
			>> --exit for close program
				>> Only for linux.
	  """)

inter = input("Enter interface name: ")
if ";" in inter:
	print("[!]That will make an error!! check it again.")
	sys.exit()
else:
	pass

####################

if inter == "--exit":
	sys.exit()
else:
	pass

mac = input("Enter new mac address: ")
if mac == "--exit":
	sys.exit()
else:
	pass

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

'''
There is another type of this tool using
optparse try it if you do not like this.
'''