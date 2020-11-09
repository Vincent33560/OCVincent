import paramiko
import time
import os
import csv

from pip._vendor.distlib.compat import raw_input


def sendRec(ssh, command):
    """Send a command to the device and receive and print the result."""

    # Send the device a command
    ssh.send("\n")
    ssh.send(str(command) + "\n")

    # Wait for the command to complete in seconds
    time.sleep(1)

    # Receive 5000 bytes and print to screen
    output = ssh.recv(5000)
    print
    output


def main():
    global username, password
    longstring = """\
    \n
            /,,
           /\  )
             \,'
          /`'`\.
              ,
             ,@,
            ,@@@,
           ,@@@@@,
    `@@@@@@@@@@@@@@@@@@@`
      `@@@@@@@@@@@@@@@`
        `@@@@@@@@@@@`
       ,@@@@@@`@@@@@@,
       @@@@`     `@@@@
      ;@`           `@;
        _   _   _   _
       (   (   (   |_)
        ~   ~   ~  |

    Cisco 
    CLI
    Configuration with
    Paramiko
    Written by: Patrick Sinotte
    Version 2.2864
    Welcome, Comrade!
    """

    # Clear screen and print welcome to screen
    os.system("clear")
    print
    longstring

    # Prompt user for pre-configured IP address and ssh credentials
    ip = raw_input("Enter IP address of device (q to quit): ")
    if ip == "q":
        exit()
    else:
        username = raw_input("username: ")
        password = raw_input("password: ")

    # Create instance of SSHClient object
    ssh_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts
    ssh_pre.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    # initiate SSH connection
    ssh_pre.connect(ip, username=username, password=password)
    print
    "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    ssh = ssh_pre.invoke_shell()
    print
    "Interactive SSH session established"

    # Strip the initial router prompt
    output = ssh.recv(1000)



    # Turn off automatic domain-lookup
    sendRec(ssh, "conf t")
    sendRec(ssh, "no ip domain-lookup")

    devMain(ssh)


def devMain(ssh):
    """The main menu once connected to a device.

    Allows user to go to show(), confMain(), connTest(), fileMan(), or main().
    """

    # Show version and connected users
    sendRec(ssh, "\x1a")
    sendRec(ssh, "show version | include Cisco IOS")
    sendRec(ssh, "show users")

    # Show main menu and interpret user choice
    menu_choice = -1
    while 0 > menu_choice or 4 < menu_choice:
        try:
            print
            "\nMAIN MENU"
            print
            "Please choose from one of the following options:"
            print
            """\n
                1 - show configuration \n
                2 - configure device \n
                3 - test connectivity \n
                4 - save/load \n
                0 - logout \n"""
            menu_choice = int(raw_input())
        except ValueError:
            print
            "Choose a number from 1 to 4"
    if menu_choice == 1:
        show(ssh)

def show(ssh):
    """Allows user to run a variety of show commands."""

    menu_choice = -1
    while 0 > menu_choice or 8 < menu_choice:
        try:
            print
            "\nSHOW MENU"
            print
            "Please choose from one of the following options:"
            print
            """\n
                1 - show running configuration \n
                2 - show ip interfaces brief \n
                3 - show routing table \n
                4 - show CDP neighbors \n
                5 - show flash \n
                6 - show version \n
                7 - show license \n
                8 - show vlans \n
                0 - back \n"""
            menu_choice = int(raw_input())
        except ValueError:
            print
            "Choose a number from 1 to 8"
    if menu_choice == 1:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show run")
    elif menu_choice == 2:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show ip int b")
    elif menu_choice == 3:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show ip route")
    elif menu_choice == 4:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show cdp neigh")
    elif menu_choice == 5:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show flash")
    elif menu_choice == 6:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show version")
    elif menu_choice == 7:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show license")
    elif menu_choice == 8:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show vlan")

    elif menu_choice == 0:
        devMain(ssh)
    show(ssh)


main()