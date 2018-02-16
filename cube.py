# class of cube product

import subprocess

class cube(object):
    def __init__(self, ipaddr, targetfirmware):
        self.ipaddr = ipaddr
        self.targetfirmware = targetfirmware
        print self.ipaddr, self.targetfirmware

    def connect(self):
        print 'trying to connect cube of', self.ipaddr
        connectcmd = 'adb connect ' + self.ipaddr
        connectresult = subprocess.check_output(connectcmd.split())
        isconnected = connectresult.find('unable to connect') # check whehter connect to device by seeking for string

        if isconnected < 0:
            print 'connected to', self.ipaddr
            return 0
        else:
            print 'unable to connect cube of', self.ipaddr
            return -1

    def remount(self):
        print 'trying to remount /system'
        remountcmd = 'adb shell mount -o remount,rw /system'
        remountresult = subprocess.check_output(remountcmd.split())
        isremount = remountresult.find('error')

        if isremount >= 0:
            print 'cannot remount /system'
            return -1
        else:
            print 'remount /system successfully'
            return 0


    def pushapk(self):
        print 'start to upgrade firmware'
        pushapkcmd = 'adb push ' + self.targetfirmware + ' /system/app'
        pushapkresult = subprocess.check_output(pushapkcmd.split())
        print 'Firmware upgrade was done'

        return 0

    def disconnect(self):
        disconnectcmd = 'adb disconnect ' + self.ipaddr;
        disconnectresult = subprocess.check_output(disconnectcmd.split())
        print('disconnect cube')

        return 0
