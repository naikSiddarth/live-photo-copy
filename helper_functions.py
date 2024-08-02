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
