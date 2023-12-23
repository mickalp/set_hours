#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:23:12 2023

@author: michal
"""

import time
import subprocess
import os
from classes import def_mnth, script_path, pt
import sys
#extra changes

# Set the total duration for script execution in seconds
total_duration = 240  # Example: 60 seconds

# Set the maximum execution time for each run of the script
max_execution_time = 2  # Example: 10 seconds


# File paths
user_input_file = pt + 'user_input.txt'
path_input_file = pt + 'path_input.txt'
mnth_year_file  = pt + 'month_year.txt'


try:
    # Get user input for name of worker
    user_input = input("Enter the path with name of file: " )
    with open(user_input_file, 'w') as file:
        file.write(user_input)

    # Get user input for the path
    path_input = input("The same NAME of WORKER as in Excel file" \
                       "(First Name Surname): ")
    with open(path_input_file, 'w') as file:
        file.write(path_input)
    
    if def_mnth == 1:
        
        month_year = input("Jesli wpisales 1 w pliku classes.py, podaj miesiac i rok w formie numerycznej"\
                          "np. jesli chcesz zeby data była generowana dla września 2023 roku podaj "\
                              "9 2023. Pamietaj, że domyślnie data jest generowana dla miesiąca poprzedzającego: "\
                                  " uruchomienie skryptu. Jesli skrypt jest włączony w innym miesiącu, niż następujący po rozliczeniu "\
                                      "należy zawsze podać miesiąc i rok w którym dane godziny były wypracowane: ")
        with open(mnth_year_file, 'w') as file:
                file.write(month_year)
                
        with open(mnth_year_file, 'r') as file:
            month_year = file.read()
            
            start_time = time.time()

        while time.time() - start_time < total_duration:
            try:
                # Run the script in a subprocess with a timeout
                process = subprocess.Popen(["python", script_path], stdin=subprocess.PIPE)
                process.communicate(input=user_input.encode() + b'\n' + path_input.encode() + b'\n' + month_year.encode(), timeout=max_execution_time)

                # Check the exit code of the script
                exit_code = process.returncode
                if exit_code == 0:
                    print("Script executed successfully. Stopping further executions.")
                    sys.exit(0)
                    break
                else:
                    print(f"Script execution exited with code {exit_code}. Retrying...")
            except subprocess.TimeoutExpired:
                # If the script execution exceeds the timeout, terminate the process
                process.terminate()
                print(f"Script execution exceeded {max_execution_time} seconds and was terminated. Retrying...")

            # Sleep for a moment to control the rate of script restarts
            time.sleep(0.01)
            

    else:
        pass


    while not (os.path.exists(user_input_file) and os.path.exists(path_input_file)):
        time.sleep(1)
        

    # Read user input from the files
    with open(user_input_file, 'r') as file:
        user_input = file.read()

    with open(path_input_file, 'r') as file:
        path_input = file.read()
        

        

    start_time = time.time()

    while time.time() - start_time < total_duration:
        try:
            # Run the script in a subprocess with a timeout
            process = subprocess.Popen(["python", script_path], stdin=subprocess.PIPE)
            process.communicate(input=user_input.encode() + b'\n' + path_input.encode(), timeout=max_execution_time)

            # Check the exit code of the script
            exit_code = process.returncode
            if exit_code == 0:
                print("Script executed successfully. Stopping further executions.")
                break
            else:
                print(f"Script execution exited with code {exit_code}. Retrying...")
        except subprocess.TimeoutExpired:
            # If the script execution exceeds the timeout, terminate the process
            process.terminate()
            print(f"Script execution exceeded {max_execution_time} seconds and was terminated. Retrying...")

        # Sleep for a moment to control the rate of script restarts
        time.sleep(0.01)

    # Continue with any cleanup or post-processing after the loop
except Exception as e:
    print(f"An error occurred: {str(e)}")
