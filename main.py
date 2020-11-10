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
    time.sleep(.5)

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
            print("Mot de passe incorrect : ")
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
        mainMenu()

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
        send(ssh, 'end')
    routeConf(ssh)

def setHostname(ssh):
    print("\n CONFIUGRATION HOSTNAME \n")
    print("-----------------------------\n")

    hostname = input("Entrez un Hostname : ")
    send(ssh, 'conf t')
    send(ssh, 'hostname ' + hostname)
    send(ssh, 'end')
    confMain(ssh)

def connTest(ssh):
    menu_choice = -1
    while 0 > menu_choice or 4 < menu_choice:
        try:
            print("\n MENU TEST DE CONNEXION\n")
            print("--------------------\n")

            print("Choisissez parmi les propositions suivantes : ")
            print(
                """\n\n\n
                1 - TRACEROUTE
                -----------------------------
                2 - PING
                -----------------------------
                0 - Quitter               
                -----------------------------
                \n\n\n"""
            )

            menu_choice = int(input())

        except ValueError:
            print("Choisissez un chiffre entre 1 et 2")

    if menu_choice == 1:
        traceTest(ssh)
    elif menu_choice == 2:
        pingTest(ssh)
    elif menu_choice == 0:
        mainMenu(ssh)


def traceTest(ssh):
    print("\nTRACEROUTE\n")
    print("--------------")

    trace = input("Entrez une addresse que vous souhaitez tracer : ")
    send(ssh, "traceroute " + trace)
    time.sleep(10)
    output = ssh.recv(65000)
    print(output.decode('ascii'))

    connTest(ssh)

def pingTest(ssh):
    print("\nTEST DE PING\n")
    print("----------------------")

    ping = input("Entrez une adresse que vous souhaitez pinguer : [q pour quitter")
    if ping == 'q':
        connTest(ssh)
    else:
        send(ssh, "ping " + ping)
        send(ssh, "end")
        time.sleep(5)
        output = ssh.recv(65000)
        print(output.decode('ascii'))

        connTest(ssh)

if __name__ == '__main__':
    main()
