import paramiko
import time
import getpass

ip = input("Entrez l'ip cible :")
username = input("Entrez hostname :")
password = input("Entrez le mot de passe :")

remote_con_pre = paramiko.SSHClient()
remote_con_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_con_pre.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

remote_con = remote_con_pre.invoke_shell()
remote_con.send(b'sh ip int br\n')
output = remote_con.recv(65535)
time.sleep(5)
print output