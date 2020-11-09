import paramiko
import logging
import time
import socket
import traceback
import re
import struct

IP = input("Entrez l'adresse IP cible : ")
Username = input("Entrez le username : ")
Password = input("Entrez le mot de passe : ")


def __init__(self, IP="", username="", password="", timeout=15):
    self.ip = IP,
    self.username = username,
    self.password = password,
    self.con_timeout = timeout,
    self.timeout = 100
    self.etablished_connection()

def establish_connection(self):
    """Establish a session with client with paramiko."""
    try:
        self.logger.info("Trying to connect to %s", self.ip)
        # Create a new SSH client object
        self.client = paramiko.client.SSHClient()
        # Set SSH key parameters to auto accept unknown hosts
        self.client.load_system_host_keys()
        # Set SSH key parameters to auto accept unknown hosts
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the host
        self.client.connect(hostname=self.ip,
                            username=self.username,
                            password=self.password,
                            timeout=self.conn_timeout
                            )
        self.logger.info("Successfully connected to %s", self.ip)

    except socket.error:
        self.logger.error("Socket error while \
                trying to connect to {}".format(self.ip))

    except paramiko.AuthenticationException:
        self.logger.error("Authentication error while \
                trying connect to {}".format(self.ip))
        return

    except paramiko.SSHException:
        return
    except Exception:
        traceback.print_exc()
    return ""
