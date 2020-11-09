#from main import run_command_on_device
#from main import router_username, router_password, router_ip
import paramiko
import time



def sendRec(ssh, command):
    """Send a command to the device and receive and print the result."""

    # Send the device a command
    ssh.send("\n")
    ssh.send(str(command) + "\n")

    # Wait for the command to complete in seconds
    time.sleep(1)

    # Receive 5000 bytes and print to screen
    output = ssh.recv(5000)
    print(output)


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
            output = ssh.recv(1000)
            print(output)


        except paramiko.AuthenticationException:
            print("Incorrect password: ")
    except:
        print("Quelque chose ne vas pas")


def Interfaces1(ssh):
    #ssh = paramiko.SSHClient()
    # Add SSH host key when missing.
    #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Load SSH host keys.
    #ssh.load_system_host_keys()
    #ssh.connect(router_ip,
                #username=router_username,
                #password=router_password,
                #look_for_keys=False)

    #DEVICE_ACCESS = ssh_pre.invoke_shell()
    sendRec(ssh, "enable")
    sendRec(ssh, "vdcvdc\n")
    ssh.send(b"conf t\n")
    ssh.send(b"int g0/1\n")
    ssh.send(b"ip address 192.168.1.25 255.255.255.0\n")
    ssh.send(b"no shut\n")
    ssh.send(b"end\n")
    ssh.send(b"sh ip int br\n")
    time.sleep(1)

    # Read output from command.
    output = ssh.recv(65000)
    print(output.decode('ascii'))

    Interfaces1(ssh)

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