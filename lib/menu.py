from lib.modules.log_parser import log_parser
from lib.modules.ip_filter import log_finder
from lib.modules.geo_ip import geo_ip
from lib.modules.ip_blocker import ip_blocker
from lib.modules.log_import import log_import

def menu():
    print('''
############################################################
##                                                        ##
##  What do you want to do?                               ##
##                                                        ##
##  1 -> look for injection requests in your nginx logs   ##
##  2 -> filter your results                              ##
##  3 -> Find out GeoIP location of these requests        ##
##  4 -> Use ufw to ban found IPs from connecting         ##
##  5 -> Grab logs from the folder                        ##
##                                                        ##
############################################################''')
    #try:
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
    else:
        print('error invalid choice')
        return menu()

    #except:
     #   print('You need to chose a number')
      #  return menu()