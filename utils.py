import time
import logging
import paramiko

logging.basicConfig(filename='log.log', level=logging.DEBUG,\
      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

def send(shell, command):
    """
    Function to send specific commands
    """

    shell.send("\n")
    shell.send(str(command) + "\n")

    time.sleep(.5)

    output = shell.recv(65000)
    print(output.decode('ascii'))

def getSSHConnection():
    """
    Main function that initializes the ssh connection by asking for the targeted ip address,
    user and password
    """

    logging.info('Connexion SSH')

    router_ip = input("Entrez l'adresse IP cible : ")
    router_username = input("Entrez le username : ")
    router_password = input("Entrez le mot de passe : ")

    try:
        ssh_pre = paramiko.SSHClient()
        ssh_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh_pre.load_system_host_keys()

        try:

            # Connect to router using username/password authentication.
            ssh_pre.connect(router_ip,
                            username=router_username,
                            password=router_password,
                            look_for_keys=False)
            print("Connexion réussie")
            shell = ssh_pre.invoke_shell()
            output = shell.recv(65000)
            print(output.decode('ascii'))

            send(shell, "enable")
            send(shell, "vdcvdc\n")

        except paramiko.AuthenticationException:
            print("Mot de passe incorrect : ")
            logging.error("Mauvais identifiant !")
    except:
        print("Quelque chose ne vas pas")
        logging.error("Problème de connexion")
    return(shell)

