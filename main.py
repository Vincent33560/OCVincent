#from main import run_command_on_device
#from main import router_username, router_password, router_ip
import paramiko
import time



def send(ssh, command):
    """Send a command to the device and receive and print the result."""

    # Send the device a command
    ssh.send("\n")
    ssh.send(str(command) + "\n")

    # Wait for the command to complete in seconds
    time.sleep(1)

    # Receive 5000 bytes and print to screen
    output = ssh.recv(65000)
    print(output.decode('ascii'))


def main():
    """ Connect to a device, run a command, and return the output."""
    router_ip = input("Entrez l'adresse IP cible : ")
    router_username = input("Entrez le username : ")
    router_password = input("Entrez le mot de passe : ")

    try:
        ssh_pre = paramiko.SSHClient()
        # Add SSH host key when missing.
        ssh_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Load SSH host keys.
        ssh_pre.load_system_host_keys()

        try:

            # Connect to router using username/password authentication.
            ssh_pre.connect(router_ip,
                        username=router_username,
                        password=router_password,
                        look_for_keys=False)
            print("Connexion réussie")
            ssh = ssh_pre.invoke_shell()
            output = ssh.recv(65000)
            print(output.decode('ascii'))

        except paramiko.AuthenticationException:
            print("Incorrect password: ")
    except:
        print("Quelque chose ne vas pas")
    mainMenu(ssh)

def mainMenu(ssh):
    send(ssh, "enable")
    send(ssh, "vdcvdc\n")

    menu_choice = -1
    while 0 > menu_choice or 4 < menu_choice:
        try:
            print("\n MENU PRINCIPAL\n")
            print("--------------------\n")

            print("Choisissez parmi les propositions suivantes : ")
            print(
                """\n\n\n
                1 - APERCU CONFIGURATION
                -----------------------------
                2 - CONFIGURATION MATERIEL
                -----------------------------
                3 - TEST DE CONNEXION
                -----------------------------
                0 - Quitter               
                -----------------------------
                \n\n\n"""
            )
            menu_choice = int(input())
        except ValueError:
            print("Choisissez un chiffre entre 1 et 3")

    if menu_choice == 1:
        showConf(ssh)
    elif menu_choice == 2:
        confMain(ssh)
    elif menu_choice == 3:
        connTest(ssh)
    elif menu_choice == 0:
        mainMenu(ssh)

def showConf(ssh):

    menu_choice =-1
    while 0 > menu_choice < 4:
        try:
            print("\n MENU APERCU CONFIGURATION\n")
            print("------------------------------\n")

            print("Choisissez parmi les propositions suivantes : ")
            print(
                """\n\n\n
                1 - SHOW RUNNING CONFIGURATION
                -----------------------------
                2 - SHOW IP INTERFACE BRIEF
                -----------------------------
                3 - SHOW ACCESS LIST
                -----------------------------
                4 - SHOW IP ROUTE                
                -----------------------------
                0 - Quitter               
                -----------------------------
                \n\n\n"""
            )
            menu_choice = int(input())
        except ValueError:
            print("Choisissez un chiffre entre 1 et 4")

        if menu_choice == 1:
            time.sleep(2)
            send(ssh, "sh run")
            time.sleep(2)
        elif menu_choice == 2:
            send(ssh, "sh ip int brief")
        elif menu_choice == 3:
            send(ssh, "sh ip access-list")
        elif menu_choice == 4:
            send(ssh, "show ip route")
        elif menu_choice == 0:
            mainMenu(ssh)
        showConf(ssh)

def confMain(ssh):
    menu_choice = -1
    while 0 > menu_choice or 4 < menu_choice:
        try:
            print("\n MENU DE CONFIGURATION\n")
            print("--------------------\n")

            print("Choisissez parmi les propositions suivantes : ")
            print(
                """\n\n\n
                1 - CONFIGURER INTERFACE
                -----------------------------
                2 - CONFIGURER ROUTE
                -----------------------------
                3 - CONFIGURER HOSTNAME
                -----------------------------
                0 - Quitter               
                -----------------------------
                \n\n\n"""
            )
            menu_choice = int(input())
        except ValueError:
            print("Choisissez un chiffre entre 1 et 3")

    if menu_choice == 1:
        intConf(ssh)
    elif menu_choice == 2:
        routeConf(ssh)
    elif menu_choice == 3:
        setHostname(ssh)
    elif menu_choice == 0:
        main()

def intConf(ssh):
    print("\n CONFIUGRATION DES INTERFACES\n")
    print("------------------------------------\n")

    send(ssh, 'sh ip int brief')
    interface = input("Choisissez une interface à configurer [q pour quitter] : \n")
    if interface == 'q':
        confMain(ssh)
    else:
        ip_address = input("Addresse IP ? : ")
        mask = input("Masque de sous-réseau : ")
        send(ssh, 'conf terminal')
        send(ssh, 'int ' + interface)
        send(ssh, 'ip add ' + ip_address + " " + mask)
        send(ssh, 'no shut')
        send(ssh, 'end')

    intConf(ssh)

def routeConf(ssh):
    print("\n CONFIUGRATION DES ROUTES\n")
    print("------------------------------------\n")

    send(ssh, 'sh ip route')
    route = input("Adresse à atteindre [q pour quitter] :  ")
    if route == "q":
        confMain(ssh)
    else:
        wildcard = input("Masque inversé : ")
        next = input("Interface ou adresse de prochain saut : ")
        send(ssh, "conf t")
        send(ssh, "ip route " + route + " " + wildcard + " " + next)
    routeConf(ssh)




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


#reponse = input("Voulez vous configurer l'interface g0/1 ?[o/n]")
#reponse = reponse.strip().lower()
#if reponse.startswith('o'):
#    int = Interfaces1(ssh)
#elif reponse.startswith('n') or reponse == '':
#    print("-------------")
#else:
#    print("repondez !")
#reponse2 = input("Voulez vous configurer l'interface g0/2 ? [o/n] ")
#reponse2 = reponse.strip().lower()
#if reponse2.startswith('o'):
#    int2 = Interfaces2()
#elif reponse2.startswith('n') or reponse == '':
#    print("----------------")
#else:
#    print('répondez svp')

if __name__ == '__main__':
    main()
