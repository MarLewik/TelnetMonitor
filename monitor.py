import getpass
import sys
import telnetlib
import time

HOST = "192.168.1.112"
PORT = "81"
TIMEOUT = "60"
#user = raw_input("Enter your remote account: ")
#password = getpass.getpass()

tn = telnetlib.Telnet()
now = time.strftime("%c")

#tn.write("ls\n")
#tn.write("exit\n")

while(not time.sleep(5)):
    #code to execute
    print "Current date & time " + time.strftime("%c")
    try:
        tn.open(HOST,PORT)
    except:
        print "Exceptio" + time.strftime("%c")
    tn.read_until("login: ")
    tn.write("Marcin" + "\n")
    tn.read_until("Password: ")
    tn.write("Lewandowski" + "\n")
    print tn.read_until("*")
    tn.close()
