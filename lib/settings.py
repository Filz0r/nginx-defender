import os
from  subprocess import run
import lib.settings as settings
from lib.config import config_check, machine_startup

# Finds the absolute path from where the script is running, 
# then it assigns a couple of variables that are imported
# in various scripts, this file is basically where global 
# constants are declared and created to be used in the rest
# of the program.
path = os.path.realpath(__file__)
main_path = os.path.realpath(__file__)[:len(path) - 15]
log_path = main_path + 'logs/'
parsed_path = main_path + 'parsed/'
results_path = main_path + 'results/'

# This block of code is where the path awareness starts
# since the program requires a username to change permissions
# to avoid running the script as sudo when filtering and 
# gathering information, this way you can run this program portably
# I'm implementing these features because my web server is a rather old
# laptop with not much juice, so when my logs get gigantic I can process them
# on my main laptop that is more modern.
username = None

if username == None:
    (username, hostname, publicIP) = config_check()

# Again here global constants are declared, however these are the constants that
# the scripts require to read, filter and produce results, the first block checks if
# the directories exist, the second, creates them if they do not exist
# If you want you can create an directory called logs in the root of the program
# and copy your files there, as long as they end with .log it will be read.
log_dir_check = os.path.isdir(main_path + 'logs')
parsed_dir_check = os.path.isdir(main_path + 'parsed')
results_dir_check = os.path.isdir(main_path + 'results')

if log_dir_check == False:
    cmd = 'mkdir ' + main_path + 'logs'
    splited_cmd = cmd.split()
    run(splited_cmd)

if parsed_dir_check == False:
    cmd = 'mkdir ' + main_path + 'parsed'
    splited_cmd = cmd.split()
    run(splited_cmd)

if results_dir_check == False:
    cmd = 'mkdir ' + main_path + 'results'
    splited_cmd = cmd.split()
    run(splited_cmd)