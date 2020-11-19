'''
@Author: Max
@

Looking on the network for available devices
'''
#imports
import sys
import subprocess
import os
from decouple import config

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

#proc1 = subprocess.Popen(['ping', IP_DEVICE[0]], stdout=subprocess.PIPE)
#proc2 = subprocess.Popen(['ping', IP_DEVICE[1]], stdout=subprocess.PIPE)

while True:
    #line1 = proc1.stdout.readline()   
    #line2 = proc2.stdout.readline()

    #if not line1 or not line2:
    #    break
    
    #connected_ip = line1.decode('utf-8').split()[3][:-1]

    #if connected_ip == IP_DEVICE:
    #    subprocess.Popen(['say','Device connected'])

    os.sys
