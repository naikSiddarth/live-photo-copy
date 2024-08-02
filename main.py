import subprocess as sp
import helper_functions as hf
from time import sleep

username = sp.run(["whoami"], capture_output=True).stdout.decode().replace("\n","")
userid = int(sp.run(["id","-u",username], capture_output=True).stdout.decode().replace("\n",""))
con_state, device_name = hf.check_for_devices(userid)
device_path = f"/run/user/{userid}/gvfs/{device_name}/"
destn_path = f"/home/{username}/Desktop/photo_folder/"

def main():
    print("press ctrl + c to exit")
    try:
        if con_state:
            inital_files = hf.get_files(userid, device_name)
        while con_state:
            new_file_exists,new_files = hf.check_for_new_file(userid, device_name, inital_files)

            if new_file_exists:
                print(f"{len(new_files)} new files found.\nCopying...")
                for file in new_files:
                    sp.run(["cp", f"{device_path}{file}", f"{destn_path}{file}"])
                inital_files = hf.get_files(userid,device_name)
                print("Done copying")
            else:
                print("No new files")

            sleep(10)
    except KeyboardInterrupt:
            print("Exiting...")

if __name__ == "__main__":
   main()