#! python3

import sys

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

if __name__=='__main__':

    inp = sys.argv[1]
    print('\n\nDisclosed IPs:\n')
    if ',' in sys.argv[1]:
        inp = inp.split(',')
        for i in inp:
            code = Big5Cookie()
            cip, cport = code.split_cookie(i)
            big_ip = code.decode_ip(cip)
            big_port = code.decode_port(cport)

            print(f'{big_ip}:{big_port}')
    else:
        code = Big5Cookie()
        cip, cport = code.split_cookie(i)
        big_ip = code.decode_ip(cip)
        big_port = code.decode_port(cport)

        print(f'{big_ip}:{big_port}')