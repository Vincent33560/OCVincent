import paramiko
import time
from getpass import getpass
from interfaces import config_interface

router_ip = input("Entrez l'adresse IP cible : ")
router_username = input("Entrez le username : ")
router_password = input("Entrez le mot de passe : ")

def run_command_on_device(router_ip, username, password):
    """ Connect to a device, run a command, and return the output."""
    try:
        ssh = paramiko.SSHClient()
        # Add SSH host key when missing.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Load SSH host keys.
        ssh.load_system_host_keys()

        try:
            # Connect to router using username/password authentication.
            ssh.connect(router_ip,
                        username=router_username,
                        password=router_password,
                        look_for_keys=False)
            print("Connexion réussie")

            # Run command.
            DEVICE_ACCESS = ssh.invoke_shell()

            config_interface

            # Read output from command.
            output = DEVICE_ACCESS.recv(65000)
            print(output.decode('ascii'))
            # Close connection.
            ssh.close()

        except paramiko.AuthenticationException:
            print("Incorrect password: ")
    except:
        print("Quelque chose ne vas pas")


# run_command_on_device(router_ip, router_username, router_password)
start_connect = run_command_on_device(router_ip, router_username, router_password)
