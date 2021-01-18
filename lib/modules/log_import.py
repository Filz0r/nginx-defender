from lib.settings import log_path
from subprocess import run, Popen
import os, re

def log_import():

    directory = os.fsencode(log_path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".log"):
            cmd1 = 'rm ' + log_path + filename
            splited_cmd1 = cmd1.split()
            run(splited_cmd1)
            continue
        else:
            continue
    try:
        cmd2 = 'sudo cp /var/log/nginx/*.log ' + log_path
        splited_cmd2 = cmd2.split()
        Popen(splited_cmd2)

        cmd3 = 'sudo chown biggie ' + log_path + '*.log'
        splited_cmd3 = cmd3.split()
        run(splited_cmd3)
        print('cmd2: ' + cmd2)
        print('cmd3: ' + cmd3)
        print('Nginx logs have been updated!')
    except:
        print('could not import')

    

