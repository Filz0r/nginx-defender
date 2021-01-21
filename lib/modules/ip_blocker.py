from lib.settings import results_path
import subprocess

def ip_blocker():
    # Rather simple block of code, I start by declaring the path to the file with all
    #  of the IPs found then I loop trough it while running the command.
    # this will also try to ban old ips, if you to keep track of them you can remove them
    # from this list manually, I'll automate this eventually.
    # also I might look into bulk blocking regions instead of single IPs in the future
    # however I don't think this is the case because if you run the geoip script you will
    # probably find out the same thing as me, these requests come from all over the world!

    path = results_path + 'ip-list.log'
    hand = open(path, 'rt')

    for ip in hand:
        cmd = 'sudo ufw insert 1 reject from ' + str(ip) + ' to any'
        splited_cmd= cmd.split()
        subprocess.run(splited_cmd)
    hand.close()    
    print('Done!')
    from lib.menu import menu
    menu()