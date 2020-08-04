#! python3

import sys
import requests
import urllib3
import re

urllib3.disable_warnings()

class Big5Cookie:
    
    def __init__(self):
        pass

    def split_cookie(self, cookie):
        split = cookie.split('.')

        ip = split[0]
        port = split[1]

        return ip, port

    def decode_ip(self, ip):

        hex_ip = hex(int(ip))
        hex_ip = hex_ip[2:]

        digits = [hex_ip[i:i+2] for i in range(0, len(hex_ip), 2)]
        add_ip = []

        for i in digits:
            val = str(int(i, 16))
            add_ip.append(val)

        return f'{add_ip[3]}.{add_ip[2]}.{add_ip[1]}.{add_ip[0]}'

    def decode_port(self, port):
        
        hex_port = hex(int(port))
        hex_port = hex_port[2:]

        digits = [hex_port[i:i+2] for i in range(0, len(hex_port), 2)]
        add_port = ''

        for i in digits:
            val = str(int(i, 16))
            if int(val) != 0:
                add_port = val + add_port

        return add_port

def get_cookie(url):
    try:
        req = requests.get(url, verify=False)
        cookie = req.cookies.get_dict()
        for i in cookie:
            if re.search(r"\d{7,}\.\d{4,}\.0000", cookie.get(i)):
                return cookie.get(i)
            else:
                continue
        return None
    except:
        return None


if __name__=='__main__':

    inp = sys.argv
    inp.pop(0)

    cookies = []
    
    for i in inp:
        f5_cookie = get_cookie(i)
        if f5_cookie != None:
            cookies.append({'url': i, 'cookie': f5_cookie})

    
    print('\nDisclosed IPs:')
    for j in cookies:
        code = Big5Cookie()
        cip, cport = code.split_cookie(j['cookie'])
        big_ip = code.decode_ip(cip)
        big_port = code.decode_port(cport)

        print(f'[{j["url"]}] = IP: {big_ip}, Port: {big_port}')