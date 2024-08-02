import subprocess as sp
def check_for_devices(userid:int) -> bool:
    """
    Arguments
      userid(int) - UID of the user runing the script

    Returns True if only one phone is connected and False if none of mopre than one devices connected
    """
    result = sp.run(["ls",f"/run/user/{userid}/gvfs/"],capture_output=True).stdout.decode().replace("\n","")
    if " " in result or result == "":
        return False , result
    else:
        return True ,result

def get_files(userid, device_name):
    result = sp.run(["ls",f"/run/user/{userid}/gvfs/{device_name}/"], capture_output=True).stdout.decode().replace("\n"," ")
    return list(result.split(" "))

def check_for_new_file(userid, device_name, inital_files):
    current_files = get_files(userid,device_name)
    if current_files == inital_files:
        return False,[]
    else:
        new_files = set(current_files) - set(inital_files)
        return True,list(new_files)
    