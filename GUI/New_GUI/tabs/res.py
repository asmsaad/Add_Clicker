
import json
from tabs.res import *
import os

from threading import Thread

# tab_details = {
#     "fingerprints": {"Device types": ["Mobile + Desktop", "Desktop", "Mobile"]}
# }





def making_command_log_formate(): 
    DATA_COMMAND = {
        "Main" : "",
        "Proxy" : "",
        "Proxy required" : "",
        # "Visits",
        "Emulation": "",    
        # "Profiles",
        "Fingerprints" : "",
        # "Captcha",
        # "Timeouts",
        # "Timeouts",
        'Utility' : "",
    }

    with open(".command_log.txt","w") as WF:
        WF.write(json.dumps(DATA_COMMAND,indent=4))
    WF.close()

def update_command_log(tab_name,command):
    with open('.command_log.txt', 'r') as RF:
        DATA_COMMAND = json.load(RF)
    RF.close()

    DATA_COMMAND[tab_name] = command

    with open(".command_log.txt","w") as WF:
        WF.write(json.dumps(DATA_COMMAND,indent=4))
    WF.close()




def run_command_in_thread(command):
    os.system(command)
    # output_file = '.output.log'

    # #def run_command_and_save_output(command, output_file):
    # # Open the output file in append mode
    # with open(output_file, "a") as file:
    #     # Start the command and redirect its output to the file
    #     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    #     # Read and write the output line by line
    #     for line in iter(process.stdout.readline, b''):
    #         file.write(line.decode("utf-8"))  # Write the line to the output file
    #         print(line.decode("utf-8").strip())  # Print the line to the terminal (optional)

    #     # Wait for the command to finish
    #     process.wait()

# # Example usage:
# command_to_run = "your_command_here"
# output_file = "output.log"
# run_command_and_save_output(command_to_run, output_file)


def making_run_command():
    with open('.command_log.txt', 'r') as RF:
        DATA_COMMAND = json.load(RF)
    RF.close()


    
    if DATA_COMMAND["Proxy"].strip() == "":
        DATA_COMMAND["Proxy required"] = ""
    

    run_command = []
    for each_command_unit in DATA_COMMAND:
        run_command.append(DATA_COMMAND[each_command_unit])

    run_command = " ".join(run_command)
    print(run_command)

    print('>>',os.getcwd())
    
     # Create a thread to run the command
    thread = Thread(target=run_command_in_thread, args=(run_command,))
    # Start the thread
    thread.start()


    return run_command


