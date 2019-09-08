import paramiko

def connect(ip, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=str(ip), username=str(user), password=str(password))
    return ssh