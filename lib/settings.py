import os
import subprocess

path = os.path.realpath(__file__)
main_path = os.path.realpath(__file__)[:len(path) - 15]
log_path = main_path + 'logs/'
parsed_path = main_path + 'parsed/'
results_path = main_path + 'results/'

log_dir_check = os.path.isdir(main_path + 'logs')
parsed_dir_check = os.path.isdir(main_path + 'parsed')
results_dir_check = os.path.isdir(main_path + 'results')

if log_dir_check == False:
    cmd = 'mkdir ' + main_path + 'logs'
    splited_cmd = cmd.split()
    subprocess.run(splited_cmd)

if parsed_dir_check == False:
    cmd = 'mkdir ' + main_path + 'parsed'
    splited_cmd = cmd.split()
    subprocess.run(splited_cmd)

if results_dir_check == False:
    cmd = 'mkdir ' + main_path + 'results'
    splited_cmd = cmd.split()
    subprocess.run(splited_cmd)