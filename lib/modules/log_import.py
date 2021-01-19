from lib.settings import log_path, username
from subprocess import run, Popen
import os, re

def log_import():
    # Copies all of the files inside the normal nginx log folder
    # onto the scripts log folder
    directory = os.fsencode(log_path)
    cmd1 = 'sudo cp -a /var/log/nginx/. ' + log_path
    splited_cmd1 = cmd1.split()
    run(splited_cmd1)
    # Then for each file it finds proceds to remove the read/write permissions
    # these files usually have root/www-data permissions this helps a lot
    # because this way you don't need sudo permittions to run the script
    # and with this I can make the script request a sudo password everytime 
    # the script actually needs root permissions to execute tasks.
    # this allows for example to place this script in a USB drive and then 
    # copy these log files onto the usb drive, allowing you to find and process
    # results on a different machine, you can after that replug the usb drive to the
    # machine and execute the ip_blocker script.
    #
    # The reason for this is rather simple, the machine you want to protect might
    # not have that much processing power, RAM, or even slow hard drives might 
    # make the script take longer to run. Its not the case for this particular script
    # but it can be a factor on the geo_ip script, the log_parser script, that deals with
    # files with thousands of lines, I/O speed is a factor for these scripts, and the slower
    # the computer is the longer it takes for these scripts to run.
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".log"):
            cmd2 = 'sudo chown www-data:' + username + log_path + filename
            splited_cmd2 = cmd2.split()
            run(splited_cmd2)
            continue
        else:
            print('did not run')
            continue
    

