import ftplib
import colorama
import os, time
from getpass import getpass

def __main__():

	def clear():
		os.system("clear")

	colorama.init()
	clear()
	SERVER = input("[+] Server : ")
	username = input("[+] Username : ")
	password = getpass("[+] Password : ")

	try:
		print("[" + colorama.Fore.LIGHTGREEN_EX + "+" + colorama.Style.RESET_ALL + "] Connecting...")
		ftp = ftplib.FTP(SERVER, timeout=100)
		ftp.login(username, password)

		print("[" + colorama.Fore.LIGHTGREEN_EX + "+" + colorama.Style.RESET_ALL + "] Connected!")
		
		while(True):
			try:
				print(
					"""
{serv} | {username} (Refresh every 5 seconds)
============================
					""".format(serv=SERVER, username=username)
					)
				ftp.dir()
				time.sleep(5)
				clear()
			except Exception as ftperror:
				print("[" + colorama.Fore.RED + "-" + colorama.Style.RESET_ALL + "] Error : {e}".format(e=str(ftperror)))
			except KeyboardInterrupt:
				exit(True)

	except Exception as e:
		print("[-] Error : {err}".format(err=str(e)))

if __name__ == "__main__":
	__main__()