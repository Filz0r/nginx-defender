from lib.settings import log_path
from subprocess import run

def log_import():

    cmd1 = 'rm -rf ' + log_path + '*.log'
    splited_cmd1 = cmd1.split()
    run(splited_cmd1)

    cmd2 = 'sudo cp /var/log/nginx/*.log ' + log_path
    splited_cmd2 = cmd2.split()
    run(splited_cmd2)

    cmd3 = 'sudo chmod 777 ' + log_path + '*.log'
    splited_cmd3 = cmd3.split()
    run(splited_cmd3)
    print('Nginx logs have been updated!')

