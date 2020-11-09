from main import router_username, router_password, router_ip
import paramiko
import  time


def Interfaces():
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
    DEVICE_ACCESS.send(b"ip address 192.168.21.25 255.255.255.0\n")
    DEVICE_ACCESS.send(b"no shut\n")
    DEVICE_ACCESS.send(b"end\n")
    DEVICE_ACCESS.send(b"sh ip int br\n")
    time.sleep(1)

    # Read output from command.
    output = DEVICE_ACCESS.recv(65000)
    print(output.decode('ascii'))

config_interface = Interfaces()



