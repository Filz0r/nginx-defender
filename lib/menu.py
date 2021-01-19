from lib.modules.log_parser import log_parser
from lib.modules.ip_filter import log_finder
from lib.modules.geo_ip import geo_ip
from lib.modules.ip_blocker import ip_blocker
from lib.modules.log_import import log_import
from lib.modules.result import result


# This is my menu solution so far you input the number of the script you want 
# to run in the input box then it runs the scripts right now its all over 
# the place and the order that the scripts come in is not the order you want 
# to run this script if you don't provide the logs before the script runs.
# Also there are a lot of funcionalities that I have yet to implement like 
# for example the script not quiting itself when you run it. It will work more 
# as a program in the future but for now this works.

def menu():
    print('''
############################################################
##                                                        ##
##  What do you want to do?                               ##
##                                                        ##
##  0 -> EXIT                                             ##
##  1 -> look for injection requests in your nginx logs   ##
##  2 -> filter your results                              ##
##  3 -> Find out GeoIP location of these requests        ##
##  4 -> Use ufw to ban found IPs from connecting         ##
##  5 -> Grab logs from the folder                        ##
##  6 -> Create a final result.log file with all of your  ##
##       data parsed and scraped!                         ##
##                                                        ##
############################################################''')
    try:
        question = input('''
############################################################
##                                                        ##
##  What do you want to do? Chose a number!               ##
##                                                        ##
############################################################
INPUT: ''')
        response = int(question)
        if response == 0:
            print('''
############################################################
##                                                        ##
##                      GOOD BYE!                         ##
##                                                        ##
############################################################''')
        elif response == 1:
            response = 0
            log_parser()
        elif response == 2:
            response = 0
            log_finder()
        elif response == 3:
            response = 0
            geo_ip()
        elif response == 4:
            response = 0
            ip_blocker()
        elif response == 5:
            response = 0
            log_import()
        elif response == 6:
            response = 0
            result()
        else:
            print('error invalid choice')
            return menu()

    except:
        print('You need to chose a number')
        return menu()