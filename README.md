## Description

This is a set of cli commands written to help bulk run cmd commands for  a cluster of raspberry pi 4's using the click and paramiko libraries.

## Dependencies

```bash
# Paramiko
pip install paramiko

# Click
pip install click
```

## Running the code

At the moment this is written on a windows os so you have to run through python interpreter like so:

```bash
python pythonCLI.py testconn
```

Also the IP addresses of my cluster are hard coded in an array of dictionaries and if you ever want to add one temporarily you just input ip, username, and password for new device and it will be added as a new dictionary in the array.

To run a specific command on each device run the "cmd" script and input your command with the --command tag like so:

```bash
python pythonCLI.py --command '/opt/vc/bin/vcgencmd measure_temp' cmd
```

This example outputs the CPU temperature for each device

## Author
Jake Pifer
