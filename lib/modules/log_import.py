from lib.settings import log_path
from subprocess import run, Popen
import os, re

def log_import():

    directory = os.fsencode(log_path)
    cmd2 = 'sudo cp -a /var/log/nginx/. ' + log_path
    splited_cmd2 = cmd2.split()
    Popen(splited_cmd2)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".log"):
            cmd3 = 'sudo chown biggie ' + log_path + filename
            splited_cmd3 = cmd3.split()
            run(splited_cmd3)
            continue
    

