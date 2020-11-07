import paramiko
import time
import getpass
from interfaces import interface

#ip = input("Entrez l'ip cible :")
#username = input("Entrez hostname :")
#password = input("Entrez le mot de passe :")

router_ip = "172.16.1.100"
router_username = "admin"
router_password = "admin1"

class a:
    def test(ip_address, username, password):

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(ip, port=22,
                    name=username,
                    mdp=password,
                    look_for_keys=False,
                    allow_agent=False)
        print("Connexion réussie !")

    def connect(self):


        connection = ssh.invoke_shell()
        connection.send("enable\n")
        time.sleep(.5)
        connection.send("vdcvdc\n")
        time.sleep(2)
        connection.send("show ip int brief\n")
        time.sleep(2)

        router_output = connection.recv(65535).decode(encoding='utf-8')

        time.sleep(.5)
        print("\n\n")
        print(str(router_output) + "\n")
        time.sleep(.5)


        interface()





sortie = test(router_ip, router_username, router_password)
inte = interface()
