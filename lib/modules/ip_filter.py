import re
from lib.settings import parsed_path, results_path

def log_finder():
    filename = input('what is the file name of the parsed log you want to filter? ')
    ip_filter(filename)


def ip_filter(filename):
    path = parsed_path + filename
    pattern = '^([0-9].+?) '
    ct = 0

    hand = open(path, 'rt')
    ip_dic = dict()
    
    for line in hand:
        line = line.rstrip()
        stuff = re.findall(pattern, line)
        ip = str(stuff)[2:-2]
        if ip not in ip_dic:
            ip_dic[ip] = 1
        else:
            ip_dic[ip] = ip_dic[ip] + 1

    filtered_log = open(results_path + 'filtered.log', 'w+')
    ip_list = open(results_path + 'ip-list.log', 'w+')
    
    for key in ip_dic:
        filtered_log.write((str(key) + ' has made ' + str(ip_dic[key]) + ' requests to your server' + '\n'))
        ip_list.write(key + '\n')
        ct = ct + 1

    print('done, I found a total of ' + str(ct) + ' different IPs making these requests')
    print('You can check out the results of this script in ' + results_path)
    from lib.menu import menu
    menu()