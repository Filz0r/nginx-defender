from lib.settings import results_path
import json, operator

def result():
    path = results_path + 'geoip-sorted.json'
    result = results_path + 'result.log'
    country_dict = dict()

    hand = open(result, 'w+')

    with open(path, 'rt') as json_file:
        data = json.load(json_file)
        # Populates the dictionary used to check what is the country with the most requests
        for info in data:
            if info['country'] not in country_dict:
                if info['requests'] > 1:
                    country_dict[info['country']] = info['requests']
                else:
                    country_dict[info['country']] = 1
            else:
                if info['requests'] > 1:
                    country_dict[info['country']] = info['requests'] + country_dict[info['country']]
                else:
                    country_dict[info['country']] = country_dict[info['country']] + 1
        # Counts the requests by timezone
        n = 0 
        m = 0
        x = 0
        y = 0
        z = 0
        o = 0
        for info in data:
            if 'Europe' in info['timezone']: n += 1
            elif 'Asia' in info['timezone']: m += 1
            elif 'America' in info['timezone']: x += 1
            elif 'Africa' in info['timezone']: y += 1
            elif 'Pacific' in info['timezone']: z += 1
            elif 'Indian' in info['timezone']: o += 1
            else:
                print('your error is:')
                print(info)
        
        total = 0
        for key in country_dict:
            total += country_dict[key]

        highest = max(country_dict.items(), key=operator.itemgetter(1))[0]

        hand.write('the country with more requests was ' + highest + ' with a total of ' + str(country_dict[highest]) + ' requests made!\n')
        hand.write('Europe requests: ' + str(n) + '\n')
        hand.write('Asia requests: ' + str(m) + '\n')
        hand.write('America requests: ' + str(x) + '\n')
        hand.write('Africa requests: ' + str(y) + '\n')
        hand.write('Pacific requests: ' + str(y) + '\n')
        hand.write('Indian requests: ' + str(y) + '\n')
        hand.write('Total requests found: ' + str(total) + '\n')
        hand.write('--------------------------\n')

        for info in data:
            hand.write('The IP: ' + str(info['ip']) + '\n')
            hand.write('The Timezone: ' + str(info['timezone']) + '\n')
            hand.write('The Country code: ' + str(info['country']) + '\n')
            hand.write('The Region: ' + str(info['region']) + '\n')
            hand.write('The City: ' + str(info['city']) + '\n')
            hand.write('The IP belongs to: ' + str(info['org']) + '\n')
            hand.write('The number of requests made: ' + str(info['requests']) + '\n')
            if 'hostname' in info:
                hand.write('The Hostname of the server: ' + str(info['hostname']) + '\n')
            else:
                hand.write('The Hostname of the server: No hostname found' + '\n')
            hand.write('--------------------------')

    hand.close()
    print('Your results are writen in the result.log file that is stored in the results directory')
