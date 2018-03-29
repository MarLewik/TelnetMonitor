import getpass
import sys
import telnetlib
import time

HOST = "192.168.1.112"
PORT = "81"
TIMEOUT = "60"
#user = raw_input("Enter your remote account: ")
#password = getpass.getpass()

#tn = telnetlib.Telnet()


while(not time.sleep(5)):
    #code to execute
    print "Current date & time " + time.strftime("%x %X")
    try:
        tn = telnetlib.Telnet(HOST,PORT)
    except:
        print "Exception" + time.strftime("%x %X")
    tn.read_until("login: ")
    tn.write("Marcin" + "\n")
    tn.read_until("Password: ")
    tn.write("Lewandowski" + "\n")
    print tn.read_until("*")
    tn.close()
