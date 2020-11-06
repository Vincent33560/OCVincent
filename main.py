import paramiko
import time
import getpass



ip = input("Entrez l'ip cible :")
username = input("Entrez hostname :")
password = input("Entrez le mot de passe :")

try:

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)
        print("Connection réussie !")

        connection = ssh.invoke_session()
        connection.send("enable\n")
        time.sleep(.5)
        connection.send("vdcvdc\n")
        time.sleep(2)
        connection.send("show ip int brief\n")
        time.sleep(2)

        router_output = connection.recv(65535)
        time.sleep(.5)
        print("\n\n")
        print(str(router_output) + "\n")
        time.sleep(.5)

        connection.send("end\n")

    except paramiko.AuthenticationException:
        print("Mot de passe incorrect" + password)

    except socket.erro:
        print("Erreur de socket")

except:
    print("Quelque chose ne va pas")
