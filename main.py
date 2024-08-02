import subprocess as sp
import helper_functions as hf

username = sp.run(["whoami"], capture_output=True).stdout.decode().replace("\n","")
userid = int(sp.run(["id","-u",username], capture_output=True).stdout.decode().replace("\n",""))



