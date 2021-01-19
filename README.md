# About

I still need to write this file properly, don't judge me, basically this this python program goes trough your NGINX logs and looks for requests for a *thonkPHP* injection request I found in my NGINX logs, it is able toto copy all of the files inside `/var/log/nginx` on to its own path, then it goes trough every single line looking for a pattern I built, and bundles all of the requests that onto a single file, from that file you can bundle all of the IP's that keep sending these requests into 2 files, the first has all of the IPs that keep sending these requests, the second tells you how many requests each IP did. Finaly we have the GeoIP functionality and the IP block solution, the GeoIP functionality helps you find
out where are these requests comming from, the second uses UFW to ban all of the unique IPs stored in the file previously mentioned.

This is still under development stage and while it only works for the mentioned request right now, when you first run this script it requests for a machine hostname, username and public IP, right now it only makes use of the username, but as time goes on I want to make it able to for example ban all requests for your wordpress admin page that don't come from your public IP, basically, helping everyone secure their NGINX webserver/reverse proxy easily.

## How to run this script

- Make sure that you are in an account with **sudo** rights, make sure that you have Python3 and git installed.

- **Don't change anything in the `sample.conf` file!!** if your webserver uses reverse DNS to host, change the `nginx-defender.conf` file instead. Eventually I'll take the sample file out of the program, but my skills are still far from implementing that.

- This script should work in any Linux distributions that are running nginx servers, I developed it with WSL and tested it on my own NGINX reverse proxy, running on Ubuntu LTS 20.04. It works as expected within these systems, but your millage may vary.

- Download the script with git by running `git clone https://github.com/Filz0r/nginx-defender`
- Then cd into the directory you just downloaded and run the following command `chmod +x nginx-defender.py`, this allows the script to be executable.
- Finally run the script by typing `./nginx-defender.py`. You can also type `python3 nginx-defender.py` from the same directory to run the script and it will run. The reasons for why I also made this script able to be executed will be discussed in the next part.

## Why I developed this script

Well this one is easy, because **security!!** Having a botnet trying to infect webservers is probably an easy task for most sysadmins, well I had no idea how to do it, so I started to learn about it and soon came to realize that you have to understand how to use iptables of firewalld... I have no idea how to use those softwares, I only know how to use UFW, so I built this tool that helps me achieve similar results, I hope, but with UFW. Eventually I want to implement plenty more functionalities to this program, like running these scripts in the background, as an system app, the installing part is easy, at least on Ubuntu systems. Finally you can find a more compreensive README inside each of the files of the script as they have lots of comments in there explaining what each block of code does, and sometimes even the why.

**DISCLAIMER:** *I am just starting you as an Python developer, and if you are one, you might see that I use a lot of `os` imports in my scripts, this is something that I've been told and read about, `os` is being depricated, but I really need it to make the program path aware and file aware in some cases, something that it does really well, so if you have read trough my code and know how to make these blocks of code more updated and have please feel free to improve it in order to improve this program!* 