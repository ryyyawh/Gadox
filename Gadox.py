#!/usr/bin/env python
# Coded: isRey....
# created: 03-02-2025
# Language: Python

import sys, os, time, signal, webbrowser, platform, subprocess

def signal_handler(signal, frame):
		isRey()
		LOGO()
		print('\033[1;m [\033[1;31mX\033[1;m] You pressed Ctrl+C!')
		time.sleep(2)
		EXITMENU()
signal.signal(signal.SIGINT, signal_handler)

def isRey():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')

def LOGO():
	isRey()
	print("""
     \033[1;31mGadoxx\033[1;m \033[1;34mBY\033[1;m isRey \033[1;33mVersion:\033[1;32m 1.0\033[1;35m
     """)

def menu():
	LOGO()
	time.sleep(1) 
	print("""
\033[1;33m    	1.\033[1;m Name
\033[1;33m     	2.\033[1;m Phone number
\033[1;33m     	3.\033[1;m Dead
\033[1;33m     	4.\033[1;m IP
\033[1;36m       99. About
	""")

	OPT = input("\033[1;35m  Select:\033[1;m ")
	if OPT == "1":
         ID()
	elif OPT == "2":
		 PHONE()
	elif OPT == "3":
		 DEAD()
	elif OPT == "4":
		 IP()
	elif OPT == "99":
		isRey()
		webbrowser.open('https://github.com/isRey-CODE?tab=repositories')
		menu()
	else:
		isRey()
		LOGO()
		print("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

def ID():
	isRey()
	LOGO()  
	time.sleep(1)
	Name = input(" Name:\033[1;m ")
	F_name = input("\033[1;35m First name:\033[1;m ")

	print("""\033[1;34m
 1. Pipl 	  10. Twitter
 2. Facebook      11. Beenverified
 3. Spokeo    	  12. Peoplelooker     
 4. Flickr        13. Myspace 
 5. Linkedin      14. Pagesjaunes   
 6. Google plus   15. Libramemoria
 7. Tumblr        16. Avis-de-deces	 
 8. Youtube       \033[1;33m00. All\033[1;34m
 9. Peekyou \033[1;m      
==============================
\033[1;36m    99. About\033[1;31m    0. Exit
		""")
	Tracker = input("\033[1;35m D0xTr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;35m ")

	if Tracker == "1":
		isRey()
		webbrowser.open('https://pipl.com/search/?q='+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		isRey()
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Name+' '+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		isRey()
		webbrowser.open('https://www.spokeo.com/'+Name+'-'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "4":
		isRey()
		webbrowser.open('https://www.flickr.com/search/people/?username='+Name+' '+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "5":
		isRey()
		webbrowser.open('https://fr.linkedin.com/pub/dir/'+Name+'/'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "6":
		isRey()
		webbrowser.open('https://plus.google.com/s/'+Name+' '+F_name+'/people')
		time.sleep(2)
		menu()
	elif Tracker == "7":
		isRey()
		webbrowser.open('https://www.tumblr.com/search/'+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "8":
		isRey()
		webbrowser.open('http://www.youtube.com/results?search_query='+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "9":
		isRey()
		webbrowser.open('https://www.peekyou.com/'+Name+'_'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "10":
		isRey()
		webbrowser.open('https://twitter.com/search?f=users&vertical=default&q= '+Name+' '+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "11":
		isRey()
		webbrowser.open('https://www.beenverified.com/lp/e030ee/1/loading?utm_id=peekyou_Peekyou_Contact_Address_Results_Button&age=&bvid=&city=&fn='+Name+'&ln='+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "12":
		isRey()
		webbrowser.open('https://www.peoplelooker.com/lp/5ee6b8/1/loading?utm_id=peekyou_peekyou_PL_phonebook_widget_web&fn='+Name+'&ln='+F_name+'&city=&state=&age=&bvid=&utm_source=peekyou&utm_medium=channel_partner&utm_campaign=peekyou_PL_phonebook_widget_web&utm_content=static#.')
		time.sleep(2)
		menu()
	elif Tracker == "13":
		isRey()
		webbrowser.open('https://myspace.com/search?q='+Name+' '+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "14":
		isRey()
		webbrowser.open('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui='+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "15":
		isRey()
		webbrowser.open('http://www.libramemoria.com/avis/?Nom='+Name+'&Prenom='+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "16":
		isRey()
		webbrowser.open('https://www.avis-de-deces.net/avis/par-nom/?lastname='+Name+'&firstname='+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "00":
		isRey()
		webbrowser.open('https://pipl.com/search/?q='+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Name+' '+F_name)
		time.sleep(2)
		webbrowser.open('https://www.spokeo.com/'+Name+'-'+F_name)
		time.sleep(2)
		webbrowser.open('https://www.flickr.com/search/people/?username='+Name+' '+F_name)
		time.sleep(2)
		webbrowser.open('https://www.linkedin.com/pub/dir/'+Name+'/'+F_name)
		time.sleep(2)
		webbrowser.open('https://plus.google.com/s/'+Name+' '+F_name+'/people')
		time.sleep(2)
		webbrowser.open('https://www.tumblr.com/search/'+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('http://www.youtube.com/results?search_query='+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('https://www.peekyou.com/'+Name+'_'+F_name)
		time.sleep(2)
		webbrowser.open('https://twitter.com/search?f=users&vertical=default&q= '+Name+' '+F_name)
		time.sleep(2)
		webbrowser.open('https://www.beenverified.com/lp/e030ee/1/loading?utm_id=peekyou_Peekyou_Contact_Address_Results_Button&age=&bvid=&city=&fn='+Name+'&ln='+F_name)
		time.sleep(2)
		webbrowser.open('https://www.peoplelooker.com/lp/5ee6b8/1/loading?utm_id=peekyou_peekyou_PL_phonebook_widget_web&fn='+Name+'&ln='+F_name+'&city=&state=&age=&bvid=&utm_source=peekyou&utm_medium=channel_partner&utm_campaign=peekyou_PL_phonebook_widget_web&utm_content=static#.')
		time.sleep(2)
		webbrowser.open('https://myspace.com/search?q='+Name+' '+F_name)
		time.sleep(2)
		webbrowser.open('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui='+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('http://www.libramemoria.com/avis/?Nom='+Name+'&Prenom='+F_name)
		time.sleep(2)
		webbrowser.open('https://www.avis-de-deces.net/avis/par-nom/?lastname='+Name+'&firstname='+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "99":
		isRey()
		webbrowser.open('https://github.com/ryyyawh?tab=repositories')
		time.sleep(2)
		menu()
	elif Tracker == "0":
		isRey()
		EXITMENU()
	else:
		isRey()
		LOGO()
		print ("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

def PHONE():
	isRey()
	LOGO()  
	time.sleep(1)
	Num = input(" Number:\033[1;m ")

	print("""\033[1;34m
  1. Okcaller        
  2. Facebook     
  3. France-inverse   
  4. Whitepages     
  5. Anywho             
  6. Canada411      
  7. Pagesjaunes \033[1;33m	    
 00. All
\033[1;m=========================
\033[1;36m   99. Back\033[1;31m  0. Exit
		""")
	Tracker = input("\033[1;35m D0xTr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;m ")

	if Tracker == "1":
		isRey()
		webbrowser.open('http://www.okcaller.com/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		isRey()
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Num)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		isRey()
		webbrowser.open('http://www.france-inverse.com/annuaire-inverse/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "4":
		isRey()
		webbrowser.open('https://www.whitepages.com/phone/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "5":
		isRey()
		webbrowser.open('https://www.anywho.com/phone/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "6":
		isRey()
		webbrowser.open('http://canada411.pagesjaunes.ca/fs/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "7":
		isRey()
		webbrowser.open('https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui='+Num)
		time.sleep(2)
		menu()
	elif Tracker == "00":
		isRey()
		webbrowser.open('http://www.okcaller.com/'+Num)
		time.sleep(2)
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Num)
		time.sleep(2)
		webbrowser.open('http://www.france-inverse.com/annuaire-inverse/'+Num)
		time.sleep(2)
		webbrowser.open('https://www.whitepages.com/phone/'+Num)
		time.sleep(2)
		webbrowser.open('https://www.anywho.com/phone/'+Num)
		time.sleep(2)
		webbrowser.open('http://canada411.pagesjaunes.ca/fs/'+Num)
		time.sleep(2)
		webbrowser.open('https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui='+Num)
		time.sleep(2)
		menu()
	elif Tracker == "99":
		isRey()
		menu()
	elif Tracker == "0":
		isRey()
		EXITMENU()
	else:
		isRey()
		LOGO() 
		print("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

def DEAD():
	isRey()
	LOGO()
	Name = input(" Name:\033[1;m ")
	F_name = input("\033[1;35m First name:\033[1;m ")

	print("""\033[1;34m
 
  1. Libramemoria  
  2. Avis-de-deces 
  3. Enmemoria \033[1;33m
 00. All\033[1;m
=============================
\033[1;36m    99. Back\033[1;31m    0. Exit
		""")
	Tracker = input("\033[1;35m D0xTr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;35m ")
	if Tracker == "1":
		isRey()
		webbrowser.open('http://www.libramemoria.com/avis/?Nom='+Name+'&Prenom='+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		isRey()
		webbrowser.open('https://www.avis-de-deces.net/avis/par-nom/?lastname='+Name+'&firstname='+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		isRey()
		webbrowser.open('http://enmemoria.lavanguardia.com/buscar?keywords='+Name+'+'+F_name+'&type=death&_fstatus=search')
		time.sleep(2)
		menu()
	elif Tracker == "00":
		isRey()
		time.sleep(2)
		webbrowser.open('http://www.libramemoria.com/avis/?Nom='+Name+'&Prenom='+F_name)
		time.sleep(2)
		webbrowser.open('https://www.avis-de-deces.net/avis/par-nom/?lastname='+Name+'&firstname='+F_name)
		time.sleep(2)
		webbrowser.open('http://enmemoria.lavanguardia.com/buscar?keywords='+Name+'+'+F_name+'&type=death&_fstatus=search')
		time.sleep(2)
		menu()
	elif Tracker == "99":
		isRey()
		menu()
	elif Tracker == "0":
		isRey()
		EXITMENU()
	else:
		isRey()
		LOGO()
		print("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

def IP():
	isRey()
	LOGO()
	ip = input(" Ip:\033[1;m ")

	print("""\033[1;34m
 
  1. G-force 
  2. whatismyipaddress
  3. Whois\033[1;33m
 00. All\033[1;m
==============================
\033[1;36m    99. Back\033[1;31m    0. Exit
		""")	
	Tracker = input("\033[1;35m D0xTr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;35m ")
	if Tracker == "1":
		isRey()
		webbrowser.open('https://www.g-force.ca/en/hosting/ip-whois?ip='+ip)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		isRey()
		webbrowser.open('http://whatismyipaddress.com/ip/'+ip)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		isRey()
		webbrowser.open('https://dig.whois.com.au/ip/'+ip)
		time.sleep(2)
		menu()
	elif Tracker == "00":
		isRey()
		time.sleep(2)
		webbrowser.open('https://www.g-force.ca/en/hosting/ip-whois?ip='+ip)
		time.sleep(2)
		webbrowser.open('http://whatismyipaddress.com/ip/'+ip)
		time.sleep(2)
		webbrowser.open('https://dig.whois.com.au/ip/'+ip)
		time.sleep(2)
		menu()
	elif Tracker == "99":
		isRey()
		menu()
	else:
		isRey()
		LOGO()
		print("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

#~~~~ EXIT ~~~~
def EXITMENU():
	isRey()
	LOGO()
	time.sleep(1)
	print("\033[1;m Thanks for using DoxTracker\033[1;m")
	time.sleep(2)
	print("\033[1;m[\033[1;31mX\033[1;m]...\033[1;32mClosing")
	time.sleep(1)
	isRey()
	sys.exit()
		
menu()
