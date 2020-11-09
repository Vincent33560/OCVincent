from main import router_username, router_password, router_ip
import paramiko
import time

#router_ip = input("Entrez l'adresse IP cible : ")
#router_username = input("Entrez le username : ")
#router_password = input("Entrez le mot de passe : ")

def Interfaces1():
    ssh = paramiko.SSHClient()
    # Add SSH host key when missing.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Load SSH host keys.
    ssh.load_system_host_keys()
    ssh.connect(router_ip,
                username=router_username,
                password=router_password,
                look_for_keys=False)

    DEVICE_ACCESS = ssh.invoke_shell()
    DEVICE_ACCESS.send(b"en\n")
    DEVICE_ACCESS.send(b"vdcvdc\n")
    DEVICE_ACCESS.send(b"conf t\n")
    DEVICE_ACCESS.send(b"int g0/1\n")
    DEVICE_ACCESS.send(b"ip address 192.168.1.25 255.255.255.0\n")
    DEVICE_ACCESS.send(b"no shut\n")
    DEVICE_ACCESS.send(b"end\n")
    DEVICE_ACCESS.send(b"sh ip int br\n")
    time.sleep(1)

    # Read output from command.
    output = DEVICE_ACCESS.recv(65000)
    print(output.decode('ascii'))


def Interfaces2():
    ssh = paramiko.SSHClient()
    # Add SSH host key when missing.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Load SSH host keys.
    ssh.load_system_host_keys()
    ssh.connect(router_ip,
                username=router_username,
                password=router_password,
                look_for_keys=False)

    DEVICE_ACCESS = ssh.invoke_shell()
    DEVICE_ACCESS.send(b"en\n")
    DEVICE_ACCESS.send(b"vdcvdc\n")
    DEVICE_ACCESS.send(b"conf t\n")
    DEVICE_ACCESS.send(b"int g0/2\n")
    DEVICE_ACCESS.send(b"ip address 192.168.2.25 255.255.255.0\n")
    DEVICE_ACCESS.send(b"no shut\n")
    DEVICE_ACCESS.send(b"end\n")
    DEVICE_ACCESS.send(b"sh ip int br\n")
    time.sleep(1)

    # Read output from command.
    output = DEVICE_ACCESS.recv(65000)
    print(output.decode('ascii'))


reponse = input("Voulez vous configurer l'interface g0/1 ?[o/n]")
reponse = reponse.strip().lower()
if reponse.startswith('o'):
    int = Interfaces1()
elif reponse.startswith('n') or reponse == '':
    print("-------------")
else:
    print("repondez !")
reponse2 = input("Voulez vous configurer l'interface g0/2 ? [o/n] ")
reponse2 = reponse.strip().lower()
if reponse2.startswith('o'):
    int2 = Interfaces2()
elif reponse2.startswith('n') or reponse == '':
    print("----------------")
else:
    print('répondez svp')