print("RUNNING OS")

print("CREATING VARIABLES")

json_work = True
os_work = True
time_work = True

print("CREATING VARIABLES ENDED")

print("INITIALIZING MODULES")

try:
    import os
except ModuleNotFoundError:
    print("WARN: MODULE OS NOT FOUNDED RUNNING WITHOUT IT [SOME FUNCTION NOT WORKING!]")
    os_work = False

try:
    import time
except ModuleNotFoundError:
    print("WARN: MODULE time NOT FOUNDED RUNNING WITHOUT IT [SOME FUNCTION NOT WORKING! EXAMPLE: WAITING BEFORE RUNNING INTERFACE]")
    time_work = False

try:
    import json
except ModuleNotFoundError:
    print("ERROR: MODULE json NOT FOUNDED RUNNING WITHOUT IT [SOME FUNCTION NOT WORKING! EXAMPLE: CONFIG]")
    json_work = False

print("INITIALIZING MODULE ENDED")

if json_work == True:
    print("INITIALIZING CONFIG FILE")

    with open("config\\config.cnf", "r") as f:
        config = f.read()
    config = json.loads(config)
    print(config)

    print("INITIALIZING CONFIG FILE ENDED")
else:
    print("CAN'T INITIALIZING CONFIG FILE BECAUSE json NOT IMPORTED SO CREATING BASIC CONFIG")
    config = {
        "name": "user",
        "time_sleep": 5,
        "mod_inp": False,
        "mod_inp_path": "mod\\inp\\cnf.cnf"
    }
    print("CREATING BASIC CONFIG ENDED")

print("CREATING INFO DATA")
info_data = {
    "Modules": {
        "system": {

        },
        "basic_python": {
            "os": os_work,
            "time": time_work,
            "json": json_work
        }
    },
    "Interface": {
        "cursor":">>"
    }
}
print("CREATING INFO DATA ENDED")

print("RUNNING INTERFACE")
print("INITIALIZING MOD_INP INPUT")
if info_data["Modules"]["basic_python"]["json"] == True:
    if config["mod_inp"] == True:
        try:
            with open(config["mod_inp_path"]) as f:
                info_data["Interface"]["cursor"] = f.read()
            print("INITIALIZING MOD_INP INPUT ENDED")
        except Exception as err:
            print("CANNOT INITIALIZING MOD_INP BECAUSE OF [" + str(err) + "] SO RUNNING WITH BASED")
            info_data["Interface"]["cursor"] = ">>"
    else:
        print("RUNNING WITHOUT MOD_INP BECAUSE ITS FALSE")
else:
    print("CANNOT INITIALIZE MOD_INP INPUT BECAUSE JSON NOT FOUNDED")

if info_data["Modules"]["basic_python"]["time"] == True:
    time.sleep(int(config["time_sleep"]))
else:
    ...

print("""
""" * 70)

if info_data["Modules"]["basic_python"]["time"] == False:
    print("WARN: MODULE time NOT FOUNDED RUNNING WITHOUT IT [SOME FUNCTION NOT WORKING! EXAMPLE: WAITING BEFORE RUNNING INTERFACE]")
else:
    pass

while True:
    if info_data["Modules"]["basic_python"]["json"] == True:
        sys = input(config["name"] + info_data["Interface"]["cursor"])
    elif config["mod_inp"] == True and info_data["Modules"]["basic_python"]["json"] == True:
        sys = input(config["name"] + info_data["Interface"]["cursor"])
    elif config["mod_inp"] == True and info_data["Modules"]["basic_python"]["json"] == False:
        sys = input(info_data["Interface"]["cursor"])
    else:
        sys = input(info_data["Interface"]["cursor"])
