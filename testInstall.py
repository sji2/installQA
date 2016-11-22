import configparser 
import os

#os.system("echo 7546 | sudo -S rm /home/vm1/Desktop/temp")

#Section 1 - Install/Decompress
os.system("mkdir /home/vm1/Desktop/temp")
os.system("tar -xzvf /home/vm1/Desktop/FEv5.tgz -C /home/vm1/Desktop/temp")


#Section 2 - configparser
conf = configparser.ConfigParser()

#Location changes to config file required
conf.read("/home/vm1/Install/testConfig.cfg")


#Section 3 - Import Configurations
temp = conf.get("Test", "tempLocation")
file1 = conf.get("Test", "feFiles")
file2 = conf.get("Test", "siFiles")
file3 = conf.get("Test", "saFiles")
file4 = conf.get("Test", "seFiles")
#file5 = conf.get("Test", "hostsFile")


#Section 4 - File Operation

#DON'T FORGET TO ADD FILE 5 (HOSTS) TO THE SCRIPT, AFTER YOU ADDED HOSTS TO BUNDLE
os.system("echo 7546 | sudo -S rm -r /var/www/html /home/vm1/git/system_integration /etc/apache2/sites-available /etc/apache2/sites-enabled")

os.system("sudo mv -f " + temp + "/html " + file1)
os.system("sudo mv -f " + temp + "/system_integration " + file2)
os.system("sudo mv -f " + temp + "/sites-available " + file3)
os.system("sudo mv -f " + temp + "/sites-enabled " + file4)
#os.system("sudo mv -f " + temp + "/hosts " + file5)


#Section 5 - Cleanup

#os.system("rm -r /home/vm164/Desktop/testCompress.tgz")
os.system("sudo rm -r " + temp)

os.system("echo")
os.system("echo Operation completed successfully.")
os.system("exit")
