import os, datetime, re
from lib.settings import log_path, parsed_path


def log_parser():
    directory = os.fsencode(log_path)
    ct = 0
    timestamp = datetime.datetime.now().strftime("%d-%b-%Y-%I:%M%P")
    parsed_log_file = 'parsed-default-' + timestamp + '.log'
    parsed_log = open(parsed_path + parsed_log_file, 'w+')
    pattern = ' ./thonkphp ThinkPHP '

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".log"):
            hand = open(log_path + filename, 'rt')
            for line in hand:
                line = line.rstrip()
                stuff = re.findall(pattern, line)
                if line.find(pattern) != -1:
                    parsed_log.write(str(line + '\n'))
                    ct = ct + 1
                if len(stuff) != 1 :
                    continue
            continue
        else:
            print('It seems like you don\'t have any logs that this script can access\nPlease run the log import script then run this again!')
            continue

    print('done, found ' + str(ct) + ' results')
