#!/usr/bin/env python3

from validate_email import validate_email
import itertools, getopt, sys, re, threading, time

data={
    'email':'',
    'bf':'',
    'chars':'1234567890abcdefghijklmnopqrsturwxyz.',
    'filein':'', 
    'fileout':'', 
    'time':0.3,
    'count':0,
    'success':0
}

def usage(msg=''):
    print("""\nUsage: argus.py [-b] [-c charset] [-i filein] [-o fileout] [-t xx]
    
    -e <email>          Single validation check
    -i <file in>        Dictionary
    -b                  Brute-force 
    -c [characters]     Characters set to bruteforce - Default is [a-z0-9.]
    -t [interval]       Set time between two verifications - Default is 0.3s - range is [0-600]
    -o [file out]       Ouput results to file
    -h                  Help
    
    Examples:
    Single Email verification
        argus.py -e example@example.com [-t 0.1]
    Dictionary verification
        argus.py -i dictionary.txt [-o results.txt] [-t 0.1]
    Brute-force verification
        argus.py -b examp**3*5@example.com [-c 1g7.] [-o results.txt] [-t 0.1]
""")

    if msg:
        print(msg)
    sys.exit(1)
    
def bruteforce_list(charset, length):
    return itertools.product(charset, repeat=length)
    
def verify(email,fileout=''):
    data['count']+=1
    if fileout:
        try:
            f = open(fileout,'a+')
            if validate_email(email):
                data['success']+=1
                f.write('[+] '+str(email)+' >> Valid\n')
            else:
                f.write('[-] '+str(email)+'\n')
            f.close()
        except IOError:
            print("[!] The file does not exist anymore...\n...Quitting...")
            sys.exit(1)
    else:
        if validate_email(email):
            data['success']+=1
            print('[+] ',email,' >> Valid')
        else:
            print('[-] ',email)

def from_file():
    try:
        file = data['filein']
        f=open(file,'r')
        while True:
            e = f.readline().replace('\n','').replace('\r','')
            if not e:
                break
            t = threading.Thread(target=verify, args=(e,data['fileout'],))
            t.start()
            time.sleep(data['time'])
    except IOError:
        print("[!] The file does not exist...\n...Quitting...")
        sys.exit(1)

def brute_force():
    if not re.findall('\*+',data['bf']):
        print('[!] (*) not found in email pattern')
        sys.exit(0)
    else:
        lenx = data['bf'].count('*')
        for e in bruteforce_list(data['chars'], lenx):
            email = data['bf']
            for s in range(lenx):
                for t in e:
                    email = email.replace('*',t, 1)
            t = threading.Thread(target=verify, args=(email,data['fileout'],))
            t.start()
            time.sleep(data['time'])

def single_check():
    try:
        if '@' not in data['email']:
            raise ValueError
        else:
            email_sub = data['email'].split("@")
        for char in email_sub[0]:
            if char not in data['chars']:
                raise ValueError
    except:
        print('[!] Email format Error')
        sys.exit(0)        
    if validate_email(data['email']):
        data['success']+=1
        print('[+] ',data['email'],' >> Valid')
    else:
        print('[-] ',data['email'])

def run_check():
    if data['email'] and not data['fileout']:
        single_check()

    elif data['bf'] and not data['fileout']:
        brute_force()

    elif data['fileout'] and not data['filein']:
        print("[*] Writing to file "+data['fileout']+"...")
        brute_force()

    elif data['fileout'] and data['filein']:
        print("[*] Writing to file "+data['fileout']+"...")
        from_file()

    elif data['filein']:
        from_file()


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'e:i:o:t:c:b:h')
    except getopt.error:
        sys.stdout = sys.stderr
        usage()
    if len(opts) == 0:
        usage()
    elif not (any('-i' in sublist for sublist in opts) or any('-b' in sublist for sublist in opts) or any('-e' in sublist for sublist in opts)):
        usage()
    elif any('-i' in sublist for sublist in opts) and any('-b' in sublist for sublist in opts) and any('-e' in sublist for sublist in opts):
        usage()
    else:
        for opt, arg in opts:
            if opt in ['-e']:
                data['email'] = arg
            if opt in ['-i']:
                data['filein'] = arg
            if opt in ['-o']:
                data['fileout'] = arg
            if opt in ['-t']:
                data['time'] = float(arg)
            if opt in ['-c']:
                data['chars'] = arg
            if opt in ['-b']:
                data['bf'] = arg
            if opt in ['-h']:
                usage()
    run_check()


banner = '''
    _                            
   / \    _ __  __ _  _   _  ___ 
  / _ \  | '__|/ _` || | | |/ __|
 / ___ \ | |  | (_| || |_| |\__ \\
/_/   \_\|_|   \__, | \__,_||___/
               |___/             
            by kod34

'''


if __name__ == '__main__':
    print(banner)
    main()