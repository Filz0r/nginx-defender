from lib.settings import results_path
import subprocess

def ip_blocker():
    path = results_path + 'ip-list.log'

    hand = open(path, 'rt')

    for ip in hand:
        cmd = 'sudo ufw insert 1 deny from ' + str(ip) + ' to any'
        splited_cmd= cmd.split()
        subprocess.run(splited_cmd)