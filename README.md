Some version of F5 BigIP devices disclose an encoded version of the internal ip address and port of the device in a cookie.  This encoded cookie is easily decoded to reveal this IP and port combination.  This is a standalone script to automate the process of finding and decoding these cookies to find internal addresses.

For more information, please see https://securityriskadvisors.com/blog/finding-and-decoding-big-ip-and-netscaler-cookies-with-burp-suite/.

Usage:

hexbot.py [url1] [url2] [url3]...