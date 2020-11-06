import paramiko
import time
import getpass


def interface():
    connection.send("conf t\n")
    time.sleep(.5)
    connection.send("int g0/1\n")
    time.sleep(2)
    connection.send("ip address 192.168.10.1 255.255.255.0\n")
    time.sleep(2)
    connection.send("no shut\n")
    connection.send("end\n")
    print("ca fonctionne")
    time.sleep(2)

