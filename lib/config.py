from configparser import ConfigParser
from subprocess import run
import os

# This function checks if there is a nginx-defender.conf file, if it does not exist
# it calls the machine_startup function and returns its values back to the settings.py
# if there is a nginx-defender.conf it then proceeds to read the hostname, username, and
# public IP that the server has and then returns these values back to settings.py
def config_check():
    from lib.settings import main_path

    conf_path = main_path + 'nginx-defender.conf'
    conf_check = os.path.isfile(conf_path)
    if conf_check == False:
        return machine_startup()
    else:
        config = ConfigParser()
        config.read(conf_path)
        app_setting = config['SETTINGS']
        hostname = app_setting['hostname']
        username = app_setting['name']
        publicIP = app_setting['publicIP']
        return hostname, username, publicIP

# This function is where the nginx-defender.conf is created, it returns 
# the hostname, username and public IP for the server
def machine_startup():
    from lib.settings import main_path

    sample_path = main_path + 'sample.conf'
    end_path = main_path + 'nginx-defender.conf'
    # Makes a copy of sample.conf renamed as nginx-defender.conf
    # This is needed to run scripts such as the log_import one, that 
    # makes the user that ran the script the owner of the copy of the 
    # logs that the script copies
    cmd = 'cp ' + sample_path + ' ' + end_path
    cmd_split = cmd.split()
    run(cmd_split)
    # Here it opens the sample.conf file and checks if the sample variables
    # are as expected then it stores each of the constants it needs from the file
    # in their respective python vars, it then proceeds to request the user for these
    # constants, as mentioned above they are required for some scripts to run.
    config = ConfigParser()
    config.read(sample_path)
    app_setting =  config['SETTINGS']
    hostname = app_setting['hostname']
    username = app_setting['user']
    publicIP = app_setting['publicIP']
    if hostname == 'none':
        question = input('What is the hostname of this machine? ')
        hostname = question
    if username == 'none':
        question = input('What is the user for this system? (sudo rights required) ')
        username = question
    if publicIP == 'none':
        question = input('What is the Public IP of this server? ')
        publicIP = question
    # This grabs the conf dictionary that it created earliear and assings
    # the new constants to this dictionary, finally it saves them in the
    # nginx-defender.conf file, you can edit this file if you need to change
    # publicIP or something else, but never edit the sample.conf file, as it's
    # required for the startup of the script
    app_setting['hostname'] = hostname
    app_setting['user'] = username
    app_setting['publicIP'] = publicIP
    with open(end_path, 'w+') as conf:
        config.write(conf)
    return hostname, username, publicIP

