import paramiko
import time
from getpass import getpass

router_ip = "192.168.100.150"
router_username = "vincent"
router_password = "admin"


class a:

    def run_command_on_device(router_ip, username, password):
        """ Connect to a device, run a command, and return the output."""

        ssh = paramiko.SSHClient()
        # Add SSH host key when missing.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Load SSH host keys.
        ssh.load_system_host_keys()


        total_attempts = 3
        for attempt in range(total_attempts):
            try:
                print("Attempt to connect: %s" % attempt)
                # Connect to router using username/password authentication.
                ssh.connect(router_ip,
                            username=router_username,
                            password=router_password,
                            look_for_keys=False)
                # Run command.
                DEVICE_ACCESS = ssh.invoke_shell()
                DEVICE_ACCESS.send(b"enable\n")
                DEVICE_ACCESS.send(b"vdcvdc\n")
                DEVICE_ACCESS.send(b"conf t\n")
                DEVICE_ACCESS.send(b"int g0/1\n")
                DEVICE_ACCESS.send(b"ip address 192.168.53.121 255.255.255.0\n")
                time.sleep(2)
                # Read output from command.
                output = DEVICE_ACCESS.recv(65000)
                print(output.decode('ascii'))
                # Close connection.
                ssh.close()
                print("c'est fait!")

            except Exception as error_message:
                print("Unable to connect")
                print(error_message)

    lancement_fin = run_command_on_device(router_ip, router_username, router_password)





