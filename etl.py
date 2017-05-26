import subprocess
import sys

try:
  #Open etl process with an arguments for right basepath and r_mode and if etl not found abort
  subprocess.call("F:\Enemy Territory - Legacy\etl.exe +set fs_basepath F:\Enemy Territory - Legacy +set r_mode 7")
except Exception(e):
  print(e)
  print("Couldn't run etl.exe\n")

  if(e):
    
    #Make decision to download installer or not
    #if decision is possitive start downloading installer either stop/abort process
	
        
	dwl = input("Do you want to download ETL Installer?\ny/n")
	
		if(dwl == "y" || dwl == "Y"):
		
		from tqdm import tqdm
		import requests

                    #Detect platform on which script is running and try downloading proper installer for win/linux os
                     if(sys.platform == "win"):

                         try:
                              #Send request to download file and get total size of that file.
                              etl_f = requests.get("https://www.etlegacy.com/download/file/83", stream=True)
                              total_size = int(etl_f.headers.get('content-length', 0));

                              #Start iterating over and writing data into file
                              with open('etl_win.exe', 'wb') as f:
                                  for data in tqdm(etl_f.iter_content(32*1024), total=total_size, unit='B', unit_scale=True):
                                      f.write(data)

                         except Exception(e):
                              print("Couldn't download file. Unkown Reason. %s" % str(e))

                     else if(sys.platform == "linux"):

                         try:
                             #Send request to download file and get total size of that file.
                              etl_f = requests.get("https://www.etlegacy.com/download/file/84", stream=True)
                              total_size = int(etl_f.headers.get('content-length', 0));

                              #Start iterating over and writing data to file
                              with open('etl_linux.sh', 'wb') as f:
                                  for data in tqdm(etl_f.iter_content(32*1024), total=total_size, unit='B', unit_scale=True):
                                      f.write(data)
                         except Exception(e):
			      print("Couldn't download file. Unkown Reason. %s" % str(e))

                     else:

                        print("Unkown platform detected!")

        else if(dwl == "n" || dwl == "N"):
		  print("Successfully exited script")

              sys.exit(0)

  else:
    print("No choice was made. Aborting!")
    sys.exit(0)
    
