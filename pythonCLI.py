import click
import requests
import paramiko
import os
import subprocess

from functions import *
from values import *


@click.group()
@click.option('--ip', '-i', help='This is the ip address of the device you wish to connect to.')
@click.option('--password', '-p', help='The password of the device you are trying to connect to.',)
@click.option('--user', '-u', help='The username of the device you are trying to connect to.',)
@click.option('--command', '-c', help='The command you wish to run on each device.',)
@click.option('--syspass', '-sp', help='The new system password')
@click.option('--sysuser', '-su', help='The new system username')
@click.option('--bulk', '-b', help='States whether this is a bulk action.')
@click.pass_context
def cli(ctx, ip, user, password, command, sysuser, syspass, bulk):
    """
    CLI tool used for SSH into rpi 4's and using commands
    """

    if(ip):
        ctx.obj['IP'] = ip
        newDevice = {
            'USER': user,
            'PASSWORD': password
        }
        ctx.obj[str(ip)] = newDevice
    elif(command):
        ctx.obj['COMMAND'] = command
    elif(sysuser):
        ctx.obj['SYSUSER'] = sysuser
    elif(syspass):
        ctx.obj['SYSPASS'] = syspass
    elif(bulk):
        ctx.obj['BULK'] = bulk


@cli.command()
@click.pass_context
def testconn(ctx):
    """
    Test connection to rpi at given ip address. This will currently print out the temperature that 
    """

    # This loops through the dict of devices and connects and shows the temp for each one
    for key in ctx.obj:
        ssh = connect(str(key), ctx.obj[str(key)]
                      ['USER'], ctx.obj[str(key)]['PASSWORD'])

        stdin, stdout, stderr = ssh.exec_command(
            '/opt/vc/bin/vcgencmd measure_temp')

        print(*stdout.readlines(), sep='\n')


@cli.command()
@click.pass_context
def cmd(ctx):
    """
    This will loop through selected devices, bulk or individual, and do the command given to it.
    """
    print(ctx.obj['BULK'])
    # Check if bulk tag is absent or not
    if(ctx.obj['BULK']):
        # This loops through the dict of devices and runs the inputted command for each one
        for key in ctx.obj:
            if(str(key) != 'COMMAND'):  # Check to make sure that the current iteration is an IP
                ssh = connect(str(key), ctx.obj[str(key)]
                              ['USER'], ctx.obj[str(key)]['PASSWORD'])

                stdin, stdout, stderr = ssh.exec_command(
                    str(ctx.obj['COMMAND']))

                print(*stdout.readlines(), sep='\n')
    # Bulk tab is absent
    else:
        # Check to make sure that IP address is present
        if(ctx.obj['IP']):
            ssh = connect(ctx.obj['IP'], ctx.obj['IP']
                          ['USER'], ctx.obj['IP']['PASSWORD'])

            stdin, stdout, stderr = ssh.exec_command(str(ctx.obj['COMMAND']))

            print(*stdout.readlines(), sep='\n')
        else: # IP address and bulk tag are not present so state so
            print("No IP address given and one is needed when not using bulk tag.")


# @cli.command()
# @click.pass_context
# def supop(ctx):
#     """
#     This is used to change the systems default username or password
#     """
#     if(ctx.obj['SYSUSER']):
#         os.system('powershell.exe $Env:PI_USER = ' + "'" + str(ctx.obj['SYSUSER']) + "'")
#         click.echo('This is the new systems username: ' + ctx.obj['SYSUSER'])
#     elif(ctx.obj['SYSPASS']):
#         os.system('powershell.exe [$Env:PI_PASS = ' + ctx.obj['SYSPASS'] + ']')
#         click.echo('This is the new systems password: ' + ctx.obj['SYSPASS'])


if __name__ == '__main__':
    cli(obj={
        '192.168.1.12': {
            'USER': user,
            'PASSWORD': password
        }
    }
    )
