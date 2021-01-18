from lib.settings import log_path
from subprocess import run, Popen
import os, re

def log_import():

    directory = os.fsencode(log_path)
    cmd1 = 'sudo cp -a /var/log/nginx/. ' + log_path
    splited_cmd1 = cmd1.split()
    run(splited_cmd1)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print('debug')
        if filename.endswith(".log"):
            cmd3 = 'sudo chown biggie ' + log_path + filename
            print(cmd3)
            splited_cmd3 = cmd3.split()
            run(splited_cmd3)
            cmd2 = 'chmod 777 ' + log_path + filename
            print(cmd2)
            splited_cmd2 = cmd2.split()
            run(splited_cmd2)
            continue
        else:
            print('did not run')
            continue
    

