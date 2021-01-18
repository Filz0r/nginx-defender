from lib.settings import results_path

def geo_ip():
    from urllib.request import urlopen
    import json, re

    # files used by the script to either read information
    # or to write information to
    path = results_path + 'ip-list.log'
    result_path = results_path + 'geo-ip.json'
    path1 = results_path + 'filtered.log'
    path2 = results_path + 'geoip-sorted.json'

    # variables and constants used to produce the output files
    info = list()
    pattern1 = ' ([0-9]) '
    result = ''
    ct = 0
    i = 0

    #handlers that read the files
    hand = open(path, 'rt')
    hand1 = open(path1, 'rt')
    # makes a request to ipinfo.io asking for information 
    # on each IP stored inside ip-list.log
    for line in hand:
        ip = line
        url = 'https://ipinfo.io/' + ip[:-1] + '/json'
        res = urlopen(url)
        data = json.load(res)
        info.append(data)
        ct = ct + 1
    # writes the response to a json file
    with open(result_path, 'w+') as outfile:
        json.dump(info, outfile, sort_keys=True, indent=4)
    # parses the json file just created and adds the ammount of requests
    # each IP made trying to inject a payload
    with open(result_path, 'rt') as json_file:
        data = json.load(json_file)
        for line in hand1:
            line = line.rstrip()
            requests_made = re.findall(pattern1, line)
            if len(requests_made) !=  1 : continue 
            req_parsed = int(str(requests_made)[2:-2])
            data[i]['requests'] = req_parsed
            i = i + 1
            
        result = data
    # writes the combined result to a new file
    with open(path2, 'w+') as output:
        json.dump(result, output, sort_keys=True, indent=4)
    print('I\'ve made a total of ' + str(ct) + ' requests to https://ipinfo.io/ and wrote the raw json output into geo-ip.json in the results folder')
    print('Then I added how many requests, each IP made to you and put all the results into geo-ip-sorted.json in the results folder\nThis is the file that the final result.log will use to give conclusions')