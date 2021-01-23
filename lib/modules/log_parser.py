import os, datetime, re
from lib.settings import log_path, parsed_path


def log_parser():
    # First we have my counting variable, then we have a timestamp and
    # finally we have the name of the file where all of the requests 
    # will be filtered out to.
    ct = 0
    timestamp = datetime.datetime.now().strftime("%d-%b-%Y-%I:%M%P")
    parsed_log_file = 'parsed-default-' + timestamp + '.log'
    # Now I create my output file and declare the pattern I want to look for
    parsed_log = open(parsed_path + parsed_log_file, 'w+')
    pattern = ' ./thonkphp ThinkPHP '
    # Finally the magic starts, for each file there is inside the log folder
    # we grab the filename
    for file in os.listdir(log_path):
        filename = os.fsdecode(file)
        # If the filename ends with .log...
        if '.log' in filename and '.gz' not in filename:
            # We open it to read it
            hand = open(log_path + filename, 'rt')
            # Then for each line in this file that has the pattern I declared earlier
            for line in hand:
                line = line.rstrip()
                stuff = re.findall(pattern, line)
                # really making sure the line has the pattern
                if line.find(pattern) != -1:
                    # I write it down to the output file
                    parsed_log.write(str(line + '\n'))
                    # And add 1 to my counter
                    ct = ct + 1
                # if the line I just found has nothing, keep on going python
                if len(stuff) != 1 :
                    continue
            hand.close()
            #continue until there are no more files with .log in the name
            continue
        else:
            # If you don't have any files with .log in this directory, well the script will skip them
            # and you will get 0 results found and an empty output file, horrray!!
            continue

    print('done, found ' + str(ct) + ' results')
    print('You can find the result of this script in the results folder with the filename: ' + str(parsed_log_file))
    from lib.menu import menu
    menu()
