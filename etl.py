import subprocess
import sys
import pyautogui
from directkeys import press

def main():

      x = []
	  y = []

	try:
	  #TODO: Implement it for Linux too
	  #		 Get etl instalation from HKEY_KEY
	  subprocess.call("HKEY_KEY +set fs_basepath F:\Enemy Territory - Legacy +set r_mode 7")
	  sys.sleep(5)
	  
	  for x, y in zip(x,y):
		pyautogui.move(x,y)
		
	  pyautogui.click()
	  	  
	  for char in u'5.135.27.11:27960':
	    press(char)
	  
	except Exception(e):
	  print("Couldn't run etl.exe\n %s" % str(e))
  
	  if(e) is Exception:
		
		#Make decision to download installer or not
		#if decision is possitive start downloading installer or stop/abort process
			
		dwl = input("Do you want to download ETL Installer?\ny/n")
		
			if(dwl == "y" || dwl == "Y"):
			
			from tqdm import tqdm
			import requests

						 if(sys.platform == "win"):

							 try:
								  etl_f = requests.get("https://www.etlegacy.com/download/file/83", stream=True)
								  total_size = int(etl_f.headers.get('content-length', 0));

								  with open('etl_win.exe', 'wb') as f:
									  for data in tqdm(etl_f.iter_content(32*1024), total=total_size, unit='B', unit_scale=True):
										  f.write(data)

							 except Exception(e):
								  print("Couldn't download file. Unkown Reason.\n %s" % str(e))
								  sys.exit(1)

						 else if(sys.platform == "linux"):

							 try:
								  etl_f = requests.get("https://www.etlegacy.com/download/file/84", stream=True)
								  total_size = int(etl_f.headers.get('content-length', 0));

								  with open('etl_linux.sh', 'wb') as f:
									  for data in tqdm(etl_f.iter_content(32*1024), total=total_size, unit='B', unit_scale=True):
										  f.write(data)
							 except Exception(e):
								 print("Couldn't download file. Unkown Reason.\n %s" % str(e))
								 sys.exit(1)

						 else:

							print("Unkown platform detected!")

			else if(dwl == "n" || dwl == "N"):
			  print("Successfully exited script")

				  sys.exit(0)

	  else:
		print("No choice was made. Aborting!")
		sys.exit(0)

if __name__ == "__main__":
  main()