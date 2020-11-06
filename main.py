import getpass
import telnetlib

HOST = "10.0.0.1"
user = input("Entre votre hostname: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Hostname : ")
tn.write(user.encode('ascii') +b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"int f0/1\n")
tn.write(b"192.168.100.1 255.255.255.0\n")
tn.write(b"no shut\n")
tn.write(b"end\n")

print(tn.read_all().decode('ascii'))