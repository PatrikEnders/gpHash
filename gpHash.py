import os
from time import sleep
import hashlib
import subprocess as sp

FAIL = '\033[91m'
OKGREEN = '\033[92m'
YELLOW = '\033[93m'
ENDC = '\033[0m'
a = 0

#print(os.listdir())
os.system('color')

while True:
    print(f"{YELLOW}Please enter the path/file name{ENDC}")
    inputed = input()
    if inputed == "stop" or inputed == "shutdown" or inputed == "a" or inputed == "a/" or inputed == "/a":
        a = 1
        break
    if inputed == "clear": 
        try:
            os.system("cls")
        except:
            os.system('clear')
        a = 1
    if inputed == "help":
        print("Commands:")
        print("clear")
        a = 1
    if a == 1:
        a = 0
    else:
        try:
            file = inputed # Location of the file (can be set a different way)
            BLOCK_SIZE = 65536 # The size of each read from the file

            file_hash_md5 = hashlib.md5()
            file_hash_sha256 = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
            file_hash_sha384 = hashlib.sha384()
            file_hash_sha512 = hashlib.sha512()
            with open(file, 'rb') as f: # Open the file to read it's bytes
                fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
                while len(fb) > 0: # While there is still data being read from the file
                    file_hash_sha256.update(fb) # Update the hash
                    file_hash_md5.update(fb)
                    file_hash_sha384.update(fb)
                    file_hash_sha512.update(fb)
                    fb = f.read(BLOCK_SIZE) # Read the next block from the file

            print ("MD5: "+f"{OKGREEN}{file_hash_md5.hexdigest()}{ENDC}")
            print ("SHA-256: "+f"{OKGREEN}{file_hash_sha256.hexdigest()}{ENDC}") # Get the hexadecimal digest of the hash
            print ("SHA-384: "+f"{OKGREEN}{file_hash_sha384.hexdigest()}{ENDC}")
            print ("SHA-512: "+f"{OKGREEN}{file_hash_sha512.hexdigest()}{ENDC}")
        except:
            print(f"{FAIL}[Error]{ENDC}")
            try:
                print(os.listdir(inputed))
            except:
                sleep(0)
