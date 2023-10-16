#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:23:12 2023

@author: michal
"""

import time
import subprocess
import os

#extra changes

# Set the total duration for script execution in seconds
total_duration = 240  # Example: 60 seconds

# Set the maximum execution time for each run of the script
max_execution_time = 2  # Example: 10 seconds

# Define the script to execute
# =============================================================================
# IN script_path PASTE DIRECTORY TO czas_pr.py PROGRAM IN FROM "path_to_script"
# with the name czas_pr.py, for example "/Users/czas_pr.py"

# In "pt" do the same but without name of program and with slash / at the end
# The same "pt" must be in program czas_pr.py!!!
# =============================================================================

# Define the script to execute
script_path = "/Users/michal/Library/CloudStorage/OneDrive-UniversityofGdansk/OneDrive - University of Gdansk (for Students)/agnieszka_gajewicz/split_hours_for_company/set_hours/work_time_v1.1.py"  # Replace with the path to your script
pt = "/Users/michal/Library/CloudStorage/OneDrive-UniversityofGdansk/OneDrive - University of Gdansk (for Students)/agnieszka_gajewicz/"



# File paths
user_input_file = pt + 'user_input.txt'
path_input_file = pt + 'path_input.txt'

try:
    # Get user input for name of worker
    user_input = input("Enter the path with name of file: " )
    with open(user_input_file, 'w') as file:
        file.write(user_input)

    # Get user input for the path
    path_input = input("The same NAME of WORKER as in Excel file \
                       (First Name Surname): ")
    with open(path_input_file, 'w') as file:
        file.write(path_input)

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
