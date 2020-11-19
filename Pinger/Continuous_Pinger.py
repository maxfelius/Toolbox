#!/usr/bin/env python3
"""
Created on Wed Feb  5 23:50:25 2020

@author: Max Felius
@email: maxfelius@hotmail.com

Purpose:
    when the program has started. Should ping every t seconds to google.
    it should log every ping with failed and passed
"""

#import
import datetime, time
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

#Global Variables
FILE_NAME = 'ping_log.txt'
WAIT_TIME = 60 #seconds

class pinger:
    def __init__(self,FILE_NAME,WAIT_TIME):
        self.FILE_NAME = FILE_NAME
        self.WAIT_TIME = WAIT_TIME

    def start(self):
        print('Started the pinger. Press Ctrl-C to quit the pinger.')

        try:
            #start loop
            while True:
                self.log_ping(self.ping('google.com'))
              
                time.sleep(self.WAIT_TIME)
        except KeyboardInterrupt:
            print('Ctrl-C was invoked. Stopping the pinger...')

    #ping funtion
    def ping(self,host):
        """
        https://stackoverflow.com/questions/2953462/pinging-servers-in-python
        
        Returns True if host (str) responds to a ping request.
        Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
        """

        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower()=='windows' else '-c'

        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, '1', host]

        return subprocess.call(command) == 0

    #log function
    def log_ping(self,result):
        with open(self.FILE_NAME,'a') as f:
            time_str = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            f.write(time_str + ' - Ping: '+str(result)+'\n')       

if __name__ == '__main__':
    pinger(FILE_NAME,WAIT_TIME).start()
