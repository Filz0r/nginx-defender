from lib.settings import results_path
import subprocess

def ip_blocker():
    path = results_path + 'ip-list.log'

    cmd = "while read line; do sudo ufw insert 1 deny from $line to any; done < " + path
    splited_cmd = cmd.split()
    subprocess.run(splited_cmd)
    print('all the ips on the ip-list.log have been banned with ufw!')