import paramiko
import time
import getpass

ip = input("Entrez l'ip cible :")
username = input("Entrez hostname :")
password = input("Entrez le mot de passe :")

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

DEVICE_ACCESS = SESSION.invoke_shell()
DEVICE_ACCESS.send(b'sh run\n')
time.sleep(2)
output = DEVICE_ACCESS.recv(65000)
print(output.decode('ascii'))

SESSION.close