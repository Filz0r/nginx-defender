from lib.settings import log_path
from subprocess import run, Popen
import os, re

def log_import():

    directory = os.fsencode(log_path)
    cmd1 = 'sudo cp -a /var/log/nginx/. ' + log_path
    splited_cmd1 = cmd1.split()
    Popen(splited_cmd1)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".log"):
            cmd3 = 'sudo chown biggie ' + log_path + filename
            splited_cmd3 = cmd3.split()
            print(cmd3)
            Popen(splited_cmd3)
            continue
    

