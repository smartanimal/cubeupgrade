import sys
import os
import socket
import struct
import cube

# check parameter, at least there should be 3 parameters
# Parameter 1: 1st IP address of IP range
# Parameter 2: IP address number of IP range
# Parameter 3: path of target firmware
# Parameter 4: time of starting upgrade firmware
# Parameter 5: Interval of two upgrade procedure

args = len(sys.argv)

if args < 3:
	print 'less parameters, should 5 parameters'
	sys.exit(0)	

ipaddrstart = sys.argv[1]
ipaddrnum = int(sys.argv[2])
targetfirmware = sys.argv[3]
upgradetime = sys.argv[4]
upgradeinterval = sys.argv[5]

ipaddressstr = ipaddrstart

# check whether upgrade firmware file exist
if not(os.path.isfile(targetfirmware)):
	print 'The file of', targetfirmware, 'doesn\'t exist, please check!'
	sys.exit(0)
	


while ipaddrnum > 0:	
	cube = cube.cube(ipaddressstr, targetfirmware)
	
	if cube.connect() < 0:
		continue
		
	if cube.remount() < 0:
		continue
		
	if cube.pushapk() < 0:
		continue
		
	if cube.disconnect() < 0:
		continue
	
	ip = socket.ntohl(struct.unpack("I",socket.inet_aton(str(ipaddressstr)))[0])
	ip += 1;
	ipaddressstr = socket.inet_ntoa(struct.pack('I',socket.htonl(ip)))	
	
	ipaddrnum -= 1
	
